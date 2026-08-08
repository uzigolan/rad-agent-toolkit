"""Shared server runtime: transport/write gating, staged-commit state, demo
devices, and backup helpers.

Extracted from server.py in plan 01 (capability grouping) so each tool group
can live in its own module (rad_mcp/tools/*) without importing the FastMCP
app module. Plan 09 later moves these groups into separate packages; this
module is the piece they will keep sharing until then.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path

from fastmcp.exceptions import ToolError
from fastmcp.server.dependencies import get_access_token

from .audit import audit

REPO_ROOT = Path(__file__).resolve().parents[2]
BACKUP_DIR = Path(__file__).resolve().parent.parent / "backups"

_TRANSPORT = os.environ.get("RAD_MCP_TRANSPORT", "stdio").lower()
_HTTP = _TRANSPORT in ("http", "streamable-http")


def _parse_tokens(var: str) -> list[str]:
    return [t.strip() for t in os.environ.get(var, "").split(",") if t.strip()]


# Per-token roles: RAD_MCP_TOKENS are read-only, RAD_MCP_WRITE_TOKENS are
# read-write. A value present in both lists is treated as read-write.
_READ_TOKENS = _parse_tokens("RAD_MCP_TOKENS")
_WRITE_TOKENS = _parse_tokens("RAD_MCP_WRITE_TOKENS")
_READONLY_ENV = os.environ.get("RAD_MCP_READONLY", "").lower() in ("1", "true", "yes")

# Interlock 1 (scoped): over HTTP the write tools are REGISTERED only when at
# least one write-scoped token exists, and every write call is re-checked at
# call time (see _require_write_scope) so only write-token holders can invoke
# them. Over stdio (local, trusted) writes are on unless RAD_MCP_READONLY.
if _HTTP:
    WRITE_TOOLS_ENABLED = bool(_WRITE_TOKENS) and not _READONLY_ENV
else:
    WRITE_TOOLS_ENABLED = not _READONLY_ENV


def _build_auth():
    """Interlock 2: HTTP requires bearer tokens — refuse to serve unauthenticated.
    Read-only tokens come from RAD_MCP_TOKENS, read-write tokens from
    RAD_MCP_WRITE_TOKENS; each token carries its scope so write tools can
    re-check the caller at call time. stdio needs no auth."""
    if not _HTTP:
        return None
    if not _READ_TOKENS and not _WRITE_TOKENS:
        raise SystemExit(
            "RAD_MCP_TRANSPORT=http requires RAD_MCP_TOKENS (read-only) and/or "
            "RAD_MCP_WRITE_TOKENS (read-write). Refusing to start an "
            "unauthenticated network server."
        )
    tokens: dict[str, dict] = {}
    for i, tok in enumerate(_READ_TOKENS):
        tokens[tok] = {"client_id": f"rad-ro-{i+1}", "scopes": ["read"]}
    # Write tokens win if a value appears in both lists.
    for i, tok in enumerate(_WRITE_TOKENS):
        tokens[tok] = {"client_id": f"rad-rw-{i+1}", "scopes": ["read", "write"]}
    from fastmcp.server.auth.providers.jwt import StaticTokenVerifier
    return StaticTokenVerifier(tokens)


def _require_write_scope() -> None:
    """Interlock 1 (per-call): over HTTP, only tokens carrying the 'write'
    scope (RAD_MCP_WRITE_TOKENS) may invoke a write tool. stdio is local and
    trusted, so it is exempt."""
    if not _HTTP:
        return
    token = get_access_token()
    scopes = list(getattr(token, "scopes", None) or [])
    if "write" not in scopes:
        raise ToolError(
            "This token is read-only. A write-scoped token "
            "(RAD_MCP_WRITE_TOKENS on the server) is required for "
            "configuration and inventory changes."
        )


# In-memory staging area: stage_id -> {device, lines, created}
_STAGES: dict[str, dict] = {}

# In-memory demo-runtime state: device name -> metadata. When present, CLI and
# SNMP read tools return deterministic demo answers instead of touching network.
_DEMO_DEVICES: dict[str, dict] = {}

_DEMO_SNMP_REF_OIDS = {
    "sysdescr": "1.3.6.1.2.1.1.1.0",
    "sysobjectid": "1.3.6.1.2.1.1.2.0",
    "sysuptime": "1.3.6.1.2.1.1.3.0",
    "sysuptimeinstance": "1.3.6.1.2.1.1.3.0",
    "sysname": "1.3.6.1.2.1.1.5.0",
    "syslocation": "1.3.6.1.2.1.1.6.0",
}


def _demo_state(device_name: str) -> dict | None:
    return _DEMO_DEVICES.get(device_name)


def _demo_confirm_bypass(device_name: str) -> bool:
    """Allow confirm-gated operations only for active in-process demo units.
    Real inventory devices always keep explicit-confirm protection."""
    return _demo_state(device_name) is not None


def _demo_start(dev, *, cli_user: str, snmp_v1: str) -> dict:
    state = {
        "name": dev.name,
        "host": dev.host,
        "family": dev.family,
        "transport": dev.transport,
        "port": dev.port,
        "started": datetime.now(timezone.utc).isoformat(),
        "cli_user": cli_user,
        "snmp_v1_configured": bool(snmp_v1),
        "debug_unlocked": False,
        "debug_in_shell": False,
        "debug_key_code": "424242",
    }
    _DEMO_DEVICES[dev.name] = state
    return state


def _demo_stop(device_name: str) -> bool:
    return _DEMO_DEVICES.pop(device_name, None) is not None


def _demo_config(dev) -> str:
    return "\n".join([
        f"! demo config for {dev.name}",
        f"! family={dev.family} host={dev.host}",
        "configure system",
        " location DM",
        " no shutdown",
        "exit all",
        "save",
    ])


def _demo_sys_object_id(family: str) -> str:
    return {
        "minid": "1.3.6.1.4.1.164.6.1.6.36",
        "etx2v": "1.3.6.1.4.1.164.6.1.6.55",
    }.get(family, "1.3.6.1.4.1.164.6.1.6.79")


def _demo_snmp_scalars(dev) -> dict[str, str]:
    return {
        "1.3.6.1.2.1.1.1.0": f"RAD demo {dev.family} software 0.0.1",
        "1.3.6.1.2.1.1.2.0": _demo_sys_object_id(dev.family),
        "1.3.6.1.2.1.1.3.0": "123456",
        "1.3.6.1.2.1.1.5.0": dev.name,
        "1.3.6.1.2.1.1.6.0": "Demo Lab",
    }


def _fallback_snmp_plan(refs: list[str], out: dict) -> dict:
    """Provide a minimal GET plan for common system scalars when the
    knowledge catalog cannot resolve refs (useful for demo/tool-check flows)."""
    if out.get("operations"):
        return out
    selected: list[str] = []
    unresolved: list[str] = []
    for ref in refs[:32]:
        raw = (ref or "").strip()
        key = raw.lower().replace("-", "").replace("_", "").replace(" ", "")
        oid = _DEMO_SNMP_REF_OIDS.get(key)
        if oid:
            selected.append(oid)
            continue
        if raw.startswith("1.3."):
            selected.append(raw if raw.endswith(".0") else raw + ".0")
            continue
        unresolved.append(ref)
    unique = list(dict.fromkeys(selected))[:64]
    if not unique:
        return out
    ops = list(out.get("operations") or [])
    ops.insert(0, {
        "tool": "snmp_get",
        "oids": unique,
        "reason": "catalog fallback for demo/tool-check system scalars",
    })
    notes = list(out.get("notes") or [])
    notes.append(
        "Fallback SNMP plan applied: catalog could not resolve requested refs, "
        "so a system-scalar GET plan was generated for tool-check coverage."
    )
    out["operations"] = ops
    out["unresolved"] = unresolved
    out["notes"] = notes
    return out


def _write_backup_content(dev, config: str) -> Path:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = BACKUP_DIR / f"{dev.name}-{stamp}.cfg"
    path.write_text(config, encoding="utf-8")
    audit("backup_config", dev.name, detail=str(path))
    return path


# ------------------------------------------------- knowledge-catalog access

def _knowledge():
    from . import knowledge as k
    return k


def _kcall(fn, *args, **kw):
    k = _knowledge()
    try:
        return fn(*args, **kw)
    except k.KnowledgeUnavailable as exc:
        raise ToolError(str(exc)) from exc


# ------------------------------------------------ skill/version introspection

def _read_skill_version(name: str) -> str | None:
    """The version the SERVER's own skills/ copy of <name> declares, or None
    if the server ships no such skill."""
    md = (REPO_ROOT / "skills" / name / "SKILL.md")
    if not md.exists():
        return None
    seen = 0
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.strip() == "---":
            seen += 1
            if seen == 2:
                break
            continue
        if seen == 1 and line.lower().startswith("version:"):
            return line.split(":", 1)[1].strip()
    return "(unset)"


def _catalog_present() -> bool:
    try:
        from . import knowledge as _k
        _k._db_path()
        return True
    except Exception:
        return False
