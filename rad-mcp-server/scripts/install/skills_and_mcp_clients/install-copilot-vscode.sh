#!/usr/bin/env bash
#
# Install rad-mcp (MCP + skills) for the GitHub Copilot VS Code extension.
#
#   ./install-copilot-vscode.sh                       # interactive transport prompt
#   ./install-copilot-vscode.sh --workspace <folder>  # set the target workspace
#   ./install-copilot-vscode.sh --http --url <url> --token <token>   # non-interactive http
#
# Writes/merges <workspace>/.vscode/mcp.json (root key "servers") and copies the
# skills to ~/.copilot/skills (read by Copilot in VS Code AND Copilot CLI).
# Replaces any existing rad-mcp entry. Afterwards: reload the VS Code window,
# accept the trust dialog, use agent mode.

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_common.sh"

WORKSPACE="$(pwd)"
while [ $# -gt 0 ]; do
    case "$1" in
        --workspace) WORKSPACE="$2"; shift 2 ;;
        --http) MODE=http; shift ;;
        --stdio) MODE=stdio; shift ;;
        --url) HTTP_URL="$2"; shift 2 ;;
        --token) HTTP_TOKEN="$2"; shift 2 ;;
        --reconfigure) RAD_RECONFIGURE=1; shift ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done

CFG="$WORKSPACE/.vscode/mcp.json"
maybe_keep_existing "$CFG" servers
if [ -n "$KEEP_EXISTING" ]; then
    echo "  mcp   -> kept existing rad-mcp entry in $CFG"
else
    prompt_transport

    if [ "$MODE" = http ]; then
        ENTRY="$(new_http_entry "$HTTP_URL" "$HTTP_TOKEN")"
    else
        assert_common_setup
        ENTRY="$(new_stdio_entry with-type)"
    fi
    set_json_mcp_entry "$CFG" servers "$ENTRY"
fi
copy_skills_to "$HOME/.copilot/skills"

echo ""
echo "Done. Now: reload the VS Code window, accept the MCP trust dialog,"
echo "switch Copilot Chat to AGENT mode, and try: 'list the managed devices'."
[ "$MODE" = http ] && echo "http mode: make sure the shared server is running, and its token matches this client's."
exit 0
