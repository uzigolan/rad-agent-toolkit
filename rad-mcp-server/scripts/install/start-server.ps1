<#
Start the rad-mcp server over HTTP (manual launch — this window IS the server;
closing it stops it). This does NOT configure any client; run the matching
install-*.ps1 in http mode for that.

  .\start-server.ps1                                            # interactive prompts
  .\start-server.ps1 -Host 0.0.0.0 -Port 8080 -WriteToken <t>
  .\start-server.ps1 -ReadToken <t> -WriteToken <t> -TlsCert c.pem -TlsKey k.pem

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
    [string]$TlsKey
)
. (Join-Path $PSScriptRoot '_common.ps1')
Assert-CommonSetup

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

# Token - need at least one; offer to generate with a chosen role.
if (-not $ReadToken -and -not $WriteToken) {
    Write-Host "No token given. Grant a bearer token:"
    Write-Host "  1) read-write (manage devices + config)"
    Write-Host "  2) read-only  (reads only)"
    $rans = Read-Host "Choice [1]"
    $tok = & $VenvPython -c "import secrets; print(secrets.token_urlsafe(32))"
    if (-not $tok) { throw "could not auto-generate a token; rerun with -ReadToken/-WriteToken" }
    if ($rans -eq '2') { $ReadToken = $tok; $role = "read-only (RAD_MCP_TOKENS)" }
    else               { $WriteToken = $tok; $role = "read-write (RAD_MCP_WRITE_TOKENS)" }
    Write-Host ""
    Write-Host "  Generated $role token - give this SAME value to the client:"
    Write-Host ""
    Write-Host "      $tok"
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

$scheme = if ($TlsCert) { "https" } else { "http" }
Write-Host "Starting rad-mcp on ${scheme}://${BindHost}:${Port}/mcp  (Ctrl-C to stop)"
if ($BindHost -ne '127.0.0.1') { Write-Host "Reachable on the LAN - internal networks only, never a public interface." }
Set-Location (Join-Path $RadRoot 'server')
& $VenvPython -m rad_mcp.server
