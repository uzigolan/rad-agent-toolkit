#!/usr/bin/env bash
#
# Install rad-mcp (MCP + skills) for GitHub Copilot in JetBrains IDEs
# (IntelliJ IDEA, PyCharm, WebStorm, ...).
#
#   ./install-copilot-intellij.sh                       # interactive transport prompt
#   ./install-copilot-intellij.sh --http --url <url> --token <token>   # non-interactive http
#
# JetBrains Copilot has TWO agent paths with separate MCP configs, and this
# script wires BOTH (field-tested 2026-07-19):
#   - classic agent mode reads ~/.config/github-copilot/intellij/mcp.json
#     (root key "servers"; one file shared by ALL JetBrains IDEs)
#   - the embedded Copilot CLI agent (the chat with /mcp, /skills, /context)
#     reads ~/.copilot/mcp-config.json (+ mcp.json kept in sync)
# Also copies the skills to ~/.copilot/skills (the same folder Copilot CLI
# and VS Code read). Replaces any existing rad-mcp entry. Afterwards: restart
# the IDE, enable Agent Skills (Settings -> GitHub Copilot -> Chat), accept
# the MCP trust prompt, use agent mode.

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
KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}")"

case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*) CFG="$LOCALAPPDATA/github-copilot/intellij/mcp.json" ;;
    *) CFG="$HOME/.config/github-copilot/intellij/mcp.json" ;;
esac

maybe_keep_existing "$CFG" servers "$NAME"
if [ -n "$KEEP_EXISTING" ]; then
    echo "  mcp   -> kept existing $NAME entry in $CFG"
else
    prompt_transport

    if [ "$MODE" = http ]; then
        ENTRY="$(new_http_entry "$HTTP_URL" "$HTTP_TOKEN" request-init)"
        # CLI shape: plain headers plus tools:["*"] which Copilot CLI expects.
        CLI_ENTRY="$("$(_py)" - "$HTTP_URL" "$HTTP_TOKEN" <<'PY'
import json, sys
url, token = sys.argv[1], sys.argv[2]
print(json.dumps({"type": "http", "url": url,
                  "headers": {"Authorization": f"Bearer {token}"},
                  "tools": ["*"]}))
PY
)"
    else
        assert_common_setup
        ENTRY="$(new_stdio_entry with-type)"
        # Copilot CLI's stdio type is "local" and has no cwd support (safe —
        # the server's own paths are module-anchored).
        CLI_ENTRY="$("$(_py)" - "$VENV_PYTHON" "$INVENTORY" <<'PY'
import json, sys
venv, inv = sys.argv[1], sys.argv[2]
print(json.dumps({"type": "local", "command": venv,
                  "args": ["-m", "rad_mcp.server"],
                  "env": {"RAD_MCP_INVENTORY": inv},
                  "tools": ["*"]}))
PY
)"
    fi
    set_json_mcp_entry "$CFG" servers "$ENTRY" "$NAME"
    # The embedded Copilot CLI agent inside the IDE chat ignores the intellij
    # mcp.json and reads the Copilot CLI config — write the same server there.
    for cli_cfg in "$HOME/.copilot/mcp-config.json" "$HOME/.copilot/mcp.json"; do
        backup_json_config "$cli_cfg"
        set_json_mcp_entry "$cli_cfg" mcpServers "$CLI_ENTRY" "$NAME"
    done
fi
show_served_catalog_hint "$KMODE" "$MODE" "${HTTP_URL:-}"
copy_skills_to "$HOME/.copilot/skills" "$KMODE"

echo ""
echo "Done. Now: restart the JetBrains IDE, enable Agent Skills"
echo "(Settings -> GitHub Copilot -> Chat), accept the MCP trust prompt,"
echo "switch Copilot Chat to AGENT mode and START A NEW CHAT, then verify:"
echo "  /mcp list      -> rad-mcp next to the builtin github-mcp-server"
echo "  /skills list   -> the three rad skills (typing / alone won't list them)"
echo "  'rad agent, list the managed devices'"
echo "NOTE: needs the OFFICIAL 'GitHub Copilot' plugin (by GitHub); the"
echo "JetBrains AI Assistant plugin/settings pages show none of this."
[ "$MODE" = http ] && echo "http mode: make sure the shared server is running, and its token matches this client's."
exit 0
