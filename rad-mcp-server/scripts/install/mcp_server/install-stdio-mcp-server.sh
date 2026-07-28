#!/usr/bin/env bash
#
# Prepare rad-mcp for stdio clients (no HTTP listener):
#   - Bootstrap server venv + dependencies (same common setup used by installers)
#   - Optionally build the knowledge catalog (rad-knowledge.sqlite)
#
# Behavior:
#   - Reuses saved stdio MIB configuration from server/.rad-mcp-stdio-config
#     when no flags are passed, and asks whether to keep it
#   - Keeps the existing catalog by default unless you choose to rebuild
#
# Examples:
#   ./install-stdio-mcp-server.sh
#   ./install-stdio-mcp-server.sh --mib-dir /path/to/MIBS
#   ./install-stdio-mcp-server.sh --skip-catalog

set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/_common.sh"

MIB_DIR=""
SKIP_CATALOG=""
while [ $# -gt 0 ]; do
    case "$1" in
        --mib-dir) MIB_DIR="$2"; shift 2 ;;
        --skip-catalog) SKIP_CATALOG=1; shift ;;
        *) echo "unknown argument: $1" >&2; exit 1 ;;
    esac
done

assert_common_setup

CATALOG="$RAD_ROOT/build/rad-knowledge.sqlite"
BUILD_SCRIPT="$RAD_ROOT/scripts/build_knowledge_catalog.py"
CONFIG_STORE="$RAD_ROOT/server/.rad-mcp-stdio-config"

echo ""
echo "stdio preparation:"
echo "  venv/deps -> ready ($VENV_PYTHON)"

CATALOG_PRESENT=""
[ -f "$CATALOG" ] && CATALOG_PRESENT=1
EXPLICIT=""
[ -n "$MIB_DIR$SKIP_CATALOG" ] && EXPLICIT=1

if [ -z "$EXPLICIT" ] && [ -f "$CONFIG_STORE" ]; then
    # shellcheck disable=SC1090
    . "$CONFIG_STORE"
    SAVED_MODE="${RAD_MCP_STDIO_MIB_MODE:-unknown}"
    SAVED_ROOT="${RAD_MCP_STDIO_MIB_ROOT:-}"

    echo "Found a saved stdio configuration from a previous run ($CONFIG_STORE):"
    echo "    MIB mode : $SAVED_MODE"
    [ -n "$SAVED_ROOT" ] && echo "    MIB root : $SAVED_ROOT"
    if [ -n "$CATALOG_PRESENT" ]; then
        SIZE_MB=$(( $(wc -c < "$CATALOG") / 1048576 ))
        echo "    catalog  : present (${SIZE_MB} MB)"
    else
        echo "    catalog  : missing"
    fi

    read -r -p "Keep this configuration (MIBs)? [Y/n]: " KEEP_ANS || KEEP_ANS=""
    case "$KEEP_ANS" in
        n|N|no|No)
            echo "Reconfiguring stdio MIB setup."
            echo ""
            ;;
        *)
            if [ -n "$CATALOG_PRESENT" ]; then
                SIZE_MB=$(( $(wc -c < "$CATALOG") / 1048576 ))
                echo "  catalog   -> kept existing (${SIZE_MB} MB): $CATALOG"
                echo ""
                echo "Done. You can now use stdio MCP entries from IDE installers."
                exit 0
            fi
            echo "  WARNING: saved configuration was kept, but the catalog file is missing."
            echo "           Continue below to build a new catalog if needed."
            echo ""
            ;;
    esac
fi

if [ -n "$SKIP_CATALOG" ]; then
    if [ -f "$CATALOG" ]; then
        echo "  catalog   -> kept existing $CATALOG"
    else
        echo "  catalog   -> skipped (none present)"
    fi
    echo ""
    echo "Done. You can now use stdio MCP entries from IDE installers."
    exit 0
fi

DO_BUILD=""
BUILD_MODE=""
RESOLVED_MIB_DIR=""

if [ -n "$MIB_DIR" ]; then
    if [ ! -d "$MIB_DIR" ]; then
        echo "MIB directory not found: $MIB_DIR" >&2
        exit 1
    fi
    RESOLVED_MIB_DIR="$(cd "$MIB_DIR" && pwd)"
    DO_BUILD=1
    BUILD_MODE="custom"
else
    if [ -n "$CATALOG_PRESENT" ]; then
        read -r -p "  Rebuild the MIB catalog? (keep current if no) [y/N]: " ANS || ANS=""
    else
        read -r -p "  Add MIBs now - build the catalog? [y/N]: " ANS || ANS=""
    fi
    case "$ANS" in
        y|Y|yes|YES|Yes) DO_BUILD=1 ;;
    esac

    if [ -n "$DO_BUILD" ]; then
        echo "  Build mode:"
        echo "    1) baseline (no extra MIB roots)"
        echo "    2) custom MIB directory"
        read -r -p "  Choice [1]: " MODE_ANS || MODE_ANS=""
        case "$MODE_ANS" in
            2|custom|Custom)
                read -r -p "  Path to the MIB directory (folder with .mib files): " MIB_PROMPT || MIB_PROMPT=""
                if [ -z "$MIB_PROMPT" ] || [ ! -d "$MIB_PROMPT" ]; then
                    echo "MIB directory not found: $MIB_PROMPT" >&2
                    exit 1
                fi
                RESOLVED_MIB_DIR="$(cd "$MIB_PROMPT" && pwd)"
                BUILD_MODE="custom"
                ;;
            *)
                BUILD_MODE="baseline"
                ;;
        esac
    fi
fi

if [ -z "$DO_BUILD" ]; then
    if [ -f "$CATALOG" ]; then
        echo "  catalog   -> kept existing $CATALOG"
    else
        echo "  catalog   -> skipped (none present)"
    fi
    echo ""
    echo "Done. You can now use stdio MCP entries from IDE installers."
    exit 0
fi

if [ "$BUILD_MODE" = "custom" ]; then
    if ! "$VENV_PYTHON" -c "import pysmi" >/dev/null 2>&1; then
        echo "  installing pysmi into the venv (one-time) ..."
        "$VENV_PYTHON" -m pip install --quiet pysmi
    fi

    echo "  catalog   -> building from MIB directory: $RESOLVED_MIB_DIR"
    "$VENV_PYTHON" "$BUILD_SCRIPT" --mib-root "$RESOLVED_MIB_DIR"
else
    echo "  catalog   -> building baseline catalog (no extra MIB roots)"
    "$VENV_PYTHON" "$BUILD_SCRIPT"
fi

if [ -f "$CATALOG" ]; then
    SIZE_MB=$(( $(wc -c < "$CATALOG") / 1048576 ))
    echo "  catalog   -> ready (${SIZE_MB} MB): $CATALOG"
    {
        echo "RAD_MCP_STDIO_MIB_MODE='$BUILD_MODE'"
        echo "RAD_MCP_STDIO_MIB_ROOT='$RESOLVED_MIB_DIR'"
    } > "$CONFIG_STORE"
    echo "  config    -> saved: $CONFIG_STORE"
else
    echo "Catalog build failed (catalog file missing after build)." >&2
    exit 1
fi

echo ""
echo "Done. You can now use stdio MCP entries from IDE installers."
