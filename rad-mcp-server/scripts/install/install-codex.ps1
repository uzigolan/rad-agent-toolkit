<#
Install rad-mcp (MCP + skills) for OpenAI Codex (CLI / IDE extension / ChatGPT
desktop — all three share ~\.codex\config.toml).

  .\install-codex.ps1                                   # stdio (default)
  .\install-codex.ps1 -Http [-Url <url>] -Token <token> # http client

Appends a [mcp_servers.rad-mcp] section to ~\.codex\config.toml (refuses if
one already exists — TOML is edited as text, remove the old section first)
and copies the skills to ~\.agents\skills. Afterwards: restart Codex.
#>
param(
    [switch]$Http,
    [string]$Url,
    [string]$Token
)
. (Join-Path $PSScriptRoot '_common.ps1')

$cfgPath = "$env:USERPROFILE\.codex\config.toml"
if ((Test-Path $cfgPath) -and ((Get-Content $cfgPath -Raw) -match '\[mcp_servers\.rad-mcp\]')) {
    throw ("$cfgPath already has a [mcp_servers.rad-mcp] section - remove or " +
           "edit that section first (disable-previous rule), then rerun.")
}

$fwd = $RadRoot -replace '\\', '/'
if ($Http) {
    $u, $t = Resolve-HttpArgs $Url $Token
    $block = @"

# rad-mcp - http client: server runs manually (read-only by the code interlock)
[mcp_servers.rad-mcp]
url = "$u"
http_headers = { Authorization = "Bearer $t" }
"@
} else {
    Assert-CommonSetup
    $block = @"

# rad-mcp - stdio: Codex launches its own instance (full toolset incl. staged writes)
[mcp_servers.rad-mcp]
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
Copy-SkillsTo "$env:USERPROFILE\.agents\skills"

Write-Host ""
Write-Host "Done. Now: restart Codex (config + skills load at startup), then verify"
Write-Host "with /mcp and /skills. Explicit skill call: `$rad-cli-operations"
if ($Http) { Write-Host "http mode: make sure the shared server is running (read-only tools)." }
