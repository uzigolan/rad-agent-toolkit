#!/usr/bin/env bash
#
# Start the rad-mcp server over HTTP (manual launch — the terminal IS the
# server; closing it stops it). This does NOT configure any client; run the
# matching install-*.sh in http mode for that.
#
#   ./start-server.sh                       # interactive host/port/token prompts
#   ./start-server.sh --host 0.0.0.0 --port 8080 --write-token <t>
#   ./start-server.sh --read-token <t> --write-token <t> --tls-cert c.pem --tls-key k.pem
#
# At least one token is required (http refuses to start unauthenticated).
#   --read-token  -> RAD_MCP_TOKENS        (read-only clients)
#   --write-token -> RAD_MCP_WRITE_TOKENS  (read-write clients: manage devices + config)

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_common.sh"

HOST=""; PORT="8080"; READ_TOKEN=""; WRITE_TOKEN=""; TLS_CERT=""; TLS_KEY=""
while [ $# -gt 0 ]; do
    case "$1" in
        --host) HOST="$2"; shift 2 ;;
        --port) PORT="$2"; shift 2 ;;
        --read-token) READ_TOKEN="$2"; shift 2 ;;
        --write-token) WRITE_TOKEN="$2"; shift 2 ;;
        --tls-cert) TLS_CERT="$2"; shift 2 ;;
        --tls-key) TLS_KEY="$2"; shift 2 ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done

assert_common_setup

# Bind address — offer loopback, this host's LAN IP, or all interfaces.
if [ -z "$HOST" ]; then
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

# Token — need at least one; offer to generate with a chosen role.
if [ -z "$READ_TOKEN" ] && [ -z "$WRITE_TOKEN" ]; then
    echo "No token given. Grant a bearer token:"
    echo "  1) read-write (manage devices + config)"
    echo "  2) read-only  (reads only)"
    read -r -p "Choice [1]: " rans || rans=""
    tok="$(_gen_token)"
    if [ -z "$tok" ]; then
        echo "could not auto-generate a token (no python found); rerun with --read-token/--write-token" >&2
        exit 1
    fi
    case "$rans" in
        2) READ_TOKEN="$tok"; role="read-only (RAD_MCP_TOKENS)" ;;
        *) WRITE_TOKEN="$tok"; role="read-write (RAD_MCP_WRITE_TOKENS)" ;;
    esac
    echo ""
    echo "  Generated $role token — give this SAME value to the client:"
    echo ""
    echo "      $tok"
    echo ""
fi

# TLS is all-or-nothing (the server also enforces this).
if [ -n "$TLS_CERT$TLS_KEY" ] && { [ -z "$TLS_CERT" ] || [ -z "$TLS_KEY" ]; }; then
    echo "--tls-cert and --tls-key must be given together." >&2
    exit 1
fi

export RAD_MCP_TRANSPORT="http"
export RAD_MCP_HOST="$HOST"
export RAD_MCP_PORT="$PORT"
export RAD_MCP_INVENTORY="$INVENTORY"
[ -n "$READ_TOKEN" ] && export RAD_MCP_TOKENS="$READ_TOKEN"
[ -n "$WRITE_TOKEN" ] && export RAD_MCP_WRITE_TOKENS="$WRITE_TOKEN"
[ -n "$TLS_CERT" ] && export RAD_MCP_TLS_CERT="$TLS_CERT"
[ -n "$TLS_KEY" ] && export RAD_MCP_TLS_KEY="$TLS_KEY"

scheme="http"; [ -n "$TLS_CERT" ] && scheme="https"
echo "Starting rad-mcp on ${scheme}://${HOST}:${PORT}/mcp  (Ctrl-C to stop)"
[ "$HOST" != "127.0.0.1" ] && echo "Reachable on the LAN — internal networks only, never a public interface."
cd "$RAD_ROOT/server"
exec "$VENV_PYTHON" -m rad_mcp.server
