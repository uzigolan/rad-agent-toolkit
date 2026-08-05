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

# The marketplace/plugin manifests are machine-local (gitignored, absolute
# venv paths) - generate them so `claude plugin marketplace add` finds a valid
# marketplace. rad-mcp-server/ itself is both marketplace and plugin root
# (skills/ and commands/ already live there).
install_rad_plugin() {
    local mp_dir="$RAD_ROOT/.claude-plugin" desc ver
    mkdir -p "$mp_dir"
    desc='Operate RAD Data Communications devices (SecFlow, ETX-1p, ETX-2) - staged-commit config safety, harvested CLI reference + manuals, SNMP/MIB tools.'
    ver="$(sed -n 's/^__version__ = "\(.*\)"/\1/p' "$RAD_ROOT/server/rad_mcp/__init__.py" 2>/dev/null)"
    ver="${ver:-0.0.0}"
    printf '{\n  "name": "rad-mcp",\n  "version": "%s",\n  "description": "%s"\n}\n' "$ver" "$desc" > "$mp_dir/plugin.json"
    printf '{\n  "name": "rad-marketplace",\n  "owner": { "name": "RAD" },\n  "plugins": [\n    { "name": "rad-mcp", "source": "./", "description": "%s" }\n  ]\n}\n' "$desc" > "$mp_dir/marketplace.json"
    # Plugin-root .mcp.json: the MCP registration the plugin carries.
    "$(_py)" -c 'import json,sys; print(json.dumps({"mcpServers": {"rad-mcp": json.loads(sys.argv[1])}}, indent=2))' "$(new_stdio_entry)" > "$RAD_ROOT/.mcp.json"
    # Re-add so the marketplace path is always current.
    claude plugin marketplace remove rad-marketplace 2>/dev/null || true
    claude plugin marketplace add "$RAD_ROOT"
    claude plugin install rad-mcp@rad-marketplace
}

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
            install_rad_plugin
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
    claude mcp remove --scope user "$NAME" 2>/dev/null || true
    claude mcp remove "$NAME" 2>/dev/null || true
    # user scope -> global registration (~/.claude.json), available in every project
    claude mcp add --scope user --transport http "$NAME" "$HTTP_URL" --header "Authorization: Bearer $HTTP_TOKEN"
    echo "  mcp   -> http client of $HTTP_URL (read-only)"
    show_mcp_config_text "transport = http
url       = $HTTP_URL
header    = Authorization: Bearer $HTTP_TOKEN" "added MCP configuration (claude mcp, token masked):"
    # Skills still need a client-side install in http mode:
    copy_skills_to "$HOME/.claude/skills" "$KMODE"
else
    assert_common_setup
    install_rad_plugin
    echo "  plugin -> rad-mcp@rad-marketplace (MCP + skills + commands)"
    show_mcp_config_text "$("$(_py)" -c 'import json,sys; print(json.dumps({"rad-mcp": json.loads(sys.argv[1])}, indent=2))' "$(new_stdio_entry)")" \
        "MCP configuration the plugin registers (stdio; the client launches the server):"
fi

echo ""
echo "Done. Now: reload the VS Code window / start a new claude session,"
echo "then verify with /mcp and try: /rad-health <device-name>."
[ "$MODE" = http ] && echo "http mode: make sure the shared server is running (read-only tools; slash commands need the plugin)."
exit 0
