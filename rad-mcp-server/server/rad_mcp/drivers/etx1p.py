"""ETX-1p family driver (compact carrier-grade demarcation units).

VERIFIED live: ETX-1p Sw 6.5.0.43 (lab unit Device3, 172.17.232.193) — modern
context-based RAD CLI (same dialect as SecFlow/ETX-2, prompt
`Device3>config>system#`), NOT the legacy ETX-1 menu CLI. Netmiko rad_etx
works as-is.
"""
from __future__ import annotations

from .radcli import RadCliDriver


class Etx1pDriver(RadCliDriver):
    family = "etx1p"
