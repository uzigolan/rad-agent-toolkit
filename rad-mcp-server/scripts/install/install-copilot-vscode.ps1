<#
Install rad-mcp (MCP + skills) for the GitHub Copilot VS Code extension.

  .\install-copilot-vscode.ps1 [-Workspace <folder>]                 # stdio (default)
  .\install-copilot-vscode.ps1 -Http [-Url <url>] -Token <token>     # http client

Writes/merges <workspace>\.vscode\mcp.json (root key "servers") and copies the
skills to ~\.copilot\skills (read by Copilot in VS Code AND Copilot CLI).
Replaces any existing rad-mcp entry. Afterwards: reload the VS Code window,
accept the trust dialog, use agent mode.
#>
param(
    [string]$Workspace = (Get-Location).Path,
    [switch]$Http,
    [string]$Url,
    [string]$Token
)
. (Join-Path $PSScriptRoot '_common.ps1')

if ($Http) {
    $u, $t = Resolve-HttpArgs $Url $Token
    $entry = New-HttpEntry -Url $u -Token $t
} else {
    Assert-CommonSetup
    $entry = New-StdioEntry -WithType
}

Set-JsonMcpEntry -Path (Join-Path $Workspace '.vscode\mcp.json') -RootKey 'servers' -Entry $entry
Copy-SkillsTo "$env:USERPROFILE\.copilot\skills"

Write-Host ""
Write-Host "Done. Now: reload the VS Code window, accept the MCP trust dialog,"
Write-Host "switch Copilot Chat to AGENT mode, and try: 'list the managed devices'."
if ($Http) { Write-Host "http mode: make sure the shared server is running (read-only tools)." }
