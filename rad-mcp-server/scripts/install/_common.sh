# Shared helpers for the per-target install scripts. Source, don't run.
# Bash 3.2+ compatible (macOS/Linux). Mirrors _common.ps1.

set -euo pipefail

# Repo layout: this file lives at rad-mcp-server/scripts/install/
_COMMON_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAD_ROOT="$(cd "$_COMMON_DIR/../.." && pwd)"
VENV_PYTHON="$RAD_ROOT/server/.venv/bin/python"
INVENTORY="$RAD_ROOT/inventory.yaml"
SKILLS_SRC="$RAD_ROOT/skills"
SKILL_NAMES=(rad-core rad-cli-operations rad-device-mng)

# Transport selection, populated by prompt_transport / flag parsing.
MODE="${MODE:-}"        # stdio | http
HTTP_URL="${HTTP_URL:-}"
HTTP_TOKEN="${HTTP_TOKEN:-}"

# Pick a python for JSON helpers (venv preferred, else system).
_py() {
    if [ -x "$VENV_PYTHON" ]; then echo "$VENV_PYTHON"
    elif command -v python3 >/dev/null 2>&1; then echo python3
    else echo python; fi
}

assert_common_setup() {
    if [ ! -x "$VENV_PYTHON" ]; then
        echo "venv not found at $VENV_PYTHON - run the common setup first (see INSTALL.md):" >&2
        echo "  cd rad-mcp-server/server && python3 -m venv .venv && .venv/bin/pip install -e ." >&2
        exit 1
    fi
}

copy_skills_to() {
    local dest="$1"
    mkdir -p "$dest"
    local s
    for s in "${SKILL_NAMES[@]}"; do
        rm -rf "$dest/$s"
        cp -R "$SKILLS_SRC/$s" "$dest/"
        echo "  skill -> $dest/$s"
    done
}

# Interactive transport picker. Honors a pre-set MODE (from flag parsing) and
# only asks for whatever is still missing. Sets MODE, HTTP_URL, HTTP_TOKEN.
# $1 (optional) = "stdio-only" to refuse http (e.g. Claude Desktop).
prompt_transport() {
    local stdio_only="${1:-}"
    if [ "$stdio_only" = "stdio-only" ]; then
        MODE=stdio
        return
    fi
    if [ -z "$MODE" ]; then
        echo "Select MCP transport:"
        echo "  1) stdio  - local, the client launches the server (full toolset incl. staged writes)"
        echo "  2) http   - client of a manually-run shared server (read-only by the code interlock)"
        local ans
        read -r -p "Choice [1]: " ans || ans=""
        case "$ans" in
            2|http|HTTP|Http) MODE=http ;;
            *) MODE=stdio ;;
        esac
    fi
    if [ "$MODE" = http ]; then
        if [ -z "$HTTP_URL" ]; then
            read -r -p "Server URL [http://127.0.0.1:8080/mcp]: " HTTP_URL || HTTP_URL=""
            HTTP_URL="${HTTP_URL:-http://127.0.0.1:8080/mcp}"
        fi
        if [ -z "$HTTP_TOKEN" ]; then
            read -r -p "Bearer token (leave blank to auto-generate one): " HTTP_TOKEN || HTTP_TOKEN=""
        fi
        if [ -z "$HTTP_TOKEN" ]; then
            HTTP_TOKEN="$("$(_py)" -c 'import secrets; print(secrets.token_urlsafe(32))')"
            if [ -z "$HTTP_TOKEN" ]; then
                echo "could not auto-generate a token (no python found); rerun with --token <t>" >&2
                exit 1
            fi
            echo ""
            echo "  Generated bearer token. Configure the server with the SAME value,"
            echo "  choosing the role you want this client to have:"
            echo "    RAD_MCP_TOKENS=<token>        read-only (reads only)"
            echo "    RAD_MCP_WRITE_TOKENS=<token>  read-write (also manage devices + config)"
            echo "  (otherwise the client can't connect):"
            echo ""
            echo "      $HTTP_TOKEN"
            echo ""
        fi
    fi
}

# Build a stdio MCP entry JSON. $1 = "with-type" to include "type":"stdio".
new_stdio_entry() {
    local with_type="${1:-}"
    "$(_py)" - "$with_type" "$VENV_PYTHON" "$RAD_ROOT" "$INVENTORY" <<'PY'
import json, sys
with_type, venv, root, inv = sys.argv[1:5]
e = {}
if with_type == "with-type":
    e["type"] = "stdio"
e["command"] = venv
e["args"] = ["-m", "rad_mcp.server"]
e["cwd"] = f"{root}/server"
e["env"] = {"RAD_MCP_INVENTORY": inv}
print(json.dumps(e))
PY
}

# Build an http MCP entry JSON. $1 = url, $2 = token.
new_http_entry() {
    "$(_py)" - "$1" "$2" <<'PY'
import json, sys
url, token = sys.argv[1], sys.argv[2]
print(json.dumps({"type": "http", "url": url,
                  "headers": {"Authorization": f"Bearer {token}"}}))
PY
}

# Create/merge a JSON config file, replacing any existing rad-mcp entry under
# the given root key ("mcpServers" or "servers"). $1=path $2=root $3=entry-json.
set_json_mcp_entry() {
    local path="$1" root="$2" entry="$3"
    mkdir -p "$(dirname "$path")"
    "$(_py)" - "$path" "$root" "$entry" <<'PY'
import json, os, sys
path, root, entry_json = sys.argv[1], sys.argv[2], sys.argv[3]
entry = json.loads(entry_json)
if os.path.exists(path):
    with open(path) as f:
        cfg = json.load(f)
else:
    cfg = {}
cfg.setdefault(root, {})
if "rad-mcp" in cfg[root]:
    del cfg[root]["rad-mcp"]
    print(f"  replaced existing rad-mcp entry in {path}")
cfg[root]["rad-mcp"] = entry
with open(path, "w") as f:
    json.dump(cfg, f, indent=2)
    f.write("\n")
print(f"  mcp   -> {path}")
PY
}
