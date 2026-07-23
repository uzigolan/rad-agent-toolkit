<#
Install rad-mcp (MCP + skills) for Claude Desktop.

  .\install-claude-desktop.ps1

Backs up the Claude Desktop config file (new Windows Store or traditional),
then merges the new rad-mcp entry (replacing any existing one). Rebuilds the
skill zips and opens the zip folder — the upload itself is manual
(Customize -> Skills).

Prompts for transport:
  stdio only — Desktop launches the server itself (full toolset incl. staged writes).

  .\install-claude-desktop.ps1 -Name my-rad   # register under a custom name (default rad-mcp)
  .\install-claude-desktop.ps1 -Reconfigure   # replace an existing rad-mcp entry (default keeps it)

By default, if rad-mcp is already in the Desktop config it is KEPT untouched;
the skill zips are rebuilt either way. Pass -Reconfigure to replace the entry.
#>
param([ValidateSet('bundled','served','')][string]$Knowledge = '', [string]$Name = 'rad-mcp', [switch]$Reconfigure)
. (Join-Path $PSScriptRoot '..\_common.ps1')

Assert-CommonSetup

# Detect config path: Windows Store packaged path first, then traditional
$cfgPath = "$env:LOCALAPPDATA\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json"
if (-not (Test-Path (Split-Path $cfgPath))) {
    $cfgPath = "$env:APPDATA\Claude\claude_desktop_config.json"
}

# Keep an existing MCP entry unless -Reconfigure. Skills are rebuilt regardless.
$keptExisting = $false
if ((-not $Reconfigure) -and (Test-KeepExisting -Path $cfgPath -RootKey 'mcpServers' -Name $Name)) {
  $keptExisting = $true
    Write-Host "  mcp   -> kept existing $Name entry in $cfgPath"
} else {
    Backup-JsonConfig -Path $cfgPath
    $entry = New-StdioEntry
    Set-JsonMcpEntry -Path $cfgPath -RootKey 'mcpServers' -Entry $entry -Name $Name
}

$Knowledge = if ($keptExisting) { Resolve-KnowledgeMode $Knowledge } else { Resolve-KnowledgeMode $Knowledge -SkipInstalledReuse }

# Skills are rebuilt no matter what (kept or reconfigured MCP).
& $VenvPython (Join-Path $RadRoot 'scripts\build_desktop_skills.py') --knowledge $Knowledge
$zipDir = Join-Path $RadRoot 'dist\claude-desktop-skills'

Write-Host ""
Write-Host "Done, two manual steps remain (Desktop offers no automation for them):"
Write-Host "  MCP client config is set in: $cfgPath (mcpServers.$Name, mode: stdio)"
Write-Host "  1. FULLY restart Desktop: system-tray icon -> Quit (window close is NOT enough), relaunch."
Write-Host "  2. Sidebar Customize -> Skills -> upload the zips now opening in Explorer"
Write-Host "     (replace existing ones if already uploaded)."
Start-Process explorer.exe $zipDir
