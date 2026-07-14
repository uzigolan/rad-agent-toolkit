"""MP-1 family driver (mp1).

Driver version: 1.0 (2026-07-14). Bump this line and the `version` attribute
together on any change to this family.

VERIFIED live: MP-1 SW 2.20(0.61) (lab unit mp-one, 172.17.161.88, prompt
`MP-1#`), 2026-07-14 — full `?`-help harvested (cli-reference-mp1.md,
command-tree-mp1.md) + manual ingested (manual-mp1/); connect transcript in
server/logs/smoke-mp-one.txt. Speaks the shared RAD context-CLI dialect over
standard SSH (netmiko `rad_etx`, no legacy algorithms), so it inherits
RadCliDriver.

**Candidate-database config model** (like mp4100 — confirmed by the root
`commit` / `discard-changes` / `sanity-check` globals in the live tree). Config
edits land in a candidate DB and do NOT touch the running config until `commit`
is issued; `discard-changes` drops the candidate. Consequence for the
staged-write flow: an mp1 stage sequence must END WITH `commit` (before the
final `exit all`) or it silently changes nothing; `save` then persists as usual.
The skill teaches this; push_config just replays lines.
"""
from __future__ import annotations

from .radcli import RadCliDriver


class Mp1Driver(RadCliDriver):
    family = "mp1"
    version = "1.0"

    # Live root tree, 2026-07-14 (mp-one, SW 2.20(0.61)) — MP-1 is a subset of
    # the mp4100 contexts (no fault/oam/peer/slot/test).
    configure_contexts = (
        "access-control", "bridge", "chassis", "cross-connect", "crypto",
        "flows", "management", "port", "protection", "pwe", "qos",
        "reporting", "router", "system", "terminal",
    )

    # ── Other override points (inherited from RadCliDriver) ────────────────
    # Extend via `RadCliDriver.<knob> + (...)`, don't restate defaults:
    #   netmiko_device_type   = "rad_etx"
    #   show_whitelist        = RadCliDriver.show_whitelist + (...)
    #   health_sequence       = (...)   # inherited; identity+alarms match the shared sweep
    #   config_export_command = "info"
    #   save_command          = "save"  # NB: candidate-DB — stage sequences must end with `commit`
    #   ssh_connect_options   = {...}   # not needed on SW 2.20; older units: legacy KEX/ciphers, timeouts
    #   connect_attempts = 5 ; connect_backoff = 3.0
