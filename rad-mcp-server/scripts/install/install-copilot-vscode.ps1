<#
Install rad-mcp (MCP + skills) for the GitHub Copilot VS Code extension.

  .\install-copilot-vscode.ps1 [-Workspace <folder>]                 # stdio (default)
  .\install-copilot-vscode.ps1 -Http [-Url <url>] -Token <token>     # http client
  .\install-copilot-vscode.ps1 -Reconfigure                          # force replace an existing entry

Writes/merges <workspace>\.vscode\mcp.json (root key "servers") and copies the
skills to ~\.copilot\skills (read by Copilot in VS Code AND Copilot CLI). If
rad-mcp is already configured (and no flags force a mode), offers to keep the
existing configuration. Afterwards: reload the VS Code window, accept the
trust dialog, use agent mode.
#>
param(
    [string]$Workspace = (Get-Location).Path,
    [switch]$Http,
    [string]$Url,
    [string]$Token,
    [switch]$Reconfigure
)
. (Join-Path $PSScriptRoot '_common.ps1')

$cfgPath = Join-Path $Workspace '.vscode\mcp.json'
$explicit = $Http -or $Url -or $Token -or $Reconfigure
if ((-not $explicit) -and (Test-KeepExisting -Path $cfgPath -RootKey 'servers')) {
    Write-Host "  mcp   -> kept existing rad-mcp entry in $cfgPath"
    Copy-SkillsTo "$env:USERPROFILE\.copilot\skills"
    Write-Host ""
    Write-Host "Done. Existing MCP config kept; skills refreshed. Reload the VS Code window."
    return
}

if ($Http) {
    $u, $t = Resolve-HttpArgs $Url $Token
    $entry = New-HttpEntry -Url $u -Token $t
} else {
    Assert-CommonSetup
    $entry = New-StdioEntry -WithType
}

Set-JsonMcpEntry -Path $cfgPath -RootKey 'servers' -Entry $entry
Copy-SkillsTo "$env:USERPROFILE\.copilot\skills"

Write-Host ""
Write-Host "Done. Now: reload the VS Code window, accept the MCP trust dialog,"
Write-Host "switch Copilot Chat to AGENT mode, and try: 'list the managed devices'."
if ($Http) { Write-Host "http mode: make sure the shared server is running, and its token matches this client's." }
