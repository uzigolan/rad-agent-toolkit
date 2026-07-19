# Shared helpers for the per-target install scripts. Dot-source, don't run.
# PowerShell 5.1 compatible.

$ErrorActionPreference = 'Stop'

# Repo layout: this file lives at rad-mcp-server/scripts/install/
$script:RadRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$script:VenvPython = Join-Path $RadRoot 'server\.venv\Scripts\python.exe'
$script:Inventory = Join-Path $RadRoot 'inventory.yaml'
$script:SkillsSrc = Join-Path $RadRoot 'skills'
$script:SkillNames = @('rad-core', 'rad-cli-operations', 'rad-device-mng')

# First interpreter that is Python >= 3.10. Returns the command or $null.
function Get-BestPython {
    # Candidates may be broken shims (e.g. stale Chocolatey shims) that print
    # their own error text to stdout — capture probe output instead of letting
    # it leak into this function's return value, and require the "RADPY" marker
    # to prove a real interpreter actually ran.
    # NB: single quotes inside the Python code — PS 5.1 mangles embedded double
    # quotes when passing arguments to native executables.
    $probe = "import sys; sys.stdout.write('RADPY'); raise SystemExit(0 if sys.version_info[:2] >= (3,10) else 1)"

    # Prefer explicit python* commands first (works on all platforms).
    foreach ($c in @('python3.13', 'python3.12', 'python3.11', 'python3.10', 'python', 'python3')) {
        $cmd = Get-Command $c -ErrorAction SilentlyContinue
        if (-not $cmd) { continue }
        try {
            $out = & $c -c $probe 2>$null
            if ($LASTEXITCODE -eq 0 -and "$out" -match 'RADPY') { return $c }
        } catch { }
    }

    # Windows fallback: discover interpreter via the Python launcher (py).
    $pyLauncher = Get-Command py -ErrorAction SilentlyContinue
    if ($pyLauncher) {
        foreach ($sel in @('-3.13', '-3.12', '-3.11', '-3.10', '-3')) {
            try {
                $out = & py $sel -c $probe 2>$null
                if ($LASTEXITCODE -ne 0 -or "$out" -notmatch 'RADPY') { continue }
                $exeOut = & py $sel -c 'import sys; print(sys.executable)' 2>$null
                if ($LASTEXITCODE -eq 0 -and $exeOut) {
                    $exe = ($exeOut -split "`r?`n" | Select-Object -First 1).ToString().Trim()
                    if ($exe -and (Test-Path $exe)) { return $exe }
                }
            } catch { }
        }
    }

    return $null
}

function Install-PortablePython {
    # Self-contained fallback when the machine has no Python >= 3.10:
    # download the official CPython NuGet package (full interpreter, venv
    # capable) and unzip it INSIDE the repo (server\.python). Nothing is
    # installed system-wide - no PATH, no registry, no admin; deleting the
    # repo folder removes it completely.
    $dest = Join-Path $script:RadRoot 'server\.python'
    $exe = Join-Path $dest 'tools\python.exe'
    if (Test-Path $exe) { return $exe }
    Write-Host "No Python >= 3.10 found - downloading a portable CPython into the repo"
    Write-Host "(one-time, ~30 MB, repo-local only; nothing installed on Windows) ..."
    $zip = Join-Path $env:TEMP "rad-portable-python-$PID.zip"
    try {
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -Uri 'https://www.nuget.org/api/v2/package/python/3.12.10' `
            -OutFile $zip -UseBasicParsing
        Expand-Archive -Path $zip -DestinationPath $dest -Force
    } catch {
        Write-Host "  portable python download failed: $($_.Exception.Message)"
        return $null
    } finally {
        Remove-Item $zip -ErrorAction SilentlyContinue
    }
    if (Test-Path $exe) {
        Write-Host "  portable python -> $exe"
        return $exe
    }
    return $null
}

function Assert-CommonSetup {
    if (Test-Path $script:VenvPython) { return }
    # No venv yet — bootstrap it automatically so install is a single command.
    # A repo-local portable python from a previous run wins; then the system
    # interpreters; last resort is downloading the portable one.
    $portable = Join-Path $script:RadRoot 'server\.python\tools\python.exe'
    $py = if (Test-Path $portable) { $portable } else { Get-BestPython }
    if (-not $py) { $py = Install-PortablePython }
    if (-not $py) {
        throw ("No Python >= 3.10 found, and the portable-python download failed " +
               "(no network / no PyPI-NuGet access?). Either fix network access and " +
               "re-run, or install Python 3.10+ (python.org), then re-run this " +
               "installer. (see INSTALL.md -> Common setup)")
    }
    Write-Host "Setting up the server venv (one-time, using $py) ..."
    & $py -m venv (Join-Path $script:RadRoot 'server\.venv')
    if ($LASTEXITCODE -ne 0) { throw "failed to create the venv with '$py -m venv'." }
    Write-Host "  installing rad-mcp into the venv (pip install -e .) ..."
    & $script:VenvPython -m pip install --quiet --upgrade pip 2>$null
    & $script:VenvPython -m pip install --quiet -e (Join-Path $script:RadRoot 'server')
    if ($LASTEXITCODE -ne 0) { throw "pip install failed - check network / PyPI access, then re-run." }
    Write-Host "  venv ready: $script:VenvPython"
}

function Copy-SkillsTo {
    # Knowledge distribution mode:
    #   bundled (default) — skills carry their references/ (~14 MB); knowledge
    #                       answers work with no MCP connection.
    #   served            — thin skills (SKILL.md only); the rad-cli-operations
    #                       references/ is omitted and served by the MCP
    #                       knowledge-catalog tools (cli_search / manual_search
    #                       / mib_*). Requires a connected rad-mcp server whose
    #                       build/rad-knowledge.sqlite is present.
    param(
        [Parameter(Mandatory)][string]$Dest,
        [ValidateSet('bundled', 'served')][string]$Knowledge = 'bundled'
    )
    New-Item -ItemType Directory -Force $Dest | Out-Null
    foreach ($s in $script:SkillNames) {
        Copy-Item -Recurse -Force (Join-Path $script:SkillsSrc $s) $Dest
        Write-Host "  skill -> $Dest\$s"
    }
    if ($Knowledge -eq 'served') {
        $refs = Join-Path $Dest 'rad-cli-operations\references'
        if (Test-Path $refs) {
            Remove-Item -Recurse -Force $refs
            Write-Host "  served mode: omitted rad-cli-operations\references (served by the MCP catalog tools)"
        }
        # Stamp the mode so the loaded skill's self-check knows it (missing = bundled).
        # Marker is an HTML comment with a unique token that never appears in prose.
        $skillmd = Join-Path $Dest 'rad-cli-operations\SKILL.md'
        if ((Test-Path $skillmd) -and ((Get-Content $skillmd -Raw) -notmatch '<!--rad-mode:')) {
            $c = Get-Content $skillmd -Raw
            $c = $c -replace '(?m)^(> \*\*Skill version:\*\*.*)$', "`$1`n<!--rad-mode:served-->"
            Set-Content -Path $skillmd -Value $c -NoNewline
        }
    }
}

function Resolve-KnowledgeMode {
    # Returns 'bundled' or 'served'. A -Knowledge flag wins; otherwise prompt
    # (bundled is the default). Warns in served mode if the catalog is absent.
    param([string]$Knowledge)
    $mode = if ($Knowledge) { $Knowledge.ToLower() } else { '' }
    if (-not $mode) {
        Write-Host ""
        Write-Host "Knowledge distribution mode:"
        Write-Host "  1) bundled  - skills carry their references (~14 MB); works with no MCP connection [default]"
        Write-Host "  2) served   - thin skills; all knowledge served by the rad-mcp catalog tools"
        $ans = Read-Host "Choice [1]"
        $mode = if ($ans -match '^2$|^served') { 'served' } else { 'bundled' }
    }
    if ($mode -eq 'served') {
        $db = Join-Path $script:RadRoot 'build\rad-knowledge.sqlite'
        if (-not (Test-Path $db)) {
            Write-Host "  WARNING: served mode needs the knowledge catalog, but $db is missing."
            Write-Host "           Build it: python scripts\build_knowledge_catalog.py --mib-root `"MIBs2:priority=200`" --mib-root `"MIBS:priority=100`""
        }
    }
    Write-Host "  knowledge mode: $mode"
    return $mode
}

function New-StdioEntry {
    # Returns a hashtable for a stdio MCP entry (client launches the server).
    param([switch]$WithType)  # Copilot wants "type": "stdio"; Claude infers it
    $e = [ordered]@{}
    if ($WithType) { $e.type = 'stdio' }
    $e.command = $script:VenvPython
    $e.args = @('-m', 'rad_mcp.server')
    $e.cwd = (Join-Path $script:RadRoot 'server')
    $e.env = @{ RAD_MCP_INVENTORY = $script:Inventory }
    return $e
}

function New-HttpEntry {
    # Returns a hashtable for an http MCP entry (server runs manually).
    # -RequestInit: JetBrains Copilot nests auth headers under "requestInit"
    # (fetch-style) instead of a top-level "headers" key.
    param(
        [Parameter(Mandatory)][string]$Url,
        [Parameter(Mandatory)][string]$Token,
        [switch]$RequestInit
    )
    if ($RequestInit) {
        return [ordered]@{
            type        = 'http'
            url         = $Url
            requestInit = @{ headers = @{ Authorization = "Bearer $Token" } }
        }
    }
    return [ordered]@{
        type    = 'http'
        url     = $Url
        headers = @{ Authorization = "Bearer $Token" }
    }
}

function Format-Json {
    # Re-indent valid JSON with 2 spaces. PS 5.1 ConvertTo-Json (even without
    # -Compress) emits ugly value-aligned output that mangles a client's config;
    # we pass its -Compress form here to get clean, git-friendly formatting
    # matching the Python (json.dump indent=2) side. Input MUST be compact,
    # already-valid JSON (escaping is preserved verbatim); this only reflows the
    # structural whitespace, tracking string literals so braces inside strings
    # are left alone.
    param([Parameter(Mandatory)][string]$Json)
    $sb = [System.Text.StringBuilder]::new()
    $unit = '  '
    $indent = 0
    $inStr = $false
    $esc = $false
    $chars = $Json.ToCharArray()
    for ($i = 0; $i -lt $chars.Length; $i++) {
        $c = $chars[$i]
        if ($inStr) {
            [void]$sb.Append($c)
            if ($esc) { $esc = $false }
            elseif ($c -eq '\') { $esc = $true }
            elseif ($c -eq '"') { $inStr = $false }
            continue
        }
        switch ($c) {
            '"' { $inStr = $true; [void]$sb.Append($c) }
            '{' { if ($chars[$i + 1] -eq '}') { [void]$sb.Append('{}'); $i++ } else { $indent++; [void]$sb.Append("{`n" + ($unit * $indent)) } }
            '[' { if ($chars[$i + 1] -eq ']') { [void]$sb.Append('[]'); $i++ } else { $indent++; [void]$sb.Append("[`n" + ($unit * $indent)) } }
            '}' { $indent--; [void]$sb.Append("`n" + ($unit * $indent) + '}') }
            ']' { $indent--; [void]$sb.Append("`n" + ($unit * $indent) + ']') }
            ',' { [void]$sb.Append(",`n" + ($unit * $indent)) }
            ':' { [void]$sb.Append(': ') }
            ' ' { }
            "`t" { }
            "`n" { }
            "`r" { }
            default { [void]$sb.Append($c) }
        }
    }
    return $sb.ToString()
}

function Remove-JsonComments {
    # Strip // line and /* */ block comments (outside string literals) so
    # JSONC configs parse with ConvertFrom-Json — IntelliJ's Copilot plugin
    # seeds mcp.json with a commented template. String-aware, same scanning
    # approach as Format-Json. NB: rewriting the file afterwards drops the
    # comments (the .bak keeps them).
    param([Parameter(Mandatory)][AllowEmptyString()][string]$Json)
    $sb = [System.Text.StringBuilder]::new()
    $inStr = $false
    $esc = $false
    $chars = $Json.ToCharArray()
    for ($i = 0; $i -lt $chars.Length; $i++) {
        $c = $chars[$i]
        if ($inStr) {
            [void]$sb.Append($c)
            if ($esc) { $esc = $false }
            elseif ($c -eq '\') { $esc = $true }
            elseif ($c -eq '"') { $inStr = $false }
            continue
        }
        if ($c -eq '"') { $inStr = $true; [void]$sb.Append($c); continue }
        if ($c -eq '/' -and ($i + 1) -lt $chars.Length) {
            if ($chars[$i + 1] -eq '/') {
                while ($i -lt $chars.Length -and $chars[$i] -ne "`n") { $i++ }
                if ($i -lt $chars.Length) { [void]$sb.Append("`n") }
                continue
            }
            if ($chars[$i + 1] -eq '*') {
                $end = $Json.IndexOf('*/', $i + 2)
                $i = if ($end -lt 0) { $chars.Length } else { $end + 1 }
                continue
            }
        }
        [void]$sb.Append($c)
    }
    return $sb.ToString()
}

function Set-JsonMcpEntry {
    # Create/merge a JSON config file, replacing any existing entry named $Name
    # under the given root key ("mcpServers" or "servers").
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][string]$RootKey,
        [Parameter(Mandatory)]$Entry,
        [string]$Name = 'rad-mcp'
    )
    if (Test-Path $Path) {
        $cfg = (Remove-JsonComments (Get-Content $Path -Raw)) | ConvertFrom-Json
    } else {
        New-Item -ItemType Directory -Force (Split-Path $Path) | Out-Null
        $cfg = [pscustomobject]@{}
    }
    if (-not $cfg.PSObject.Properties[$RootKey]) {
        $cfg | Add-Member -NotePropertyName $RootKey -NotePropertyValue ([pscustomobject]@{})
    }
    $root = $cfg.$RootKey
    if ($root.PSObject.Properties[$Name]) {
        $root.PSObject.Properties.Remove($Name)
        Write-Host "  replaced existing $Name entry in $Path"
    }
    $root | Add-Member -NotePropertyName $Name -NotePropertyValue ([pscustomobject]$Entry)
    $json = Format-Json ($cfg | ConvertTo-Json -Depth 10 -Compress)
    [System.IO.File]::WriteAllText($Path, $json + "`n")
    Write-Host "  mcp   -> $Path"
    Show-McpConfigText -Text (Format-Json (([pscustomobject]@{ $Name = [pscustomobject]$Entry }) | ConvertTo-Json -Depth 10 -Compress))
}

function Hide-BearerToken {
    # Mask bearer tokens in display text (keep first/last 4 chars of long tokens).
    param([AllowEmptyString()][string]$Text)
    return [regex]::Replace($Text, 'Bearer\s+([^\s"''\}]+)', {
        param($m)
        $tok = $m.Groups[1].Value
        $masked = if ($tok.Length -gt 8) { $tok.Substring(0, 4) + '...' + $tok.Substring($tok.Length - 4) } else { '***' }
        "Bearer $masked"
    })
}

function Show-McpConfigText {
    # Echo the MCP configuration that was just written, tokens masked.
    param(
        [Parameter(Mandatory)][string]$Text,
        [string]$Title = 'added MCP configuration (token masked):'
    )
    Write-Host ""
    Write-Host "  $Title"
    foreach ($line in ((Hide-BearerToken $Text).Trim() -split "`r?`n")) { Write-Host "    $line" }
    Write-Host ""
}

function Backup-JsonConfig {
    # Copy <Path> to <Path>.bak.<yyyyMMdd-HHmmss> before overwriting, if it exists.
    param([Parameter(Mandatory)][string]$Path)
    if (-not (Test-Path $Path)) { return }
    $ts = (Get-Date -Format 'yyyyMMdd-HHmmss')
    $backup = "$Path.bak.$ts"
    Copy-Item $Path $backup
    Write-Host "  backup -> $backup"
}

function Invoke-TransportPrompt {
    # Interactive stdio/http transport picker.  Returns a hashtable:
    #   @{ Mode='stdio'|'http'; Url='...'; Token='...' }
    Write-Host ""
    Write-Host "Select MCP transport:"
    Write-Host "  1) stdio  - local; the client launches the server via command/args (full toolset)"
    Write-Host "  2) http   - remote; connect to an http(s) server by URL + bearer token (read-only)"
    $ans = Read-Host "Choice [1]"
    $mode = if ($ans -match '^2$|^http$|^HTTP$|^Http$') { 'http' } else { 'stdio' }
    if ($mode -eq 'http') {
        Write-Host "  Note: Claude Desktop is the exception - it only accepts HTTPS URLs."
        do {
            $url = Read-Host "Server URL [http://127.0.0.1:8080/mcp]"
            if (-not $url) { $url = 'http://127.0.0.1:8080/mcp' }
            if ($url -notmatch '^https?://') {
                Write-Host "  ERROR: URL must start with http:// or https://. Please re-enter."
            }
        } while ($url -notmatch '^https?://')
        $token = Read-Host "Bearer token (leave blank to auto-generate one)"
        if (-not $token) {
            try   { $token = (& $script:VenvPython -c 'import secrets; print(secrets.token_urlsafe(32))' 2>$null).Trim() }
            catch { $token = '' }
            if (-not $token) {
                # Pure-PS fallback: 32 random bytes as base64url
                $bytes = [byte[]]::new(32)
                [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
                $token = [System.Convert]::ToBase64String($bytes) -replace '[+/=]', ''
            }
            Write-Host ""
            Write-Host "  Generated bearer token. Configure the server with the SAME value:"
            Write-Host "    RAD_MCP_TOKENS=<token>        read-only"
            Write-Host "    RAD_MCP_WRITE_TOKENS=<token>  read-write (also manage devices + config)"
            Write-Host ""
            Write-Host "      $token"
            Write-Host ""
        }
        return @{ Mode = 'http'; Url = $url; Token = $token }
    }
    return @{ Mode = 'stdio'; Url = ''; Token = '' }
}

function Resolve-HttpArgs {
    param([string]$Url, [string]$Token)
    if (-not $Url) { $Url = 'http://127.0.0.1:8080/mcp' }
    if (-not $Token) {
        throw "http mode needs -Token <bearer-token> (ask the server host, or generate: python -c `"import secrets; print(secrets.token_urlsafe(32))`")"
    }
    return @($Url, $Token)
}

function Test-KeepExisting {
    # If a rad-mcp entry already exists in the JSON config, summarize it and ask
    # whether to keep it. Returns $true to keep (caller then skips writing the
    # entry, leaving the config untouched). Returns $false when there is nothing
    # to keep or the user chose to reconfigure. Skipped entirely when -Reconfigure.
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][string]$RootKey,
        [string]$Name = 'rad-mcp',
        [switch]$Reconfigure
    )
    if ($Reconfigure) { return $false }
    if (-not (Test-Path $Path)) { return $false }
    try { $cfg = (Remove-JsonComments (Get-Content $Path -Raw)) | ConvertFrom-Json } catch { return $false }
    $root = $cfg.$RootKey
    if (-not $root -or -not $root.PSObject.Properties[$Name]) { return $false }
    $e = $root.$Name
    $type = if ($e.PSObject.Properties['type']) { $e.type } else { 'stdio' }
    if ($type -eq 'http') {
        $auth = ''
        if ($e.PSObject.Properties['headers'] -and $e.headers.PSObject.Properties['Authorization']) {
            $auth = $e.headers.Authorization
        } elseif ($e.PSObject.Properties['requestInit'] -and
                  $e.requestInit.PSObject.Properties['headers'] -and
                  $e.requestInit.headers.PSObject.Properties['Authorization']) {
            $auth = $e.requestInit.headers.Authorization
        }
        $tok = if ($auth) { ($auth -split ' ')[-1] } else { '' }
        $masked = if ($tok.Length -gt 8) { $tok.Substring(0, 4) + '...' + $tok.Substring($tok.Length - 4) }
                  elseif ($tok) { 'set' } else { 'none' }
        $summary = "http  url=$($e.url)  token=$masked"
    } else {
        $cmd = if ($e.PSObject.Properties['command']) { $e.command } else { '?' }
        $summary = "$type  command=$cmd"
    }
    Write-Host "$Name is already configured in ${Path}:"
    Write-Host "    $summary"
    Write-Host "  1) Keep existing configuration (leave it unchanged)"
    Write-Host "  2) Reconfigure from scratch (re-run setup and replace it)"
    $ans = Read-Host "Choice [1]"
    switch ($ans) {
        '2' { return $false }
        'r' { return $false }
        'reconfigure' { return $false }
        default { return $true }
    }
}
