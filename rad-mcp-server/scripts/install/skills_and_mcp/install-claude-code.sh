#!/usr/bin/env bash
#
# Install rad-mcp (MCP + skills + slash commands) for Claude Code (CLI and the
# VS Code extension - both read the same plugin/config).
#
#   ./install-claude-code.sh                       # interactive transport prompt
#   ./install-claude-code.sh --http --url <url> --token <token>   # non-interactive http
#
# Stdio mode uses the plugin system (`claude` CLI must be on PATH): the plugin
# carries MCP registration, all 3 skills, and the 4 slash commands.
# Http mode removes any existing rad-mcp registration first, then adds the URL.
# Afterwards: reload the VS Code window / start a new claude session.

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_common.sh"

while [ $# -gt 0 ]; do
    case "$1" in
        --http) MODE=http; shift ;;
        --stdio) MODE=stdio; shift ;;
        --url) HTTP_URL="$2"; shift 2 ;;
        --token) HTTP_TOKEN="$2"; shift 2 ;;
        --name) NAME="$2"; shift 2 ;;   # http mode only; plugin/stdio uses the plugin's bundled name
        --reconfigure) RAD_RECONFIGURE=1; shift ;;
        --knowledge) RAD_KNOWLEDGE="$2"; shift 2 ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done
NAME="${NAME:-rad-mcp}"

if ! command -v claude >/dev/null 2>&1; then
    echo "the 'claude' CLI is not on PATH - install Claude Code first (https://claude.com/claude-code)" >&2
    exit 1
fi

# Keep an existing MCP registration unless flags/--reconfigure force a change.
# Skills refresh either way: http re-copies client-side; stdio re-installs the
# plugin (refreshes bundled skills + commands; same MCP registration).
if [ -z "$MODE" ] && [ -z "$HTTP_URL" ] && [ -z "$HTTP_TOKEN" ] && [ "${RAD_RECONFIGURE:-}" != "1" ]; then
    MCP_GET="$(claude mcp get "$NAME" 2>/dev/null || true)"
    if [ -n "$MCP_GET" ] || claude plugin list 2>/dev/null | grep -q 'rad-mcp'; then
        KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}")"
        echo "$NAME is already configured with Claude Code - keeping the MCP config."
        if printf '%s' "$MCP_GET" | grep -qi 'http'; then
            copy_skills_to "$HOME/.claude/skills" "$KMODE"
        else
            assert_common_setup
            REPO_ROOT="$(cd "$RAD_ROOT/.." && pwd)"
            claude plugin marketplace add "$REPO_ROOT"
            claude plugin install rad-mcp@rad-marketplace
            echo "  plugin -> refreshed rad-mcp@rad-marketplace (skills + commands; MCP unchanged)"
        fi
        echo ""
        echo "Done - kept MCP config, refreshed skills. Reload the VS Code window / start a new claude session."
        exit 0
    fi
fi

KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}" skip-installed)"

prompt_transport

if [ "$MODE" = http ]; then
    claude mcp remove "$NAME" 2>/dev/null || true
    claude mcp add --transport http "$NAME" "$HTTP_URL" --header "Authorization: Bearer $HTTP_TOKEN"
    echo "  mcp   -> http client of $HTTP_URL (read-only)"
    show_mcp_config_text "transport = http
url       = $HTTP_URL
header    = Authorization: Bearer $HTTP_TOKEN" "added MCP configuration (claude mcp, token masked):"
    # Skills still need a client-side install in http mode:
    copy_skills_to "$HOME/.claude/skills" "$KMODE"
else
    assert_common_setup
    REPO_ROOT="$(cd "$RAD_ROOT/.." && pwd)"
    claude plugin marketplace add "$REPO_ROOT"
    claude plugin install rad-mcp@rad-marketplace
    echo "  plugin -> rad-mcp@rad-marketplace (MCP + 3 skills + 4 commands)"
    show_mcp_config_text "$("$(_py)" -c 'import json,sys; print(json.dumps({"rad-mcp": json.loads(sys.argv[1])}, indent=2))' "$(new_stdio_entry)")" \
        "MCP configuration the plugin registers (stdio; the client launches the server):"
fi

echo ""
echo "Done. Now: reload the VS Code window / start a new claude session,"
echo "then verify with /mcp and try: /rad-health <device-name>."
[ "$MODE" = http ] && echo "http mode: make sure the shared server is running (read-only tools; slash commands need the plugin)."
exit 0
