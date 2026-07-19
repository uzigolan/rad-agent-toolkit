<#
Install rad-mcp (MCP + skills) for GitHub Copilot in JetBrains IDEs (IntelliJ
IDEA, PyCharm, WebStorm, ...).

  .\install-copilot-intellij.ps1                                   # interactive prompts
  .\install-copilot-intellij.ps1 -Http [-Url <url>] -Token <token> # http client
  .\install-copilot-intellij.ps1 -Reconfigure                      # force replace an existing entry

JetBrains Copilot has TWO agent paths with separate MCP configs, and this
script wires BOTH (field-tested 2026-07-19):
  - classic agent mode reads %LOCALAPPDATA%\github-copilot\intellij\mcp.json
    (root key "servers"; one file shared by ALL JetBrains IDEs)
  - the embedded Copilot CLI agent (the chat with /mcp, /skills, /context)
    reads ~\.copilot\mcp-config.json (+ mcp.json kept in sync)
Also copies the skills to ~\.copilot\skills (the same folder Copilot CLI and
VS Code read). If rad-mcp is already configured (and no flags force a mode),
offers to keep the existing configuration. Afterwards: restart the IDE,
enable Agent Skills (Settings -> GitHub Copilot -> Chat), accept the MCP
trust prompt, use agent mode.
#>
param(
    [ValidateSet('bundled','served','')][string]$Knowledge = '',
    [switch]$Http,
    [string]$Url,
    [string]$Token,
    [string]$Name = 'rad-mcp',
    [switch]$Reconfigure
)
. (Join-Path $PSScriptRoot '..\_common.ps1')
$Knowledge = Resolve-KnowledgeMode $Knowledge

$cfgPath = Join-Path $env:LOCALAPPDATA 'github-copilot\intellij\mcp.json'
New-Item -ItemType Directory -Force (Split-Path $cfgPath) | Out-Null
Backup-JsonConfig -Path $cfgPath

$explicit = $Http -or $Url -or $Token -or $Reconfigure
if ((-not $explicit) -and (Test-KeepExisting -Path $cfgPath -RootKey 'servers' -Name $Name)) {
    Write-Host "  mcp   -> kept existing $Name entry in $cfgPath"
    Copy-SkillsTo "$env:USERPROFILE\.copilot\skills" -Knowledge $Knowledge
    Write-Host ""
    Write-Host "Done. Existing MCP config kept; skills refreshed. Restart the IDE."
    return
}

$mode = 'stdio'; $u = ''; $t = ''
if (-not ($Http -or $Url -or $Token)) {
    # Interactive transport prompt when no flags given
    $transport = Invoke-TransportPrompt
    if ($transport.Mode -eq 'http') { $mode = 'http'; $u = $transport.Url; $t = $transport.Token }
} elseif ($Http) {
    $mode = 'http'
    $u, $t = Resolve-HttpArgs $Url $Token
}

if ($mode -eq 'http') {
    $entry = New-HttpEntry -Url $u -Token $t -RequestInit
    $cliEntry = New-HttpEntry -Url $u -Token $t
    $cliEntry.tools = @('*')
} else {
    Assert-CommonSetup
    $entry = New-StdioEntry -WithType
    # Copilot CLI's stdio type is "local" and has no cwd support (safe — the
    # server's own paths are module-anchored).
    $cliEntry = [ordered]@{
        type    = 'local'
        command = $VenvPython
        args    = @('-m', 'rad_mcp.server')
        env     = @{ RAD_MCP_INVENTORY = $Inventory }
        tools   = @('*')
    }
}

Set-JsonMcpEntry -Path $cfgPath -RootKey 'servers' -Entry $entry -Name $Name
# The embedded Copilot CLI agent inside the IDE chat ignores intellij\mcp.json
# and reads the Copilot CLI config — write the same server there too.
foreach ($p in @("$env:USERPROFILE\.copilot\mcp-config.json", "$env:USERPROFILE\.copilot\mcp.json")) {
    Backup-JsonConfig -Path $p
    Set-JsonMcpEntry -Path $p -RootKey 'mcpServers' -Entry $cliEntry -Name $Name
}
Copy-SkillsTo "$env:USERPROFILE\.copilot\skills" -Knowledge $Knowledge

Write-Host ""
Write-Host "Done. Now: restart the JetBrains IDE, enable Agent Skills"
Write-Host "(Settings -> GitHub Copilot -> Chat), accept the MCP trust prompt,"
Write-Host "switch Copilot Chat to AGENT mode and START A NEW CHAT, then verify:"
Write-Host "  /mcp list      -> rad-mcp next to the builtin github-mcp-server"
Write-Host "  /skills list   -> the three rad skills (typing / alone won't list them)"
Write-Host "  'rad agent, list the managed devices'"
Write-Host "NOTE: needs the OFFICIAL 'GitHub Copilot' plugin (by GitHub); the"
Write-Host "JetBrains AI Assistant plugin/settings pages show none of this."
if ($Http) { Write-Host "http mode: make sure the shared server is running, and its token matches this client's." }
