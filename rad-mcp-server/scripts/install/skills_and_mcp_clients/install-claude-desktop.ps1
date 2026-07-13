<#
Install rad-mcp (MCP + skills) for Claude Desktop.

  .\install-claude-desktop.ps1        # stdio (the only config-file mode Desktop supports)

Merges the stdio entry into %APPDATA%\Claude\claude_desktop_config.json
(replacing any existing rad-mcp entry), rebuilds the skill zips, and opens
the zip folder — the upload itself is manual (Customize -> Skills), Desktop
has no API for it.

No -Http switch: Desktop's config file is stdio-only (verified 2026-07-10);
for a remote server use the Customize -> Connectors UI instead.
#>
. (Join-Path $PSScriptRoot '..\_common.ps1')

Assert-CommonSetup

Set-JsonMcpEntry -Path "$env:APPDATA\Claude\claude_desktop_config.json" `
                 -RootKey 'mcpServers' -Entry (New-StdioEntry)

& $VenvPython (Join-Path $RadRoot 'scripts\build_desktop_skills.py')
$zipDir = Join-Path $RadRoot 'dist\claude-desktop-skills'

Write-Host ""
Write-Host "Done, two manual steps remain (Desktop offers no automation for them):"
Write-Host "  1. FULLY restart Desktop: system-tray icon -> Quit (window close is NOT enough), relaunch."
Write-Host "  2. Sidebar Customize -> Skills -> upload the zips now opening in Explorer"
Write-Host "     (replace existing ones if already uploaded)."
Start-Process explorer.exe $zipDir
