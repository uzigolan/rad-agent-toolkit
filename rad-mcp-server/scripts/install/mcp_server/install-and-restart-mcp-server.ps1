<#
(Re)start the rad-mcp server over HTTP (manual launch — this window IS the
server; closing it stops it). If a server is already listening on the chosen
port, it is stopped first. This does NOT configure any client; run the
matching install-*.ps1 in http mode for that.

  .\install-and-restart-mcp-server.ps1                            # interactive prompts
  .\install-and-restart-mcp-server.ps1 -BindHost 0.0.0.0 -Port 8080 -WriteToken <t>
  .\install-and-restart-mcp-server.ps1 -ReadToken <t> -WriteToken <t> -TlsCert c.pem -TlsKey k.pem

At least one token is required (http refuses to start unauthenticated).
  -ReadToken  -> RAD_MCP_TOKENS        (read-only clients)
  -WriteToken -> RAD_MCP_WRITE_TOKENS  (read-write clients: manage devices + config)
#>
param(
    [string]$BindHost,
    [int]$Port = 8080,
    [string]$ReadToken,
    [string]$WriteToken,
    [string]$TlsCert,
    [string]$TlsKey,
    [switch]$NewTokens
)
. (Join-Path $PSScriptRoot '..\_common.ps1')
Assert-CommonSetup

# Tokens persist across restarts in this gitignored file so a restart reuses the
# same values (no need to reconfigure clients). Delete it or pass -NewTokens to
# regenerate.
$TokenStore = Join-Path $RadRoot 'server\.rad-mcp-tokens'

function Get-FirstIPv4 {
    try {
        return (Get-NetIPAddress -AddressFamily IPv4 -ErrorAction Stop |
            Where-Object { $_.IPAddress -ne '127.0.0.1' -and $_.PrefixOrigin -ne 'WellKnown' } |
            Select-Object -First 1 -ExpandProperty IPAddress)
    } catch { return $null }
}

# Bind address — offer loopback, this host's LAN IP, or all interfaces.
if (-not $BindHost) {
    $ip = Get-FirstIPv4
    Write-Host "Bind address (RAD_MCP_HOST):"
    Write-Host "  1) 127.0.0.1     (this machine only)"
    if ($ip) { Write-Host "  2) $ip     (this host's LAN address - reachable by other machines)" }
    Write-Host "  3) 0.0.0.0       (all interfaces)"
    $hans = Read-Host "Choice [1]"
    switch ($hans) {
        '2'     { $BindHost = if ($ip) { $ip } else { '127.0.0.1' } }
        '3'     { $BindHost = '0.0.0.0' }
        ''      { $BindHost = '127.0.0.1' }
        '1'     { $BindHost = '127.0.0.1' }
        default { $BindHost = $hans }
    }
}

# Token - reuse saved tokens across restarts; otherwise generate and save them.
$fromStore = $false
if (-not $ReadToken -and -not $WriteToken -and -not $NewTokens -and (Test-Path $TokenStore)) {
    Get-Content $TokenStore | ForEach-Object {
        if ($_ -match "^\s*([A-Z_]+)\s*=\s*'?([^']*)'?\s*$") {
            if ($matches[1] -eq 'RAD_MCP_WRITE_TOKENS') { $WriteToken = $matches[2] }
            elseif ($matches[1] -eq 'RAD_MCP_TOKENS') { $ReadToken = $matches[2] }
        }
    }
    if ($WriteToken -or $ReadToken) {
        $fromStore = $true
        Write-Host "Reusing saved tokens from $TokenStore (-NewTokens to regenerate):"
        if ($WriteToken) { Write-Host "    read-write (RAD_MCP_WRITE_TOKENS):  $WriteToken" }
        if ($ReadToken)  { Write-Host "    read-only  (RAD_MCP_TOKENS):        $ReadToken" }
        Write-Host ""
    }
}

if (-not $ReadToken -and -not $WriteToken) {
    Write-Host "No token given. Generate bearer token(s):"
    Write-Host "  1) read-write only  (manage devices + config)"
    Write-Host "  2) read-only only   (reads only)"
    Write-Host "  3) both             (one read-write + one read-only - hand out either)"
    $rans = Read-Host "Choice [3]"
    function New-Tok { & $VenvPython -c "import secrets; print(secrets.token_urlsafe(32))" }
    switch ($rans) {
        '1' { $WriteToken = New-Tok }
        '2' { $ReadToken  = New-Tok }
        default { $WriteToken = New-Tok; $ReadToken = New-Tok }
    }
    if (-not $WriteToken -and -not $ReadToken) { throw "could not auto-generate a token; rerun with -ReadToken/-WriteToken" }
    Write-Host ""
    Write-Host "  Generated token(s) - give each to whichever client you choose:"
    if ($WriteToken) { Write-Host "    read-write (RAD_MCP_WRITE_TOKENS):  $WriteToken" }
    if ($ReadToken)  { Write-Host "    read-only  (RAD_MCP_TOKENS):        $ReadToken" }
    Write-Host ""
    Write-Host "  A client's Authorization: Bearer <value> must match one of these exactly,"
    Write-Host "  or it gets 401 Unauthorized. The role follows whichever token it uses."
    Write-Host ""
}

# Persist the tokens (unless just loaded from the store) so the next restart
# reuses them without reconfiguring clients.
if (-not $fromStore -and ($WriteToken -or $ReadToken)) {
    $lines = @()
    if ($WriteToken) { $lines += "RAD_MCP_WRITE_TOKENS='$WriteToken'" }
    if ($ReadToken)  { $lines += "RAD_MCP_TOKENS='$ReadToken'" }
    Set-Content -Path $TokenStore -Value $lines
    Write-Host "Saved tokens to $TokenStore (gitignored; reused on next start)."
    Write-Host ""
}

# TLS is all-or-nothing (the server also enforces this).
if (($TlsCert -or $TlsKey) -and -not ($TlsCert -and $TlsKey)) {
    throw "-TlsCert and -TlsKey must be given together."
}

$env:RAD_MCP_TRANSPORT = "http"
$env:RAD_MCP_HOST      = $BindHost
$env:RAD_MCP_PORT      = "$Port"
$env:RAD_MCP_INVENTORY = $Inventory
if ($ReadToken)  { $env:RAD_MCP_TOKENS       = $ReadToken }
if ($WriteToken) { $env:RAD_MCP_WRITE_TOKENS = $WriteToken }
if ($TlsCert)    { $env:RAD_MCP_TLS_CERT     = $TlsCert }
if ($TlsKey)     { $env:RAD_MCP_TLS_KEY      = $TlsKey }

# Restart: if a server is already listening on this port, stop it first.
try {
    $pids = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue |
        Select-Object -ExpandProperty OwningProcess -Unique
    foreach ($procId in $pids) {
        if ($procId -and $procId -ne $PID) {
            Write-Host "Port $Port already in use - stopping existing server (PID $procId) ..."
            Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
        }
    }
} catch { }

$scheme = if ($TlsCert) { "https" } else { "http" }
Write-Host "Starting rad-mcp on ${scheme}://${BindHost}:${Port}/mcp  (Ctrl-C to stop)"
if ($BindHost -ne '127.0.0.1') { Write-Host "Reachable on the LAN - internal networks only, never a public interface." }
Set-Location (Join-Path $RadRoot 'server')
& $VenvPython -m rad_mcp.server
