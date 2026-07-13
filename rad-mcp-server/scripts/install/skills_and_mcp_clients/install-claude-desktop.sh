#!/usr/bin/env bash
#
# Install rad-mcp (MCP + skills) for Claude Desktop.
#
#   ./install-claude-desktop.sh        # stdio (the only config-file mode Desktop supports)
#
# Merges the stdio entry into Claude Desktop's config (replacing any existing
# rad-mcp entry), rebuilds the skill zips, and opens the zip folder - the upload
# itself is manual (Customize -> Skills), Desktop has no API for it.
#
# No http switch: Desktop's config file is stdio-only (verified 2026-07-10);
# for a remote server use the Customize -> Connectors UI instead.

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_common.sh"

prompt_transport stdio-only
assert_common_setup

case "$(uname -s)" in
    Darwin) CFG_PATH="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
            OPEN_CMD=open ;;
    *)      CFG_PATH="$HOME/.config/Claude/claude_desktop_config.json"
            OPEN_CMD=xdg-open ;;
esac

set_json_mcp_entry "$CFG_PATH" mcpServers "$(new_stdio_entry)"

"$VENV_PYTHON" "$RAD_ROOT/scripts/build_desktop_skills.py"
ZIP_DIR="$RAD_ROOT/dist/claude-desktop-skills"

echo ""
echo "Done, two manual steps remain (Desktop offers no automation for them):"
echo "  1. FULLY restart Desktop: quit from the tray/menu (window close is NOT enough), relaunch."
echo "  2. Sidebar Customize -> Skills -> upload the zips now opening in your file manager"
echo "     (replace existing ones if already uploaded)."
command -v "$OPEN_CMD" >/dev/null 2>&1 && "$OPEN_CMD" "$ZIP_DIR" || echo "  zips are in: $ZIP_DIR"
exit 0
