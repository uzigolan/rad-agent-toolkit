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

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_common.sh"

while [ $# -gt 0 ]; do
    case "$1" in
        --http) MODE=http; shift ;;
        --stdio) MODE=stdio; shift ;;
        --url) HTTP_URL="$2"; shift 2 ;;
        --token) HTTP_TOKEN="$2"; shift 2 ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done

if ! command -v claude >/dev/null 2>&1; then
    echo "the 'claude' CLI is not on PATH - install Claude Code first (https://claude.com/claude-code)" >&2
    exit 1
fi

prompt_transport

if [ "$MODE" = http ]; then
    claude mcp remove rad-mcp 2>/dev/null || true
    claude mcp add --transport http rad-mcp "$HTTP_URL" --header "Authorization: Bearer $HTTP_TOKEN"
    echo "  mcp   -> http client of $HTTP_URL (read-only)"
    # Skills still need a client-side install in http mode:
    copy_skills_to "$HOME/.claude/skills"
else
    assert_common_setup
    REPO_ROOT="$(cd "$RAD_ROOT/.." && pwd)"
    claude plugin marketplace add "$REPO_ROOT"
    claude plugin install rad-mcp@rad-marketplace
    echo "  plugin -> rad-mcp@rad-marketplace (MCP + 3 skills + 4 commands)"
fi

echo ""
echo "Done. Now: reload the VS Code window / start a new claude session,"
echo "then verify with /mcp and try: /rad-health <device-name>."
[ "$MODE" = http ] && echo "http mode: make sure the shared server is running (read-only tools; slash commands need the plugin)."
exit 0
