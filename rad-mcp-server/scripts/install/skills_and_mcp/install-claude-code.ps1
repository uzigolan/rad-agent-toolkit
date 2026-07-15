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
    [switch]$Http,
    [string]$Url,
    [string]$Token,
    [string]$Name = 'rad-mcp',   # http mode only; plugin/stdio mode uses the plugin's bundled name
    [switch]$Reconfigure
)
. (Join-Path $PSScriptRoot '..\_common.ps1')

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    throw "the 'claude' CLI is not on PATH - install Claude Code first (https://claude.com/claude-code)"
}

# Keep an existing MCP registration unless flags/-Reconfigure force a change.
# Skills are refreshed either way: for http, re-copy client-side; for stdio, the
# plugin re-install refreshes bundled skills + commands (same MCP registration,
# not a reconfiguration).
$explicit = $Http -or $Url -or $Token -or $Reconfigure
if (-not $explicit) {
    $mcpGet = (claude mcp get $Name 2>$null | Out-String)
    $mcpOk  = ($LASTEXITCODE -eq 0 -and $mcpGet.Trim())
    $pluginOk = ((claude plugin list 2>$null | Out-String) -match 'rad-mcp')
    if ($mcpOk -or $pluginOk) {
        Write-Host "$Name is already configured with Claude Code - keeping the MCP config."
        if ($mcpOk -and $mcpGet -match 'http') {
            Copy-SkillsTo "$env:USERPROFILE\.claude\skills"
        } else {
            Assert-CommonSetup
            $repoRoot = (Resolve-Path (Join-Path $RadRoot '..')).Path
            claude plugin marketplace add $repoRoot
            claude plugin install rad-mcp@rad-marketplace
            Write-Host "  plugin -> refreshed rad-mcp@rad-marketplace (skills + commands; MCP unchanged)"
        }
        Write-Host ""
        Write-Host "Done - kept MCP config, refreshed skills. Reload the VS Code window / start a new claude session."
        return
    }
}

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
    claude mcp remove $Name 2>$null
    claude mcp add --transport http $Name $u --header "Authorization: Bearer $t"
    Write-Host "  mcp   -> http client of $u (read-only)"
    Show-McpConfigText -Text ("transport = http`nurl       = $u`nheader    = Authorization: Bearer $t") `
                       -Title 'added MCP configuration (claude mcp, token masked):'
    # Skills still need a client-side install in http mode:
    Copy-SkillsTo "$env:USERPROFILE\.claude\skills"
} else {
    Assert-CommonSetup
    $repoRoot = (Resolve-Path (Join-Path $RadRoot '..')).Path
    claude plugin marketplace add $repoRoot
    claude plugin install rad-mcp@rad-marketplace
    Write-Host "  plugin -> rad-mcp@rad-marketplace (MCP + 3 skills + 4 commands)"
    $stdioEntry = New-StdioEntry
    Show-McpConfigText -Text (Format-Json (([pscustomobject]@{ 'rad-mcp' = [pscustomobject]$stdioEntry }) | ConvertTo-Json -Depth 10 -Compress)) `
                       -Title 'MCP configuration the plugin registers (stdio; the client launches the server):'
}

Write-Host ""
Write-Host "Done. Now: reload the VS Code window / start a new claude session,"
Write-Host "then verify with /mcp and try: /rad-health <device-name>."
if ($Http) { Write-Host "http mode: make sure the shared server is running (read-only tools; slash commands need the plugin)." }
