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
    [string]$Token
)
. (Join-Path $PSScriptRoot '..\_common.ps1')

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    throw "the 'claude' CLI is not on PATH - install Claude Code first (https://claude.com/claude-code)"
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
    claude mcp remove rad-mcp 2>$null
    claude mcp add --transport http rad-mcp $u --header "Authorization: Bearer $t"
    Write-Host "  mcp   -> http client of $u (read-only)"
    # Skills still need a client-side install in http mode:
    Copy-SkillsTo "$env:USERPROFILE\.claude\skills"
} else {
    Assert-CommonSetup
    $repoRoot = (Resolve-Path (Join-Path $RadRoot '..')).Path
    claude plugin marketplace add $repoRoot
    claude plugin install rad-mcp@rad-marketplace
    Write-Host "  plugin -> rad-mcp@rad-marketplace (MCP + 3 skills + 4 commands)"
}

Write-Host ""
Write-Host "Done. Now: reload the VS Code window / start a new claude session,"
Write-Host "then verify with /mcp and try: /rad-health <device-name>."
if ($Http) { Write-Host "http mode: make sure the shared server is running (read-only tools; slash commands need the plugin)." }
