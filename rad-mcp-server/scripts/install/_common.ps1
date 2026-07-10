# Shared helpers for the per-target install scripts. Dot-source, don't run.
# PowerShell 5.1 compatible.

$ErrorActionPreference = 'Stop'

# Repo layout: this file lives at rad-mcp-server/scripts/install/
$script:RadRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$script:VenvPython = Join-Path $RadRoot 'server\.venv\Scripts\python.exe'
$script:Inventory = Join-Path $RadRoot 'inventory.yaml'
$script:SkillsSrc = Join-Path $RadRoot 'skills'
$script:SkillNames = @('rad-core', 'rad-cli-operations', 'rad-device-mng')

function Assert-CommonSetup {
    if (-not (Test-Path $script:VenvPython)) {
        throw ("venv not found at $script:VenvPython - run the common setup first " +
               "(see INSTALL.md): cd rad-mcp-server\server; python -m venv .venv; " +
               ".venv\Scripts\pip install -e .")
    }
}

function Copy-SkillsTo {
    param([Parameter(Mandatory)][string]$Dest)
    New-Item -ItemType Directory -Force $Dest | Out-Null
    foreach ($s in $script:SkillNames) {
        Copy-Item -Recurse -Force (Join-Path $script:SkillsSrc $s) $Dest
        Write-Host "  skill -> $Dest\$s"
    }
}

function New-StdioEntry {
    # Returns a hashtable for a stdio MCP entry (client launches the server).
    param([switch]$WithType)  # Copilot wants "type": "stdio"; Claude infers it
    $e = [ordered]@{}
    if ($WithType) { $e.type = 'stdio' }
    $e.command = $script:VenvPython
    $e.args = @('-m', 'rad_mcp.server')
    $e.cwd = (Join-Path $script:RadRoot 'server')
    $e.env = @{ RAD_MCP_INVENTORY = $script:Inventory }
    return $e
}

function New-HttpEntry {
    # Returns a hashtable for an http MCP entry (server runs manually).
    param([Parameter(Mandatory)][string]$Url, [Parameter(Mandatory)][string]$Token)
    return [ordered]@{
        type    = 'http'
        url     = $Url
        headers = @{ Authorization = "Bearer $Token" }
    }
}

function Set-JsonMcpEntry {
    # Create/merge a JSON config file, replacing any existing rad-mcp entry
    # under the given root key ("mcpServers" or "servers").
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][string]$RootKey,
        [Parameter(Mandatory)]$Entry
    )
    if (Test-Path $Path) {
        $cfg = Get-Content $Path -Raw | ConvertFrom-Json
    } else {
        New-Item -ItemType Directory -Force (Split-Path $Path) | Out-Null
        $cfg = [pscustomobject]@{}
    }
    if (-not $cfg.PSObject.Properties[$RootKey]) {
        $cfg | Add-Member -NotePropertyName $RootKey -NotePropertyValue ([pscustomobject]@{})
    }
    $root = $cfg.$RootKey
    if ($root.PSObject.Properties['rad-mcp']) {
        $root.PSObject.Properties.Remove('rad-mcp')
        Write-Host "  replaced existing rad-mcp entry in $Path"
    }
    $root | Add-Member -NotePropertyName 'rad-mcp' -NotePropertyValue ([pscustomobject]$Entry)
    $json = $cfg | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($Path, $json + "`n")
    Write-Host "  mcp   -> $Path"
}

function Resolve-HttpArgs {
    param([string]$Url, [string]$Token)
    if (-not $Url) { $Url = 'http://127.0.0.1:8080/mcp' }
    if (-not $Token) {
        throw "http mode needs -Token <bearer-token> (ask the server host, or generate: python -c `"import secrets; print(secrets.token_urlsafe(32))`")"
    }
    return @($Url, $Token)
}
