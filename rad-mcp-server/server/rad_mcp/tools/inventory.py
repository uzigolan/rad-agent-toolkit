"""inventory group — fleet writes (add/update/remove device).

Off by default in the lean profile (RAD_MCP_INVENTORY_WRITE=true to enable):
a shared HTTP deployment must not let any connected client rewrite the fleet.
Credential provisioning is NOT here — set_device_credentials was removed from
the MCP surface entirely (plan 01); use the rad-mcp-set-credentials CLI on
the server host. Future home: the rad-inventory server (plan 09).
"""
from __future__ import annotations

from ..audit import audit
from ..drivers import get_driver
from ..inventory import (add_device_entry, get_device, remove_device_entry,
                         update_device_entry)
from ..runtime import _demo_confirm_bypass, _demo_stop, _require_write_scope


def register_inventory_tools(mcp) -> None:
    """Register the 3 inventory write tools (caller gates on write mode)."""

    @mcp.tool()
    def add_device(
        name: str,
        host: str,
        family: str,
        transport: str = "ssh",
        port: int | None = None,
        groups: list[str] | None = None,
        description: str = "",
        overwrite: bool = False,
    ) -> dict:
        """Register a new device in the inventory (facts only — credentials
        are set separately, by a human, with the rad-mcp-set-credentials CLI
        on the server host). Write-gated: stdio by default, or HTTP with a
        write-scoped token. `family` must be a driver rad-mcp already ships
        (see list_devices/drivers — e.g. 'secflow', 'etx1p', 'etx2'); this
        does not add support for a new CLI dialect, only a new unit of an
        existing one.

        `transport` is 'ssh' (default) or 'telnet' — same CLI over either.
        `port` defaults to the transport's standard port (22 for ssh, 23 for
        telnet) when omitted. Prefer ssh when the unit offers both; telnet
        sends credentials and config in cleartext, so reserve it for units
        (or lab setups) where SSH is unavailable.

        After this call: have someone on the server host run
        `rad-mcp-set-credentials <name>` (prompts for the password; also
        handles SNMP secrets), or put RAD_MCP_<NAME>_USERNAME /
        RAD_MCP_<NAME>_PASSWORD (name upper-cased, dashes -> underscores) in
        server/.env by hand — or rely on the global RAD_MCP_USERNAME /
        RAD_MCP_PASSWORD if this device shares them. NEW .env keys are picked
        up automatically on the next connection (no restart); only CHANGING
        an already-loaded key still needs a server restart. Then run
        test_connectivity, then health_check.
        """
        _require_write_scope()
        get_driver(family)  # raises with the valid-family list if unknown
        inv_path = add_device_entry(
            name, host, family, transport=transport, port=port,
            groups=groups or [], description=description, overwrite=overwrite,
        )
        audit("add_device", name,
              detail=f"host={host} family={family} transport={transport} overwrite={overwrite}")
        env_prefix = "RAD_MCP_" + name.upper().replace("-", "_")
        return {
            "status": f"Added '{name}' to {inv_path.name}.",
            "device": get_device(name).summary(),
            "next_steps": [
                f"Have someone on the server host set its credentials with the "
                f"CLI: rad-mcp-set-credentials {name} --username <user> "
                "(prompts for the password; SNMP flags available — see --help). "
                f"Alternative: put {env_prefix}_USERNAME / {env_prefix}_PASSWORD "
                "in server/.env by hand, or rely on the global "
                "RAD_MCP_USERNAME/RAD_MCP_PASSWORD if shared.",
                f"Run test_connectivity('{name}') then health_check('{name}').",
                f"If '{family}'s CLI reference is missing this unit's context "
                f"or firmware differs from what was harvested, run "
                f"/rad-harvest {name} to build/refresh it.",
            ],
        }

    @mcp.tool()
    def update_device(
        name: str,
        host: str | None = None,
        family: str | None = None,
        transport: str | None = None,
        port: int | None = None,
        groups: list[str] | None = None,
        description: str | None = None,
    ) -> dict:
        """Update a subset of an existing inventory device's fields (host,
        family, transport, port, groups, description). Omitted parameters
        keep their current value. `transport` is 'ssh' or 'telnet'; when the
        transport changes and the port was the old transport's default, the
        port re-resolves to the new default (22 for ssh, 23 for telnet) —
        pass `port` explicitly to override. Does not touch credentials —
        those are managed with the rad-mcp-set-credentials CLI on the server
        host. Changing `family` mid-life is unusual (normally means
        the entry was misconfigured, not that the hardware changed) — confirm
        with the user before doing that specifically.
        """
        _require_write_scope()
        if family is not None:
            get_driver(family)  # raises with the valid-family list if unknown
        updated = update_device_entry(
            name, host=host, family=family, transport=transport, port=port,
            groups=groups, description=description,
        )
        audit("update_device", name,
              detail=f"host={host} family={family} transport={transport} groups={groups}")
        return {"status": f"Updated '{name}'.", "device": updated.summary()}

    @mcp.tool()
    def remove_device(name: str, confirm: bool = False) -> str:
        """Remove a device from the local inventory. Does not touch the
        device itself or delete any backups/audit history — this only stops
        rad-mcp from knowing about it. Requires confirm=true after the user
        has approved removing this specific device."""
        _require_write_scope()
        if not confirm and not _demo_confirm_bypass(name):
            return "REFUSED: remove_device requires confirm=true after the user has approved removing this device."
        get_device(name)  # raises with the known-devices list if unknown
        was_demo = _demo_stop(name)
        remove_device_entry(name)
        audit("remove_device", name)
        demo_note = " Demo runtime stopped." if was_demo else ""
        return f"Removed '{name}' from the inventory.{demo_note} (Credentials in server/.env, if any, were left in place — remove those manually if no longer needed.)"
