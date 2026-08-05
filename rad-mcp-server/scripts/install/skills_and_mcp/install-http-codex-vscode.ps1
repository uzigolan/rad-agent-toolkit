<#
Combined HTTP install for Codex on VS Code:
  1. Install Codex MCP config + skills in HTTP mode

Use this when your shared HTTP MCP server is already running.

Run from anywhere:
  .\install-http-codex-vscode.ps1
  .\install-http-codex-vscode.ps1 -Url http://127.0.0.1:8080/mcp -Token <token>
#>
param(
    [string]$Url,
    [string]$Token,
    [string]$Name = 'rad-mcp',
    [switch]$Reconfigure
)

$codexInstaller = Join-Path $PSScriptRoot 'install-codex.ps1'

$codexArgs = @{ Http = $true; Name = $Name; Knowledge = 'served' }
if ($Url) { $codexArgs['Url'] = $Url }
if ($Token) { $codexArgs['Token'] = $Token }
if ($Reconfigure) { $codexArgs['Reconfigure'] = $true }

Write-Host "Installing Codex MCP config + skills (http) ..."
& $codexInstaller @codexArgs
exit $LASTEXITCODE
