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
    # Prefer explicit python* commands first (works on all platforms).
    foreach ($c in @('python3.13', 'python3.12', 'python3.11', 'python3.10', 'python', 'python3')) {
        $cmd = Get-Command $c -ErrorAction SilentlyContinue
        if (-not $cmd) { continue }
        try {
            & $c -c 'import sys; raise SystemExit(0 if sys.version_info[:2] >= (3,10) else 1)' 2>$null
            if ($LASTEXITCODE -eq 0) { return $c }
        } catch { }
    }

    # Windows fallback: discover interpreter via the Python launcher (py).
    $pyLauncher = Get-Command py -ErrorAction SilentlyContinue
    if ($pyLauncher) {
        foreach ($sel in @('-3.13', '-3.12', '-3.11', '-3.10', '-3')) {
            try {
                & py $sel -c 'import sys; raise SystemExit(0 if sys.version_info[:2] >= (3,10) else 1)' 2>$null
                if ($LASTEXITCODE -ne 0) { continue }
                $exeOut = & py $sel -c 'import sys; print(sys.executable)' 2>$null
                if ($LASTEXITCODE -eq 0 -and $exeOut) {
                    $exe = ($exeOut -split "`r?`n" | Select-Object -First 1).ToString().Trim()
                    if ($exe) { return $exe }
                }
            } catch { }
        }
    }

    return $null
}

function Assert-CommonSetup {
    if (Test-Path $script:VenvPython) { return }
    # No venv yet — bootstrap it automatically so install is a single command.
    $py = Get-BestPython
    if (-not $py) {
        throw ("No Python >= 3.10 found, and the server venv doesn't exist yet. " +
               "Install Python 3.10+ (python.org), then re-run this installer. " +
               "(see INSTALL.md -> Common setup)")
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
    param([Parameter(Mandatory)][string]$Dest)
    New-Item -ItemType Directory -Force $Dest | Out-Null
    foreach ($s in $script:SkillNames) {
        Copy-Item -Recurse -Force (Join-Path $script:SkillsSrc $s) $Dest
        Write-Host "  skill -> $Dest\$s"
    }
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
    param([Parameter(Mandatory)][string]$Url, [Parameter(Mandatory)][string]$Token)
    return [ordered]@{
        type    = 'http'
        url     = $Url
        headers = @{ Authorization = "Bearer $Token" }
    }
}

function Set-JsonMcpEntry {
    # Create/merge a JSON config file, replacing any existing rad-mcp entry
    # under the given root key ("mcpServers" or "servers").
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][string]$RootKey,
        [Parameter(Mandatory)]$Entry
    )
    if (Test-Path $Path) {
        $cfg = Get-Content $Path -Raw | ConvertFrom-Json
    } else {
        New-Item -ItemType Directory -Force (Split-Path $Path) | Out-Null
        $cfg = [pscustomobject]@{}
    }
    if (-not $cfg.PSObject.Properties[$RootKey]) {
        $cfg | Add-Member -NotePropertyName $RootKey -NotePropertyValue ([pscustomobject]@{})
    }
    $root = $cfg.$RootKey
    if ($root.PSObject.Properties['rad-mcp']) {
        $root.PSObject.Properties.Remove('rad-mcp')
        Write-Host "  replaced existing rad-mcp entry in $Path"
    }
    $root | Add-Member -NotePropertyName 'rad-mcp' -NotePropertyValue ([pscustomobject]$Entry)
    $json = $cfg | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($Path, $json + "`n")
    Write-Host "  mcp   -> $Path"
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
    Write-Host "  2) http   - remote; connect to an HTTPS server by URL + bearer token (read-only)"
    $ans = Read-Host "Choice [1]"
    $mode = if ($ans -match '^2$|^http$|^HTTP$|^Http$') { 'http' } else { 'stdio' }
    if ($mode -eq 'http') {
        Write-Host "  Note: Claude Desktop only accepts HTTPS URLs for remote MCP servers."
        Write-Host "        HTTP URLs work with other clients; proceed at your own risk."
        do {
            $url = Read-Host "Server URL [https://127.0.0.1:8080/mcp]"
            if (-not $url) { $url = 'https://127.0.0.1:8080/mcp' }
            if ($url -notmatch '^https?://') {
                Write-Host "  ERROR: URL must start with http:// or https://. Please re-enter."
            } elseif ($url -match '^http://') {
                Write-Host "  WARNING: http:// URL detected. Claude Desktop requires https://."
                Write-Host "           If you're using another MCP client, this is fine. Proceeding..."
                break
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
        [switch]$Reconfigure
    )
    if ($Reconfigure) { return $false }
    if (-not (Test-Path $Path)) { return $false }
    try { $cfg = Get-Content $Path -Raw | ConvertFrom-Json } catch { return $false }
    $root = $cfg.$RootKey
    if (-not $root -or -not $root.PSObject.Properties['rad-mcp']) { return $false }
    $e = $root.'rad-mcp'
    $type = if ($e.PSObject.Properties['type']) { $e.type } else { 'stdio' }
    if ($type -eq 'http') {
        $auth = ''
        if ($e.PSObject.Properties['headers'] -and $e.headers.PSObject.Properties['Authorization']) {
            $auth = $e.headers.Authorization
        }
        $tok = if ($auth) { ($auth -split ' ')[-1] } else { '' }
        $masked = if ($tok.Length -gt 8) { $tok.Substring(0, 4) + '...' + $tok.Substring($tok.Length - 4) }
                  elseif ($tok) { 'set' } else { 'none' }
        $summary = "http  url=$($e.url)  token=$masked"
    } else {
        $cmd = if ($e.PSObject.Properties['command']) { $e.command } else { '?' }
        $summary = "$type  command=$cmd"
    }
    Write-Host "rad-mcp is already configured in ${Path}:"
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
