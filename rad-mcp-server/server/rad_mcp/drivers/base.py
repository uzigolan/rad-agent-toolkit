"""Driver ABC: one implementation per RAD product family.

A driver encodes the CLI dialect — which commands are safe to read with,
which command set constitutes a health check, and how config is exported
and saved. Transport is the backend's job, not the driver's.
"""
from __future__ import annotations

from abc import ABC


class RadDriver(ABC):
    family: str
    netmiko_device_type: str

    # Read commands must start with one of these prefixes (lower-cased match).
    show_whitelist: tuple[str, ...] = ()

    # Known navigable contexts under the config root (for context-read validation).
    configure_contexts: tuple[str, ...] = ()

    # Full command sequence (including context navigation) run by health_check
    # over a single session, in order.
    health_sequence: tuple[str, ...] = ()

    # Command that dumps the full device configuration.
    config_export_command: str = ""

    # Command that persists running config to startup.
    save_command: str = ""

    def is_show_allowed(self, command: str) -> bool:
        cmd = command.strip().lower()
        return any(cmd.startswith(prefix) for prefix in self.show_whitelist)
