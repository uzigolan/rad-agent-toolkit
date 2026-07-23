#!/usr/bin/env bash
#
# Install rad-mcp (MCP + skills) for the GitHub Copilot CLI (`copilot`).
#
#   ./install-copilot-cli.sh                       # interactive transport prompt
#   ./install-copilot-cli.sh --http --url <url> --token <token>   # non-interactive http
#
# Writes/merges ~/.copilot/mcp-config.json AND ~/.copilot/mcp.json (root key
# "mcpServers" — CLI versions disagree on the filename, so both are kept in
# sync; the embedded Copilot CLI agent in JetBrains IDEs reads mcp-config.json,
# field-tested 2026-07-19) and copies the skills to ~/.copilot/skills.
# Replaces any existing rad-mcp entry.
# Afterwards: RESTART the copilot session (skills + MCP load at startup only).

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

# Both filenames the CLI has used; kept in sync (mcp-config.json is what the
# JetBrains-embedded CLI agent reads).
CFG="$HOME/.copilot/mcp-config.json"
CFG_ALT="$HOME/.copilot/mcp.json"
maybe_keep_existing "$CFG" mcpServers "$NAME"
if [ -n "$KEEP_EXISTING" ]; then
    KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}")"
    echo "  mcp   -> kept existing $NAME entry in $CFG"
else
    KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}" skip-installed)"
    prompt_transport

    if [ "$MODE" = http ]; then
        # http entry plus tools:["*"] which Copilot CLI expects.
        ENTRY="$("$(_py)" - "$HTTP_URL" "$HTTP_TOKEN" <<'PY'
import json, sys
url, token = sys.argv[1], sys.argv[2]
print(json.dumps({"type": "http", "url": url,
                  "headers": {"Authorization": f"Bearer {token}"},
                  "tools": ["*"]}))
PY
)"
    else
        assert_common_setup
        # Copilot CLI's stdio type is "local" and has no cwd support (the server's
        # own paths are module-anchored, so that's safe).
        ENTRY="$("$(_py)" - "$VENV_PYTHON" "$INVENTORY" <<'PY'
import json, sys
venv, inv = sys.argv[1], sys.argv[2]
print(json.dumps({"type": "local", "command": venv,
                  "args": ["-m", "rad_mcp.server"],
                  "env": {"RAD_MCP_INVENTORY": inv},
                  "tools": ["*"]}))
PY
)"
    fi
    backup_json_config "$CFG"
    backup_json_config "$CFG_ALT"
    set_json_mcp_entry "$CFG" mcpServers "$ENTRY" "$NAME"
    set_json_mcp_entry "$CFG_ALT" mcpServers "$ENTRY" "$NAME"
fi
copy_skills_to "$HOME/.copilot/skills" "$KMODE"

echo ""
echo "Done. Now: restart the copilot session, then verify with /mcp show and /skills list."
echo "First tool call prompts for permission - answer 'yes, always'."
[ "$MODE" = http ] && echo "http mode: make sure the shared server is running, and its token matches this client's."
exit 0
