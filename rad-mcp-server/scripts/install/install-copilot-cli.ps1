<#
Install rad-mcp (MCP + skills) for the GitHub Copilot CLI (`copilot`).

  .\install-copilot-cli.ps1                                   # stdio (default)
  .\install-copilot-cli.ps1 -Http [-Url <url>] -Token <token> # http client

Writes/merges ~\.copilot\mcp-config.json (root key "mcpServers") and copies
the skills to ~\.copilot\skills. Replaces any existing rad-mcp entry.
Afterwards: RESTART the copilot session (skills + MCP load at startup only).
#>
param(
    [switch]$Http,
    [string]$Url,
    [string]$Token
)
. (Join-Path $PSScriptRoot '_common.ps1')

if ($Http) {
    $u, $t = Resolve-HttpArgs $Url $Token
    $entry = New-HttpEntry -Url $u -Token $t
    $entry.tools = @('*')
} else {
    Assert-CommonSetup
    # Copilot CLI's stdio type is "local" and has no cwd support (the server's
    # own paths are module-anchored, so that's safe).
    $entry = [ordered]@{
        type    = 'local'
        command = $VenvPython
        args    = @('-m', 'rad_mcp.server')
        env     = @{ RAD_MCP_INVENTORY = $Inventory }
        tools   = @('*')
    }
}

Set-JsonMcpEntry -Path "$env:USERPROFILE\.copilot\mcp-config.json" -RootKey 'mcpServers' -Entry $entry
Copy-SkillsTo "$env:USERPROFILE\.copilot\skills"

Write-Host ""
Write-Host "Done. Now: restart the copilot session, then verify with /mcp show and /skills list."
Write-Host "First tool call prompts for permission - answer 'yes, always'."
if ($Http) { Write-Host "http mode: make sure the shared server is running (read-only tools)." }
