"""ETX-2V family driver (etx2v).

Driver version: 1.0 (2026-07-15). Bump this line and the `version` attribute
together on any change to this family.

RAD ETX-2V (onboarding target manual `ETX-2V-CA_AC_2CMB_4U_D_mn`: a 4U chassis,
AC feed, CMB common cards). Despite the chassis hardware, the CLI is RAD's
**uCPE-OS** platform (VNF hosting), NOT a chassis/slot/card model — so it gets
its own family, distinct from the compact ETX-2I covered by `etx2`.

VERIFIED live (2026-07-15, etx2v-1 @ 172.17.240.100, prompt `uCPE-OS#`): the
modern shared RAD context CLI (netmiko rad_etx) — `configure system`,
`exit all`, `info`/`save` globals all behave as on the other context-CLI
families. Standard SSH (connected cleanly on the default profile; NOT fragile
like minid). Full harvest: 719-node `tree`, 527 captures in 7.4 min, device
verified clean (all 23 temp objects rolled back, zero zzz-hrvst residue).
Distinctive: a top-level `virtualization` context (uCPE/NFV instance +
repository/network) not present on any other family; also crypto/ipsec, oam
twamp, management ldap. CLI reference + hardware/BIOS manual harvested
(cli-reference-etx2v.md, manual-etx2v/).
"""
from __future__ import annotations

from .radcli import RadCliDriver


class Etx2vDriver(RadCliDriver):
    family = "etx2v"
    version = "1.0"

    # Grounded from the live 719-node tree (etx2v-1, uCPE-OS), 2026-07-15.
    configure_contexts = (
        "access-control", "bridge", "crypto", "fault", "management", "oam",
        "port", "qos", "reporting", "router", "system", "terminal",
        "virtualization",
    )

    # ── Other override points (inherited from RadCliDriver) ────────────────
    # Extend via `RadCliDriver.<knob> + (...)`, don't restate defaults:
    #   netmiko_device_type   = "rad_etx"
    #   show_whitelist        = RadCliDriver.show_whitelist + (...)
    #   health_sequence       = (...)   # ETX-2 lacks `show resources`
    #   config_export_command = "info"
    #   save_command          = "save"
    #   ssh_connect_options   = {...}   # only if probe shows a fragile SSH
    #   connect_attempts = 5 ; connect_backoff = 3.0
