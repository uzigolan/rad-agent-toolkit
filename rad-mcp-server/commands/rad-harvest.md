---
description: Re-harvest a RAD device's CLI `?`-help into the skill reference (after a firmware upgrade, or when the reference is missing a context). Also use when addressed via "abayev" / "noam" / "rad agent" — e.g. "rad agent, re-harvest lab-sf1p", "noam, refresh the etx1p CLI reference"
argument-hint: <device-name> [subtree, e.g. configure crypto]
---

Re-harvest CLI knowledge for: $ARGUMENTS

Parse the arguments: first token is the device name (if omitted, `list_devices`
and ask); anything after it is a subtree path for a partial refresh.

1. **Launch in the background** — a full run is ~8 min, a branch ~2–3 min;
   never block the chat on it and never poll (the completion notification
   re-invokes you):

   ```
   rad-mcp-server\server\.venv\Scripts\python.exe rad-mcp-server\scripts\harvest_cli.py harvest <device> [--branch "<subtree>"]
   ```

   Tell the user it is running and what it will refresh, then yield.

2. **When it completes, review the report** (tail of the task output):
   - **Diff**: report ADDED / REMOVED / CHANGED counts to the user.
     `REMOVED > 0` without a firmware downgrade is a red flag — a context
     whose entry failed silently drops its entire subtree; investigate
     (`git diff` the reference for lost `##` sections) before accepting.
   - **Temp objects**: every "entered via TEMP object" line must have a
     matching clean rollback line. Any rollback that errored → escalate to
     the user immediately with the transcript.
   - Spot-check a couple of CHANGED entries in the jsonl: clean help text =
     fine; prompt fragments or truncation = capture noise, re-run the branch.

3. **Verify the device is clean**: `get_config` on the device and search the
   export for `zzz-hrvst` — must be zero hits. Then check every numeric temp
   object this run's "entered via TEMP object" list reported (e.g. `lag 4`,
   `pw 63`, `mep 9999`) — each one must also be absent from the export. This
   is belt-and-suspenders on top of the rollback log.

4. **Sync the skill copies**: copy
   `rad-mcp-server/skills/rad-cli-operations/references/*` to
   `~/.claude/skills/rad-cli-operations/references/`. Remind the user that
   Claude Desktop needs the skill zip rebuilt (`scripts/build_desktop_skills.py`)
   and re-uploaded — that cannot be done from here.

5. **Offer to commit** the refreshed references (one commit; git history is
   the CLI-evolution record across firmware versions).

Safety notes: the harvester is read-only except for short-lived temp objects
it creates to enter parameterized contexts and rolls back immediately —
string-named ones use a fixed `zzz-hrvst` placeholder, numeric-indexed ones
(`mep`, `lag`, `pw`, `test` only — an explicit allow-list, checked against
the manual before each addition) try up to 6 free indices ascending from the
bottom of the declared range, skipping any already in use. Ascending, not a
single guess from the top: the CLI's own declared range isn't reliable on
real hardware (etx2i's `lag` advertises `[1..4]` but rejects 4 with "Invalid
LAG ID"; `test` under rfc2544 declares no range at all but only accepts
1-8) — real license/hardware limits are often lower than the generic syntax
range. `twamp` is deliberately excluded from the allow-list, and on etx2i
that turned out to matter for two different reasons once the harvester's
refusal-text capture was extended to string-named creates too (not just
numeric): `controller`/`profile` are refused with a device-confirmed
`cli error: License required` — a real license gate, not a code/safety gap
any allow-list change could close — while `responder` is refused for an
unrelated reason (`parameter or keyword missing or wrong`, wants
`[<number>] light [l2-probe]`), the same class of "needs a second argument"
gap as `pw`. If every tried index/string is refused, the harvester captures
the device's own refusal text for each attempt — plus, for numeric attempts,
one read-only `<name> <idx> ?` follow-up probe — and logs all of it into
that context's "not entered" reference entry, so a gap always comes with
its own device-confirmed reason attached, not a guess. The harvester never
enters `admin`/`file` danger contexts and never sends
`clear-*`/`delete`/`reboot` tokens with Enter. Safe to re-run at any time.
