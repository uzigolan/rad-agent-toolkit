"""dev group — in-process demo devices.

Tool-check / eval fixtures: a demo device answers CLI and SNMP reads
deterministically without any network. Off by default in the lean profile
(RAD_MCP_DEV_TOOLS=true to enable); kept because plan 00's eval harness uses
these as fixtures. Dropped entirely after plan 09.
"""
from __future__ import annotations

from fastmcp.exceptions import ToolError

from ..audit import audit
from ..drivers import get_driver
from ..inventory import (add_device_entry, get_device, remove_device_entry,
                         set_device_credentials as _set_device_credentials)
from ..runtime import (_demo_confirm_bypass, _demo_start, _demo_stop,
                       _require_write_scope)


def register_dev_tools(mcp) -> None:
    """Register the 2 demo-device tools (caller gates on write mode)."""

    @mcp.tool()
    def run_demo_device(
        name: str = "rad-toolcheck-demo",
        host: str = "127.0.0.1",
        family: str = "etx2",
        transport: str = "ssh",
        port: int | None = None,
        groups: list[str] | None = None,
        description: str = "temporary local demo for MCP status checks",
        username: str = "demo",
        password: str = "demo",
        snmp_v1_community: str = "public",
        overwrite: bool = True,
    ) -> dict:
        """Create/update and start a local in-process demo device.

        This helper exists for MCP tool validation when no real hardware is
        registered. It writes a normal inventory entry, stores CLI+SNMP secrets
        the same way the rad-mcp-set-credentials CLI does, and marks the device
        as demo-live so CLI/SNMP read tools return deterministic OK responses.
        """
        _require_write_scope()
        get_driver(family)
        inv_path = add_device_entry(
            name, host, family, transport=transport, port=port,
            groups=groups or ["toolcheck", "demo"], description=description,
            overwrite=overwrite,
        )
        _set_device_credentials(name, username, password, snmp_v1_community=snmp_v1_community)
        dev = get_device(name)
        state = _demo_start(dev, cli_user=username, snmp_v1=snmp_v1_community)
        audit("run_demo_device", name, detail=f"family={family} host={host}")
        return {
            "status": f"Demo device '{name}' is running.",
            "inventory": inv_path.name,
            "device": dev.summary(),
            "demo_runtime": {
                "started": state["started"],
                "cli_user": state["cli_user"],
                "snmp_v1_configured": state["snmp_v1_configured"],
            },
            "next_steps": [
                f"Run test_connectivity('{name}').",
                f"Run health_check('{name}').",
                f"Run snmp_probe('{name}').",
            ],
        }

    @mcp.tool()
    def stop_demo_device(name: str = "rad-toolcheck-demo", remove_from_inventory: bool = False,
                         confirm: bool = False) -> dict:
        """Stop an in-process demo device started by run_demo_device.

        Set remove_from_inventory=true to also remove its inventory row.
        When removing, confirm=true is required.
        """
        _require_write_scope()
        was_demo = _demo_confirm_bypass(name)
        stopped = _demo_stop(name)
        removed = False
        if remove_from_inventory:
            if not confirm and not was_demo:
                raise ToolError("remove_from_inventory=true requires confirm=true")
            get_device(name)
            remove_device_entry(name)
            removed = True
        audit("stop_demo_device", name, detail=f"stopped={stopped} removed={removed}")
        return {
            "status": f"Demo device '{name}' stopped." if stopped else f"No active demo runtime for '{name}'.",
            "removed_from_inventory": removed,
        }
