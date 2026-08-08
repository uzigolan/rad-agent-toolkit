"""Tool-profile resolution (plan 01 — capability grouping).

The server's tools are organized into capability groups that mirror the
future per-server boundaries in docs/plan/DECOMPOSITION.md:

  knowledge      offline catalog searches (mib_*/cli_search/manual_search/...)
  device         inventory reads + CLI reads + the staged-commit write flow
  snmp           read-only SNMP (GET/GETNEXT; this toolkit never sends SET)
  debug          the hidden `debug` tree — menu, OS shell, logon challenge
  inventory      fleet writes (add/update/remove device)
  dev            in-process demo devices (eval/tool-check fixtures)
  introspection  version/status reporting tools (folded into rad://status)

RAD_MCP_TOOL_PROFILE selects the surface:

  legacy (default)  every group registered — same surface as before this
                    change (minus set_device_credentials, which is no longer
                    an MCP tool in ANY profile; use the rad-mcp-set-credentials
                    CLI). Group flags are IGNORED so the surface stays
                    predictable for existing installs.
  lean              knowledge + device + snmp (25 tools). Optional groups are
                    opt-in per flag:
                      RAD_MCP_SNMP=false          drop the 4 SNMP tools
                      RAD_MCP_DEBUG_TOOLS=true    add the 8 debug tools
                      RAD_MCP_INVENTORY_WRITE=true add add/update/remove_device
                      RAD_MCP_DEV_TOOLS=true      add run/stop_demo_device

RAD_MCP_READONLY=true always wins over profile and flags: write tools are
never registered when it is set, in either profile.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field

_TRUE = ("1", "true", "yes")
_FALSE = ("0", "false", "no")

PROFILES = ("legacy", "lean")


@dataclass(frozen=True)
class ToolProfile:
    name: str
    knowledge: bool
    device: bool
    snmp: bool
    debug: bool
    inventory: bool
    dev: bool
    introspection: bool
    flags: dict = field(default_factory=dict)

    def groups(self) -> dict[str, bool]:
        return {
            "knowledge": self.knowledge,
            "device": self.device,
            "snmp": self.snmp,
            "debug": self.debug,
            "inventory": self.inventory,
            "dev": self.dev,
            "introspection": self.introspection,
        }


def _flag(env: dict, var: str, default: bool) -> bool:
    raw = (env.get(var) or "").strip().lower()
    if not raw:
        return default
    if raw in _TRUE:
        return True
    if raw in _FALSE:
        return False
    raise SystemExit(f"{var} must be a boolean (true/false), got {raw!r}")


def resolve_profile(env: dict | None = None) -> ToolProfile:
    """Resolve RAD_MCP_TOOL_PROFILE + group flags once, at startup.

    Unknown profile values fail fast — no silent fallback to a surface the
    operator did not ask for.
    """
    env = dict(os.environ if env is None else env)
    name = (env.get("RAD_MCP_TOOL_PROFILE") or "legacy").strip().lower()
    if name not in PROFILES:
        raise SystemExit(
            f"Unknown RAD_MCP_TOOL_PROFILE {name!r} — valid values: "
            + ", ".join(PROFILES)
        )
    flags = {
        "RAD_MCP_SNMP": env.get("RAD_MCP_SNMP", ""),
        "RAD_MCP_DEBUG_TOOLS": env.get("RAD_MCP_DEBUG_TOOLS", ""),
        "RAD_MCP_INVENTORY_WRITE": env.get("RAD_MCP_INVENTORY_WRITE", ""),
        "RAD_MCP_DEV_TOOLS": env.get("RAD_MCP_DEV_TOOLS", ""),
    }
    if name == "legacy":
        # Byte-for-byte the pre-grouping surface (minus set_device_credentials):
        # flags are ignored so existing installs see no change.
        return ToolProfile(
            name="legacy", knowledge=True, device=True, snmp=True,
            debug=True, inventory=True, dev=True, introspection=True,
            flags=flags,
        )
    return ToolProfile(
        name="lean",
        knowledge=True,
        device=True,
        snmp=_flag(env, "RAD_MCP_SNMP", True),
        debug=_flag(env, "RAD_MCP_DEBUG_TOOLS", False),
        inventory=_flag(env, "RAD_MCP_INVENTORY_WRITE", False),
        dev=_flag(env, "RAD_MCP_DEV_TOOLS", False),
        introspection=False,  # folded into the rad://status resource
        flags=flags,
    )
