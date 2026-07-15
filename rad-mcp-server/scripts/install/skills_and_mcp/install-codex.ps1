<#
Install rad-mcp (MCP + skills) for OpenAI Codex (CLI / IDE extension / ChatGPT
desktop — all three share ~\.codex\config.toml).

  .\install-codex.ps1                                   # interactive prompts
  .\install-codex.ps1 -Http [-Url <url>] -Token <token> # http client
  .\install-codex.ps1 -Reconfigure                      # replace an existing entry (default keeps it)

By default, if a [mcp_servers.rad-mcp] section already exists it is KEPT and
only the skills are refreshed. Pass -Reconfigure to replace it (TOML is edited
as text, so remove the old section by hand first, then rerun with -Reconfigure).
#>
param(
    [switch]$Http,
    [string]$Url,
    [string]$Token,
    [string]$Name = 'rad-mcp',
    [switch]$Reconfigure
)
. (Join-Path $PSScriptRoot '..\_common.ps1')

$cfgPath = "$env:USERPROFILE\.codex\config.toml"
$sectionRe = "\[mcp_servers\.$([regex]::Escape($Name))\]"
$exists = (Test-Path $cfgPath) -and ((Get-Content $cfgPath -Raw) -match $sectionRe)
$explicit = $Http -or $Url -or $Token -or $Reconfigure
if ($exists -and -not $explicit) {
    # Keep the existing MCP config untouched; still refresh the skills.
    Write-Host "$Name is already configured in ${cfgPath}: keeping it (pass -Reconfigure to replace)."
    Copy-SkillsTo "$env:USERPROFILE\.agents\skills"
    Write-Host ""
    Write-Host "Done - kept existing MCP config, refreshed skills. Restart Codex."
    return
}
if ($exists) {
    throw ("$cfgPath already has a [mcp_servers.$Name] section - TOML is edited " +
           "as text, so remove that section by hand first, then rerun.")
}

# Backup before changes
if (Test-Path $cfgPath) {
    $ts = (Get-Date -Format 'yyyyMMdd-HHmmss')
    $backup = "$cfgPath.bak.$ts"
    Copy-Item $cfgPath $backup
    Write-Host "  backup -> $backup"
}

$fwd = $RadRoot -replace '\\', '/'

if (-not ($Http -or $Url -or $Token)) {
    # Interactive transport prompt when no flags given
    $transport = Invoke-TransportPrompt
    if ($transport.Mode -eq 'http') {
        $u, $t = $transport.Url, $transport.Token
        $block = @"

# $Name - http client: server runs manually (read-only by the code interlock)
[mcp_servers.$Name]
url = "$u"
http_headers = { Authorization = "Bearer $t" }
"@
    } else {
        Assert-CommonSetup
        $block = @"

# $Name - stdio: Codex launches its own instance (full toolset incl. staged writes)
[mcp_servers.$Name]
command = "$fwd/server/.venv/Scripts/python.exe"
args = ["-m", "rad_mcp.server"]
cwd = "$fwd/server"
env = { RAD_MCP_INVENTORY = "$fwd/inventory.yaml" }
startup_timeout_sec = 20
"@
    }
} elseif ($Http) {
    $u, $t = Resolve-HttpArgs $Url $Token
    $block = @"

# $Name - http client: server runs manually (read-only by the code interlock)
[mcp_servers.$Name]
url = "$u"
http_headers = { Authorization = "Bearer $t" }
"@
} else {
    Assert-CommonSetup
    $block = @"

# $Name - stdio: Codex launches its own instance (full toolset incl. staged writes)
[mcp_servers.$Name]
command = "$fwd/server/.venv/Scripts/python.exe"
args = ["-m", "rad_mcp.server"]
cwd = "$fwd/server"
env = { RAD_MCP_INVENTORY = "$fwd/inventory.yaml" }
startup_timeout_sec = 20
"@
}

New-Item -ItemType Directory -Force (Split-Path $cfgPath) | Out-Null
Add-Content -Path $cfgPath -Value $block
Write-Host "  mcp   -> $cfgPath"
Show-McpConfigText -Text $block
Copy-SkillsTo "$env:USERPROFILE\.agents\skills"

Write-Host ""
Write-Host "Done. Now: restart Codex (config + skills load at startup), then verify"
Write-Host "with /mcp and /skills. Explicit skill call: `$rad-cli-operations"
if ($transport.Mode -eq 'http' -or $Http) { Write-Host "http mode: make sure the shared server is running (read-only tools)." }
