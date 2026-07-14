"""Driver ABC: one implementation per RAD product family.

A driver encodes the CLI dialect — which commands are safe to read with,
which command set constitutes a health check, and how config is exported
and saved. Transport is the backend's job, not the driver's.
"""
from __future__ import annotations

from abc import ABC


class RadDriver(ABC):
    family: str
    # Driver version — bump when THIS family's behavior changes (contexts,
    # health sweep, SSH profile, quirks). Baseline "1.0" for every family; lets
    # us tell which driver revision is loaded (introspect: get_driver(fam).version).
    version: str = "1.0"
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

    # Extra keyword args merged into the SSH ConnectHandler for this family
    # (Netmiko → Paramiko). This is where a family with an OLDER or LESS STABLE
    # SSH server declares what it needs: legacy key-exchange/ciphers via
    # `disabled_algorithms`, longer `conn_timeout`/`banner_timeout`/`auth_timeout`,
    # TCP `keepalive`, or slower pacing (`global_delay_factor`, `fast_cli=False`).
    # Keys must be valid ConnectHandler params. Read-only — never mutate in place;
    # the backend layers it over its baseline. Empty = use the shared defaults.
    ssh_connect_options: dict[str, object] = {}

    # SSH connect retry policy. RAD units reject a new session while the prior
    # one is still tearing down, and flaky links need more patience — a family
    # on an unstable connection can raise attempts / lengthen the backoff.
    connect_attempts: int = 3
    connect_backoff: float = 2.0   # seconds; delay before retry N is backoff * N

    def is_show_allowed(self, command: str) -> bool:
        cmd = command.strip().lower()
        return any(cmd.startswith(prefix) for prefix in self.show_whitelist)
