"""Read-only SNMP client (GET / GETNEXT walk / identity probe).

NOT a `Backend` subclass — that ABC is CLI-shaped (execute/push_config); SNMP
is a second, read-only window onto the device. Config writes stay exclusively
on the CLI's staged-commit flow: this module never sends SET, by construction.

Credentials (env only, same policy as SSH — never in inventory or tool args):
  RAD_MCP_<NAME>_SNMP_COMMUNITY      v2c community           (per-device)
  RAD_MCP_<NAME>_SNMP_V1_COMMUNITY   v1 community            (per-device —
                                     MP-4100 answers ONLY v1; verified live)
  RAD_MCP_<NAME>_SNMP_V3_USER        v3 USM user, no-auth    (per-device)
  RAD_MCP_SNMP_COMMUNITY / _SNMP_V1_COMMUNITY / _SNMP_V3_USER (global fallbacks)
Per-device beats global; precedence v3 > v2c > v1 when several are set.
(v3 auth/priv keys can be added here when a lab unit actually uses them.)

Agent lessons baked in (verified live 2026-07-16 on minid-1 + etx2v-1 — see
skills/rad-cli-operations/references/snmp-support.md):
  * GETNEXT only — RAD small agents mishandle GETBULK (arc jumps, mis-order).
  * End-of-view = SILENCE, not endOfMibView: both agents stop answering at
    the same spot (ENTITY-MIB entPhysical*.1001). A mid-walk timeout is
    retried once after a pause, then accepted as end-of-view.
  * The minid agent's NEXT chain is SPARSE — discovery walks under-report;
    poll it with explicit OID GETs (snmp_get), not walks.
"""
from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path

from ..inventory import Device, _refresh_env

_REPO = Path(__file__).resolve().parents[3]          # rad-mcp-server/
_OID_MAP_PATH = _REPO / "skills" / "rad-cli-operations" / "references" / "snmp-oid-map.json"
_oid_map: dict[str, str] | None = None

# sysObjectID -> family (RAD enterprise arc 1.3.6.1.4.1.164.6.1.6.<product>).
# Grows as units are probed; see snmp-support.md's live-probe table.
SYS_OBJECT_FAMILY = {  # ALL 7 families verified live 2026-07-16
    "1.3.6.1.4.1.164.6.1.6.36": "minid",
    "1.3.6.1.4.1.164.6.1.6.55": "etx2v",
    "1.3.6.1.4.1.164.6.1.6.68": "etx1p",
    "1.3.6.1.4.1.164.6.1.6.79": "etx2",
    "1.3.6.1.4.1.164.6.1.10.7": "secflow",
    "1.3.6.1.4.1.164.6.1.3.120": "mp4100",
    "1.3.6.1.4.1.164.6.1.3.179": "mp1",
}

SYSTEM_OIDS = {
    "sysDescr": "1.3.6.1.2.1.1.1.0",
    "sysObjectID": "1.3.6.1.2.1.1.2.0",
    "sysUpTime": "1.3.6.1.2.1.1.3.0",
    "sysName": "1.3.6.1.2.1.1.5.0",
    "sysLocation": "1.3.6.1.2.1.1.6.0",
}


def _load_oid_map() -> dict[str, str]:
    global _oid_map
    if _oid_map is None:
        try:
            raw = json.loads(_OID_MAP_PATH.read_text(encoding="utf-8"))
            _oid_map = {k: v for k, v in raw.items() if not k.startswith("_")}
        except Exception:
            _oid_map = {}
    return _oid_map


def resolve_name(oid: str) -> str:
    """Longest-prefix symbolic name from the compiled MIB map, or the raw OID."""
    m = _load_oid_map()
    parts = oid.split(".")
    for i in range(len(parts), 1, -1):
        hit = m.get(".".join(parts[:i]))
        if hit:
            rest = ".".join(parts[i:])
            return f"{hit}{'.' + rest if rest else ''}"
    return oid


def _auth_for(device: Device):
    """Resolve pysnmp auth object from env. Raises RuntimeError when unset."""
    from pysnmp.hlapi.v3arch.asyncio import CommunityData, UsmUserData

    _refresh_env()
    prefix = "RAD_MCP_" + device.name.upper().replace("-", "_")
    v3 = os.environ.get(f"{prefix}_SNMP_V3_USER") or os.environ.get("RAD_MCP_SNMP_V3_USER")
    community = os.environ.get(f"{prefix}_SNMP_COMMUNITY") or os.environ.get("RAD_MCP_SNMP_COMMUNITY")
    v1 = os.environ.get(f"{prefix}_SNMP_V1_COMMUNITY") or os.environ.get("RAD_MCP_SNMP_V1_COMMUNITY")
    if v3:
        return UsmUserData(v3)                       # no-auth-no-priv
    if community:
        return CommunityData(community, mpModel=1)   # v2c
    if v1:
        return CommunityData(v1, mpModel=0)          # v1 (MP-4100 is v1-only)
    raise RuntimeError(
        f"No SNMP credentials for '{device.name}': set {prefix}_SNMP_COMMUNITY "
        f"(v2c), {prefix}_SNMP_V1_COMMUNITY (v1), or {prefix}_SNMP_V3_USER "
        "(v3 no-auth) in server/.env (or the RAD_MCP_SNMP_* globals)."
    )


async def _a_get(device: Device, oids: list[str], timeout: float = 3.0) -> dict[str, str]:
    from pysnmp.hlapi.v3arch.asyncio import (
        SnmpEngine, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, get_cmd,
    )
    engine = SnmpEngine()
    try:
        transport = await UdpTransportTarget.create((device.host, 161), timeout=timeout, retries=1)
        auth = _auth_for(device)
        out: dict[str, str] = {}
        for oid in oids:
            errInd, errStat, errIdx, varBinds = await get_cmd(
                engine, auth, transport, ContextData(), ObjectType(ObjectIdentity(oid)))
            if errInd:
                out[oid] = f"ERROR: {errInd}"
                continue
            if errStat:
                out[oid] = f"PDU-ERROR: {errStat.prettyPrint()}"
                continue
            for vb in varBinds:
                out[str(vb[0].get_oid())] = vb[1].prettyPrint()
        return out
    finally:
        engine.close_dispatcher()


async def _a_walk(device: Device, root: str, max_rows: int,
                  timeout: float = 3.0) -> tuple[list[tuple[str, str]], bool, str]:
    """GETNEXT walk within `root`. Returns (rows, capped?, stop_note)."""
    from pysnmp.hlapi.v3arch.asyncio import (
        SnmpEngine, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, next_cmd,
    )
    engine = SnmpEngine()
    rows: list[tuple[str, str]] = []
    capped, note = False, ""
    try:
        transport = await UdpTransportTarget.create((device.host, 161), timeout=timeout, retries=1)
        auth = _auth_for(device)
        cur = ObjectType(ObjectIdentity(root))
        root_p = tuple(int(x) for x in root.split("."))
        retried = False
        while len(rows) < max_rows:
            errInd, errStat, errIdx, table = await next_cmd(
                engine, auth, transport, ContextData(), cur)
            if errInd:
                if not retried:
                    retried = True
                    await asyncio.sleep(2.0)
                    continue
                note = (f"agent stopped responding after "
                        f"{rows[-1][0] if rows else root} (RAD agents signal "
                        "end-of-view by silence — expected, not an outage)")
                break
            retried = False
            if errStat or not table:
                break
            vb = table[0]
            oid_t = tuple(vb[0].get_oid().asTuple())
            if oid_t[:len(root_p)] != root_p:
                break  # left the subtree — complete
            oid_s = str(vb[0].get_oid())
            if vb[1].__class__.__name__ == "EndOfMibView":
                break
            if rows and oid_s == rows[-1][0]:
                note = "agent looped (same OID twice)"
                break
            rows.append((oid_s, vb[1].prettyPrint()))
            if len(rows) >= max_rows:
                capped = True
                break
            cur = ObjectType(ObjectIdentity(oid_s))
        return rows, capped, note
    finally:
        engine.close_dispatcher()


# --- sync wrappers (FastMCP runs sync tools in a worker thread) ------------

def snmp_get(device: Device, oids: list[str]) -> dict[str, str]:
    """Explicit GETs — the reliable way to poll the sparse-agent families."""
    return asyncio.run(_a_get(device, oids))


def snmp_walk(device: Device, root: str, max_rows: int = 200) -> tuple[list[tuple[str, str]], bool, str]:
    return asyncio.run(_a_walk(device, root, max_rows))


def snmp_probe(device: Device) -> dict[str, str]:
    """MIB-II system-group identity + sysObjectID -> family hint."""
    raw = asyncio.run(_a_get(device, list(SYSTEM_OIDS.values())))
    out: dict[str, str] = {}
    for label, oid in SYSTEM_OIDS.items():
        out[label] = raw.get(oid, raw.get(oid.rstrip(".0"), ""))
    sys_oid = out.get("sysObjectID", "")
    # pysnmp renders it like 'SNMPv2-SMI::enterprises.164.6.1.6.36' or numeric
    num = sys_oid.replace("SNMPv2-SMI::enterprises", "1.3.6.1.4.1")
    out["family_hint"] = SYS_OBJECT_FAMILY.get(num, "(unknown sysObjectID — add to SYS_OBJECT_FAMILY once identified)")
    return out
