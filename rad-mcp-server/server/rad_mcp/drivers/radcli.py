"""Shared RAD CLI dialect — the context-based hierarchical CLI used by the
modern RAD portfolio (ETX-2 family, SecFlow family, and others).

VERIFIED live against SecFlow-1p (SF-1p, Sw 6.5.0.35), July 2026 — full
command tree in server/logs/smoke-lab-sf1p.txt. Netmiko device_type: rad_etx.

Verified dialect facts:
- Prompt: `<name>#`. `exit all` returns to root from any context.
- `show ...` commands exist only INSIDE contexts, not at root.
- Global commands available everywhere: info, level-info, help, tree, ping,
  trace-route, history, save, copy, exec, exit, logout.
- Root `info` dumps the full running configuration in replayable CLI form.
- Alarms/logs: `configure reporting` -> show active-alarms / alarm-log / log.
- Device identity: `configure system` -> show device-information.
- Startup/rollback config files: `file` context -> show startup-config etc.
- DANGEROUS context: `admin` holds reboot / force-reboot / factory-default*.

Product families with a different CLI (e.g. legacy ETX-1, MP-4100/Megaplex)
get their own driver base rather than subclassing this one.
"""
from __future__ import annotations

from .base import RadDriver


class RadCliDriver(RadDriver):
    """Base driver for every RAD product speaking the shared context CLI."""

    netmiko_device_type = "rad_etx"

    # Root-safe / global read commands (single-line, no context needed).
    show_whitelist = (
        "show",        # only meaningful inside a context; harmless error at root
        "info",
        "level-info",
        "help",
        "tree",
        "ping",
        "trace-route",
        "history",
    )

    # Known second-level contexts under `configure`; subclasses narrow/extend
    # per product. Used to validate context navigation for context-scoped reads.
    configure_contexts = (
        "access-control", "bridge", "crypto", "fault", "management", "monitor",
        "oam", "port", "protection", "qos", "reporting", "router", "sd-iot",
        "system", "terminal",
    )

    # Health sweep: full command sequence run over one session, in order.
    health_sequence = (
        "exit all",
        "configure system",
        "show device-information",
        "exit all",
        "configure reporting",
        "show active-alarms",
        "exit all",
    )

    config_export_command = "info"   # verified: root info = full running config
    save_command = "save"            # verified: global command
