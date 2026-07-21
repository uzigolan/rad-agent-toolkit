"""SecFlow family driver (SF-1p / SecFlow secure industrial gateways).

Driver version: 1.0 (2026-07-14). Bump this line and the `version` attribute
together on any change to this family.

VERIFIED live: SF-1p Sw 6.5.0.35 (lab unit SF-1p-187). Inherits the shared
RAD CLI dialect; SecFlow-specific contexts include sd-iot and the industrial
port types. Netmiko rad_etx works as-is.
"""
from __future__ import annotations

from .radcli import RadCliDriver


class SecFlowDriver(RadCliDriver):
    family = "secflow"
    version = "1.0"

    # Debug OS shell: Ubuntu Linux, same as ETX-1p — `debug shell` from an
    # already-debug_logon'd session, `exit` returns to the RAD CLI.
    debug_shell_enter_cmd = "debug shell"
    debug_shell_exit_cmd = "exit"

    # ── Override points (all inherited from RadCliDriver) ──────────────────
    # SecFlow matches the shared context-CLI dialect today. To diverge, set a
    # knob below — extend tuples via `RadCliDriver.<knob> + (...)` rather than
    # restating a default (restating would drift when the base changes):
    #   netmiko_device_type   = "rad_etx"
    #   show_whitelist        = RadCliDriver.show_whitelist + (...)
    #   configure_contexts    = RadCliDriver.configure_contexts + (...)  # e.g. sd-iot / industrial ports
    #   health_sequence       = (...)                 # full sweep, run in one session
    #   config_export_command = "info"
    #   save_command          = "save"
    #   def is_show_allowed(self, command: str) -> bool: ...   # only for exotic read rules
    #   ssh_connect_options   = {...}   # older/unstable SSH: legacy KEX/ciphers, timeouts, keepalive
    #   connect_attempts = 5 ; connect_backoff = 3.0            # more retry patience on a flaky link
