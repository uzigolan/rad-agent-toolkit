<#
Install rad-mcp (MCP + skills + slash commands) for Claude Code (CLI and the
VS Code extension — both read the same plugin/config).

  .\install-claude-code.ps1                                   # interactive prompts
  .\install-claude-code.ps1 -Http [-Url <url>] -Token <token> # http client

Default mode uses the plugin system (`claude` CLI must be on PATH): the
plugin carries MCP registration, all 3 skills, and the 4 slash commands.
Http mode removes any existing rad-mcp registration first, then adds the URL.
Afterwards: reload the VS Code window / start a new claude session.
#>
param(
    [ValidateSet('bundled','served','')][string]$Knowledge = '',
    [switch]$Http,
    [string]$Url,
    [string]$Token,
    [string]$Name = 'rad-mcp',   # http mode only; plugin/stdio mode uses the plugin's bundled name
    [switch]$Reconfigure
)
. (Join-Path $PSScriptRoot '..\_common.ps1')

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    # Fresh installs land in ~\.local\bin; shells opened before the install
    # don't have it on PATH yet, so pick it up for this session.
    $claudeBin = Join-Path $env:USERPROFILE '.local\bin'
    if (Test-Path (Join-Path $claudeBin 'claude.exe')) {
        $env:Path += ";$claudeBin"
    }
}
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    throw "the 'claude' CLI is not on PATH - install Claude Code first (https://claude.com/claude-code)"
}

function Install-RadPlugin {
    # The marketplace/plugin manifests are machine-local (gitignored, absolute
    # venv paths) - generate them so `claude plugin marketplace add` finds a
    # valid marketplace. rad-mcp-server/ itself is both marketplace and plugin
    # root (skills/ and commands/ already live there).
    $mpDir = Join-Path $RadRoot '.claude-plugin'
    New-Item -ItemType Directory -Force $mpDir | Out-Null

    $ver = '0.0.0'
    $initPy = Join-Path $RadRoot 'server\rad_mcp\__init__.py'
    if ((Test-Path $initPy) -and ((Get-Content $initPy -Raw) -match '__version__\s*=\s*"([^"]+)"')) { $ver = $Matches[1] }

    $desc = 'Operate RAD Data Communications devices (SecFlow, ETX-1p, ETX-2) - staged-commit config safety, harvested CLI reference + manuals, SNMP/MIB tools.'
    # ASCII avoids the PS5.1 UTF8 BOM, which some JSON parsers reject
    [System.IO.File]::WriteAllText((Join-Path $mpDir 'plugin.json'),
        (([ordered]@{ name = 'rad-mcp'; version = $ver; description = $desc } | ConvertTo-Json)))
    [System.IO.File]::WriteAllText((Join-Path $mpDir 'marketplace.json'),
        (([ordered]@{
            name    = 'rad-marketplace'
            owner   = @{ name = 'RAD' }
            plugins = @([ordered]@{ name = 'rad-mcp'; source = './'; description = $desc })
        } | ConvertTo-Json -Depth 5)))

    # Plugin-root .mcp.json: the MCP registration the plugin carries.
    [System.IO.File]::WriteAllText((Join-Path $RadRoot '.mcp.json'),
        ((@{ mcpServers = @{ 'rad-mcp' = [pscustomobject](New-StdioEntry) } } | ConvertTo-Json -Depth 5)))

    # Re-add so the marketplace path is always current; stderr from remove/add
    # on a fresh machine is expected, don't let EAP=Stop turn it terminating.
    $eap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    try {
        claude plugin marketplace remove rad-marketplace 2>$null
        claude plugin marketplace add $RadRoot
        claude plugin install rad-mcp@rad-marketplace
        if ($LASTEXITCODE -ne 0) { throw "claude plugin install failed (exit $LASTEXITCODE)" }
    } finally { $ErrorActionPreference = $eap }
}

# Keep an existing MCP registration unless flags/-Reconfigure force a change.
# Skills are refreshed either way: for http, re-copy client-side; for stdio, the
# plugin re-install refreshes bundled skills + commands (same MCP registration,
# not a reconfiguration).
$explicit = $Http -or $Url -or $Token -or $Reconfigure
if (-not $explicit) {
    # claude prints "No MCP server named ..." to stderr on a fresh install; with
    # ErrorActionPreference='Stop' a 2>$null redirect turns that into a
    # terminating error, so relax it around the probe calls.
    $eap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    try {
        $mcpGet = (claude mcp get $Name 2>$null | Out-String)
        $mcpOk  = ($LASTEXITCODE -eq 0 -and $mcpGet.Trim())
        $pluginOk = ((claude plugin list 2>$null | Out-String) -match 'rad-mcp')
    } finally { $ErrorActionPreference = $eap }
    if ($mcpOk -or $pluginOk) {
        $Knowledge = Resolve-KnowledgeMode $Knowledge
        Write-Host "$Name is already configured with Claude Code - keeping the MCP config."
        if ($mcpOk -and $mcpGet -match 'http') {
            Copy-SkillsTo "$env:USERPROFILE\.claude\skills" -Knowledge $Knowledge
        } else {
            Assert-CommonSetup
            Install-RadPlugin
            Write-Host "  plugin -> refreshed rad-mcp@rad-marketplace (skills + commands; MCP unchanged)"
        }
        Write-Host ""
        Write-Host "Done - kept MCP config, refreshed skills. Reload the VS Code window / start a new claude session."
        return
    }
}

$Knowledge = Resolve-KnowledgeMode $Knowledge -SkipInstalledReuse

if (-not ($Http -or $Url -or $Token)) {
    # Interactive transport prompt when no flags given
    $transport = Invoke-TransportPrompt
    $Http = ($transport.Mode -eq 'http')
    if ($Http) {
        $Url = $transport.Url
        $Token = $transport.Token
    }
}

if ($Http -or $Url -or $Token) {
    $u, $t = Resolve-HttpArgs $Url $Token
    # Removing a not-yet-registered entry writes to stderr; don't let that terminate.
    $eap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    try { claude mcp remove --scope user $Name 2>$null; claude mcp remove $Name 2>$null } finally { $ErrorActionPreference = $eap }
    # user scope -> global registration (~/.claude.json), available in every project
    claude mcp add --scope user --transport http $Name $u --header "Authorization: Bearer $t"
    Write-Host "  mcp   -> http client of $u (read-only)"
    Show-McpConfigText -Text ("transport = http`nurl       = $u`nheader    = Authorization: Bearer $t") `
                       -Title 'added MCP configuration (claude mcp, token masked):'
    # Skills still need a client-side install in http mode:
    Copy-SkillsTo "$env:USERPROFILE\.claude\skills" -Knowledge $Knowledge
} else {
    Assert-CommonSetup
    Install-RadPlugin
    Write-Host "  plugin -> rad-mcp@rad-marketplace (MCP + skills + commands)"
    $stdioEntry = New-StdioEntry
    Show-McpConfigText -Text (Format-Json (([pscustomobject]@{ 'rad-mcp' = [pscustomobject]$stdioEntry }) | ConvertTo-Json -Depth 10 -Compress)) `
                       -Title 'MCP configuration the plugin registers (stdio; the client launches the server):'
}

Write-Host ""
Write-Host "Done. Now: reload the VS Code window / start a new claude session,"
Write-Host "then verify with /mcp and try: /rad-health <device-name>."
if ($Http) { Write-Host "http mode: make sure the shared server is running (read-only tools; slash commands need the plugin)." }
