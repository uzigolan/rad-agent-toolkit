"""MCP prompts (plan 06) — curated workflows on the portable MCP primitive.

The Claude Code slash commands in `commands/*.md` only exist on Claude Code.
MCP `prompts` are the portable equivalent: server-defined, parameterised,
discoverable by any compliant client (Claude Desktop, VS Code Copilot, Codex).

Single definition, zero drift: the three prompts that mirror slash commands
(`rad_health`, `rad_backup`, `rad_harvest`) load their bodies from the
canonical `commands/<name>.md` files at invocation time — the slash command
and the MCP prompt can never disagree. The other three (`rad_snmp_survey`,
`rad_family_compare`, `rad_onboard_device`) are new, defined here.

A prompt body is instructions to the model, not a script: it states the
method (which layer to consult in what order, when to verify live, when to
stage) and lets the model adapt. Bodies stay well under ~1,500 tokens;
knowledge is referenced via `rad://` resources and tools, never inlined.

Decomposition note (docs/plan/DECOMPOSITION.md): prompts ship with the server
that owns the work — `rad_family_compare` → rad-knowledge; `rad_health`,
`rad_backup`, `rad_snmp_survey` → rad-device; `rad_onboard_device` →
rad-inventory; `rad_harvest` → rad-forge (ingestion, plan 08). Until the
split, all six live here, tagged with their future home.
"""
from __future__ import annotations

from .runtime import REPO_ROOT

COMMANDS_DIR = REPO_ROOT / "commands"


def _command_body(name: str, arguments: str) -> str:
    """Load `commands/<name>.md`, strip YAML frontmatter, fill $ARGUMENTS.

    Read at invocation time (not import) so an edited command file is picked
    up without a server restart — same behaviour Claude Code gives the slash
    command itself.
    """
    text = (COMMANDS_DIR / f"{name}.md").read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:].lstrip("\n")
    return text.replace("$ARGUMENTS", arguments)


def register_prompts(mcp) -> None:
    """Register the six workflow prompts. Additive and read-only in itself —
    a prompt returns instructions; any writes the model then performs still go
    through the staged stage_config -> commit_config flow."""

    @mcp.prompt(name="rad_health",
                description="Health-check one RAD device or a whole group and "
                            "summarize alarms/reachability as a table. "
                            "Read-only.",
                tags={"rad-device"})
    def rad_health(device: str = "", group: str = "") -> str:
        """Run a health sweep on a device or group.

        Args:
            device: device name from list_devices (leave empty when using group)
            group: group name — health-checks every device in it
        """
        target = device or group or "(none given — list devices and ask the user which)"
        return _command_body("rad-health", target)

    @mcp.prompt(name="rad_backup",
                description="Back up the running configuration of one RAD "
                            "device or a group to the local backup archive.",
                tags={"rad-device"})
    def rad_backup(device: str = "", group: str = "") -> str:
        """Back up configurations for a device or group.

        Args:
            device: device name from list_devices (leave empty when using group)
            group: group name — backs up every device in it
        """
        target = device or group or "(none given — list devices and ask the user which)"
        return _command_body("rad-backup", target)

    @mcp.prompt(name="rad_harvest",
                description="Re-harvest a RAD device's CLI ?-help into the "
                            "skill reference (after a firmware upgrade, or "
                            "when the reference misses a context). Creates "
                            "and rolls back short-lived temp objects on live "
                            "hardware — the body restates the mandatory "
                            "cleanup verification. Requires an explicit "
                            "device.",
                tags={"rad-forge"})
    def rad_harvest(device: str, family: str = "", version: str = "",
                    subtree: str = "") -> str:
        """Re-harvest CLI knowledge from a live device.

        Args:
            device: device name from list_devices — REQUIRED; harvesting
                touches live hardware and must never run against a guess
            family: driver family (informational; the harvester derives it
                from the inventory — state it to catch a mismatch early)
            version: firmware version being harvested (recorded in the
                commit message so git history maps reference ↔ firmware)
            subtree: optional context path (e.g. "configure crypto") for a
                partial refresh instead of the full ~8-minute run
        """
        if not device.strip():
            raise ValueError(
                "rad_harvest requires an explicit device argument — "
                "harvesting creates temp objects on live hardware and must "
                "never target a guessed device.")
        args = device if not subtree else f"{device} {subtree}"
        body = _command_body("rad-harvest", args)
        notes = []
        if family:
            notes.append(f"The user states the device family is `{family}` — "
                         "verify it matches the inventory entry before starting.")
        if version:
            notes.append(f"Firmware version being harvested: `{version}` — "
                         "include it in the reference commit message.")
        if notes:
            body += "\n\n" + "\n".join(notes)
        return body

    @mcp.prompt(name="rad_snmp_survey",
                description="Survey a RAD device over SNMP: probe "
                            "credentials/engine, identify it, walk the key "
                            "tables, and propose a monitoring poll plan. "
                            "Read-only.",
                tags={"rad-device"})
    def rad_snmp_survey(device: str) -> str:
        """SNMP-survey one device.

        Args:
            device: device name from list_devices
        """
        return f"""Run a read-only SNMP survey of: {device}

1. `snmp_probe` first — it discovers which credentials/version work and
   returns identity basics. If SNMP is unreachable, stop and report why
   (agent off? community not set? use `cli_search` for the family's SNMP
   enable syntax and suggest it — do not change configuration).
2. Identify: sysDescr, sysObjectID, sysUpTime, sysLocation/sysContact.
   Use `mib_describe`/`mib_search` to translate sysObjectID and any
   family-specific OIDs into names — never guess OID meanings.
3. Walk the interface table (`snmp_walk` on ifTable / ifXTable) and report:
   port name, admin/oper status, speed, and any error counters that are
   non-zero. Respect the walk row cap; note if the table was truncated.
4. `snmp_build_poll_plan` for the device and present the suggested
   monitoring plan (OIDs, poll intervals) as a table.
5. Summarize: device identity, SNMP version in use, interface health,
   and the recommended poll plan. Read-only throughout — no snmp set,
   no configuration changes."""

    @mcp.prompt(name="rad_family_compare",
                description="Compare two RAD device families on a topic "
                            "(feature, CLI syntax, limits) strictly from the "
                            "harvested knowledge corpus — never from model "
                            "memory.",
                tags={"rad-knowledge"})
    def rad_family_compare(family_a: str, family_b: str, topic: str) -> str:
        """Compare two families on one topic.

        Args:
            family_a: first driver family (e.g. etx2)
            family_b: second driver family (e.g. mp4100)
            topic: what to compare (e.g. "QoS", "1588 sync", "VLAN tagging")
        """
        return f"""Compare `{family_a}` vs `{family_b}` on: {topic}

Ground every claim in the knowledge corpus — never answer from memory:

1. `cli_search(topic, family=...)` for BOTH families — the harvested command
   trees are the source of truth for what each CLI actually offers.
2. `manual_search(topic, family=...)` for both — limits, defaults, and
   procedures the bare syntax doesn't show.
3. `datasheet_search(topic)` where hardware capability matters (port counts,
   throughput, environmental limits).
4. Produce a side-by-side table: capability / syntax / limits per family,
   with a short "practical difference" note per row.
5. Where one family has no corpus coverage for the topic, say exactly that
   ("no harvested commands / manual sections match") — absence of evidence
   is the finding; do not fill gaps from memory. If a claim needs live
   confirmation, say which `run_show` would verify it rather than running it."""

    @mcp.prompt(name="rad_onboard_device",
                description="Register an additional RAD device of an "
                            "already-supported family into the inventory and "
                            "verify it end-to-end. (A brand-new FAMILY needs "
                            "the full /rad-onboard-family pipeline instead.)",
                tags={"rad-inventory"})
    def rad_onboard_device(host: str, family: str) -> str:
        """Onboard one more device of a known family.

        Args:
            host: management IP or hostname of the new unit
            family: driver family (etx2, etx1p, secflow, mp4100, mp1, minid, etx2v)
        """
        return f"""Onboard a new device: host `{host}`, family `{family}`

1. Confirm `{family}` is a supported driver family (`list_versions` or
   `rad://status`). If it is NOT, STOP — a new family needs the full
   /rad-onboard-family pipeline (live unit + user manual + CLI harvest),
   not this prompt.
2. Gather the remaining facts from the user before touching anything:
   device name and group (host and family are given). Check `list_devices`
   for a name or host collision first.
3. `add_device` with the facts. Credentials are NOT set through the
   conversation: tell the user to run the `rad-mcp-set-credentials` CLI on
   the server host, and wait for their confirmation.
4. Verify: `test_connectivity`, then `health_check`. Confirm the detected
   prompt/dialect looks right for `{family}`; surface any active alarms.
5. Take a first `backup_config` so the archive has a day-zero baseline.
6. Report: inventory entry, connectivity result, alarm summary, backup path.
   If any step fails, report the exact error and stop — do not retry with
   guessed credentials or a different family."""
