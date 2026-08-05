<#
Combined stdio install for Codex on VS Code:
  1. Prepare the local stdio MCP server (venv + optional catalog)
  2. Install Codex MCP config + skills in stdio mode

This wrapper forces skills to install in served mode.

Run from anywhere:
  .\install-stdio-codex-vscode.ps1
  .\install-stdio-codex-vscode.ps1 -MibDir C:\MIBS
#>
param(
    [string]$MibDir,
    [switch]$SkipCatalog,
    [string]$Name = 'rad-mcp',
    [switch]$Reconfigure
)

$mcpInstaller = Join-Path $PSScriptRoot '..\mcp_server\install-stdio-mcp-server.ps1'
$codexInstaller = Join-Path $PSScriptRoot 'install-codex.ps1'

$mcpArgs = @{}
if ($MibDir) { $mcpArgs['MibDir'] = $MibDir }
if ($SkipCatalog) { $mcpArgs['SkipCatalog'] = $true }

Write-Host "Step 1/2: preparing local stdio MCP server ..."
& $mcpInstaller @mcpArgs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$codexArgs = @{ Name = $Name; Knowledge = 'served' }
if ($Reconfigure) { $codexArgs['Reconfigure'] = $true }

Write-Host ""
Write-Host "Step 2/2: installing Codex MCP config + skills (stdio) ..."
& $codexInstaller @codexArgs
exit $LASTEXITCODE
