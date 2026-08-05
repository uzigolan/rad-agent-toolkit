<#
Combined stdio install for VS Code Copilot:
  1. Prepare the local stdio MCP server (venv + optional catalog)
  2. Install VS Code Copilot MCP config + skills in stdio mode

This wrapper forces skills to install in served mode.

Run from anywhere:
  .\install-stdio-copilot-vscode.ps1
  .\install-stdio-copilot-vscode.ps1 -MibDir C:\MIBS
#>
param(
    [string]$MibDir,
    [switch]$SkipCatalog,
    [string]$Name = 'rad-mcp',
    [switch]$Reconfigure
)

$mcpInstaller = Join-Path $PSScriptRoot '..\mcp_server\install-stdio-mcp-server.ps1'
$copilotInstaller = Join-Path $PSScriptRoot 'install-copilot-vscode.ps1'

$mcpArgs = @{}
if ($MibDir) { $mcpArgs['MibDir'] = $MibDir }
if ($SkipCatalog) { $mcpArgs['SkipCatalog'] = $true }

Write-Host "Step 1/2: preparing local stdio MCP server ..."
& $mcpInstaller @mcpArgs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$copilotArgs = @{ Stdio = $true; Name = $Name; Knowledge = 'served' }
if ($Reconfigure) { $copilotArgs['Reconfigure'] = $true }

Write-Host ""
Write-Host "Step 2/2: installing VS Code Copilot MCP config + skills (stdio) ..."
& $copilotInstaller @copilotArgs
exit $LASTEXITCODE