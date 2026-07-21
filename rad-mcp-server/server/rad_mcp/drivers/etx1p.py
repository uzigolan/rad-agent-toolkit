"""ETX-1p family driver (compact carrier-grade demarcation units).

Driver version: 1.0 (2026-07-14). Bump this line and the `version` attribute
together on any change to this family.

VERIFIED live: ETX-1p Sw 6.5.0.43 (lab unit Device3, 172.17.232.193) — modern
context-based RAD CLI (same dialect as SecFlow/ETX-2, prompt
`Device3>config>system#`), NOT the legacy ETX-1 menu CLI. Netmiko rad_etx
works as-is.
"""
from __future__ import annotations

from .radcli import RadCliDriver


class Etx1pDriver(RadCliDriver):
    family = "etx1p"
    version = "1.0"

    # Debug OS shell: Ubuntu Linux, same as SecFlow — `debug shell` from an
    # already-debug_logon'd session, `exit` returns to the RAD CLI.
    debug_shell_enter_cmd = "debug shell"
    debug_shell_exit_cmd = "exit"

    # ── Override points (all inherited from RadCliDriver) ──────────────────
    # ETX-1p speaks the modern shared dialect (NOT the legacy etx1 menu CLI)
    # and matches it today. To diverge, set a knob below — extend tuples via
    # `RadCliDriver.<knob> + (...)`, don't restate defaults:
    #   netmiko_device_type   = "rad_etx"
    #   show_whitelist        = RadCliDriver.show_whitelist + (...)
    #   configure_contexts    = RadCliDriver.configure_contexts + (...)
    #   health_sequence       = (...)                 # full sweep, run in one session
    #   config_export_command = "info"
    #   save_command          = "save"
    #   def is_show_allowed(self, command: str) -> bool: ...   # only for exotic read rules
    #   ssh_connect_options   = {...}   # older/unstable SSH: legacy KEX/ciphers, timeouts, keepalive
    #   connect_attempts = 5 ; connect_backoff = 3.0            # more retry patience on a flaky link
