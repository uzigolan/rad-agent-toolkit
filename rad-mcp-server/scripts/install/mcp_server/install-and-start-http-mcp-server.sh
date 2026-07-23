#!/usr/bin/env bash
#
# Install and start the rad-mcp server over HTTP/HTTPS (manual launch — the
# terminal IS the server; closing it stops it). If a server is already
# listening on the chosen port, it is stopped first (so re-running restarts
# it). This does NOT configure any client; run the matching install-*.sh in
# http mode for that.
#
#   ./install-and-start-http-mcp-server.sh                       # interactive host/port/token prompts
#   ./install-and-start-http-mcp-server.sh --host 0.0.0.0 --port 8080 --write-token <t>
#   ./install-and-start-http-mcp-server.sh --read-token <t> --write-token <t> --tls-cert c.pem --tls-key k.pem
#   ./install-and-start-http-mcp-server.sh --keep-devices | --reset-devices   # skip the device question
#
# DEVICE INVENTORY: when inventory.yaml already has devices, the script asks
# whether to USE them or RESET — reset empties the inventory AND strips every
# device secret (usernames, passwords, SNMP communities) from server/.env via
# scripts/reset_devices.py (timestamped .bak backups; token/TLS/config keys
# are preserved). --keep-devices / --reset-devices answer it non-interactively.
#
# CONFIG REUSE: the full configuration (bind host, port, name, TLS) is saved to
# server/.rad-mcp-http-config (tokens to server/.rad-mcp-tokens), both
# gitignored. On the next run with no flags it shows that saved config and asks
# "Keep this configuration? [Y/n]" — Yes starts immediately with everything
# reused; No runs the full interactive setup. Any flag skips the prompt.
#
# At least one token is required (http refuses to start unauthenticated). With
# no token flags, the interactive prompt offers read-write, read-only, or BOTH
# (one of each), so you can hand out whichever role to each client.
#   --read-token  -> RAD_MCP_TOKENS        (read-only clients)
#   --write-token -> RAD_MCP_WRITE_TOKENS  (read-write clients: manage devices + config)
#   --name        -> RAD_MCP_SERVER_NAME   (server name reported to clients; default rad-mcp)
# Pass both flags to run with a read-only AND a read-write token at once.
#
# TLS NOTE: Claude Desktop (and most hosted MCP clients) only connect to HTTPS
# endpoints. Provide --tls-cert + --tls-key (PEM files) or answer the
# interactive prompt. Without TLS the server runs plain HTTP — only clients
# that accept plain-HTTP endpoints (e.g. local VS Code / Codex) will connect.
#
# KNOWLEDGE CATALOG (optional): build/rad-knowledge.sqlite is the MIB catalog the
# mib_* tools + served-mode clients read (a gitignored build artifact). It is
# listed in the saved-config summary and kept as-is when you answer "Keep this
# configuration (incl. MIBs)" — no separate MIB question then. Otherwise the
# script asks interactively (a y/N question): if a catalog is present it offers to
# rebuild it (default keep); if absent it offers to build one (default skip).
# Answering y prompts for a MIB directory and builds it (auto-installs pysmi).
# --build-catalog is an optional non-interactive shortcut that auto-answers y.

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_common.sh"

HOST=""; PORT="8080"; READ_TOKEN=""; WRITE_TOKEN=""; TLS_CERT=""; TLS_KEY=""; NEW_TOKENS=""; NAME="rad-mcp"; BUILD_CATALOG=""; KEEP_DEVICES=""; RESET_DEVICES=""
while [ $# -gt 0 ]; do
    case "$1" in
        --host) HOST="$2"; shift 2 ;;
        --port) PORT="$2"; shift 2 ;;
        --read-token) READ_TOKEN="$2"; shift 2 ;;
        --write-token) WRITE_TOKEN="$2"; shift 2 ;;
        --name) NAME="$2"; shift 2 ;;
        --new-tokens) NEW_TOKENS=1; shift ;;
        --tls-cert) TLS_CERT="$2"; shift 2 ;;
        --tls-key) TLS_KEY="$2"; shift 2 ;;
        --build-catalog) BUILD_CATALOG=1; shift ;;
        --keep-devices) KEEP_DEVICES=1; shift ;;
        --reset-devices) RESET_DEVICES=1; shift ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done

assert_common_setup

# --- Device inventory: use existing devices, or reset everything ------------
# "Reset" empties inventory.yaml AND strips every device secret (usernames,
# passwords, SNMP communities) from server/.env — server config keys (tokens,
# TLS, name) are preserved, and both files get a timestamped .bak first.
if [ -n "$KEEP_DEVICES" ] && [ -n "$RESET_DEVICES" ]; then
    echo "--keep-devices and --reset-devices are mutually exclusive." >&2; exit 1
fi
DEV_COUNT=0
if [ -f "$INVENTORY" ]; then
    DEV_COUNT=$(grep -Ec '^[[:space:]]*-[[:space:]]*name[[:space:]]*:' "$INVENTORY" || true)
fi
if [ "$DEV_COUNT" -gt 0 ] && [ -z "$KEEP_DEVICES" ]; then
    DO_RESET="$RESET_DEVICES"
    if [ -z "$RESET_DEVICES" ]; then
        echo ""
        echo "Existing device inventory found: $DEV_COUNT device(s) in inventory.yaml."
        printf "Use existing devices, or reset (remove ALL devices incl. passwords + SNMP communities)? [use/reset] (default use): "
        read -r ANS
        case "$ANS" in r|reset|R|RESET|Reset) DO_RESET=1 ;; esac
    fi
    if [ -n "$DO_RESET" ]; then
        "$VENV_PYTHON" "$RAD_ROOT/scripts/reset_devices.py" || { echo "device reset failed — nothing was started." >&2; exit 1; }
    else
        echo "  devices -> keeping the existing inventory ($DEV_COUNT device(s))."
    fi
fi

# --- HTTP/HTTPS mode ---
# Tokens persist across restarts in this gitignored file so a restart reuses the
# same values (no need to reconfigure clients). Delete it or pass --new-tokens
# to regenerate.
TOKEN_STORE="$RAD_ROOT/server/.rad-mcp-tokens"

# Full HTTP configuration (bind host / port / name / TLS paths) persists here so
# a restart can reuse everything without re-answering any prompt. Tokens stay in
# $TOKEN_STORE (above). Both files live in server/ and are gitignored.
CONFIG_STORE="$RAD_ROOT/server/.rad-mcp-http-config"
KEEP_CONFIG=""

# Did the user override anything on the command line? (PORT/NAME have defaults,
# so compare against them.)
EXPLICIT=""
[ -n "$HOST$READ_TOKEN$WRITE_TOKEN$TLS_CERT$TLS_KEY$NEW_TOKENS" ] && EXPLICIT=1
[ "$PORT" != "8080" ] && EXPLICIT=1
[ "$NAME" != "rad-mcp" ] && EXPLICIT=1

# Offer to keep a prior configuration only when nothing was overridden and a
# saved config exists. "Yes" reuses it all and skips every prompt below; "No"
# falls through to the full interactive setup (today's flow).
if [ -z "$EXPLICIT" ] && [ -f "$CONFIG_STORE" ]; then
    # shellcheck disable=SC1090
    . "$CONFIG_STORE"
    saved_host="${RAD_MCP_HOST:-}"; saved_port="${RAD_MCP_PORT:-}"
    saved_name="${RAD_MCP_SERVER_NAME:-}"
    saved_cert="${RAD_MCP_TLS_CERT:-}"; saved_key="${RAD_MCP_TLS_KEY:-}"
    echo "Found a saved configuration from a previous run ($CONFIG_STORE):"
    echo "    bind host : $saved_host"
    echo "    port      : $saved_port"
    echo "    name      : $saved_name"
    if [ -n "$saved_cert" ]; then echo "    TLS       : HTTPS ($saved_cert)"; else echo "    TLS       : none (plain HTTP)"; fi
    echo "    tokens    : reused from .rad-mcp-tokens"
    if [ -f "$RAD_ROOT/build/rad-knowledge.sqlite" ]; then
        echo "    MIBs      : catalog present ($(( $(stat -c%s "$RAD_ROOT/build/rad-knowledge.sqlite" 2>/dev/null || echo 0) / 1048576 )) MB) - kept as-is"
    else
        echo "    MIBs      : no catalog (MIB tools disabled) - kept as-is"
    fi
    read -r -p "Keep this configuration (incl. MIBs)? [Y/n]: " keep_ans || keep_ans=""
    case "$keep_ans" in
        n|N|no|No) echo "Reconfiguring from scratch." ;;
        *)
            KEEP_CONFIG=1
            HOST="$saved_host"; PORT="${saved_port:-$PORT}"; NAME="${saved_name:-$NAME}"
            TLS_CERT="$saved_cert"; TLS_KEY="$saved_key"
            if [ -n "$TLS_CERT" ] && [ ! -f "$TLS_CERT" ]; then
                echo "  WARNING: saved TLS cert not found ($TLS_CERT) — starting without TLS."
                TLS_CERT="" TLS_KEY=""
            fi
            echo "Keeping saved configuration (tokens still loaded below)."
            ;;
    esac
    echo ""
fi

# Bind address — offer loopback, this host's LAN IP, or all interfaces.
if [ -z "$KEEP_CONFIG" ] && [ -z "$HOST" ]; then
    ip="$(_first_ipv4)"
    echo "Bind address (RAD_MCP_HOST):"
    echo "  1) 127.0.0.1     (this machine only)"
    [ -n "$ip" ] && echo "  2) $ip     (this host's LAN address — reachable by other machines)"
    echo "  3) 0.0.0.0       (all interfaces)"
    read -r -p "Choice [1]: " hans || hans=""
    case "$hans" in
        ""|1) HOST="127.0.0.1" ;;
        2) HOST="${ip:-127.0.0.1}" ;;
        3) HOST="0.0.0.0" ;;
        *) HOST="$hans" ;;
    esac
fi

# Token — reuse saved tokens across restarts; otherwise generate and save them.
FROM_STORE=""
if [ -z "$READ_TOKEN" ] && [ -z "$WRITE_TOKEN" ] && [ "$NEW_TOKENS" != "1" ] && [ -f "$TOKEN_STORE" ]; then
    # shellcheck disable=SC1090
    . "$TOKEN_STORE"
    WRITE_TOKEN="${RAD_MCP_WRITE_TOKENS:-}"
    READ_TOKEN="${RAD_MCP_TOKENS:-}"
    if [ -n "$WRITE_TOKEN" ] || [ -n "$READ_TOKEN" ]; then
        FROM_STORE=1
        echo "Reusing saved tokens from $TOKEN_STORE (--new-tokens to regenerate):"
        [ -n "$WRITE_TOKEN" ] && echo "    read-write (RAD_MCP_WRITE_TOKENS):  $WRITE_TOKEN"
        [ -n "$READ_TOKEN" ]  && echo "    read-only  (RAD_MCP_TOKENS):        $READ_TOKEN"
        echo ""
    fi
fi

if [ -z "$READ_TOKEN" ] && [ -z "$WRITE_TOKEN" ]; then
    echo "No token given. Generate bearer token(s):"
    echo "  1) read-write only  (manage devices + config)"
    echo "  2) read-only only   (reads only)"
    echo "  3) both             (one read-write + one read-only — hand out either)"
    read -r -p "Choice [3]: " rans || rans=""
    case "$rans" in
        1) WRITE_TOKEN="$(_gen_token)" ;;
        2) READ_TOKEN="$(_gen_token)" ;;
        *) WRITE_TOKEN="$(_gen_token)"; READ_TOKEN="$(_gen_token)" ;;
    esac
    if [ -z "$WRITE_TOKEN" ] && [ -z "$READ_TOKEN" ]; then
        echo "could not auto-generate a token (no python found); rerun with --read-token/--write-token" >&2
        exit 1
    fi
    echo ""
    echo "  Generated token(s) — give each to whichever client you choose:"
    [ -n "$WRITE_TOKEN" ] && echo "    read-write (RAD_MCP_WRITE_TOKENS):  $WRITE_TOKEN"
    [ -n "$READ_TOKEN" ]  && echo "    read-only  (RAD_MCP_TOKENS):        $READ_TOKEN"
    echo ""
    echo "  A client's Authorization: Bearer <value> must match one of these exactly,"
    echo "  or it gets 401 Unauthorized. The role follows whichever token it uses."
    echo ""
fi

# Persist the tokens (unless they were just loaded from the store) so the next
# restart reuses them without reconfiguring clients.
if [ -z "$FROM_STORE" ] && { [ -n "$WRITE_TOKEN" ] || [ -n "$READ_TOKEN" ]; }; then
    ( umask 077
      {
        [ -n "$WRITE_TOKEN" ] && echo "RAD_MCP_WRITE_TOKENS='$WRITE_TOKEN'"
        [ -n "$READ_TOKEN" ]  && echo "RAD_MCP_TOKENS='$READ_TOKEN'"
      } > "$TOKEN_STORE" )
    chmod 600 "$TOKEN_STORE" 2>/dev/null || true
    echo "Saved tokens to $TOKEN_STORE (gitignored; reused on next start)."
    echo ""
fi

# TLS — prompt interactively when not supplied as flags.
# Required for Claude Desktop and other HTTPS-only clients.
if [ -z "$KEEP_CONFIG" ] && [ -z "$TLS_CERT" ] && [ -z "$TLS_KEY" ]; then
    TLS_DIR="$RAD_ROOT/server/tls"
    DEFAULT_CERT="$TLS_DIR/rad-mcp.crt"
    DEFAULT_KEY="$TLS_DIR/rad-mcp.key"
    CERT_EXISTS=0 KEY_EXISTS=0
    [ -f "$DEFAULT_CERT" ] && CERT_EXISTS=1
    [ -f "$DEFAULT_KEY" ]  && KEY_EXISTS=1

    echo ""
    echo "TLS configuration (required for Claude Desktop and other HTTPS-only clients):"
    if [ "$CERT_EXISTS" = "1" ] && [ "$KEY_EXISTS" = "1" ]; then
        echo "  Found existing cert from previous run: $DEFAULT_CERT"
        echo "  1) No TLS       - plain HTTP (delete the old cert); only plain-HTTP clients (local VS Code/Codex) will connect"
        echo "  2) Reuse cert   - HTTPS; use the existing certificate"
        echo "  3) Self-signed  - HTTPS; generate a new cert + key (replaces the old one)"
        echo "  4) Imported     - HTTPS; provide paths to different PEM cert + key files"
        read -r -p "Choice [2]: " tls_ans || tls_ans=""
        case "$tls_ans" in
            1|no|No)
                echo "  Deleting old certificate..."
                rm -f "$DEFAULT_CERT" "$DEFAULT_KEY"
                TLS_CERT="" TLS_KEY=""
                ;;
            2|reuse|Reuse)
                TLS_CERT="$DEFAULT_CERT"
                TLS_KEY="$DEFAULT_KEY"
                ;;
            3|self|Self)
                TLS_CERT="$DEFAULT_CERT"
                TLS_KEY="$DEFAULT_KEY"
                mkdir -p "$TLS_DIR"
                echo "  Generating self-signed certificate (10 years) ..."
                "$VENV_PYTHON" - "$TLS_CERT" "$TLS_KEY" "$HOST" <<'PY'
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
PY
                chmod 600 "$TLS_KEY"
                echo "  NOTE: clients must trust or skip-verify this self-signed cert."
                ;;
            4|imp|Imp|import|Import)
                read -r -p "Path to TLS certificate PEM: " TLS_CERT || TLS_CERT=""
                read -r -p "Path to TLS private key PEM: "  TLS_KEY  || TLS_KEY=""
                ;;
            *)
                TLS_CERT="$DEFAULT_CERT"
                TLS_KEY="$DEFAULT_KEY"
                ;;
        esac
    else
        echo "  1) No TLS       - plain HTTP; only plain-HTTP clients (local VS Code/Codex) will connect"
        echo "  2) Self-signed  - HTTPS; generate a new cert + key automatically (fastest)"
        echo "  3) Imported     - HTTPS; provide paths to existing PEM cert + key files"
        read -r -p "Choice [1]: " tls_ans || tls_ans=""
        case "$tls_ans" in
            2|self|Self)
                mkdir -p "$TLS_DIR"
                TLS_CERT="$DEFAULT_CERT"
                TLS_KEY="$DEFAULT_KEY"
                echo "  Generating self-signed certificate (10 years) ..."
                "$VENV_PYTHON" - "$TLS_CERT" "$TLS_KEY" "$HOST" <<'PY'
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
PY
                chmod 600 "$TLS_KEY"
                echo "  NOTE: clients must trust or skip-verify this self-signed cert."
                ;;
            3|imp|Imp|import|Import)
                read -r -p "Path to TLS certificate PEM: " TLS_CERT || TLS_CERT=""
                read -r -p "Path to TLS private key PEM: "  TLS_KEY  || TLS_KEY=""
                ;;
        esac
    fi
fi
# TLS is all-or-nothing (the server also enforces this).
if [ -n "$TLS_CERT$TLS_KEY" ] && { [ -z "$TLS_CERT" ] || [ -z "$TLS_KEY" ]; }; then
    echo "--tls-cert and --tls-key must be given together." >&2
    exit 1
fi

# Persist the full resolved configuration so the next start can offer to reuse
# it with a single "keep?" prompt (tokens are saved separately in $TOKEN_STORE).
( umask 077
  {
    echo "RAD_MCP_HOST='$HOST'"
    echo "RAD_MCP_PORT='$PORT'"
    echo "RAD_MCP_SERVER_NAME='$NAME'"
    echo "RAD_MCP_TLS_CERT='$TLS_CERT'"
    echo "RAD_MCP_TLS_KEY='$TLS_KEY'"
  } > "$CONFIG_STORE" )
[ -z "$KEEP_CONFIG" ] && { echo "Saved configuration to $CONFIG_STORE (reused on next start)."; echo ""; }

export RAD_MCP_TRANSPORT="http"
export RAD_MCP_SERVER_NAME="$NAME"
export RAD_MCP_HOST="$HOST"
export RAD_MCP_PORT="$PORT"
export RAD_MCP_INVENTORY="$INVENTORY"
[ -n "$READ_TOKEN" ] && export RAD_MCP_TOKENS="$READ_TOKEN" || unset RAD_MCP_TOKENS
[ -n "$WRITE_TOKEN" ] && export RAD_MCP_WRITE_TOKENS="$WRITE_TOKEN" || unset RAD_MCP_WRITE_TOKENS
[ -n "$TLS_CERT" ] && export RAD_MCP_TLS_CERT="$TLS_CERT" || unset RAD_MCP_TLS_CERT
[ -n "$TLS_KEY" ] && export RAD_MCP_TLS_KEY="$TLS_KEY" || unset RAD_MCP_TLS_KEY

# Restart: if a server is already listening on this port, stop it first.
pids=""
if command -v lsof >/dev/null 2>&1; then
    pids="$(lsof -ti tcp:"$PORT" -sTCP:LISTEN 2>/dev/null || true)"
elif command -v fuser >/dev/null 2>&1; then
    pids="$(fuser "$PORT/tcp" 2>/dev/null | tr -s ' ' | sed 's/^ *//' || true)"
fi
if [ -n "$pids" ]; then
    echo "Port $PORT already in use — stopping existing server (PID: $pids) ..."
    # shellcheck disable=SC2086
    kill $pids 2>/dev/null || true
    sleep 1
    for p in $pids; do
        if kill -0 "$p" 2>/dev/null; then kill -9 "$p" 2>/dev/null || true; fi
    done
fi

scheme="http"; [ -n "$TLS_CERT" ] && scheme="https"
[ -n "$WRITE_TOKEN" ] && echo "  read-write token (RAD_MCP_WRITE_TOKENS): $WRITE_TOKEN"
[ -n "$READ_TOKEN" ]  && echo "  read-only  token (RAD_MCP_TOKENS):        $READ_TOKEN"
if [ -n "$TLS_CERT" ]; then
    echo "  TLS cert: $TLS_CERT"
    echo "  TLS key:  $TLS_KEY"
    echo "  (FastMCP logs 'transport http' — transport name, not scheme; Uvicorn confirms https://)"
fi
# Knowledge catalog (OPTIONAL) — the MIB tools (mib_search/describe/table/...)
# and served-mode clients read build/rad-knowledge.sqlite. Always ASK about MIBs
# interactively: if a catalog is present, offer to rebuild it (default: keep);
# if absent, offer to build one (default: skip). Either way the answer is a
# y/N prompt, not a flag. --build-catalog is only an optional non-interactive
# shortcut (auto-yes to the build question).
CATALOG="$RAD_ROOT/build/rad-knowledge.sqlite"
show_catalog_present() {
    echo "  knowledge catalog: present ($(( $(stat -c%s "$CATALOG" 2>/dev/null || echo 0) / 1048576 )) MB) - MIB tools + served-mode supported"
}
if [ -f "$CATALOG" ]; then
    CATALOG_PRESENT=1
    show_catalog_present
else
    CATALOG_PRESENT=0
    echo "  knowledge catalog: not present. It powers the MIB tools (mib_search/describe/table/...);"
    echo "  CLI + bundled knowledge work fine without it."
fi

DO_BUILD=""
if [ "$BUILD_CATALOG" = "1" ]; then
    DO_BUILD=1
elif [ "$KEEP_CONFIG" = "1" ]; then
    DO_BUILD=""   # "keep configuration (incl. MIBs)" already covered the catalog — don't ask again
else
    if [ "$CATALOG_PRESENT" = "1" ]; then
        printf "  Rebuild the MIB catalog from a MIB directory? (keep current if no) [y/N]: "
    else
        printf "  Add MIBs now - build the catalog from a MIB directory? [y/N]: "
    fi
    read -r ANS || ANS=""
    case "$ANS" in y|Y|yes|YES) DO_BUILD=1 ;; esac
fi

if [ "$DO_BUILD" = "1" ]; then
    printf "  Path to the MIB directory (folder with .mib files): "
    read -r MIB_DIR || MIB_DIR=""
    if [ -n "$MIB_DIR" ] && [ -d "$MIB_DIR" ]; then
        MIB_ABS="$(cd "$MIB_DIR" && pwd)"
        if ! "$VENV_PYTHON" -c "import pysmi" 2>/dev/null; then
            echo "  installing pysmi into the venv (one-time) ..."
            "$VENV_PYTHON" -m pip install --quiet pysmi
        fi
        echo "  building the catalog from $MIB_ABS (this can take a few minutes) ..."
        if "$VENV_PYTHON" "$RAD_ROOT/scripts/build_knowledge_catalog.py" --mib-root "$MIB_ABS" && [ -f "$CATALOG" ]; then
            show_catalog_present
        else
            echo "  WARNING: catalog build failed - continuing (see output above)."
        fi
    else
        echo "  WARNING: '$MIB_DIR' not found - continuing without (re)building."
    fi
elif [ "$CATALOG_PRESENT" != "1" ]; then
    echo "  building baseline knowledge catalog (CLI/manual/datasheets/reference docs; no extra MIB roots) ..."
    if "$VENV_PYTHON" "$RAD_ROOT/scripts/build_knowledge_catalog.py" && [ -f "$CATALOG" ]; then
        show_catalog_present
    else
        echo "  WARNING: baseline catalog build failed - continuing (see output above)."
    fi
fi
echo "Starting $NAME on ${scheme}://${HOST}:${PORT}/mcp  (Ctrl-C to stop)"
[ "$HOST" != "127.0.0.1" ] && echo "Reachable on the LAN — internal networks only, never a public interface."
(cd "$RAD_ROOT/server" && exec "$VENV_PYTHON" -m rad_mcp.server)
