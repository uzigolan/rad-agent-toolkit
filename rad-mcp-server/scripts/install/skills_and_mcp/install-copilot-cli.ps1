<#
Install rad-mcp (MCP + skills) for the GitHub Copilot CLI (`copilot`).

  .\install-copilot-cli.ps1                                   # interactive prompts
  .\install-copilot-cli.ps1 -Http [-Url <url>] -Token <token> # http client
  .\install-copilot-cli.ps1 -Reconfigure                      # force replace an existing entry

Writes/merges ~\.copilot\mcp-config.json AND ~\.copilot\mcp.json (root key
"mcpServers" — CLI versions disagree on the filename, so both are kept in
sync; the embedded Copilot CLI agent in JetBrains IDEs reads mcp-config.json,
field-tested 2026-07-19) and copies the skills to ~\.copilot\skills. If
rad-mcp is already configured (and no flags force a mode), offers to keep the
existing configuration.
Afterwards: RESTART the copilot session (skills + MCP load at startup only).
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

# Both filenames the CLI has used; kept in sync (mcp-config.json is what the
# JetBrains-embedded CLI agent reads).
$cfgPaths = @("$env:USERPROFILE\.copilot\mcp-config.json", "$env:USERPROFILE\.copilot\mcp.json")
$cfgPath = $cfgPaths[0]
New-Item -ItemType Directory -Force (Split-Path $cfgPath) | Out-Null
foreach ($p in $cfgPaths) { Backup-JsonConfig -Path $p }

$explicit = $Http -or $Url -or $Token -or $Reconfigure
if ((-not $explicit) -and (Test-KeepExisting -Path $cfgPath -RootKey 'mcpServers' -Name $Name)) {
    $Knowledge = Resolve-KnowledgeMode $Knowledge
    Write-Host "  mcp   -> kept existing $Name entry in $cfgPath"
    Copy-SkillsTo "$env:USERPROFILE\.copilot\skills" -Knowledge $Knowledge
    Write-Host ""
    Write-Host "Done. Existing MCP config kept; skills refreshed. Restart the copilot session."
    return
}

$Knowledge = Resolve-KnowledgeMode $Knowledge -SkipInstalledReuse

if (-not ($Http -or $Url -or $Token)) {
    # Interactive transport prompt when no flags given
    $transport = Invoke-TransportPrompt
    if ($transport.Mode -eq 'http') {
        $u, $t = $transport.Url, $transport.Token
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
} elseif ($Http -or $Url -or $Token) {
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
} else {
    Assert-CommonSetup
    $entry = [ordered]@{
        type    = 'local'
        command = $VenvPython
        args    = @('-m', 'rad_mcp.server')
        env     = @{ RAD_MCP_INVENTORY = $Inventory }
        tools   = @('*')
    }
}

foreach ($p in $cfgPaths) {
    Set-JsonMcpEntry -Path $p -RootKey 'mcpServers' -Entry $entry -Name $Name
}
Copy-SkillsTo "$env:USERPROFILE\.copilot\skills" -Knowledge $Knowledge

Write-Host ""
Write-Host "Done. Now: restart the copilot session, then verify with /mcp show and /skills list."
Write-Host "First tool call prompts for permission - answer 'yes, always'."
if ($Http) { Write-Host "http mode: make sure the shared server is running, and its token matches this client's." }
if ($Http) { Write-Host "http mode: make sure the shared server is running (read-only tools)." }
