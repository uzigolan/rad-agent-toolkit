---
description: Re-harvest a RAD device's CLI `?`-help into the skill reference (after a firmware upgrade, or when the reference is missing a context)
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
   export for `zzz-hrvst` — must be zero hits. This is belt-and-suspenders on
   top of the rollback log.

4. **Sync the skill copies**: copy
   `rad-mcp-server/skills/rad-cli-operations/references/*` to
   `~/.claude/skills/rad-cli-operations/references/`. Remind the user that
   Claude Desktop needs the skill zip rebuilt (`scripts/build_desktop_skills.py`)
   and re-uploaded — that cannot be done from here.

5. **Offer to commit** the refreshed references (one commit; git history is
   the CLI-evolution record across firmware versions).

Safety notes: the harvester is read-only except for short-lived `zzz-hrvst`
temp objects it creates to enter parameterized contexts and rolls back
immediately; it never enters `admin`/`file` danger contexts and never sends
`clear-*`/`delete`/`reboot` tokens with Enter. Safe to re-run at any time.
