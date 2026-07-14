<#
Install and start the rad-mcp server over HTTP/HTTPS (manual launch — this
window IS the server; closing it stops it). If a server is already listening on
the chosen port, it is stopped first (so re-running restarts it). This does NOT
configure any client; run the matching install-*.ps1 in http mode for that.

  .\install-and-start-http-mcp-server.ps1                            # interactive prompts
  .\install-and-start-http-mcp-server.ps1 -BindHost 0.0.0.0 -Port 8080 -WriteToken <t>
  .\install-and-start-http-mcp-server.ps1 -ReadToken <t> -WriteToken <t> -TlsCert c.pem -TlsKey k.pem

At least one token is required (http refuses to start unauthenticated).
  -ReadToken  -> RAD_MCP_TOKENS        (read-only clients)
  -WriteToken -> RAD_MCP_WRITE_TOKENS  (read-write clients: manage devices + config)
  -Name       -> RAD_MCP_SERVER_NAME   (server name reported to clients; default rad-mcp)

TLS NOTE: Claude Desktop (and most hosted MCP clients) only connect to HTTPS
endpoints. Provide -TlsCert + -TlsKey (PEM files) or answer the interactive
prompt. Without TLS the server runs plain HTTP — only clients that accept
plain-HTTP endpoints (e.g. local VS Code / Codex) will connect.
#>
param(
    [string]$BindHost,
    [int]$Port = 8080,
    [string]$ReadToken,
    [string]$WriteToken,
    [string]$TlsCert,
    [string]$TlsKey,
    [string]$Name = 'rad-mcp',
    [switch]$NewTokens
)
. (Join-Path $PSScriptRoot '..\_common.ps1')
Assert-CommonSetup

# --- HTTP/HTTPS mode ---
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

# TLS — prompt interactively when not supplied as flags.
# Required for Claude Desktop and other HTTPS-only clients.
if (-not $TlsCert -and -not $TlsKey) {
    $tlsDir  = Join-Path $RadRoot 'server\tls'
    $defaultCert = Join-Path $tlsDir 'rad-mcp.crt'
    $defaultKey  = Join-Path $tlsDir 'rad-mcp.key'
    $certExists  = Test-Path $defaultCert
    $keyExists   = Test-Path $defaultKey

    Write-Host ""
    Write-Host "TLS configuration (required for Claude Desktop and other HTTPS-only clients):"
    if ($certExists -and $keyExists) {
        Write-Host "  Found existing cert from previous run: $defaultCert"
        Write-Host "  1) No TLS       - plain HTTP (delete the old cert); only plain-HTTP clients (local VS Code/Codex) will connect"
        Write-Host "  2) Reuse cert   - HTTPS; use the existing certificate"
        Write-Host "  3) Self-signed  - HTTPS; generate a new cert + key (replaces the old one)"
        Write-Host "  4) Imported     - HTTPS; provide paths to different PEM cert + key files"
        $tlsAns = Read-Host "Choice [2]"
        if ($tlsAns -match '^1$|^no') {
            Write-Host "  Deleting old certificate..."
            Remove-Item -Force -ErrorAction SilentlyContinue $defaultCert, $defaultKey
            $TlsCert = ''; $TlsKey = ''
        } elseif ($tlsAns -match '^2$|^reuse') {
            $TlsCert = $defaultCert
            $TlsKey = $defaultKey
        } elseif ($tlsAns -match '^3$|^self') {
            $TlsCert = $defaultCert
            $TlsKey = $defaultKey
            Write-Host "  Generating self-signed certificate (10 years) ..."
            $pyScript = @'
import sys, datetime, ipaddress, pathlib
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
cert_path, key_path, bind_host = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, u"rad-mcp")])
now = datetime.datetime.now(datetime.timezone.utc)
sans = [x509.IPAddress(ipaddress.IPv4Address("127.0.0.1")), x509.DNSName("localhost")]
if bind_host not in ("127.0.0.1", "0.0.0.0", "localhost", ""):
    try: sans.append(x509.IPAddress(ipaddress.IPv4Address(bind_host)))
    except ValueError: sans.append(x509.DNSName(bind_host))
cert = (x509.CertificateBuilder()
    .subject_name(name).issuer_name(name).public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(now).not_valid_after(now + datetime.timedelta(days=3650))
    .add_extension(x509.SubjectAlternativeName(sans), critical=False)
    .sign(key, hashes.SHA256()))
cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
key_path.write_bytes(key.private_bytes(serialization.Encoding.PEM,
    serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption()))
print(f"  cert -> {cert_path}")
print(f"  key  -> {key_path}")
'@
            New-Item -ItemType Directory -Force $tlsDir | Out-Null
            $tmpPy = [System.IO.Path]::GetTempFileName() + '.py'
            try {
                [System.IO.File]::WriteAllText($tmpPy, $pyScript)
                & $VenvPython $tmpPy $TlsCert $TlsKey $BindHost
                if ($LASTEXITCODE -ne 0) { throw "Self-signed certificate generation failed." }
            } finally { Remove-Item -ErrorAction SilentlyContinue $tmpPy }
            Write-Host "  NOTE: clients must trust or skip-verify this self-signed cert."
        } elseif ($tlsAns -match '^4$|^imp') {
            $TlsCert = Read-Host "Path to TLS certificate PEM"
            $TlsKey  = Read-Host "Path to TLS private key PEM"
        }
    } else {
        Write-Host "  1) No TLS       - plain HTTP; only plain-HTTP clients (local VS Code/Codex) will connect"
        Write-Host "  2) Self-signed  - HTTPS; generate a new cert + key automatically (fastest)"
        Write-Host "  3) Imported     - HTTPS; provide paths to existing PEM cert + key files"
        $tlsAns = Read-Host "Choice [1]"
        if ($tlsAns -match '^2$|^self') {
            New-Item -ItemType Directory -Force $tlsDir | Out-Null
            $TlsCert = $defaultCert
            $TlsKey  = $defaultKey
            Write-Host "  Generating self-signed certificate (10 years) ..."
            $pyScript = @'
import sys, datetime, ipaddress, pathlib
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
cert_path, key_path, bind_host = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, u"rad-mcp")])
now = datetime.datetime.now(datetime.timezone.utc)
sans = [x509.IPAddress(ipaddress.IPv4Address("127.0.0.1")), x509.DNSName("localhost")]
if bind_host not in ("127.0.0.1", "0.0.0.0", "localhost", ""):
    try: sans.append(x509.IPAddress(ipaddress.IPv4Address(bind_host)))
    except ValueError: sans.append(x509.DNSName(bind_host))
cert = (x509.CertificateBuilder()
    .subject_name(name).issuer_name(name).public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(now).not_valid_after(now + datetime.timedelta(days=3650))
    .add_extension(x509.SubjectAlternativeName(sans), critical=False)
    .sign(key, hashes.SHA256()))
cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
key_path.write_bytes(key.private_bytes(serialization.Encoding.PEM,
    serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption()))
print(f"  cert -> {cert_path}")
print(f"  key  -> {key_path}")
'@
            $tmpPy = [System.IO.Path]::GetTempFileName() + '.py'
            try {
                [System.IO.File]::WriteAllText($tmpPy, $pyScript)
                & $VenvPython $tmpPy $TlsCert $TlsKey $BindHost
                if ($LASTEXITCODE -ne 0) { throw "Self-signed certificate generation failed." }
            } finally { Remove-Item -ErrorAction SilentlyContinue $tmpPy }
            Write-Host "  NOTE: clients must trust or skip-verify this self-signed cert."
        } elseif ($tlsAns -match '^3$|^imp') {
            $TlsCert = Read-Host "Path to TLS certificate PEM"
            $TlsKey  = Read-Host "Path to TLS private key PEM"
        }
    }
}
# TLS is all-or-nothing (the server also enforces this).
if (($TlsCert -or $TlsKey) -and -not ($TlsCert -and $TlsKey)) {
    throw "-TlsCert and -TlsKey must be given together."
}

$env:RAD_MCP_TRANSPORT   = "http"
$env:RAD_MCP_SERVER_NAME = $Name
$env:RAD_MCP_HOST        = $BindHost
$env:RAD_MCP_PORT        = "$Port"
$env:RAD_MCP_INVENTORY   = $Inventory
if ($ReadToken)  { $env:RAD_MCP_TOKENS       = $ReadToken }
if ($WriteToken) { $env:RAD_MCP_WRITE_TOKENS = $WriteToken }
if ($TlsCert)    { $env:RAD_MCP_TLS_CERT     = $TlsCert } else { Remove-Item Env:RAD_MCP_TLS_CERT -ErrorAction SilentlyContinue }
if ($TlsKey)     { $env:RAD_MCP_TLS_KEY      = $TlsKey }   else { Remove-Item Env:RAD_MCP_TLS_KEY -ErrorAction SilentlyContinue }

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
if ($WriteToken) { Write-Host "  read-write token (RAD_MCP_WRITE_TOKENS): $WriteToken" }
if ($ReadToken)  { Write-Host "  read-only  token (RAD_MCP_TOKENS):        $ReadToken" }
if ($TlsCert) {
    Write-Host "  TLS cert: $TlsCert"
    Write-Host "  TLS key:  $TlsKey"
    Write-Host "  (FastMCP logs 'transport http' - transport name, not the scheme; Uvicorn confirms https://)"
}
Write-Host "Starting $Name on ${scheme}://${BindHost}:${Port}/mcp  (Ctrl-C to stop)"
if ($BindHost -ne '127.0.0.1') { Write-Host "Reachable on the LAN - internal networks only, never a public interface." }
Push-Location (Join-Path $RadRoot 'server')
try { & $VenvPython -m rad_mcp.server }
finally { Pop-Location }
