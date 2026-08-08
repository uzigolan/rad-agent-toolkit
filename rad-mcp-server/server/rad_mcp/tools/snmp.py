"""snmp group — read-only SNMP tools.

Read-only by construction (GET / GETNEXT only — this toolkit never sends
SET; config writes stay on the CLI's staged-commit flow). Credentials come
from server/.env (RAD_MCP_<NAME>_SNMP_COMMUNITY / _SNMP_V3_USER); see
backends/snmp.py for the RAD-agent quirks these tools encode. Future home:
the rad-device server (plan 09). Lean profile: on by default, RAD_MCP_SNMP=false
drops the group.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

from fastmcp.exceptions import ToolError

from ..audit import audit
from ..boundary import wrap_device_output
from ..inventory import get_device
from ..runtime import (REPO_ROOT, _demo_snmp_scalars, _demo_state,
                       _fallback_snmp_plan, _kcall, _knowledge)


def _snmp():
    try:
        from ..backends import snmp as _mod
        import pysnmp  # noqa: F401 — surface a clean error if absent
        return _mod
    except ImportError as exc:
        raise ToolError(
            "SNMP support needs the 'pysnmp' package in the server venv: "
            "pip install pysnmp  (then retry)"
        ) from exc


def _decorate(oid: str, val: str) -> str:
    """Append catalog semantics (enum meaning, units) to a live value.
    Graceful no-op when the knowledge catalog is absent."""
    try:
        from .. import knowledge as k
        d = k.decode_value(oid, val)
    except Exception:
        d = None
    if not d:
        return val
    out = val
    if d.get("meaning"):
        out += f"  = {d['meaning']}"
    if d.get("units"):
        out += f" [{d['units']}]"
    return out


def _log_observation(dev, tool: str, subject: str, observed: str) -> None:
    """Append-only live capability evidence (design Phase 4: stored separately
    from MIB definitions; the next catalog build can import this file)."""
    try:
        path = REPO_ROOT / "server" / "logs" / "capability-observations.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps({
                "ts": datetime.now(timezone.utc).isoformat(),
                "family": dev.family, "device": dev.name, "tool": tool,
                "subject": subject, "observed": observed,
                "evidence_type": "live-snmp",
            }) + "\n")
    except Exception:
        pass  # evidence logging must never break a live read


def _wrap_values(values: dict, dev, tool: str) -> dict:
    """Wrap each device-returned SNMP value in the untrusted-output boundary
    (plan 02). Keys (OIDs/symbols) and server-derived fields stay bare —
    only device-originated strings are marked."""
    return {
        key: (val if key == "family_hint"
              else wrap_device_output(val, device=dev.name, family=dev.family,
                                      command=f"{tool} {key}"))
        for key, val in values.items()
    }


def register_snmp_tools(mcp) -> None:
    """Register the 4 read-only SNMP tools."""

    @mcp.tool()
    def snmp_probe(device: str) -> dict[str, str]:
        """SNMP identity probe (read-only): MIB-II system group — exact firmware
        via sysDescr, plus a sysObjectID -> family hint. Works without any CLI/SSH
        session, so it is the safe first contact for fragile-SSH units."""
        dev = get_device(device)
        if _demo_state(dev.name):
            values = _demo_snmp_scalars(dev)
            out = {
                "sysDescr": values["1.3.6.1.2.1.1.1.0"],
                "sysObjectID": values["1.3.6.1.2.1.1.2.0"],
                "sysName": values["1.3.6.1.2.1.1.5.0"],
                "sysLocation": values["1.3.6.1.2.1.1.6.0"],
                "family_hint": dev.family,
            }
            audit("snmp_probe", device, detail="demo")
            return _wrap_values(out, dev, "snmp_probe")
        s = _snmp()
        out = s.snmp_probe(dev)
        audit("snmp_probe", device)
        return _wrap_values(out, dev, "snmp_probe")

    @mcp.tool()
    def snmp_get(device: str, oids: list[str]) -> dict[str, str]:
        """SNMP GET of explicit OIDs (read-only), values keyed by OID with the
        symbolic name appended and decoded with catalog semantics (enum meaning,
        units) when the knowledge catalog is present. This — not snmp_walk — is
        the reliable way to poll families whose agent has a sparse GETNEXT chain
        (minid)."""
        dev = get_device(device)
        if not oids:
            raise ToolError("pass at least one OID, e.g. ['1.3.6.1.2.1.1.1.0']")
        if len(oids) > 64:
            raise ToolError("max 64 OIDs per call — split larger polls")
        if _demo_state(dev.name):
            scalars = _demo_snmp_scalars(dev)
            out = {
                f"{oid}  ({oid})": scalars.get(oid, "ERROR: noSuchObject") for oid in oids
            }
            audit("snmp_get", device, detail=f"demo::{len(oids)} oids")
            return _wrap_values(out, dev, "snmp_get")
        s = _snmp()
        raw = s.snmp_get(dev, oids)
        audit("snmp_get", device, detail=f"{len(oids)} oids")
        answered = sum(1 for v in raw.values() if not v.startswith(("ERROR", "PDU-ERROR")))
        _log_observation(dev, "snmp_get", f"{len(oids)} explicit OIDs", f"{answered} answered")
        return _wrap_values(
            {f"{oid}  ({s.resolve_name(oid)})": _decorate(oid, val) for oid, val in raw.items()},
            dev, "snmp_get")

    @mcp.tool()
    def snmp_walk(device: str, oid: str, max_rows: int = 200) -> dict:
        """SNMP GETNEXT walk within a subtree (read-only), row-capped. Returns
        symbolic rows plus explicit completeness flags — `capped` means MORE data
        exists beyond max_rows, and RAD agents signal end-of-view by silence
        (reported in `note`, not an error). On minid prefer snmp_get: its agent's
        NEXT chain is sparse and walks under-report."""
        dev = get_device(device)
        max_rows = max(1, min(int(max_rows), 2000))
        if _demo_state(dev.name):
            scalars = _demo_snmp_scalars(dev)
            rows = {k: v for k, v in scalars.items() if k.startswith(oid.rstrip("."))}
            ordered = dict(sorted(rows.items())[:max_rows])
            audit("snmp_walk", device, detail=f"demo::{oid} ({len(ordered)} rows)")
            return {
                "root": f"{oid}  ({oid})",
                "rows": _wrap_values({f"{k}  ({k})": v for k, v in ordered.items()},
                                     dev, "snmp_walk"),
                "row_count": len(ordered),
                "capped": len(rows) > len(ordered),
                "note": "demo data",
            }
        s = _snmp()
        rows, capped, note = s.snmp_walk(dev, oid, max_rows)
        audit("snmp_walk", device, detail=f"{oid} ({len(rows)} rows)")
        _log_observation(dev, "snmp_walk", f"walk {oid}",
                         f"{len(rows)} rows{' (capped)' if capped else ''}{'; ' + note if note else ''}")
        return {
            "root": f"{oid}  ({s.resolve_name(oid)})",
            "rows": _wrap_values(
                {f"{o}  ({s.resolve_name(o)})": _decorate(o, v) for o, v in rows},
                dev, "snmp_walk"),
            "row_count": len(rows),
            "capped": capped,
            "note": note or ("complete" if not capped else ""),
        }

    @mcp.tool()
    def snmp_build_poll_plan(refs: list[str], family: str, max_rows_per_walk: int = 200) -> dict:
        """Build an OFFLINE SNMP poll plan from concepts/symbols/OIDs for a target
        family (Phase 4). Resolves refs against the knowledge catalog, expands
        tables, excludes non-readable and notification-only objects, and honors
        the family's live-verified transport profile (version, GET-vs-walk
        strategy, end-of-view behavior). NEVER contacts a device — show the
        returned operations to the user and ask the confirmation question before
        executing them via snmp_get/snmp_walk."""
        k = _knowledge()
        if not refs:
            raise ToolError("pass at least one concept/symbol/OID, e.g. ['erpTable', 'ERP R-APS counters']")
        out = _kcall(k.build_poll_plan, refs, family, max_rows_per_walk=max_rows_per_walk)
        out = _fallback_snmp_plan(refs, out)
        audit("snmp_build_poll_plan", "-", detail=f"{family}: {len(refs)} refs")
        return out
