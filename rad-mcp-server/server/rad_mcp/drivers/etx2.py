"""ETX-2 family driver (ETX-203AX / ETX-205A / ETX-220A / ETX-2I class
carrier-Ethernet demarcation devices).

VERIFIED live (2026-07, ETX-2I Hw 0.2/D, Sw 6.8.5(1.116)): context-based CLI,
`tree`, `show device-information`, `show active-alarms` all work as on
SecFlow/ETX-1p. Confirmed dialect differences vs. the other families:
  - `show resources` is NOT recognized here (works on SecFlow/ETX-1p) — don't
    rely on it for health checks on this family.
  - Ports are slot/port-numbered ("Ethernet 0/2"), a third convention besides
    SecFlow's flat numbers ("Ethernet 3") and ETX-1p's named ports ("lan1").
  - `configure test` (Y.1564, RFC2544, L3SAT SLA test suites) is a real,
    harvested top-level context that does NOT exist on SecFlow/ETX-1p (0 hits
    in either family's harvest) — ETX-2-only, carrier-Ethernet demarcation
    feature. Found 2026-07-09: cli_help/run_show_in_context refused it
    ("unknown configure context 'test'") because it was missing from this
    allowlist even though the harvester had already proven it real.
Full CLI reference + manual layer harvested for this family
(cli-reference-etx2.md, manual-etx2/).
"""
from __future__ import annotations

from .radcli import RadCliDriver


class Etx2Driver(RadCliDriver):
    family = "etx2"

    # ETX-2 adds carrier-Ethernet contexts; superset kept permissive until a
    # live ETX-2 `tree` capture grounds this list.
    configure_contexts = RadCliDriver.configure_contexts + ("flows", "spanning-tree", "test")
