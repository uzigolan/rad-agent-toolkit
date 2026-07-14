"""Megaplex-4100 family driver (MP-4100 multiservice access nodes).

Driver version: 1.0 (2026-07-14). Bump this line and the `version` attribute
together on any change to this family.

VERIFIED live: MP-4100 Mn 4.91 (lab unit marks-mp4, prompt `mp4100#`),
2026-07-12. Contrary to the old "different CLI - own driver base"
assumption, the MP-4100 speaks the SAME context-based dialect as the
modern portfolio (tree/info/level-info/save globals, per-level `?` help,
`config term length 0` pager disable works, netmiko rad_etx connects) -
with ONE structural difference:

**Candidate-database config model.** Config edits land in a candidate DB
and do NOT touch the running config until the device's own `commit` global
is issued (`discard-changes` drops the candidate). Consequence for the
staged-write flow: a staged sequence for mp4100 must END WITH `commit`
(before the final `exit all`) or it silently changes nothing; `save` then
persists as usual. The skill teaches this; push_config just replays lines.

MP-specific `configure` children (from the live tree): chassis,
cross-connect, peer, pwe, slot, flows, test - TDM/PDH heritage the ETX
family lacks.
"""
from __future__ import annotations

from .radcli import RadCliDriver


class Mp4100Driver(RadCliDriver):
    family = "mp4100"
    version = "1.0"

    # Live root tree, 2026-07-12 (marks-mp4, Mn 4.91).
    configure_contexts = (
        "access-control", "bridge", "chassis", "cross-connect", "crypto",
        "fault", "flows", "management", "oam", "peer", "port", "protection",
        "pwe", "qos", "reporting", "router", "slot", "system", "terminal",
        "test",
    )

    # Identity + alarms confirmed in the manual (Mn 4.91 ch. 10/11):
    # config>system# show device-information, configure reporting ->
    # show active-alarms - identical to the shared dialect, so the
    # inherited health_sequence / config_export_command / save_command apply.

    # ── Other override points (inherited from RadCliDriver) ────────────────
    # Extend via `RadCliDriver.<knob> + (...)`, don't restate defaults:
    #   netmiko_device_type   = "rad_etx"
    #   show_whitelist        = RadCliDriver.show_whitelist + (...)
    #   health_sequence       = (...)   # inherited; identity+alarms match the shared sweep
    #   config_export_command = "info"
    #   save_command          = "save"  # NB: candidate-DB model — stage sequences must end with `commit`
    #   def is_show_allowed(self, command: str) -> bool: ...
    #   ssh_connect_options   = {...}   # older/unstable SSH: legacy KEX/ciphers, timeouts, keepalive
    #   connect_attempts = 5 ; connect_backoff = 3.0            # more retry patience on a flaky link
