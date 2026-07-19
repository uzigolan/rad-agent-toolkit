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

# First interpreter that is Python >= 3.10, preferring newer explicit names.
# Empty if none is found (e.g. RHEL where python3 is 3.6).
# Candidates may be broken shims that print error text to stdout — this
# function's stdout is captured by callers, so probe output must never leak
# into it, and the RADPY marker proves a real interpreter actually ran.
_best_python() {
    local c out
    for c in python3.13 python3.12 python3.11 python3.10 python3 python; do
        command -v "$c" >/dev/null 2>&1 || continue
        out="$("$c" -c 'import sys; sys.stdout.write("RADPY" if sys.version_info[:2] >= (3, 10) else "")' 2>/dev/null)" || continue
        if [ "$out" = "RADPY" ]; then
            echo "$c"; return 0
        fi
    done
    return 1
}

assert_common_setup() {
    if [ -x "$VENV_PYTHON" ]; then return; fi
    # No venv yet — bootstrap it automatically so install is a single command.
    local py; py="$(_best_python || true)"
    if [ -z "$py" ]; then
        echo "No Python >= 3.10 found, and the server venv doesn't exist yet." >&2
        echo "  (RHEL's default python3 is often 3.6, too old.)" >&2
        echo "  On RHEL-family:  sudo dnf install -y python3.11   (or python3.12)" >&2
        echo "  then re-run this installer." >&2
        echo "  (see INSTALL.md -> Common setup)" >&2
        exit 1
    fi
    echo "Setting up the server venv (one-time, using $py) ..." >&2
    "$py" -m venv "$RAD_ROOT/server/.venv" >&2 || {
        echo "failed to create the venv with '$py -m venv' (venv module missing?)." >&2
        echo "  On RHEL-family:  sudo dnf install -y python3.11 python3.11-pip" >&2
        exit 1
    }
    echo "  installing rad-mcp into the venv (pip install -e .) ..." >&2
    "$VENV_PYTHON" -m pip install --quiet --upgrade pip >&2 || true
    "$VENV_PYTHON" -m pip install --quiet -e "$RAD_ROOT/server" >&2 || {
        echo "pip install failed - check network / PyPI access, then re-run." >&2
        exit 1
    }
    echo "  venv ready: $VENV_PYTHON" >&2
}

copy_skills_to() {
    # $1 = dest, $2 = knowledge mode (bundled|served; default bundled).
    #   bundled — skills carry references/ (~14 MB); works with no MCP.
    #   served  — thin skills; rad-cli-operations/references/ omitted and served
    #             by the MCP catalog tools (needs the rad-mcp catalog present).
    local dest="$1"
    local knowledge="${2:-bundled}"
    mkdir -p "$dest"
    local s
    for s in "${SKILL_NAMES[@]}"; do
        rm -rf "$dest/$s"
        cp -R "$SKILLS_SRC/$s" "$dest/"
        echo "  skill -> $dest/$s"
    done
    if [ "$knowledge" = "served" ]; then
        [ -d "$dest/rad-cli-operations/references" ] && {
            rm -rf "$dest/rad-cli-operations/references"
            echo "  served mode: omitted rad-cli-operations/references (served by the MCP catalog tools)"
        }
        # Stamp the mode so the loaded skill's self-check knows it (missing =
        # bundled). Marker is an HTML comment with a token never used in prose.
        local md="$dest/rad-cli-operations/SKILL.md"
        if [ -f "$md" ] && ! grep -q '<!--rad-mode:' "$md"; then
            sed -i 's#^\(> \*\*Skill version:\*\*.*\)$#\1\n<!--rad-mode:served-->#' "$md"
        fi
    fi
}

resolve_knowledge_mode() {
    # echoes 'bundled' or 'served'. $1 = flag value ('' to prompt).
    local mode="$1"
    if [ -z "$mode" ]; then
        echo "Knowledge distribution mode:" >&2
        echo "  1) bundled  - skills carry their references (~14 MB); works with no MCP connection [default]" >&2
        echo "  2) served   - thin skills; all knowledge served by the rad-mcp catalog tools" >&2
        printf "Choice [1]: " >&2
        read -r ans || ans=""
        case "$ans" in 2|served|Served) mode=served ;; *) mode=bundled ;; esac
    fi
    mode="$(printf '%s' "$mode" | tr 'A-Z' 'a-z')"
    if [ "$mode" = "served" ] && [ ! -f "$RAD_ROOT/build/rad-knowledge.sqlite" ]; then
        echo "  WARNING: served mode needs the knowledge catalog, but build/rad-knowledge.sqlite is missing." >&2
        echo "           Build it: python scripts/build_knowledge_catalog.py --mib-root \"MIBs2:priority=200\" --mib-root \"MIBS:priority=100\"" >&2
    fi
    echo "  knowledge mode: $mode" >&2
    printf '%s' "$mode"
}

# First non-loopback IPv4 of this host (best-effort, Linux/macOS). Empty if none.
_first_ipv4() {
    local ip=""
    if command -v hostname >/dev/null 2>&1; then
        ip="$(hostname -I 2>/dev/null | awk '{print $1}')"
    fi
    if [ -z "$ip" ] && command -v ip >/dev/null 2>&1; then
        ip="$(ip -4 -o addr show scope global 2>/dev/null | awk '{print $4}' | cut -d/ -f1 | head -n1)"
    fi
    echo "$ip"
}

# Generate a URL-safe bearer token (32 bytes). Empty if no python is available.
_gen_token() {
    "$(_py)" -c 'import secrets; print(secrets.token_urlsafe(32))' 2>/dev/null || echo ""
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
        echo "  1) stdio  - local; the client launches the server via command/args (full toolset)"
        echo "  2) http   - remote; connect to an HTTPS server by URL + bearer token (read-only)"
        local ans
        read -r -p "Choice [1]: " ans || ans=""
        case "$ans" in
            2|http|HTTP|Http) MODE=http ;;
            *) MODE=stdio ;;
        esac
    fi
    if [ "$MODE" = http ]; then
        if [ -z "$HTTP_URL" ]; then
            local ip; ip="$(_first_ipv4)"
            echo "Note: Claude Desktop only accepts HTTPS URLs for remote MCP servers."
            echo "      HTTP URLs work with other clients."
            echo "Server URL:"
            echo "  1) https://127.0.0.1:8080/mcp   (server on this same machine)"
            if [ -n "$ip" ]; then
                echo "  2) https://$ip:8080/mcp   (this host's LAN address)"
            fi
            echo "  or type a full http:// or https:// URL"
            local uans
            while true; do
                read -r -p "Choice [1]: " uans || uans=""
                case "$uans" in
                    ""|1) HTTP_URL="https://127.0.0.1:8080/mcp"; break ;;
                    2) HTTP_URL="${ip:+https://$ip:8080/mcp}"; HTTP_URL="${HTTP_URL:-https://127.0.0.1:8080/mcp}"; break ;;
                    https://*) HTTP_URL="$uans"; break ;;
                    http://*)
                        echo "  WARNING: http:// URL detected. Claude Desktop requires https://."
                        echo "           If you're using another MCP client, this is fine."
                        HTTP_URL="$uans"
                        break
                        ;;
                    *) echo "  (unrecognized, using localhost)"; HTTP_URL="https://127.0.0.1:8080/mcp"; break ;;
                esac
            done
        fi
        if [ -z "$HTTP_TOKEN" ]; then
            read -r -p "Bearer token (leave blank to auto-generate one): " HTTP_TOKEN || HTTP_TOKEN=""
        fi
        if [ -z "$HTTP_TOKEN" ]; then
            HTTP_TOKEN="$(_gen_token)"
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

# Build an http MCP entry JSON. $1 = url, $2 = token, $3 = "request-init" to
# nest auth headers under "requestInit" (JetBrains Copilot) instead of a
# top-level "headers" key.
new_http_entry() {
    "$(_py)" - "$1" "$2" "${3:-}" <<'PY'
import json, sys
url, token, style = sys.argv[1], sys.argv[2], sys.argv[3]
headers = {"Authorization": f"Bearer {token}"}
e = {"type": "http", "url": url}
if style == "request-init":
    e["requestInit"] = {"headers": headers}
else:
    e["headers"] = headers
print(json.dumps(e))
PY
}

# Backup a JSON config file to <path>.bak.<timestamp> before overwriting.
# No-op if the file does not yet exist.
backup_json_config() {
    local path="$1"
    [ -f "$path" ] || return 0
    local ts; ts="$(date +%Y%m%d-%H%M%S)"
    cp "$path" "$path.bak.$ts"
    echo "  backup -> $path.bak.$ts"
}

# Create/merge a JSON config file, replacing any existing rad-mcp entry under
# the given root key ("mcpServers" or "servers"). $1=path $2=root $3=entry-json.
set_json_mcp_entry() {
    local path="$1" root="$2" entry="$3" name="${4:-rad-mcp}"
    mkdir -p "$(dirname "$path")"
    "$(_py)" - "$path" "$root" "$entry" "$name" <<'PY'
import json, os, sys
path, root, entry_json, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
entry = json.loads(entry_json)
if os.path.exists(path):
    with open(path) as f:
        cfg = json.load(f)
else:
    cfg = {}
cfg.setdefault(root, {})
if name in cfg[root]:
    del cfg[root][name]
    print(f"  replaced existing {name} entry in {path}")
cfg[root][name] = entry
with open(path, "w") as f:
    json.dump(cfg, f, indent=2)
    f.write("\n")
print(f"  mcp   -> {path}")
PY
    show_mcp_config_text "$("$(_py)" -c 'import json,sys; print(json.dumps({sys.argv[2]: json.loads(sys.argv[1])}, indent=2))' "$entry" "$name")"
}

# Print an MCP config snippet with any bearer token masked (first4...last4).
# $1 = config text, $2 = optional title line.
show_mcp_config_text() {
    local title="${2:-added MCP configuration (token masked):}"
    echo ""
    echo "  $title"
    "$(_py)" - "$1" <<'PY'
import re, sys

def _mask(m):
    tok = m.group(1)
    return "Bearer " + (tok[:4] + "..." + tok[-4:] if len(tok) > 8 else "***")

text = re.sub(r'Bearer\s+([^\s"\'}]+)', _mask, sys.argv[1].strip("\n"))
for line in text.splitlines():
    print("    " + line)
PY
    echo ""
}

# If a rad-mcp entry already exists in the JSON config, summarize it and ask
# whether to keep it. Sets KEEP_EXISTING=1 when the user keeps it (the caller
# then skips prompt_transport + set_json_mcp_entry, leaving the config as-is).
# Skipped when reconfiguration is explicit: flags preset MODE, or --reconfigure
# sets RAD_RECONFIGURE=1. $1=config-path $2=root-key $3=entry-name (default rad-mcp).
KEEP_EXISTING=""
maybe_keep_existing() {
    local path="$1" root="$2" name="${3:-rad-mcp}"
    KEEP_EXISTING=""
    [ -n "$MODE" ] && return                       # flags => reconfigure
    [ "${RAD_RECONFIGURE:-}" = "1" ] && return      # --reconfigure => reconfigure
    local summary
    summary="$("$(_py)" - "$path" "$root" "$name" <<'PY'
import json, os, sys
path, root, name = sys.argv[1], sys.argv[2], sys.argv[3]
if not os.path.exists(path):
    sys.exit(0)
try:
    with open(path) as f:
        cfg = json.load(f)
except Exception:
    sys.exit(0)
e = (cfg.get(root) or {}).get(name)
if not e:
    sys.exit(0)
t = e.get("type", "stdio")
if t == "http":
    url = e.get("url", "?")
    auth = ((e.get("headers") or {}).get("Authorization", "")
            or ((e.get("requestInit") or {}).get("headers") or {}).get("Authorization", ""))
    tok = auth.split()[-1] if auth else ""
    masked = (tok[:4] + "..." + tok[-4:]) if len(tok) > 8 else ("set" if tok else "none")
    print(f"http  url={url}  token={masked}")
else:
    print(f"{t}  command={e.get('command', '?')}")
PY
)"
    [ -z "$summary" ] && return
    echo "$name is already configured in $path:"
    echo "    $summary"
    echo "  1) Keep existing configuration (leave it unchanged)"
    echo "  2) Reconfigure from scratch (re-run the prompts and replace it)"
    local ans
    read -r -p "Choice [1]: " ans || ans=""
    case "$ans" in
        2|r|R|reconfigure) KEEP_EXISTING="" ;;
        *) KEEP_EXISTING=1 ;;
    esac
}
