<#
Manual generic installer helper for rad-mcp (skills + MCP snippets).

  .\install-generic.ps1
  .\install-generic.ps1 -Http -Url http://127.0.0.1:8080/mcp -Token <token>
    .\install-generic.ps1 -SkillMode embedded

What it does:
  - Skills: either show served skill source paths, or build embedded desktop zips
  - MCP: prompts for stdio/http and prints manual config snippets for common clients

What it does NOT do:
  - does not write any client config files
  - does not copy skills into user/workspace folders
#>
param(
    [ValidateSet('served','embedded','')][string]$SkillMode = '',
    [ValidateSet('bundled','served','')][string]$Knowledge = '',
    [switch]$Http,
    [string]$Url,
    [string]$Token,
    [string]$Name = 'rad-mcp'
)

. (Join-Path $PSScriptRoot '..\_common.ps1')

$configStore = Join-Path $RadRoot 'server\.rad-mcp-generic-config'

function Save-GenericConfig {
    param(
        [ValidateSet('served', 'embedded')][string]$SkillMode,
        [ValidateSet('served', 'bundled')][string]$Knowledge,
        [Parameter(Mandatory)][ValidateSet('stdio', 'http')][string]$Mode,
        [string]$Url,
        [string]$Token
    )
    Set-Content -Path $configStore -Value @(
        "RAD_MCP_GENERIC_SKILL_MODE='$SkillMode'",
        "RAD_MCP_GENERIC_KNOWLEDGE='$Knowledge'",
        "RAD_MCP_GENERIC_MODE='$Mode'",
        "RAD_MCP_GENERIC_URL='$Url'",
        "RAD_MCP_GENERIC_TOKEN='$Token'"
    )
}

function Mask-Token {
    param([string]$Token)
    if (-not $Token) { return 'none' }
    if ($Token.Length -gt 8) { return ($Token.Substring(0, 4) + '...' + $Token.Substring($Token.Length - 4)) }
    return 'set'
}

function Show-EntrySnippet {
    param(
        [Parameter(Mandatory)][string]$Title,
        [Parameter(Mandatory)][string]$RootKey,
        [Parameter(Mandatory)]$Entry,
        [string]$PathHint = ''
    )
    $text = Format-Json (([pscustomobject]@{ $Name = [pscustomobject]$Entry }) | ConvertTo-Json -Depth 10 -Compress)
    Show-McpConfigText -Text $text -Title $Title
    Write-Host "    root key: $RootKey"
    if ($PathHint) { Write-Host "    file    : $PathHint" }
    Write-Host ""
}

$mode = 'stdio'
$u = ''
$t = ''
$explicitSkills = [bool]($SkillMode -or $Knowledge)
$explicitTransport = [bool]($Http -or $Url -or $Token)
$explicit = [bool]($explicitSkills -or $explicitTransport)
$usedSavedConfig = $false

if (-not $explicit -and (Test-Path $configStore)) {
    $saved = @{}
    Get-Content $configStore | ForEach-Object {
        if ($_ -match "^\s*([A-Z_]+)\s*=\s*'?([^']*)'?\s*$") { $saved[$matches[1]] = $matches[2] }
    }
    $savedSkillMode = if ($saved['RAD_MCP_GENERIC_SKILL_MODE']) { $saved['RAD_MCP_GENERIC_SKILL_MODE'] } else { 'served' }
    $savedKnowledge = if ($saved['RAD_MCP_GENERIC_KNOWLEDGE']) { $saved['RAD_MCP_GENERIC_KNOWLEDGE'] } else { if ($savedSkillMode -eq 'embedded') { 'bundled' } else { 'served' } }
    $savedMode = if ($saved['RAD_MCP_GENERIC_MODE']) { $saved['RAD_MCP_GENERIC_MODE'] } else { 'stdio' }
    $savedUrl = if ($saved['RAD_MCP_GENERIC_URL']) { $saved['RAD_MCP_GENERIC_URL'] } else { '' }
    $savedToken = if ($saved['RAD_MCP_GENERIC_TOKEN']) { $saved['RAD_MCP_GENERIC_TOKEN'] } else { '' }

    Write-Host "$Name generic setup is already configured in ${configStore}:"
    Write-Host "    skills mode=$savedSkillMode  knowledge=$savedKnowledge"
    if ($savedMode -eq 'http') {
        Write-Host "    mcp    mode=http  url=$savedUrl  token=$(Mask-Token $savedToken)"
    } else {
        Write-Host "    mcp    mode=stdio"
    }
    Write-Host "Keep this configuration? [Y/n]"
    $keepAns = Read-Host "Answer"
    if ($keepAns -notmatch '^(n|no|2|r|reconfigure)$') {
        $SkillMode = $savedSkillMode
        $Knowledge = $savedKnowledge
        $mode = if ($savedMode -eq 'http') { 'http' } else { 'stdio' }
        $u = $savedUrl
        $t = $savedToken
        $usedSavedConfig = $true
    }
}

if (-not $SkillMode) {
    Write-Host ""
    Write-Host "Skills delivery mode:"
    Write-Host "  1) served   - show SKILL.md paths only (manual copy/reference)"
    Write-Host "  2) embedded - build desktop skill zip artifacts"
    $sm = Read-Host "Choice [1]"
    $SkillMode = if ($sm -match '^2$|^embedded$') { 'embedded' } else { 'served' }
}

Write-Host ""
Write-Host "skills mode -> $SkillMode"
if ($SkillMode -eq 'served') {
    if (-not $Knowledge) { $Knowledge = 'served' }
    Write-Host "  source skills folder: $SkillsSrc"
    Write-Host "  served mode: use SKILL.md only (do not copy references/ or other files)"
    Write-Host "  rad-core           : $(Join-Path $SkillsSrc 'rad-core\SKILL.md')"
    Write-Host "  rad-cli-operations : $(Join-Path $SkillsSrc 'rad-cli-operations\SKILL.md')"
    Write-Host "  rad-device-mng     : $(Join-Path $SkillsSrc 'rad-device-mng\SKILL.md')"
    Write-Host ""
    Write-Host "Manual usage examples:"
    Write-Host "  - Copilot user scope   -> %USERPROFILE%\.copilot\skills\<skill-name>\SKILL.md"
    Write-Host "  - Claude user scope    -> %USERPROFILE%\.claude\skills\<skill-name>\SKILL.md"
    Write-Host "  - Workspace scope      -> .github/skills/<skill-name>/SKILL.md"
} else {
    if (-not $Knowledge) { $Knowledge = 'bundled' }
    Write-Host "  embedded knowledge mode -> $Knowledge"
    Assert-CommonSetup
    & $VenvPython (Join-Path $RadRoot 'scripts\build_desktop_skills.py') --knowledge $Knowledge
    if ($LASTEXITCODE -ne 0) { throw 'desktop skill zip build failed.' }
    $zipDir = Join-Path $RadRoot 'dist\claude-desktop-skills'
    Write-Host "  embedded zips built -> $zipDir"
    Write-Host "  upload these zips where the client expects packaged skills (Claude Desktop: Customize -> Skills)."
}

if ($explicitTransport -and $Http) {
    $mode = 'http'
    $u, $t = Resolve-HttpArgs $Url $Token
} elseif ($explicitTransport) {
    # Any explicit URL/token means http intent.
    $mode = 'http'
    $u, $t = Resolve-HttpArgs $Url $Token
} elseif (-not $usedSavedConfig) {
    $transport = Invoke-TransportPrompt
    if ($transport.Mode -eq 'http') {
        $mode = 'http'
        $u = $transport.Url
        $t = $transport.Token
    } else {
        $mode = 'stdio'
        $u = ''
        $t = ''
    }
}

if ($usedSavedConfig -and $mode -eq 'http' -and (-not $u -or -not $t)) {
    Write-Host "  Saved HTTP configuration is incomplete; re-entering transport setup."
    $transport = Invoke-TransportPrompt
    if ($transport.Mode -eq 'http') {
        $mode = 'http'
        $u = $transport.Url
        $t = $transport.Token
    } else {
        $mode = 'stdio'
        $u = ''
        $t = ''
    }
}

Write-Host ""
Write-Host "mcp transport -> $mode"

if ($mode -eq 'stdio') {
    Assert-CommonSetup
}

Show-ServedCatalogHint -Knowledge $Knowledge -Mode $mode -Url $u

if ($mode -eq 'stdio') {
    $vscode = New-StdioEntry -WithType
    $claude = New-StdioEntry
    $copilotCli = [ordered]@{
        type    = 'local'
        command = $VenvPython
        args    = @('-m', 'rad_mcp.server')
        env     = @{ RAD_MCP_INVENTORY = $Inventory }
        tools   = @('*')
    }
} else {
    $vscode = New-HttpEntry -Url $u -Token $t
    $claude = New-HttpEntry -Url $u -Token $t
    $copilotCli = New-HttpEntry -Url $u -Token $t
    $copilotCli.tools = @('*')
}

Write-Host ""
Write-Host "Manual MCP configuration snippets (token masked):"
Write-Host ""
$intellijEntry = if ($mode -eq 'stdio') { New-StdioEntry -WithType } else { New-HttpEntry -Url $u -Token $t -RequestInit }
Show-EntrySnippet -Title 'VS Code Copilot:' -RootKey 'servers' -Entry $vscode -PathHint '%APPDATA%\Code\User\mcp.json'
Show-EntrySnippet -Title 'JetBrains Copilot (classic MCP path):' -RootKey 'servers' -Entry $intellijEntry -PathHint '%LOCALAPPDATA%\github-copilot\intellij\mcp.json'
Show-EntrySnippet -Title 'JetBrains embedded Copilot CLI agent:' -RootKey 'mcpServers' -Entry $copilotCli -PathHint '%USERPROFILE%\.copilot\mcp-config.json'
Show-EntrySnippet -Title 'Claude Code / Claude Desktop shape:' -RootKey 'mcpServers' -Entry $claude -PathHint '%APPDATA%\Claude\claude_desktop_config.json (Desktop) or ~/.claude.json/.mcp.json (Claude Code)'

Write-Host "Next steps:"
Write-Host "  1. Merge one relevant snippet into your target client config file (root key as shown)."
Write-Host "  2. Restart the client/session."
Write-Host "  3. Verify with: 'list the managed devices'."
if ($mode -eq 'http') {
    Write-Host "  4. Ensure your HTTP server is running and token matches exactly."
}

if ($mode -eq 'http') { Save-GenericConfig -SkillMode $SkillMode -Knowledge $Knowledge -Mode 'http' -Url $u -Token $t }
else                  { Save-GenericConfig -SkillMode $SkillMode -Knowledge $Knowledge -Mode 'stdio' -Url '' -Token '' }
