"""SecFlow family driver (SF-1p / SecFlow secure industrial gateways).

VERIFIED live: SF-1p Sw 6.5.0.35 (lab unit SF-1p-187). Inherits the shared
RAD CLI dialect; SecFlow-specific contexts include sd-iot and the industrial
port types. Netmiko rad_etx works as-is.
"""
from __future__ import annotations

from .radcli import RadCliDriver


class SecFlowDriver(RadCliDriver):
    family = "secflow"
