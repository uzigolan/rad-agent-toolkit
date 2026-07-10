# Verified command map — full table

Every row is **firmware-verified** (live on a lab unit, or confirmed against
the harvested `?`-help reference with its captured prompt). This file is the
grow-as-you-go layer: SKILL.md carries only the core rows; everything else
lives here so the skill stays small while the map keeps growing.

**Commands are family-specific.** The three families share the dialect, but
not every command exists everywhere — ALWAYS match the `Families` column
against the target device's inventory `family` before answering. `all` =
confirmed in the harvested references of secflow, etx1p, AND etx2
(cross-checked 2026-07-10). Port naming still differs per family even for
`all` rows: secflow ports are numeric (`ethernet 3`), etx1p ports are named
(`ethernet lan1`).

**Curation rules:**
- Never add a row from memory or vendor docs alone — verify against
  `cli-reference-<family>.md` (context header + command present) or live
  `cli_help` first.
- Fill the `Families` column with what you actually checked — never write
  `all` without confirming in all three references.
- Commit additions — this file ships with the skill, so a promoted command
  saves lookups for every user, not just this machine.

| Purpose | Context | Command | Families |
|---|---|---|---|
| Device identity (model, SW, MAC, uptime) | `configure system` | `show device-information` | all |
| CPU / RAM / disk metrics | `configure system` | `show resources` | secflow, etx1p — **NOT etx2** |
| System info / date | `configure system` | `show system`, `show system-date` | all |
| Hardware+software inventory | `configure system` | `show summary-inventory` | all |
| Full diagnostic dump (slow) | `configure system` | `show tech-support` | all |
| Active alarms | `configure reporting` | `show active-alarms` | all |
| Active alarms with timestamps + descriptions | `configure reporting` | `show active-alarms-details` | all |
| Alarm / event log | `configure reporting` | `show alarm-log`, `show log`, `show log-summary` | all |
| Port config (admin state, VLANs) | `configure port ethernet <n>` | `info` | all (global cmd) |
| All-ports status summary | `configure port` | `show summary` | all |
| Single port status (link, speed) | `configure port ethernet <n>` | `show status` | all |
| Port traffic statistics | `configure port ethernet <n>` | `show statistics` | all |
| Router interfaces (admin/oper state, IPs, bindings) | `configure router <n>` | `show summary-interface` | all |
| Routing/neighbor tables | `configure router <n>` | `show routing-table`†, `show arp-table`, `show rib` | all |
| Startup config | `file` | `show startup-config` | all |
| Rollback config | `file` | `show rollback-config` | all |
| Software status | `admin software` | `show status` | all |
| Full running config | root | `info` | all (global cmd) |
| Command discovery | any context | `tree` (levels below here), `help` | all (global cmd) |
| Persist config | any context | `save` | all (global cmd) |

† syntax accepted; returned empty on the lab unit (no dynamic routes) —
output format unverified.
