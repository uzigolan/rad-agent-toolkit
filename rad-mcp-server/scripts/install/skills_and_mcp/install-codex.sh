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
        --name) NAME="$2"; shift 2 ;;
        --reconfigure) RAD_RECONFIGURE=1; shift ;;
        --knowledge) RAD_KNOWLEDGE="$2"; shift 2 ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done
NAME="${NAME:-rad-mcp}"

CFG_PATH="$HOME/.codex/config.toml"
if [ -f "$CFG_PATH" ] && grep -q "\[mcp_servers\.${NAME}\]" "$CFG_PATH"; then
    # By default keep the existing MCP config and just refresh the skills.
    if [ -z "$MODE" ] && [ -z "$HTTP_URL" ] && [ -z "$HTTP_TOKEN" ] && [ "${RAD_RECONFIGURE:-}" != "1" ]; then
        KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}")"
        echo "$NAME is already configured in $CFG_PATH: keeping it (pass --reconfigure to replace)."
        copy_skills_to "$HOME/.agents/skills" "$KMODE"
        echo ""
        echo "Done - kept existing MCP config, refreshed skills. Restart Codex."
        exit 0
    fi
    # Reconfigure requested, but TOML sections are text: remove the old one first.
    echo "$CFG_PATH already has a [mcp_servers.$NAME] section - TOML is edited as" >&2
    echo "text, so remove that section by hand first, then rerun." >&2
    exit 1
fi

KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}" skip-installed)"

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
# $NAME - http client: server runs manually (read-only by the code interlock)
[mcp_servers.$NAME]
url = \"$HTTP_URL\"
http_headers = { Authorization = \"Bearer $HTTP_TOKEN\" }
"
else
    assert_common_setup
    BLOCK="
# $NAME - stdio: Codex launches its own instance (full toolset incl. staged writes)
[mcp_servers.$NAME]
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
show_mcp_config_text "$BLOCK"
copy_skills_to "$HOME/.agents/skills" "$KMODE"

echo ""
echo "Done. Now: restart Codex (config + skills load at startup), then verify"
echo "with /mcp and /skills. Explicit skill call: \$rad-cli-operations"
[ "$MODE" = http ] && echo "http mode: make sure the shared server is running (read-only tools)."
exit 0
