#!/usr/bin/env bash
#
# Manual generic installer helper for rad-mcp (skills + MCP snippets).
#
#   ./install-generic.sh
#   ./install-generic.sh --http --url http://127.0.0.1:8080/mcp --token <token>
#   ./install-generic.sh --skill-mode embedded
#
# What it does:
#   - Skills: either show served skill source paths, or build embedded desktop zips
#   - MCP: prompts for stdio/http and prints manual config snippets for common clients
#
# What it does NOT do:
#   - does not write any client config files
#   - does not copy skills into user/workspace folders

set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_common.sh"

CONFIG_STORE="$RAD_ROOT/server/.rad-mcp-generic-config"

SKILL_MODE=""
KNOWLEDGE=""
while [ $# -gt 0 ]; do
    case "$1" in
        --skill-mode) SKILL_MODE="$2"; shift 2 ;;
        --knowledge) KNOWLEDGE="$2"; shift 2 ;;
        --http) MODE=http; shift ;;
        --url) HTTP_URL="$2"; shift 2 ;;
        --token) HTTP_TOKEN="$2"; shift 2 ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done

show_entry_snippet() {
    # $1 title, $2 root key, $3 entry json, $4 path hint
    local title="$1" root="$2" entry_json="$3" path_hint="${4:-}"
    local wrapped
    wrapped="$($(_py) -c 'import json,sys; print(json.dumps({sys.argv[2]: json.loads(sys.argv[1])}, indent=2))' "$entry_json" "rad-mcp")"
    show_mcp_config_text "$wrapped" "$title"
    echo "    root key: $root"
    [ -n "$path_hint" ] && echo "    file    : $path_hint"
    echo ""
}

save_generic_transport_config() {
    # $1 skill_mode, $2 knowledge, $3 mode, $4 url, $5 token
    local skill_mode="$1" knowledge="$2" mode="$3" url="${4:-}" token="${5:-}"
    {
        echo "RAD_MCP_GENERIC_SKILL_MODE='$skill_mode'"
        echo "RAD_MCP_GENERIC_KNOWLEDGE='$knowledge'"
        echo "RAD_MCP_GENERIC_MODE='$mode'"
        echo "RAD_MCP_GENERIC_URL='$url'"
        echo "RAD_MCP_GENERIC_TOKEN='$token'"
    } > "$CONFIG_STORE"
}

USED_SAVED_TRANSPORT=""
EXPLICIT_TRANSPORT=""
[ -n "${MODE:-}${HTTP_URL:-}${HTTP_TOKEN:-}" ] && EXPLICIT_TRANSPORT=1
if [ -n "${HTTP_URL:-}${HTTP_TOKEN:-}" ] && [ "${MODE:-}" != "http" ]; then MODE=http; fi
EXPLICIT_SKILLS=""
[ -n "${SKILL_MODE:-}${KNOWLEDGE:-}" ] && EXPLICIT_SKILLS=1
EXPLICIT_ANY=""
[ -n "$EXPLICIT_TRANSPORT$EXPLICIT_SKILLS" ] && EXPLICIT_ANY=1

if [ -z "$EXPLICIT_ANY" ] && [ -f "$CONFIG_STORE" ]; then
    # shellcheck disable=SC1090
    . "$CONFIG_STORE"
    SAVED_SKILL_MODE="${RAD_MCP_GENERIC_SKILL_MODE:-served}"
    SAVED_KNOWLEDGE="${RAD_MCP_GENERIC_KNOWLEDGE:-}"
    if [ -z "$SAVED_KNOWLEDGE" ]; then
        if [ "$SAVED_SKILL_MODE" = "embedded" ]; then SAVED_KNOWLEDGE="bundled"; else SAVED_KNOWLEDGE="served"; fi
    fi
    SAVED_MODE="${RAD_MCP_GENERIC_MODE:-stdio}"
    SAVED_URL="${RAD_MCP_GENERIC_URL:-}"
    SAVED_TOKEN="${RAD_MCP_GENERIC_TOKEN:-}"
    if [ ${#SAVED_TOKEN} -gt 8 ]; then
        MASKED_TOKEN="${SAVED_TOKEN:0:4}...${SAVED_TOKEN: -4}"
    elif [ -n "$SAVED_TOKEN" ]; then
        MASKED_TOKEN="set"
    else
        MASKED_TOKEN="none"
    fi

    echo "rad-mcp generic setup is already configured in $CONFIG_STORE:"
    echo "    skills mode=$SAVED_SKILL_MODE  knowledge=$SAVED_KNOWLEDGE"
    if [ "$SAVED_MODE" = "http" ]; then
        echo "    mcp    mode=http  url=$SAVED_URL  token=$MASKED_TOKEN"
    else
        echo "    mcp    mode=stdio"
    fi
    echo "Keep this configuration? [Y/n]"
    read -r -p "Answer: " KEEP_ANS || KEEP_ANS=""
    case "$KEEP_ANS" in
        n|N|no|No|NO|2|r|R|reconfigure) ;;
        *)
            SKILL_MODE="$SAVED_SKILL_MODE"
            KNOWLEDGE="$SAVED_KNOWLEDGE"
            MODE="$SAVED_MODE"
            HTTP_URL="$SAVED_URL"
            HTTP_TOKEN="$SAVED_TOKEN"
            USED_SAVED_TRANSPORT=1
            ;;
    esac
fi

if [ -z "$SKILL_MODE" ]; then
    echo ""
    echo "Skills delivery mode:"
    echo "  1) served   - show SKILL.md paths only (manual copy/reference)"
    echo "  2) embedded - build desktop skill zip artifacts"
    read -r -p "Choice [1]: " sm || sm=""
    case "$sm" in
        2|embedded|Embedded) SKILL_MODE="embedded" ;;
        *) SKILL_MODE="served" ;;
    esac
fi

echo ""
echo "skills mode -> $SKILL_MODE"
if [ "$SKILL_MODE" = "served" ]; then
    [ -z "$KNOWLEDGE" ] && KNOWLEDGE="served"
    echo "  source skills folder: $SKILLS_SRC"
    echo "  served mode: use SKILL.md only (do not copy references/ or other files)"
    while IFS= read -r skill; do
        [ -n "$skill" ] || continue
        printf '  %-18s: %s\n' "$skill" "$SKILLS_SRC/$skill/SKILL.md"
    done <<EOF
$(get_rad_skill_names)
EOF
    echo ""
    echo "Manual usage examples:"
    echo "  - Copilot user scope   -> ~/.copilot/skills/<skill-name>/SKILL.md"
    echo "  - Claude user scope    -> ~/.claude/skills/<skill-name>/SKILL.md"
    echo "  - Workspace scope      -> .github/skills/<skill-name>/SKILL.md"
else
    [ -z "$KNOWLEDGE" ] && KNOWLEDGE="bundled"
    echo "  embedded knowledge mode -> $KNOWLEDGE"
    assert_common_setup
    "$VENV_PYTHON" "$RAD_ROOT/scripts/build_desktop_skills.py" --knowledge "$KNOWLEDGE"
    ZIP_DIR="$RAD_ROOT/dist/claude-desktop-skills"
    echo "  embedded zips built -> $ZIP_DIR"
    echo "  upload these zips where the client expects packaged skills (Claude Desktop: Customize -> Skills)."
fi

if [ -n "$EXPLICIT_TRANSPORT" ]; then
    if [ "${MODE:-}" = "http" ]; then
        if [ -z "${HTTP_URL:-}" ]; then HTTP_URL="http://127.0.0.1:8080/mcp"; fi
        if [ -z "${HTTP_TOKEN:-}" ]; then
            echo "http mode needs --token <bearer-token>" >&2
            exit 1
        fi
    fi
elif [ -z "$USED_SAVED_TRANSPORT" ]; then
    prompt_transport
elif [ "${MODE:-}" = "http" ] && { [ -z "${HTTP_URL:-}" ] || [ -z "${HTTP_TOKEN:-}" ]; }; then
    echo "  Saved HTTP configuration is incomplete; re-entering transport setup."
    prompt_transport
fi

echo ""
echo "mcp transport -> $MODE"

if [ "$MODE" = "stdio" ]; then
    assert_common_setup
fi

show_served_catalog_hint "$KNOWLEDGE" "$MODE" "$HTTP_URL"

if [ "$MODE" = "stdio" ]; then
    VSCODE_ENTRY="$(new_stdio_entry with-type)"
    INTELLIJ_ENTRY="$VSCODE_ENTRY"
    CLAUDE_ENTRY="$(new_stdio_entry)"
    COPILOT_CLI_ENTRY="$($(_py) - "$VENV_PYTHON" "$INVENTORY" <<'PY'
import json, sys
venv, inv = sys.argv[1], sys.argv[2]
print(json.dumps({
  "type": "local",
  "command": venv,
  "args": ["-m", "rad_mcp.server"],
  "env": {"RAD_MCP_INVENTORY": inv},
  "tools": ["*"]
}))
PY
)"
else
    VSCODE_ENTRY="$(new_http_entry "$HTTP_URL" "$HTTP_TOKEN")"
    INTELLIJ_ENTRY="$(new_http_entry "$HTTP_URL" "$HTTP_TOKEN" request-init)"
    CLAUDE_ENTRY="$VSCODE_ENTRY"
    COPILOT_CLI_ENTRY="$($(_py) - "$VSCODE_ENTRY" <<'PY'
import json, sys
entry = json.loads(sys.argv[1])
entry["tools"] = ["*"]
print(json.dumps(entry))
PY
)"
fi

echo ""
echo "Manual MCP configuration snippets (token masked):"
echo ""
show_entry_snippet "VS Code Copilot:" "servers" "$VSCODE_ENTRY" "~/.config/Code/User/mcp.json"
show_entry_snippet "JetBrains Copilot (classic MCP path):" "servers" "$INTELLIJ_ENTRY" "~/.config/github-copilot/intellij/mcp.json"
show_entry_snippet "JetBrains embedded Copilot CLI agent:" "mcpServers" "$COPILOT_CLI_ENTRY" "~/.copilot/mcp-config.json"
show_entry_snippet "Claude Code / Claude Desktop shape:" "mcpServers" "$CLAUDE_ENTRY" "~/Library/Application Support/Claude/claude_desktop_config.json (Desktop) or ~/.claude.json/.mcp.json (Claude Code)"

echo "Next steps:"
echo "  1. Merge one relevant snippet into your target client config file (root key as shown)."
echo "  2. Restart the client/session."
echo "  3. Verify with: 'list the managed devices'."
if [ "$MODE" = "http" ]; then
    echo "  4. Ensure your HTTP server is running and token matches exactly."
fi

if [ "$MODE" = "http" ]; then
    save_generic_transport_config "$SKILL_MODE" "$KNOWLEDGE" "http" "$HTTP_URL" "$HTTP_TOKEN"
else
    save_generic_transport_config "$SKILL_MODE" "$KNOWLEDGE" "stdio" "" ""
fi
