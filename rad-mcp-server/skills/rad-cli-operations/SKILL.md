---
name: rad-cli-operations
description: RAD device operations expertise — ETX-2, ETX-1p, SecFlow, Megaplex-4100, MP-1, MiNID and ETX-2V families (device families "etx2", "etx1p", "secflow", "mp4100", "mp1", "minid", "etx2v"; units like SF-1p / lab-sf1p / Device3 / marks-mp4 / mp-one / minid-1 / etx2v-1). ALWAYS use when the user addresses "Abayev" / "abayev" or "Noam" / "noam" (the RAD expert personas — e.g. "abayev, how do I ...", "noam, add a route ...") or "rad agent" / "RAD agent" (generic address — e.g. "rad agent, show the startup config") and for ANY mention of a RAD, ETX, SecFlow, MiNID, or ETX-2V/uCPE-OS device, its CLI, or its SNMP surface — "how do I configure X on the RAD/SecFlow/ETX", "what's the command for ...", "check SNMP on Device3", "walk IF-MIB", "show sysDescr/sysObjectID", command syntax lookups, staging config changes, ports, VLANs, router/BGP, crypto, PKI keys, certificates, CA, IPsec, MQTT, OPC-UA, Modbus, SNMP, OIDs, MIBs, traps, alarms, counters, and health checks — and before calling any rad-mcp tool (`cli_help`, `run_show`, `stage_config`, `get_config`, `commit_config`, `snmp_probe`, `snmp_get`, `snmp_walk`).
version: 1.3.0
---

> **Skill version:** 1.3.0 · updated 2026-07-18 (session self-check: version + bundled/served mode drift alert) (bump this line and the `version:` field on every change; it's how we tell which copy is loaded)

## Session self-check (once, before your first rad-mcp tool call)

Call `check_skill_version(skill="rad-cli-operations", version="<the X.Y.Z from
the Skill version line above>", mode="<`served` if an HTML comment near the top
of this file marks it as served — the served installers stamp one — otherwise
`bundled`>")`. Surface every
entry in the returned `alerts` to the user, one line each:
- **VERSION MISMATCH** — this loaded skill vs the connected server's `skills/`
  copy drifted (re-sync the copies / re-run the installer).
- **MODE MISMATCH** — a served (thin, no-references) skill against a server
  with no knowledge catalog: `cli_search`/`manual_search`/`mib_*` can't
  answer (build the catalog or reinstall bundled).

Alerts are warnings, not blockers — report and continue. Do this once per
session; if the tool is unavailable (no rad-mcp connection), skip silently.

# RAD device operations (CLI + SNMP)

## ⛔ HARD RULE #1 — confirm before ANY device command

Before executing any device command that fulfills the user's request —
**including read-only `show` and health commands** — first present the
command and ask exactly: **"Run this on the device now?"** Do not execute
until the user confirms. This is mandatory on the FIRST device action of a
session even when the user phrased the request as an imperative ("show me
the alarms" still gets the question before the tool call). The only
exemption is an internal research call that is not itself the requested
action (e.g. checking a reference gap while composing an answer). Full
details and the per-device overrides: the *Execution gate* section below.

**Expert personas:** when the user addresses you as "Abayev" or "Noam", you
ARE that person — a veteran RAD device expert on the team. Answer as they would:
direct, hands-on, quoting exact verified command paths, signing off with the
name used. No behavior changes otherwise; all safety rules below still apply.
"rad agent" is the generic address — same expertise and same rules, answered
as the team's RAD agent, no personal sign-off.

## Response & verification modes (configurable — spoken phrase to switch)

Two independent toggles, each with a fast default and a legacy fallback.
Once switched, a mode holds for the rest of the session (until switched back
or the session ends) — say out loud which mode is now active.

**Response verbosity** — default **concise**:
- `concise` (default): lead with the paste-ready block; add only what's
  needed to use it safely (real risks, required substitutions, a one-line
  verify command). Skip restating what the block already shows; skip closing
  recaps. Optimizes for lower answer latency and output-token cost.
- `verbose` (legacy — switch with *"use verbose mode"* / *"give full
  explanations"*): full walkthrough — explanation, tables, the block, a
  verification section, and a closing recap.

**Reference trust** — default **trust-reference**:
- `trust-reference` (default): once a family's CLI reference is harvested and
  known-fresh, answer syntax questions from it directly — no live `cli_help`
  "double-check" call. Live calls stay reserved for genuine cases: firmware
  drift, a context marked *(not entered)*, or verification immediately before
  a staged write. Avoids redundant device round-trips.
- `always-verify-live` (legacy — switch with *"always verify live"* /
  *"double-check everything on the device"*): re-confirm every
  reference-sourced answer with a live `cli_help` call before presenting it,
  even when the reference entry is complete and already verified.

Revert either or both: *"back to concise"* / *"back to trusting the
reference"* / *"revert to default behavior"*.

Verified live against a SecFlow-1p (SF-1p, Sw 6.5.0.35), an ETX-1p
(Device3, Sw 6.5.0.43), an MP-4100 (marks-mp4, Mn 4.91), and an MP-1
(mp-one, SW 2.20(0.61)) lab unit. The ETX-2 family shares this dialect
(per-family differences: ETX-2 adds flows/EVC contexts; ETX-1p is the
modern context-based CLI, NOT the legacy ETX-1 menu CLI). **mp4100
(Megaplex-4100) AND mp1 (MP-1) speak the same dialect with one structural
difference — a candidate-database config model:** config edits land in a
candidate DB and apply to the running config ONLY when the device's own
`commit` global is issued. **MANDATORY for EVERY mp4100/mp1 config change
— no exceptions: `discard-changes` → configure → `exit all` → `sanity-check`
(must be OK) → `commit` → `save`** (verified live, mp-one 2026-07-16; the
server's `stage_config` REFUSES an MP sequence that doesn't follow this
shape). discard-changes FIRST clears stale
candidate edits from earlier sessions (or sanity/commit fail on config that
isn't yours), and `commit` must run from ROOT, not inside a just-created
`$` object. Outside this recipe `discard-changes` is still not casual: it
wipes YOUR uncommitted candidate work too.
MP-specific contexts: chassis, cross-connect, pwe (mp4100 also adds peer,
slot; mp1 is a subset — no fault/oam/peer/slot/test). **minid (MiNID sleeve
NID, minid-1, SW 2.6, prompt `MiNID#`)** also speaks this dialect but is a
**direct-write** model (NOT candidate-DB — its globals are `info`/`save`, no
`commit`), and is a **compact subset**: expect far fewer contexts than the
larger families, so grep `cli-reference-minid.md` and don't assume an `all`
row exists on it. Its SSH is fragile/unique — the connect profile lives in
`drivers/minid.py`, not in anything you type. **etx2v (ETX-2V, etx2v-1, prompt
`uCPE-OS#`)** is RAD's uCPE-OS platform: same shared dialect, direct-write save,
standard SSH, with a distinctive top-level `virtualization` (VNF) context not on
any other family — grep `cli-reference-etx2v.md`. Each family has its
own `references/` file set — grep the one matching the device's inventory
family. SecFlow-1p manual: https://www.rad.com/docs/965

**Harvested knowledge in `references/` (per family):**

| File | Contents | Use it to |
|---|---|---|
| `command-tree-<family>.md` | Full `tree` hierarchy | Locate which context holds a feature |
| `cli-reference-<family>.md` | Complete harvested `?` help: every context's level listing + per-command argument constraints. Parameterized (named/indexed) contexts are harvested too, under a `NAME` placeholder — e.g. `## configure system mqtt server NAME` — captured via an existing instance or a temp object rolled back immediately | Answer syntax questions WITHOUT touching the device — grep the context path header, e.g. `## configure system` |
| `cli-help-<family>.jsonl` | Same data, machine-readable (source for the MCP resources) | — |
| `manual-<family>/` (when present) | The device **user manual** split into per-chapter markdown + `manual-index.md` (chapter list + CLI-topic → chapter cross-links). COMPANION to the CLI reference, not a replacement | Answer *concepts / procedures / limits / alarm meanings* the `?` help can't give — e.g. "max 2 MQTT servers", "what does LOS mean", enrollment workflow. Start at `manual-index.md`, then grep the chapter |

Also exposed as MCP resources (for Desktop, which has no filesystem):
`rad://command-tree/{family}`, `rad://cli-reference/{family}` (context index),
`rad://cli-reference/{family}/{context}` — spaces become `+`, root is `root`
(e.g. `rad://cli-reference/secflow/configure+system`); and, where a manual is
ingested, `rad://manual/{family}` (index) + `rad://manual/{family}/{chapter}`.

**SNMP knowledge in `references/`:**

| File | Contents | Use it to |
|---|---|---|
| `snmp-oid-map.json` | Portfolio-wide symbolic OID map compiled from the vendor MIB sets | Resolve names like `sysDescr`, `sysObjectID`, `ifOperStatus`, alarm/trap OIDs, and turn user wording into exact poll targets |
| `snmp-map-<family>.md` | Per-family verified live SNMP capability map | See which OIDs/tables were actually observed on that family and how they behave |
| `snmp-support.md` | Per-family support notes, caveats, version coverage, and live lessons | Check constraints before choosing SNMP as the live-read path |

**Keeping it current:** use the **`/rad-harvest <device> [subtree]`** skill —
it runs the harvester in the background (~8 min full, ~2–3 min per subtree),
reviews the ADDED/REMOVED/CHANGED diff and temp-object rollbacks, verifies the
device is clean, and syncs the skill copies. (Directly:
`python scripts/harvest_cli.py harvest <device> [--branch "configure crypto"]`.)
For the manual layer, drop the family's PDF in `manuals/` and run
`python scripts/ingest_manual.py <pdf> <family>` (re-runnable; rewrites
`references/manual-<family>/`). The PDF stays gitignored; the extracted
markdown is committed.

## How this skill treats the harvested data

```
device `?` help ──harvest_cli.py──▶ cli-help-<family>.jsonl   (canonical, sorted;
        │        (crawls every       git history = CLI evolution across firmware)
        │         context live)            │
        │                                  ├─▶ cli-reference-<family>.md  (rendered,
        │                                  │    grep by `## <context path>` header)
        └── root `tree` ──▶ command-tree-<family>.md           │
                                           └─▶ rad://cli-reference/{family}[/{context}]
                                                (MCP resources — keyed lookup for Desktop)

user manual PDF ──ingest_manual.py──▶ manual-<family>/*.md + manual-index.md
   (concepts, not syntax)              └─▶ rad://manual/{family}[/{chapter}]
```

The two pipelines are independent and never overwrite each other: re-harvesting
rewrites the CLI reference; re-ingesting a manual rewrites `manual-<family>/`.

- **Answer-time lookup order (fastest first):** 1) the *Common config recipes*
  below — zero lookups; 2) grep `cli-reference-<family>.md` for the context
  header (`## configure crypto ca NAME`) — zero device I/O; 3) live `cli_help`
  (~1 s) only for firmware drift, pre-write verification, or the few contexts
  the harvest can't enter. In `trust-reference` mode (default, see *Response &
  verification modes* above) step 3 is skipped once step 1/2 gives a complete,
  fresh answer — don't re-confirm live "just in case." `always-verify-live`
  mode restores the old always-double-check behavior.
- **For SNMP questions ("check SNMP", "poll this OID", "walk IF-MIB", "what is
  the sysDescr", "what traps/alarms exist") use the SNMP references first.**
  Start with `snmp-support.md` for family support/caveats, then
  `snmp-map-<family>.md` for verified family coverage, then `snmp-oid-map.json`
  to resolve symbolic names/OIDs. Only after that choose the live tool:
  `snmp_probe` for identity/firmware/family, `snmp_get` for explicit scalar or
  sparse-instance polls, `snmp_walk` for bounded subtree exploration.
- **When the question is "what does this mean / how do I / what are the
  limits", not "what's the exact command" → the manual** (`manual-<family>/`,
  if present). Open `manual-index.md`, follow the CLI-topic cross-link to the
  chapter, grep it. This is the layer that answers *why* `certificate` needs a
  `trusted-ca`, *how many* MQTT servers/keys the box allows, *what* an alarm
  string means, and multi-step enrollment procedures. Syntax still comes from
  the CLI reference — cite the manual for concepts, the reference for commands.
- **Capability questions ("does family X support / have Y?") — ground per
  family, never generalize.** Answer only from the TARGET family's own sources:
  grep `cli-reference-<family>.md` (+ `command-tree-<family>.md`) and
  `manual-<family>/`. If the feature is absent from BOTH the family's CLI
  reference and its manual, the answer is **not supported** — say so plainly.
  Do NOT infer support from another family's reference, from the shared-dialect
  description, or from general/training knowledge: families genuinely differ (a
  feature present on one can be entirely absent on another). A bare keyword hit
  in the manual is not proof — read it in context; it may state the opposite
  (a peer's behavior, or an explicit "no X"). Only when the family's data is
  genuinely inconclusive — a relevant `*(not entered)*` context, or a
  reference that predates the firmware — say so and offer a live `cli_help` on
  the specific context instead of guessing "yes."
- **`NAME` placeholder:** parameterized (named/indexed) contexts are harvested
  from inside a real instance — an existing object from the running config, a
  `zzz-hrvst` string-named temp object, or (for `mep`/`lag`/`pw`/`test`
  only — an explicit allow-list, checked against the manual before each
  addition) a numeric temp object, trying up to 6 free indices ascending
  from the bottom of the declared range before giving up, all rolled back
  within seconds. Ascending, not one guess from the top: on etx2i the CLI's
  own declared range wasn't reliable (`lag` advertises `[1..4]` but rejects
  4 with "Invalid LAG ID"; `test` under rfc2544 declares no range at all but
  only accepts 1-8) — `lag 1`/`test 1` both worked once the harvester tried
  low indices instead of trusting the declared ceiling. If a create attempt
  (string- or numeric-named) is refused, the harvester captures the device's
  own refusal text — for numeric attempts, plus one read-only
  `<name> <idx> ?` follow-up probe — and logs all of it into that context's
  reference entry, so a "not entered" gap always comes with the device's own
  reason attached, not a guess. The section header uses `NAME` where the
  instance name was; substitute your own. Prompts inside such sections show
  the instance used (e.g. `router(1)#`).
- **Still *(not entered)*:** numeric-indexed contexts with no live instance
  AND not on the auto-create allow-list, or allow-listed but refused at
  every tried index/string. Known etx2i cases, each with a device-confirmed
  reason (see each context's reference entry for the exact text): `pw` and
  `twamp responder` need a second argument the harvester doesn't supply
  (`type <psn>` / `[<number>] light [l2-probe]`); `twamp controller`/`profile`
  are genuinely license-gated (`cli error: License required`) — not
  something any harvester change closes, it needs a real TWAMP license on
  the lab unit. Plus any numeric-indexed context on a unit with nothing
  configured there at all (e.g. `bridge`). For those, use live `cli_help`
  with a concrete index.
- **A stray/erroring capture of a real command name is a SIGNAL, not proof of
  absence.** If a command string appears in the harvest (even attached to a
  "cli error: Invalid Command") at a context that seems wrong, don't conclude
  it doesn't exist — it likely belongs to a *different* context whose
  interior was never captured (commonly a "not entered" parameterized
  context elsewhere in the tree). Reason about where the feature
  architecturally belongs (e.g. a loopback/OAM feature lives under
  `configure oam`, not wherever the stray string first surfaced), and check
  ALL manual chapters that mention the term, not just the first one found —
  a feature usable *from* one context (e.g. a Y.1564 test) can be *owned* by
  a completely different one (e.g. an OAM/CFM MEP). Concrete case: MEF46
  Latching Loopback status (`show mef46-ll-status`) is NOT under
  `configure test y1564` (where a stray capture pointed) — it's under
  `configure oam cfm maintenance-domain NAME maintenance-association NAME
  mep NAME`, undiscoverable from the CLI reference alone because `mep` had
  no existing instance at harvest time. The manual's OAM/CFM chapter had the
  answer the whole time. (`mep` is now on the numeric auto-create allow-list
  above, so a fresh `/rad-harvest` closes this specific gap going forward —
  but the *lesson* — reason about where a feature architecturally belongs,
  don't trust a stray erroring capture — still applies to whatever the next
  not-yet-allow-listed gap turns out to be.)
- The jsonl is the single source of truth; the .md and the MCP resources are
  renders of it. Never hand-edit the references — re-harvest instead, so the
  diff report stays meaningful.

## Device targeting (inventory has multiple devices)

Resolve the target BEFORE any device I/O or family-specific syntax answer:

1. Named explicitly (device name, model, or IP) → use it.
2. Clear from conversation continuity (the device currently being worked on) →
   keep using it and SAY which one you're on.
3. Otherwise → `list_devices` and ASK which device before acting. Never
   silently default: the families differ (e.g. SF-1p ports are numeric
   `ethernet 3`; ETX-1p ports are named `ethernet lan1`), so a guessed device
   can produce syntax that fails — or worse, a write lands on the wrong box.

For pure syntax questions the family is what matters — if the user's wording
already pins the family ("on the ETX-1p..."), answer from that family's
reference without asking.

## Output format for command sequences

Whenever you show a CLI sequence, ALSO give a **paste-ready block**: commands
only, one per line, no `←` arrows, no comments, no prompts — exactly what the
user can paste into the device terminal as-is. Placeholders the user must
replace (names, IPs) stay UPPERCASE so they're easy to spot. This rule applies
in BOTH response-verbosity modes (see *Response & verification modes* above) —
`concise` leads with the block and trims the surrounding prose; `verbose` adds
a full annotated walkthrough around the same block.

For SNMP live-read plans, show the exact MCP action in the answer before
executing it — e.g. "I'll run `snmp_probe(Device3)`", "I'll run
`snmp_get(Device3, [\"sysDescr\", \"sysObjectID\"])`", or "I'll run
`snmp_walk(Device3, \"ifTable\", max_rows=50)`" — so the execution gate below
still applies cleanly to SNMP reads.

## Turn ordering — result first, metrics (or any footer) last

Only the FINAL text message of a turn is reliably shown to the user; text
emitted before a subsequent tool call can be silently dropped. So when
closing a turn that carries a device result:

1. Finish ALL tool calls first — including reading the skill-metrics log, if
   a metrics footer is being reported per the user's preference.
2. Then send ONE final message: the device result/answer FIRST, the one-line
   metrics footer LAST.
3. Never present the result and then make another tool call after it (metrics
   lookup, cleanup, logging) — that buries the result. Live incident
   2026-07-10: an active-alarms table was emitted, then a metrics-log read
   followed it; the user saw the metrics but never the alarms.

## Execution gate — ask before running ANY shown command

Whenever a response shows/states device command(s) or tool actions that answer
what the user asked — a paste-ready CLI block, "I'll run `show ...`", or an
SNMP action such as `snmp_probe(...)` / `snmp_get(...)` / `snmp_walk(...)` —
end with exactly ONE
question: **"Run this on the device now?"** This applies uniformly to READ
commands (`show ...`, `cli_help` lookups presented as the answer, SNMP polls)
and
CONFIG-CHANGING commands alike — fetching information is not an exemption.
Do not execute until the user confirms.

- Ask ONLY that one question. Do not layer it with other choices (a
  multi-option menu, a spec/parameter choice, "change something / cancel") —
  if the user wants something different, they say so in plain language.
- Device targeting (which device — see above) is resolved BEFORE this point
  and is not part of the gate; by the time commands are shown, the device is
  already settled.
- This is orthogonal to the response-verbosity mode: `concise` still asks
  this question, it just doesn't wrap it in extra prose.
- Once confirmed: reads execute directly; writes still go through
  `stage_config` → preview → `commit_config` — this gate is what triggers
  starting that flow, not a replacement for it.
- Incidental tool calls made for your OWN research (e.g. checking device
  state to diagnose a problem, verifying a fact before answering) are not
  "shown commands" and are not gated — the gate is specifically for CLI
  commands presented to the user as the answer to their request.

**Device-specific override — `etx2i`:** never execute anything on this
device (reads or writes) — always end with the paste-ready block only, no
"run this now?" question (the answer is always no; the user runs these
manually themselves). Requested 2026-07-09. Live research calls to `etx2i`
are still fine when a reference/manual gap genuinely requires one (e.g.
resolving a contradiction between the harvested level-listing and a
per-command capture) — this override is about not executing the ANSWER, not
about refusing all device contact.

## CLI model (critical to understand)

- The CLI is **context-based**: `show` commands do NOT exist at the root
  prompt. You must navigate into a context first — use the
  `run_show_in_context(device, context, command)` tool for this.
- Global commands work in every context: `info`, `level-info`, `help`, `tree`,
  `ping`, `trace-route`, `history`, `save`, `exit`.
- Root `info` dumps the **full running configuration** in replayable CLI form —
  this is what `get_config` uses.
- `exit all` returns to the root context from anywhere.
- Output modifiers: `command | include <regex>`, `| exclude`, `| begin`.

## SNMP model (read-only live window)

- SNMP in this toolkit is **read-only by construction**: only `snmp_probe`,
  `snmp_get`, and `snmp_walk` exist; SNMP SET is not implemented anywhere.
- `snmp_probe(device)` is the fast identity check: use it for `sysDescr`,
  `sysObjectID`, exact firmware without SSH, and family confirmation.
- `snmp_get(device, oids)` is the default for exact questions: explicit OIDs or
  symbolic names, scalar polls, and sparse instance checks. Prefer it on MiNID
  and whenever you already know the target objects.
- `snmp_walk(device, oid, max_rows)` is for bounded subtree discovery only. It
  uses GETNEXT, not GETBULK, and the answer must state the cap when the walk is
  intentionally partial.
- Family support and caveats live in `references/snmp-support.md`. Respect
  them: for example, MiNID's agent is sparse, so prefer `snmp_get`; if a family
  or firmware is marked unsupported/inconclusive there, say so plainly instead
  of improvising.
- When a user asks to "check SNMP on the device", the default live sequence is:
  1) `snmp_probe` for identity/family/firmware, 2) targeted `snmp_get` for the
  exact objects requested, 3) `snmp_walk` only if the request is table/subtree
  shaped and the support notes say the family behaves well enough for a walk.

## Verified command map (core; full map is a reference file)

The **full, growing map lives in `references/verified-commands.md`** — for
any "how do I see / check X" question, grep THAT file first (it's cheaper
and more targeted than the full CLI reference; fall back to
`cli-reference-<family>.md` only when it has no row). Its rows carry a
**`Families` column — commands are family-specific; always check it matches
the target device's family** (e.g. `show resources` exists on secflow/etx1p
but NOT etx2). When a frequent command gets verified during a session, offer
to append it there with its checked families — a committed row saves the
lookup for every user of the skill. Core rows (all families) every session
needs:

| Purpose | Context | Command |
|---|---|---|
| Device identity (model, SW, MAC, uptime) | `configure system` | `show device-information` |
| Active alarms | `configure reporting` | `show active-alarms` |
| All-ports status summary | `configure port` | `show summary` |
| Full running config | root | `info` |
| Command discovery | any context | `tree` (levels below here), `help` |
| Persist config | any context | `save` |

Top-level `configure` contexts (SF-1p): access-control, bridge, crypto, fault,
management, monitor, oam, port, protection, qos, reporting, router, sd-iot,
system, terminal.

Some contexts are **indexed** and refuse navigation without an index — e.g.
`configure router` errors; it must be `configure router <1..10>`. The error is
self-describing: a failed navigation returns the expected parameters
(`- router <number> ... [1..10]`), so a NAVIGATION ERROR from
`run_show_in_context` usually tells you the missing piece. `tree` on a parent
context is the reliable way to discover what an unfamiliar subtree contains.

## Common config recipes (verified live — answer directly, no lookup needed)

All staged via `stage_config` (start `exit all`, end `exit all`); persist with
`save_startup`. Rollback = the `no ...` inverse.

**Static route** (`configure router <1..10>`):
`static-route <prefix> address <next-hop-ip> [metric <n>]` — next hop can also
be `interface <if>` or `tunnel-interface <t>`; prefix IPv4 or IPv6. Remove
with the FULL route spec — `no static-route <prefix> address <next-hop>` —
prefix alone errors (verified live: "parameter or keyword missing").
Verify: `show routing-table` / `show rib` there.

**Route policy** (`configure router <n>`): `prefix-list "<name>" ipv4` →
`deny|permit <prefix> sequence <n>` lines → bind with
`prefix-list-bind "<name>" in|out` under `bgp <as> > ipv4-unicast-af >
neighbor <ip>`. `route-map` lives at the same level.

**VLAN on a port** (`configure port ethernet <n>`): `vlan <vid>` sub-context →
`no shutdown` inside it; port itself needs `no shutdown` too. Bind L3:
`configure router <n> interface <i>` → `bind ethernet <p> vlan <vid>`.

**Device certificate → MQTTS** (verified live incl. full argument forms —
the reference's shallow `?` probes don't show them; failed-command errors do):
key `configure crypto key` → `generate key-name <n> type rsa size
{2048|3072|4096} [application x509]`. ⚠ **KEY LIMIT — state this BEFORE
generating:** the ETX-1p holds a **maximum of ONE key pair** (manual §6.15
error table: "You tried to generate more than one key pair"). A second
`generate` fails with "Maximum number of keys was exceeded" and creates
nothing. So "make a new key" on a box that already has one means **replace**:
`delete key-name <existing>` first — which breaks any cert built on it. Say
the limit up front; do not stage a second-key generate as if it will succeed.
Self-signed cert `configure crypto pki` →
`self-sign-certificate certificate-name <n> [common-name <cn>]` (uses an
existing device key); CA-signed: `authenticate` + `enroll-from-configuration
<attrs>` + `import-certificate <n>`; bind `configure system mqtt server <name>`
→ `address url <url> [protocol {ssl|tcp}] [port <1..65535, default 1883>]`
(or `address ip <ip> ...`) and `certificate <cert-name> trusted-ca <ca-name>`
(trusted-ca is REQUIRED — point it at a `configure crypto ca <name>` object).
On SecFlow, `show status` may report "MQTT Server Not Configured in LoRa
Gateway" — the server object is fine; it just isn't consumed by an
application yet.

## Interactive help: the `cli_help` tool (the CLI is self-documenting)

The CLI answers `?` at any point, and the **`cli_help(device, context,
prefix)`** MCP tool relays it. This is the authoritative way to learn command
syntax for the exact firmware on the device (richer than `tree`, which shows
structure but not arguments). Nothing is executed — the tool clears the
pending input after capturing the help.

- `cli_help(dev, context, "")` — lists every command/leaf at that level with
  one-line descriptions (context `""` = root).
- `cli_help(dev, context, "<command> ")` — **trailing space matters** — lists
  the command's arguments with types and constraints, e.g. prefix
  `"location "` → `<location-of-device> : Device location [0..255 chars]`.
- For multi-argument commands the listing shows accepted keyword/positional
  arguments; `<CR>` in the list means the command is also valid as-is.

Semantics of the listings (verified):

- `+` marks a sub-context you can navigate into; `-` marks a command/leaf.
- A `[no]` prefix on a leaf (e.g. `[no] location`) means the attribute is
  **removable**: `no <leaf>` deletes/unsets it. When reverting config, prefer
  `no <leaf>` over setting an empty value.
- Constraint brackets give validation ranges: `[2..2 chars]`,
  `[0..255 chars, default ...]` — validate values with `cli_help` BEFORE
  staging config, not after a commit fails.
- Level `?` listings also enumerate the context's `show` commands — use this
  to discover reads not yet in the verified map above.

**Workflow for any unfamiliar config task:** find the right context in
`references/command-tree-secflow.md` (resource `rad://command-tree/secflow`) →
read that context's section in `references/cli-reference-secflow.md` (resource
`rad://cli-reference/secflow/<context>`) for the level listing and argument
constraints → only if the context is parameterized or firmware differs, use
live `cli_help` → stage config.

Useful writable leaves under `configure system`: `name "..."`, `location "..."`,
`contact "..."` (safe, non-service-affecting — good for write-path testing).

## ⚠ Dangerous areas — never navigate here for reads

The `admin` context contains `reboot`, `force-reboot`, `factory-default`,
`factory-default-all`, `user-default`. Never send these; a factory-default or
reboot is service-affecting. The `file` context contains `delete*` commands —
only use its `show ...` commands.

Contexts are not purely navigational — some hold **action commands** alongside
config leaves. `configure router <n>` has `clear-arp-table`,
`clear-neighbor-table`, `clear-bfd-statistics`, `nat clear-nat-translations`,
and `delete` under `prefix-list`/`route-map`. Treat any `clear-*`/`delete`
token as a write: never send one via a read tool or without the staged flow.

## Health interpretation

1. `show device-information` — confirm expected SW version and sane uptime.
2. `show active-alarms` — any major/critical alarm → investigate before changes.
3. For service issues: physical port status → bridge/router state → OAM state.

## Config changes

Config lines for `stage_config` must be a complete, self-contained sequence
starting and ending at root, mirroring the `info` export format, e.g.:

```
exit all
configure system
location "site-A rack 3"
exit all
```

Always end with `exit all`. **On `mp4100` and `mp1` this recipe is MANDATORY
for every change, first line to last: `discard-changes` → configure →
`exit all` → `sanity-check` → `commit` → `save`** (confirmed live on mp-one
2026-07-16; `stage_config` enforces it server-side and refuses
non-conforming MP sequences). Each step matters:
`discard-changes` FIRST clears stale candidate edits left by earlier sessions —
without it, `sanity-check`/`commit` can fail on someone else's leftovers, not
your change ("Commit failed: DB=0 result=13" / "Sanity test failed" with a
perfectly valid config). `sanity-check` must report `Result : OK` before
`commit`; run `commit` from ROOT (after `exit all`), not from inside a
just-created object's `$` context — it fails there. `discard-changes` outside
this recipe is still not casual: it resets the whole candidate to running,
discarding YOUR uncommitted work too. On the other families, changes affect the **running** config
immediately; on all families nothing survives reboot until `save_startup` —
a revert is just staging the previous value back.
Verify after commit by re-running the relevant context `info` or `show`.
Rollback: stage the inverse commands or restore from the pre-commit backup
(path is in the commit_config output).

**Check documented limits BEFORE staging a bounded/additive write.** When a
write *creates one more of something* — a key, certificate, MQTT/OPC-UA server,
zone, neighbor, SNMP target — the device caps the count, and the cap lives in
the **manual**, not the `?` help. Before staging, grep `manual-<family>/` for
the scaling/limit statement (or the error-reference table) and **state the
limit to the user up front**; if they're already at it, say so and offer the
replace path rather than staging a doomed "add" that only fails at commit.
Known caps: ETX-1p = **1 key pair**, **2 MQTT servers** (manual §6.9/§6.15).
This is a hard lesson — the "add a second key" case was discovered at commit
instead of warned in advance; don't repeat it.
