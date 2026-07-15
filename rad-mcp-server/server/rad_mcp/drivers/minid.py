"""MiNID family driver (minid).

Driver version: 1.0 (2026-07-15). Bump this line and the `version` attribute
together on any change to this family.

RAD MiNID — Miniature Network Interface Device: a sleeve / SFP-form-factor
demarcation unit ("sleeve device"). This is its OWN family, unrelated to any
other in the registry; it does not share MP-1/MP-4100 lineage. Onboarding
target: unit at 172.17.166.55 (SW 2.6 per manual "MiNID_ver_2_6_mn").

VERIFIED live (2026-07-15, minid-1 @ 172.17.166.55, prompt `MiNID#`, SW 2.6):
the modern shared RAD context CLI (netmiko rad_etx) — probe confirmed
`MiNID#` → `MiNID>config>system#` navigation with `info`/`save` globals
(**direct-write save**, NOT candidate-DB). 401-node `tree`, 225 captures.
Manual + CLI reference harvested (cli-reference-minid.md, manual-minid/).

Two MiNID-specific traits the harvester had to handle (now general fixes in
scripts/harvest_cli.py): (1) `tree`/help paginate with a bare `more...` prompt
(no dashes) advanced by SPACE, and the tree is double-spaced — both normalized;
(2) the SSH is FRAGILE — it drops on a long (~76-min) full crawl, so minid was
harvested BRANCH-BY-BRANCH (per-subtree sessions, one-time `--tree-cache`), the
resilient path for an unstable link. Re-harvest the same way, not with a single
full run.

SSH is FRAGILE and UNIQUE. This family ships a deliberately patient connection
profile (long timeouts, keepalive, slow pacing, extra retry patience) via the
per-family SSH knobs below. Even so it cannot sustain a full-tree session —
prefer `--branch` runs. The patient profile is intentionally conservative;
speeding it up (fast_cli, lower global_delay_factor) risks more drops.
"""
from __future__ import annotations

from .radcli import RadCliDriver


class MinidDriver(RadCliDriver):
    family = "minid"
    version = "1.0"

    # Grounded from the live 401-node tree (minid-1, SW 2.6), 2026-07-15.
    # MiNID is a compact NID — 12 configure contexts, no crypto/fault/bridge.
    configure_contexts = (
        "access-control", "flows", "management", "oam", "packet-capture",
        "port", "qos", "reporting", "router", "service", "system", "test",
    )

    # ── Fragile-SSH profile (the reason this family needs its own driver knobs) ─
    # Patient defaults for an old / unstable SSH server. Merged over the backend
    # baseline by SSHBackend._connect; read-only, never mutated in place.
    ssh_connect_options = {
        "conn_timeout": 30,        # slow to accept the TCP/SSH session
        "banner_timeout": 30,      # slow to send the SSH banner
        "auth_timeout": 30,        # slow auth exchange
        "keepalive": 10,           # TCP keepalive so a quiet session isn't dropped
        "global_delay_factor": 2,  # pace sends slower for a fragile CLI
        "fast_cli": False,         # disable aggressive timing
        # If the SMOKE TEST shows a key-exchange/cipher handshake failure, add
        # legacy algorithms here, e.g.:
        #   "disabled_algorithms": {"pubkeys": [...], "kex": [...]},
        # and record in the docstring which ones the unit required.
    }

    # Fragile link + a unit that may reject a new session while the prior one is
    # still tearing down: retry more, and wait longer between attempts.
    connect_attempts = 6
    connect_backoff = 4.0

    # ── Other override points (inherited from RadCliDriver) ────────────────
    # Extend via `RadCliDriver.<knob> + (...)`, don't restate defaults:
    #   netmiko_device_type   = "rad_etx"   # revisit if MiNID is not context-CLI
    #   show_whitelist        = RadCliDriver.show_whitelist + (...)
    #   health_sequence       = (...)
    #   config_export_command = "info"
    #   save_command          = "save"
