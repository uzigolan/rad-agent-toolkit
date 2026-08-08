"""Capability-grouped tool registration (plan 01).

One module per group; each exposes a `register_<group>_tools(mcp)` function.
The groups mirror the future server boundaries in docs/plan/DECOMPOSITION.md,
so plan 09 becomes moving these modules between packages, not untangling one
file. Which groups get registered is decided once at startup by
rad_mcp.profile.resolve_profile() — see server.py.
"""
from .knowledge import register_knowledge_tools
from .device import register_device_tools
from .snmp import register_snmp_tools
from .debug import register_debug_tools
from .inventory import register_inventory_tools
from .dev import register_dev_tools
from .introspection import register_introspection_tools

__all__ = [
    "register_knowledge_tools",
    "register_device_tools",
    "register_snmp_tools",
    "register_debug_tools",
    "register_inventory_tools",
    "register_dev_tools",
    "register_introspection_tools",
]
