<#
Prepare rad-mcp for stdio clients (no HTTP listener):
  - Bootstrap server venv + dependencies (same common setup used by installers)
    - Optionally build the knowledge catalog (rad-knowledge.sqlite)

Behavior:
    - Reuses saved stdio MIB configuration from server\.rad-mcp-stdio-config
        when no flags are passed, and asks whether to keep it
    - Keeps the existing catalog by default unless you choose to rebuild

Examples:
    .\install-stdio-mcp-server.ps1
    .\install-stdio-mcp-server.ps1 -MibDir C:\MIBS
    .\install-stdio-mcp-server.ps1 -SkipCatalog
#>
param(
    [string]$MibDir,
    [switch]$SkipCatalog
)

. (Join-Path $PSScriptRoot '..\_common.ps1')

Assert-CommonSetup

$catalog = Join-Path $RadRoot 'build\rad-knowledge.sqlite'
$buildScript = Join-Path $RadRoot 'scripts\build_knowledge_catalog.py'
$configStore = Join-Path $RadRoot 'server\.rad-mcp-stdio-config'

Write-Host ""
Write-Host "stdio preparation:"
Write-Host "  venv/deps -> ready ($VenvPython)"

$catalogPresent = Test-Path $catalog
$keepConfig = $false
$explicitParams = [bool]($MibDir -or $SkipCatalog)

if (-not $explicitParams -and (Test-Path $configStore)) {
    $saved = @{}
    Get-Content $configStore | ForEach-Object {
        if ($_ -match "^\s*([A-Z_]+)\s*=\s*'?([^']*)'?\s*$") { $saved[$matches[1]] = $matches[2] }
    }

    Write-Host "Found a saved stdio configuration from a previous run ($configStore):"
    $savedMode = if ($saved['RAD_MCP_STDIO_MIB_MODE']) { $saved['RAD_MCP_STDIO_MIB_MODE'] } else { 'unknown' }
    Write-Host "    MIB mode : $savedMode"
    if ($saved['RAD_MCP_STDIO_MIB_ROOT']) { Write-Host "    MIB root : $($saved['RAD_MCP_STDIO_MIB_ROOT'])" }
    if ($catalogPresent) {
        $sizeMb = [math]::Round((Get-Item $catalog).Length / 1MB)
        Write-Host "    catalog  : present ($sizeMb MB)"
    } else {
        Write-Host "    catalog  : missing"
    }

    $keepAns = Read-Host "Keep this configuration (MIBs)? [Y/n]"
    if ($keepAns -notmatch '^[nN]') {
        $keepConfig = $true
        if ($catalogPresent) {
            $sizeMb = [math]::Round((Get-Item $catalog).Length / 1MB)
            Write-Host "  catalog   -> kept existing ($sizeMb MB): $catalog"
            Write-Host ""
            Write-Host "Done. You can now use stdio MCP entries from IDE installers."
            return
        }
        Write-Host "  WARNING: saved configuration was kept, but the catalog file is missing."
        Write-Host "           Continue below to build a new catalog if needed."
    } else {
        Write-Host "Reconfiguring stdio MIB setup."
    }
    Write-Host ""
}

if ($SkipCatalog) {
    if (Test-Path $catalog) {
        Write-Host "  catalog   -> kept existing $catalog"
    } else {
        Write-Host "  catalog   -> skipped (none present)"
    }
    Write-Host ""
    Write-Host "Done. You can now use stdio MCP entries from IDE installers."
    return
}

$doBuild = $false
$buildMode = ''
$resolvedMibDir = ''

if ($MibDir) {
    if (-not (Test-Path $MibDir)) {
        throw "MIB directory not found: $MibDir"
    }
    $resolvedMibDir = (Resolve-Path $MibDir).Path
    $doBuild = $true
    $buildMode = 'custom'
} else {
    $q = if ($catalogPresent) { "  Rebuild the MIB catalog? (keep current if no) [y/N]" }
         else                 { "  Add MIBs now - build the catalog? [y/N]" }
    $ans = Read-Host $q
    $doBuild = ($ans -match '^(y|yes)$')

    if ($doBuild) {
        Write-Host "  Build mode:"
        Write-Host "    1) baseline (no extra MIB roots)"
        Write-Host "    2) custom MIB directory"
        $modeAns = Read-Host "  Choice [1]"
        if ($modeAns -match '^2$|^custom') {
            $mibPrompt = Read-Host "  Path to the MIB directory (folder with .mib files)"
            if (-not $mibPrompt -or -not (Test-Path $mibPrompt)) {
                throw "MIB directory not found: $mibPrompt"
            }
            $resolvedMibDir = (Resolve-Path $mibPrompt).Path
            $buildMode = 'custom'
        } else {
            $buildMode = 'baseline'
        }
    }
}

if (-not $doBuild) {
    if (Test-Path $catalog) {
        Write-Host "  catalog   -> kept existing $catalog"
    } else {
        Write-Host "  catalog   -> skipped (none present)"
    }
    Write-Host ""
    Write-Host "Done. You can now use stdio MCP entries from IDE installers."
    return
}

$eapPrev = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
try {
    if ($buildMode -eq 'custom') {
        & $VenvPython -c "import pysmi" 2>$null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "  installing pysmi into the venv (one-time) ..."
            & $VenvPython -m pip install --quiet pysmi
            if ($LASTEXITCODE -ne 0) { throw "Failed installing pysmi" }
        }

        Write-Host "  catalog   -> building from MIB directory: $resolvedMibDir"
        & $VenvPython $buildScript --mib-root "$resolvedMibDir"
    } else {
        Write-Host "  catalog   -> building baseline catalog (no extra MIB roots)"
        & $VenvPython $buildScript
    }
    $buildOk = ($LASTEXITCODE -eq 0)
} finally {
    $ErrorActionPreference = $eapPrev
}

if ($buildOk -and (Test-Path $catalog)) {
    $sizeMb = [math]::Round((Get-Item $catalog).Length / 1MB)
    Write-Host "  catalog   -> ready ($sizeMb MB): $catalog"
    Set-Content -Path $configStore -Value @(
        "RAD_MCP_STDIO_MIB_MODE='$buildMode'",
        "RAD_MCP_STDIO_MIB_ROOT='$resolvedMibDir'"
    )
    Write-Host "  config    -> saved: $configStore"
} else {
    throw "Catalog build failed (see output above)."
}

Write-Host ""
Write-Host "Done. You can now use stdio MCP entries from IDE installers."
