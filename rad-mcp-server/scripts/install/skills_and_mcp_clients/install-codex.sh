#!/usr/bin/env bash
#
# Install rad-mcp (MCP + skills) for OpenAI Codex (CLI / IDE extension / ChatGPT
# desktop - all three share ~/.codex/config.toml).
#
#   ./install-codex.sh                       # interactive transport prompt
#   ./install-codex.sh --http --url <url> --token <token>   # non-interactive http
#
# Appends a [mcp_servers.rad-mcp] section to ~/.codex/config.toml (refuses if
# one already exists - TOML is edited as text, remove the old section first)
# and copies the skills to ~/.agents/skills. Afterwards: restart Codex.

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_common.sh"

while [ $# -gt 0 ]; do
    case "$1" in
        --http) MODE=http; shift ;;
        --stdio) MODE=stdio; shift ;;
        --url) HTTP_URL="$2"; shift 2 ;;
        --token) HTTP_TOKEN="$2"; shift 2 ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done

CFG_PATH="$HOME/.codex/config.toml"
if [ -f "$CFG_PATH" ] && grep -q '\[mcp_servers\.rad-mcp\]' "$CFG_PATH"; then
    echo "$CFG_PATH already has a [mcp_servers.rad-mcp] section - remove or edit" >&2
    echo "that section first (disable-previous rule), then rerun." >&2
    exit 1
fi

# Backup before modifying
if [ -f "$CFG_PATH" ]; then
    ts=$(date +%Y%m%d-%H%M%S)
    backup="$CFG_PATH.bak.$ts"
    cp "$CFG_PATH" "$backup"
    echo "  backup -> $backup"
fi

prompt_transport

if [ "$MODE" = http ]; then
    BLOCK="
# rad-mcp - http client: server runs manually (read-only by the code interlock)
[mcp_servers.rad-mcp]
url = \"$HTTP_URL\"
http_headers = { Authorization = \"Bearer $HTTP_TOKEN\" }
"
else
    assert_common_setup
    BLOCK="
# rad-mcp - stdio: Codex launches its own instance (full toolset incl. staged writes)
[mcp_servers.rad-mcp]
command = \"$RAD_ROOT/server/.venv/bin/python\"
args = [\"-m\", \"rad_mcp.server\"]
cwd = \"$RAD_ROOT/server\"
env = { RAD_MCP_INVENTORY = \"$INVENTORY\" }
startup_timeout_sec = 20
"
fi

mkdir -p "$(dirname "$CFG_PATH")"
printf '%s\n' "$BLOCK" >> "$CFG_PATH"
echo "  mcp   -> $CFG_PATH"
copy_skills_to "$HOME/.agents/skills"

echo ""
echo "Done. Now: restart Codex (config + skills load at startup), then verify"
echo "with /mcp and /skills. Explicit skill call: \$rad-cli-operations"
[ "$MODE" = http ] && echo "http mode: make sure the shared server is running (read-only tools)."
exit 0
