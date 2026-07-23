#!/usr/bin/env bash
#
# Install rad-mcp (MCP + skills) for Claude Desktop.
#
#   ./install-claude-desktop.sh
#
# Backs up the Claude Desktop config file (new Windows Store or traditional),
# then merges the new rad-mcp entry (replacing any existing one).  Rebuilds
# the skill zips and opens the zip folder - the upload itself is manual
# (Customize -> Skills).
#
# Transport:
#   stdio only - Desktop launches the server itself (full toolset incl. staged writes).

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_common.sh"

NAME="rad-mcp"
while [ $# -gt 0 ]; do
    case "$1" in
        --name) NAME="$2"; shift 2 ;;
        --knowledge) RAD_KNOWLEDGE="$2"; shift 2 ;;
        --reconfigure) RAD_RECONFIGURE=1; shift ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done

assert_common_setup

case "$(uname -s)" in
    Darwin) CFG_PATH="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
            OPEN_CMD=open ;;
    MINGW*|MSYS*|CYGWIN*)
        # Windows: check Store packaged path first
        if [ -d "$LOCALAPPDATA/Packages/Claude_pzs8sxrjxfjjc/LocalCache/Roaming/Claude" ]; then
            CFG_PATH="$LOCALAPPDATA/Packages/Claude_pzs8sxrjxfjjc/LocalCache/Roaming/Claude/claude_desktop_config.json"
        else
            CFG_PATH="$APPDATA/Claude/claude_desktop_config.json"
        fi
        OPEN_CMD=explorer ;;
    *)      CFG_PATH="$HOME/.config/Claude/claude_desktop_config.json"
            OPEN_CMD=xdg-open ;;
esac

# Keep an existing MCP entry unless --reconfigure. Skills are rebuilt regardless.
maybe_keep_existing "$CFG_PATH" mcpServers "$NAME"
if [ -n "$KEEP_EXISTING" ]; then
    KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}")"
    echo "  mcp   -> kept existing $NAME entry in $CFG_PATH"
else
    KMODE="$(resolve_knowledge_mode "${RAD_KNOWLEDGE:-}" skip-installed)"
    backup_json_config "$CFG_PATH"
    set_json_mcp_entry "$CFG_PATH" mcpServers "$(new_stdio_entry)" "$NAME"
fi

# Skills are rebuilt no matter what (kept or reconfigured MCP).
"$VENV_PYTHON" "$RAD_ROOT/scripts/build_desktop_skills.py" --knowledge "$KMODE"
ZIP_DIR="$RAD_ROOT/dist/claude-desktop-skills"

echo ""
echo "Done, two manual steps remain (Desktop offers no automation for them):"
echo "  MCP client config is set in: $CFG_PATH (mcpServers.$NAME, mode: stdio)"
echo "  1. FULLY restart Desktop: quit from the tray/menu (window close is NOT enough), relaunch."
echo "  2. Sidebar Customize -> Skills -> upload the zips now opening in your file manager"
echo "     (replace existing ones if already uploaded)."
command -v "$OPEN_CMD" >/dev/null 2>&1 && "$OPEN_CMD" "$ZIP_DIR" || echo "  zips are in: $ZIP_DIR"
exit 0
