"""ETX-2 family driver (ETX-203AX / ETX-205A / ETX-220A class carrier-Ethernet
demarcation devices).

Speaks the shared RAD CLI dialect (see radcli.py). NOT YET verified against a
live ETX-2 unit — the dialect facts were verified on a SecFlow-1p, and Netmiko's
rad_etx type was written for ETX. Verify with `python -m rad_mcp.smoke <device>`
when an ETX-2 lab unit is available, and adjust configure_contexts (ETX-2 has
flows/EVC contexts the SecFlow tree does not show).
"""
from __future__ import annotations

from .radcli import RadCliDriver


class Etx2Driver(RadCliDriver):
    family = "etx2"

    # ETX-2 adds carrier-Ethernet contexts; superset kept permissive until a
    # live ETX-2 `tree` capture grounds this list.
    configure_contexts = RadCliDriver.configure_contexts + ("flows", "spanning-tree")
