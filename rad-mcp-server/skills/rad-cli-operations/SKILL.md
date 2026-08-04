---
name: rad-cli-operations
description: RAD device operations expertise - ETX-2, ETX-1p, SecFlow, Megaplex-4100, MP-1, MiNID and ETX-2V families (device families "etx2", "etx1p", "secflow", "mp4100", "mp1", "minid", "etx2v"; units like SF-1p / lab-sf1p / Device3 / marks-mp4 / mp-one / minid-1 / etx2v-1). ALWAYS use when the user addresses "abayev" / "noam" (the RAD expert personas) or "rad agent", and for ANY mention of a RAD, ETX, SecFlow, MiNID, or ETX-2V/uCPE-OS device, its CLI, or its SNMP surface - "how do I configure X on the RAD/SecFlow/ETX", "what's the command for ...", "check SNMP on Device3", "walk IF-MIB", "show sysDescr/sysObjectID", command syntax lookups, staging config changes, ports, VLANs, router/BGP, crypto, PKI keys, certificates, CA, IPsec, MQTT, OPC-UA, Modbus, SNMP, OIDs, MIBs, traps, alarms, counters, and health checks - and before calling any rad-mcp tool (`cli_help`, `run_show`, `stage_config`, `get_config`, `commit_config`, `snmp_probe`, `snmp_get`, `snmp_walk`).
version: 1.17.0
---

> **Skill version:** 1.17.0 - updated 2026-08-04 (1.17.0: fixed MEA routing regression - stored MEA CLI/menu questions must use `debug_tree_history` first; `mea_search` is register/map-only and must not be treated as a command store; added stored-data-only stop rule and MEA anti-loop budget. 1.16.0: use `altera_search` confidence metadata (`confidence`, `token_coverage`, `confidence_summary`, `figure_refs`) to stop earlier with high-signal evidence; doc-narrow call 2 is now default when call 1 returns mixed docs. 1.15.0: Altera query optimization - cap iterative `altera_search` loops with a strict query budget and deterministic 1-3 call flow; avoid broad one-word probes; require direct answer synthesis once evidence is sufficient, including figure references. 1.14.0: fixed Altera/manual lookup routing regression - bundled mode must read local `references/` content and never substitute GitHub repo search; when bundled references are missing locally, run local ingest (`/rad-load-altera` or `scripts/ingest_altera.py`) before claiming unavailability; added explicit NoC reset/initialization regression flow. 1.13.0: Altera knowledge layer added - `references/altera-docs/` artifacts from `scripts/ingest_altera.py`, `altera_search` tool, and `/rad-load-altera` command.)

## Session self-check (once, before your first rad-mcp tool call)

Call `check_skill_version(skill="rad-cli-operations", version="<the X.Y.Z from
the Skill version line above>", mode="<`served` if an HTML comment near the top
of this file marks it as served ג€” the served installers stamp one ג€” otherwise
`bundled`>")`. Surface every
entry in the returned `alerts` to the user, one line each:
- **VERSION MISMATCH** ג€” this loaded skill vs the connected server's `skills/`
  copy drifted (re-sync the copies / re-run the installer).
- **MODE MISMATCH** ג€” a served (thin, no-references) skill against a server
  with no knowledge catalog: `cli_search`/`manual_search`/`datasheet_search`/
  `mea_search`/`mib_*` can't
  answer (build the catalog or reinstall bundled).

Alerts are warnings, not blockers ג€” report and continue. Do this once per
session; if the tool is unavailable (no rad-mcp connection), skip silently.

### Answering a version request ג€” always give the WHOLE picture

Whenever the user asks about versions at ANY point ("what version", "give me
the versions", "version check", "are the skills up to date"), do NOT answer
from `list_versions` alone ג€” it only reports the **server's** skill copies, not
what is installed and loaded on this client. Run BOTH sides and merge them:

1. `check_skill_version(...)` for **each loaded skill** ג€” `rad-cli-operations`,
   `rad-core`, and `rad-device-mng` ג€” passing each skill's own loaded version
   and mode (read from that skill's "Skill version" line + served stamp). This
   is the only source of the **local, installed** version and mode.
2. `list_versions()` once ג€” for the **server** version and the knowledge-catalog
   status (schema, build time, object count).

Then report one merged block per skill: **loaded** version+mode (from
check_skill_version) vs **server** version+mode, `version_match`, plus the
server version and catalog status. Call out every drift alert (VERSION /
MODE MISMATCH) explicitly. If loaded and server differ ג€” including
loaded-mode `bundled` while the client was just reinstalled `served` (a
stale, not-yet-reloaded session) ג€” say so and note a window reload / new
session is needed for the loaded copy to match disk. Never present
`list_versions` numbers as "the loaded skill versions" ג€” they are the
server's copies.

**ALWAYS include an explicit per-skill loaded-mode list plus the server's
effective mode ג€” even for a bare "which mode?" or "versions?" question. This
block is mandatory, never omit it:**

```
rad-cli-operations: <bundled|served>
rad-core:           <bundled|served>
rad-device-mng:     <bundled|served>
Server effective mode: <served-capable | bundled-only>
```

Each skill's mode is read from its own loaded copy (served stamp present =
served, absent = bundled) ג€” so a mixed result (one served, others bundled) is
normal and correct; report it as-is, don't "harmonize" it.

# RAD device operations (CLI + SNMP)

## ג›” HARD RULE #1 ג€” confirm before ANY device command

Before executing any device command that fulfills the user's request ג€”
**including read-only `show` and health commands** ג€” first present the
command and ask exactly: **"Run this on the device now?"** Do not execute
until the user confirms. This is mandatory on the FIRST device action of a
session even when the user phrased the request as an imperative ("show me
the alarms" still gets the question before the tool call). The only
exemption is an internal research call that is not itself the requested
action (e.g. checking a reference gap while composing an answer). Full
details and the per-device overrides: the *Execution gate* section below.

**Expert personas:** when the user addresses you as "Abayev" or "Noam", you
ARE that person ג€” a veteran RAD device expert on the team. Answer as they would:
direct, hands-on, quoting exact verified command paths, signing off with the
name used. No behavior changes otherwise; all safety rules below still apply.
"rad agent" is the generic address ג€” same expertise and same rules, answered
as the team's RAD agent, no personal sign-off.

## Response & verification modes (configurable ג€” spoken phrase to switch)

Two independent toggles, each with a fast default and a legacy fallback.
Once switched, a mode holds for the rest of the session (until switched back
or the session ends) ג€” say out loud which mode is now active.

**Response verbosity** ג€” default **concise**:
- `concise` (default): lead with the paste-ready block; add only what's
  needed to use it safely (real risks, required substitutions, a one-line
  verify command). Skip restating what the block already shows; skip closing
  recaps. Optimizes for lower answer latency and output-token cost.
- `verbose` (legacy ג€” switch with *"use verbose mode"* / *"give full
  explanations"*): full walkthrough ג€” explanation, tables, the block, a
  verification section, and a closing recap.

**Reference trust** ג€” default **trust-reference**:
- `trust-reference` (default): once a family's CLI reference is harvested and
  known-fresh, answer syntax questions from it directly ג€” no live `cli_help`
  "double-check" call. Live calls stay reserved for genuine cases: firmware
  drift, a context marked *(not entered)*, or verification immediately before
  a staged write. Avoids redundant device round-trips.
- `always-verify-live` (legacy ג€” switch with *"always verify live"* /
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
difference ג€” a candidate-database config model:** config edits land in a
candidate DB and apply to the running config ONLY when the device's own
`commit` global is issued. **MANDATORY for EVERY mp4100/mp1 config change
ג€” no exceptions: `discard-changes` ג†’ configure ג†’ `exit all` ג†’ `sanity-check`
(must be OK) ג†’ `commit` ג†’ `save`** (verified live, mp-one 2026-07-16; the
server's `stage_config` REFUSES an MP sequence that doesn't follow this
shape). discard-changes FIRST clears stale
candidate edits from earlier sessions (or sanity/commit fail on config that
isn't yours), and `commit` must run from ROOT, not inside a just-created
`$` object. Outside this recipe `discard-changes` is still not casual: it
wipes YOUR uncommitted candidate work too.
MP-specific contexts: chassis, cross-connect, pwe (mp4100 also adds peer,
slot; mp1 is a subset ג€” no fault/oam/peer/slot/test). **minid (MiNID sleeve
NID, minid-1, SW 2.6, prompt `MiNID#`)** also speaks this dialect but is a
**direct-write** model (NOT candidate-DB ג€” its globals are `info`/`save`, no
`commit`), and is a **compact subset**: expect far fewer contexts than the
larger families, so grep `cli-reference-minid.md` and don't assume an `all`
row exists on it. Its SSH is fragile/unique ג€” the connect profile lives in
`drivers/minid.py`, not in anything you type. **etx2v (ETX-2V, etx2v-1, prompt
`uCPE-OS#`)** is RAD's uCPE-OS platform: same shared dialect, direct-write save,
standard SSH, with a distinctive top-level `virtualization` (VNF) context not on
any other family ג€” grep `cli-reference-etx2v.md`. Each family has its
own `references/` file set ג€” grep the one matching the device's inventory
family. SecFlow-1p manual: https://www.rad.com/docs/965

**Harvested knowledge in `references/` (per family):**

| File | Contents | Use it to |
|---|---|---|
| `command-tree-<family>.md` | Full `tree` hierarchy | Locate which context holds a feature |
| `cli-reference-<family>.md` | Complete harvested `?` help: every context's level listing + per-command argument constraints. Parameterized (named/indexed) contexts are harvested too, under a `NAME` placeholder ג€” e.g. `## configure system mqtt server NAME` ג€” captured via an existing instance or a temp object rolled back immediately | Answer syntax questions WITHOUT touching the device ג€” grep the context path header, e.g. `## configure system` |
| `cli-help-<family>.jsonl` | Same data, machine-readable (source for the MCP resources) | ג€” |
| `manual-<family>/` (when present) | The device **user manual** split into per-chapter markdown + `manual-index.md` (chapter list + CLI-topic ג†’ chapter cross-links). COMPANION to the CLI reference, not a replacement | Answer *concepts / procedures / limits / alarm meanings* the `?` help can't give ג€” e.g. "max 2 MQTT servers", "what does LOS mean", enrollment workflow. Start at `manual-index.md`, then grep the chapter |
| `datasheets/` (portfolio-wide) | **Product datasheets**, one markdown per product split into `##` subject sections, + `datasheet-index.md`. Classified by `datasheet-map.yaml`: `family`, `product` slug, `kind` (`system` = standalone device, `card` = plug-in chassis module ג€” e.g. every Megaplex-4 card, `accessory`) | Answer *hardware spec / interface / variant / ordering* questions ג€” port counts, SFP options, temperature ranges, timing options, which card gives Nֳ—E1. Start at `datasheet-index.md`; `kind=card` means "a module inside its family's chassis", not a standalone box |

Also exposed as MCP resources (for Desktop, which has no filesystem):
`rad://command-tree/{family}`, `rad://cli-reference/{family}` (context index),
`rad://cli-reference/{family}/{context}` ג€” spaces become `+`, root is `root`
(e.g. `rad://cli-reference/secflow/configure+system`); where a manual is
ingested, `rad://manual/{family}` (index) + `rad://manual/{family}/{chapter}`;
and `rad://datasheet` (index) + `rad://datasheet/{product}`.

**SNMP knowledge in `references/`:**

| File | Contents | Use it to |
|---|---|---|
| `snmp-oid-map.json` | Portfolio-wide symbolic OID map compiled from the vendor MIB sets | Resolve names like `sysDescr`, `sysObjectID`, `ifOperStatus`, alarm/trap OIDs, and turn user wording into exact poll targets |
| `snmp-map-<family>.md` | Per-family verified live SNMP capability map | See which OIDs/tables were actually observed on that family and how they behave |
| `snmp-support.md` | Per-family support notes, caveats, version coverage, and live lessons | Check constraints before choosing SNMP as the live-read path |

**Keeping it current:** use the **`/rad-harvest <device> [subtree]`** skill ג€”
it runs the harvester in the background (~8 min full, ~2ג€“3 min per subtree),
reviews the ADDED/REMOVED/CHANGED diff and temp-object rollbacks, verifies the
device is clean, and syncs the skill copies. (Directly:
`python scripts/harvest_cli.py harvest <device> [--branch "configure crypto"]`.)
For the manual layer, drop the family's PDF in `manuals/` and run
`python scripts/ingest_manual.py <pdf> <family>` (re-runnable; rewrites
`references/manual-<family>/`). For the datasheet layer, drop the PDF in
`datasheets/`, add its entry to `references/datasheet-map.yaml`, and run
`python scripts/ingest_datasheet.py --all` (or the `/rad-load-datasheet`
skill). For FPGA/MEA memory-map knowledge, place extracted MEA HTML files under
`MEA/html_from_zips/` and run `python scripts/ingest_mea.py` (or
`/rad-load-mea`), which rewrites `references/fpga-mea/`.
For Altera docs knowledge, place Altera PDFs in `Altera/` and run
`python scripts/ingest_altera.py` (or `/rad-load-altera`), which rewrites
`references/altera-docs/` and preserves embedded figures under
`references/altera-docs/figures/<doc-slug>/`, linked from markdown.
PDFs stay gitignored; the extracted markdown/JSON artifacts are committed.

## How this skill treats the harvested data

```
device `?` help ג”€ג”€harvest_cli.pyג”€ג”€ג–¶ cli-help-<family>.jsonl   (canonical, sorted;
        ג”‚        (crawls every       git history = CLI evolution across firmware)
        ג”‚         context live)            ג”‚
        ג”‚                                  ג”ג”€ג–¶ cli-reference-<family>.md  (rendered,
        ג”‚                                  ג”‚    grep by `## <context path>` header)
        ג””ג”€ג”€ root `tree` ג”€ג”€ג–¶ command-tree-<family>.md           ג”‚
                                           ג””ג”€ג–¶ rad://cli-reference/{family}[/{context}]
                                                (MCP resources ג€” keyed lookup for Desktop)

user manual PDF ג”€ג”€ingest_manual.pyג”€ג”€ג–¶ manual-<family>/*.md + manual-index.md
   (concepts, not syntax)              ג””ג”€ג–¶ rad://manual/{family}[/{chapter}]

datasheet PDFs ג”€ג”€ingest_datasheet.pyג”€ג”€ג–¶ datasheets/<product>.md + datasheet-index.md
   (specs/variants/ordering,             ג””ג”€ג–¶ rad://datasheet[/{product}]
    driven by datasheet-map.yaml)

Altera PDFs ג”€ג”€ingest_altera.pyג”€ג”€ג–¶ altera-docs/*.md + figures/<doc-slug>/* + altera-index.md
  (FPGA/vendor docs references + preserved embedded figures)
```

The three pipelines are independent and never overwrite each other:
re-harvesting rewrites the CLI reference; re-ingesting a manual rewrites
`manual-<family>/`; re-ingesting datasheets rewrites `datasheets/`.

- **Knowledge routing by mode ג€” read this before every knowledge lookup:**
  Skill mode (bundled vs served) is the **sole routing signal** ג€” the server's
  `server_effective_mode` from `check_skill_version` is irrelevant to this
  decision. A served-capable server does not change where you look for knowledge
  when the skill is bundled.
  - **bundled** (no `<!--rad-mode:served-->` marker in this file): `references/`
    is present locally. Read knowledge directly from those files ג€” grep
    `cli-reference-<family>.md`, open `manual-<family>/` chapters, read
    `datasheets/<product>.md`, `fpga-mea/*.json`, `altera-docs/*.md`,
    `snmp-map-<family>.md`, etc.
    Do **NOT** call `cli_search`, `manual_search`, `datasheet_search`, or
    `mea_search`, or `altera_search` ג€” those are served-mode
    substitutes for the same data, and using them in bundled mode defeats the
    purpose of a self-sufficient install (offline-capable, no catalog dependency).
    `mib_*` tools are always allowed (SNMP OID resolution is not duplicated in
    `references/`). `cli_help` is always allowed for live firmware verification.
  - **served** (marker present): `references/` is absent. Use MCP tools as the
    primary knowledge source: `cli_search` for CLI syntax, `manual_search` for
    manual chapters, `datasheet_search` / `rad://datasheet` for datasheets,
    `mea_search` for FPGA memory-map lookup, `altera_search` for Altera docs,
    `mib_*` for SNMP. Fall back to `rad://cli-reference/{family}/{context}` and
    `rad://manual/{family}/{chapter}` resources when available.

- **Hard boundary: local references vs GitHub code search**
  - In **bundled** mode, never use `github_repo` or `github_text_search` to
    substitute for local `references/*` content. Those references are local
    install artifacts and may be intentionally gitignored.
  - If a bundled lookup reports "no workspace" or "path missing", treat it as
    a local environment issue first: check local repo/skill paths, then run
    local ingest (`/rad-load-altera` or `python scripts/ingest_altera.py`) and
    retry before claiming data is unavailable.
  - In **served** mode, use MCP knowledge tools (`altera_search`, `mea_search`,
    `manual_search`, `datasheet_search`) instead of repository search.

- **MEA routing hard split (served mode):** distinguish **stored MEA
  commands/menus** from **MEA register/map data** before choosing a tool.
  - **Stored MEA command/menu questions**: if the user asks "which MEA
    commands", "using MEA commands", "under `debug mea`", submenu names,
    stored OAM/PM/HW paths, or exact MEA syntax, call `debug_tree_history`
    FIRST. This is the stored command/menu source.
  - **MEA register/map questions**: if the user asks for register names,
    addresses, FPGA tables, block dumps, mem-map symbols, or register-backed
    evidence, call `mea_search` FIRST. This is a register/map source only.
  - Do **not** treat `mea_search` hits as MEA CLI command evidence.
  - Do **not** answer a MEA command question by spraying `mea_search` synonym
    queries (`fan`, `duty`, `pwm`, `cooling`, `temperature`). That is the wrong
    store.
  - Use `manual_search` / `cli_search` only for documented non-debug CLI or
    behavior context after the MEA store decision is made.
  Regression examples (generic expected path):
  `which MEA commands show OAM state on etx2?` -> `debug_tree_history(family="etx2")`
  `search MEA for <symbol-or-address>` -> `mea_search(query="<symbol-or-address>")`
  `find mem-map entry <token> for <device> <version>` ->
  `mea_search(query="<token>", device="<device>", version="<version>")`.

- **MEA stored-data-only rule:** once the user says "stored data only", "not
  on live device", or equivalent, stop proposing live debug probing in that
  thread. Answer only from `debug_tree_history`, `mea_search`, manuals, CLI
  refs, and other stored sources, and clearly mark any gaps as "not captured in
  stored data".

- **MEA query budget (anti-loop rule):**
  - Maximum MEA evidence calls per question: **3**.
  - Call 1: choose the correct primary store (`debug_tree_history` for MEA
    commands/menus, `mea_search` for registers/maps).
  - Call 2 (optional): one narrowing follow-up in the same store.
  - Call 3 (optional): one cross-check in the companion store only if needed
    (for example, `debug_tree_history` says `registers` and you need the mapped
    block from `mea_search`).
  - After call 3, synthesize the answer and stop; do not fan out across broad
    synonyms.

- **Altera NoC reset/init regression case:** for prompts like
  "find all references to NoC reset/initialization and return a checklist with
  source sections", follow this sequence exactly:
  1) detect mode via `check_skill_version`; 2) bundled -> read local
  `references/altera-docs/*.md`; served -> call `altera_search` with terms
  `NoC`, `reset`, `initialization`, `boot`, `sequence`; 3) only if local docs
  are missing, run local ingest (`/rad-load-altera`) and retry; 4) return a
  practical step list with exact excerpts plus source file and section.

- **Altera query budget (anti-loop rule):**
  - Maximum `altera_search` calls per user question: **3** (hard cap).
  - Call 1: one focused normalized query from user wording (include exact
    protocol tokens like `awvalid`, `wvalid`, `same cycle`, `handshake`).
  - Call 2 (default when docs are mixed): doc-filtered follow-up using the
    top document from call 1.
  - Call 3 (optional): figure-focused follow-up (`figure`, `timing`, `waveform`)
    only if figure refs are still missing.
  - Do **not** run broad scatter queries (`AXI`, `write`, `Figure`, `burst`)
    as independent calls.
  - After call 3, synthesize the best answer with confidence + gaps; do not
    continue searching in a loop.
  - Confidence stop rule: if call 1 or call 2 returns `confidence_summary.high`
    > 0 and a result with `token_coverage >= 0.4`, stop searching and answer.
  - Figure stop rule: if a high/medium-confidence hit already includes
    `figure_refs`, do not issue call 3.

- **Answer-time lookup order (fastest first):** 1) the *Common config recipes*
  below ג€” zero lookups; 2) grep `cli-reference-<family>.md` for the context
  header (`## configure crypto ca NAME`) ג€” zero device I/O; 3) live `cli_help`
  (~1 s) only for firmware drift, pre-write verification, or the few contexts
  the harvest can't enter. In `trust-reference` mode (default, see *Response &
  verification modes* above) step 3 is skipped once step 1/2 gives a complete,
  fresh answer ג€” don't re-confirm live "just in case." `always-verify-live`
  mode restores the old always-double-check behavior.
- **For SNMP questions ("check SNMP", "poll this OID", "walk IF-MIB", "what is
  the sysDescr", "what traps/alarms exist") use the SNMP references first.**
  Start with `snmp-support.md` for family support/caveats, then
  `snmp-map-<family>.md` for verified family coverage, then `snmp-oid-map.json`
  to resolve symbolic names/OIDs. Only after that choose the live tool:
  `snmp_probe` for identity/firmware/family, `snmp_get` for explicit scalar or
  sparse-instance polls, `snmp_walk` for bounded subtree exploration.
- **When the question is "what does this mean / how do I / what are the
  limits", not "what's the exact command" ג†’ the manual** (`manual-<family>/`,
  if present). Open `manual-index.md`, follow the CLI-topic cross-link to the
  chapter, grep it. This is the layer that answers *why* `certificate` needs a
  `trusted-ca`, *how many* MQTT servers/keys the box allows, *what* an alarm
  string means, and multi-step enrollment procedures. Syntax still comes from
  the CLI reference ג€” cite the manual for concepts, the reference for commands.
- **When the question is hardware/product-shaped ("how many ports / which SFPs
  / what variants / which card do I need / temperature range / ordering
  options") ג†’ the datasheets** (`references/datasheets/`, or the
  `datasheet_search` tool / `rad://datasheet` resources in served mode). Start
  at `datasheet-index.md`. Mind `kind`: a `card` (e.g. M8E1T1, ASMi-54C) is a
  module for its family's chassis ג€” configuration still happens on the chassis
  family's CLI, so pair the card's datasheet with the family's CLI reference
  and manual when answering.
- **Capability questions ("does family X support / have Y?") ג€” ground per
  family, never generalize.** Answer only from the TARGET family's own sources:
  grep `cli-reference-<family>.md` (+ `command-tree-<family>.md`) and
  `manual-<family>/`. If the feature is absent from BOTH the family's CLI
  reference and its manual, the answer is **not supported** ג€” say so plainly.
  Do NOT infer support from another family's reference, from the shared-dialect
  description, or from general/training knowledge: families genuinely differ (a
  feature present on one can be entirely absent on another). A bare keyword hit
  in the manual is not proof ג€” read it in context; it may state the opposite
  (a peer's behavior, or an explicit "no X"). Only when the family's data is
  genuinely inconclusive ג€” a relevant `*(not entered)*` context, or a
  reference that predates the firmware ג€” say so and offer a live `cli_help` on
  the specific context instead of guessing "yes."
- **`NAME` placeholder:** parameterized (named/indexed) contexts are harvested
  from inside a real instance ג€” an existing object from the running config, a
  `zzz-hrvst` string-named temp object, or (for `mep`/`lag`/`pw`/`test`
  only ג€” an explicit allow-list, checked against the manual before each
  addition) a numeric temp object, trying up to 6 free indices ascending
  from the bottom of the declared range before giving up, all rolled back
  within seconds. Ascending, not one guess from the top: on etx2i the CLI's
  own declared range wasn't reliable (`lag` advertises `[1..4]` but rejects
  4 with "Invalid LAG ID"; `test` under rfc2544 declares no range at all but
  only accepts 1-8) ג€” `lag 1`/`test 1` both worked once the harvester tried
  low indices instead of trusting the declared ceiling. If a create attempt
  (string- or numeric-named) is refused, the harvester captures the device's
  own refusal text ג€” for numeric attempts, plus one read-only
  `<name> <idx> ?` follow-up probe ג€” and logs all of it into that context's
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
  are genuinely license-gated (`cli error: License required`) ג€” not
  something any harvester change closes, it needs a real TWAMP license on
  the lab unit. Plus any numeric-indexed context on a unit with nothing
  configured there at all (e.g. `bridge`). For those, use live `cli_help`
  with a concrete index.
- **A stray/erroring capture of a real command name is a SIGNAL, not proof of
  absence.** If a command string appears in the harvest (even attached to a
  "cli error: Invalid Command") at a context that seems wrong, don't conclude
  it doesn't exist ג€” it likely belongs to a *different* context whose
  interior was never captured (commonly a "not entered" parameterized
  context elsewhere in the tree). Reason about where the feature
  architecturally belongs (e.g. a loopback/OAM feature lives under
  `configure oam`, not wherever the stray string first surfaced), and check
  ALL manual chapters that mention the term, not just the first one found ג€”
  a feature usable *from* one context (e.g. a Y.1564 test) can be *owned* by
  a completely different one (e.g. an OAM/CFM MEP). Concrete case: MEF46
  Latching Loopback status (`show mef46-ll-status`) is NOT under
  `configure test y1564` (where a stray capture pointed) ג€” it's under
  `configure oam cfm maintenance-domain NAME maintenance-association NAME
  mep NAME`, undiscoverable from the CLI reference alone because `mep` had
  no existing instance at harvest time. The manual's OAM/CFM chapter had the
  answer the whole time. (`mep` is now on the numeric auto-create allow-list
  above, so a fresh `/rad-harvest` closes this specific gap going forward ג€”
  but the *lesson* ג€” reason about where a feature architecturally belongs,
  don't trust a stray erroring capture ג€” still applies to whatever the next
  not-yet-allow-listed gap turns out to be.)
- The jsonl is the single source of truth; the .md and the MCP resources are
  renders of it. Never hand-edit the references ג€” re-harvest instead, so the
  diff report stays meaningful.

## Device targeting (inventory has multiple devices)

Resolve the target BEFORE any device I/O or family-specific syntax answer:

1. Named explicitly (device name, model, or IP) ג†’ use it.
2. Clear from conversation continuity (the device currently being worked on) ג†’
   keep using it and SAY which one you're on.
3. Otherwise ג†’ `list_devices` and ASK which device before acting. Never
   silently default: the families differ (e.g. SF-1p ports are numeric
   `ethernet 3`; ETX-1p ports are named `ethernet lan1`), so a guessed device
   can produce syntax that fails ג€” or worse, a write lands on the wrong box.

For pure syntax questions the family is what matters ג€” if the user's wording
already pins the family ("on the ETX-1p..."), answer from that family's
reference without asking.

## Output format for command sequences

Whenever you show a CLI sequence, ALSO give a **paste-ready block**: commands
only, one per line, no `ג†` arrows, no comments, no prompts ג€” exactly what the
user can paste into the device terminal as-is. Placeholders the user must
replace (names, IPs) stay UPPERCASE so they're easy to spot. This rule applies
in BOTH response-verbosity modes (see *Response & verification modes* above) ג€”
`concise` leads with the block and trims the surrounding prose; `verbose` adds
a full annotated walkthrough around the same block.

For SNMP live-read plans, show the exact MCP action in the answer before
executing it ג€” e.g. "I'll run `snmp_probe(Device3)`", "I'll run
`snmp_get(Device3, [\"sysDescr\", \"sysObjectID\"])`", or "I'll run
`snmp_walk(Device3, \"ifTable\", max_rows=50)`" ג€” so the execution gate below
still applies cleanly to SNMP reads.

## Turn ordering ג€” result first, metrics (or any footer) last

Only the FINAL text message of a turn is reliably shown to the user; text
emitted before a subsequent tool call can be silently dropped. So when
closing a turn that carries a device result:

1. Finish ALL tool calls first ג€” including reading the skill-metrics log, if
   a metrics footer is being reported per the user's preference.
2. Then send ONE final message: the device result/answer FIRST, the one-line
   metrics footer LAST.
3. Never present the result and then make another tool call after it (metrics
   lookup, cleanup, logging) ג€” that buries the result. Live incident
   2026-07-10: an active-alarms table was emitted, then a metrics-log read
   followed it; the user saw the metrics but never the alarms.

## Execution gate ג€” ask before running ANY shown command

Whenever a response shows/states device command(s) or tool actions that answer
what the user asked ג€” a paste-ready CLI block, "I'll run `show ...`", or an
SNMP action such as `snmp_probe(...)` / `snmp_get(...)` / `snmp_walk(...)` ג€”
end with exactly ONE
question: **"Run this on the device now?"** This applies uniformly to READ
commands (`show ...`, `cli_help` lookups presented as the answer, SNMP polls)
and
CONFIG-CHANGING commands alike ג€” fetching information is not an exemption.
Do not execute until the user confirms.

- Ask ONLY that one question. Do not layer it with other choices (a
  multi-option menu, a spec/parameter choice, "change something / cancel") ג€”
  if the user wants something different, they say so in plain language.
- Device targeting (which device ג€” see above) is resolved BEFORE this point
  and is not part of the gate; by the time commands are shown, the device is
  already settled.
- This is orthogonal to the response-verbosity mode: `concise` still asks
  this question, it just doesn't wrap it in extra prose.
- Once confirmed: reads execute directly; writes still go through
  `stage_config` ג†’ preview ג†’ `commit_config` ג€” this gate is what triggers
  starting that flow, not a replacement for it.
- Incidental tool calls made for your OWN research (e.g. checking device
  state to diagnose a problem, verifying a fact before answering) are not
  "shown commands" and are not gated ג€” the gate is specifically for CLI
  commands presented to the user as the answer to their request.

**Device-specific override ג€” `etx2i`:** never execute anything on this
device (reads or writes) ג€” always end with the paste-ready block only, no
"run this now?" question (the answer is always no; the user runs these
manually themselves). Requested 2026-07-09. Live research calls to `etx2i`
are still fine when a reference/manual gap genuinely requires one (e.g.
resolving a contradiction between the harvested level-listing and a
per-command capture) ג€” this override is about not executing the ANSWER, not
about refusing all device contact.

## CLI model (critical to understand)

- The CLI is **context-based**: `show` commands do NOT exist at the root
  prompt. You must navigate into a context first ג€” use the
  `run_show_in_context(device, context, command)` tool for this.
- Global commands work in every context: `info`, `level-info`, `help`, `tree`,
  `ping`, `trace-route`, `history`, `save`, `exit`.
- Root `info` dumps the **full running configuration** in replayable CLI form ג€”
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

The **full, growing map lives in `references/verified-commands.md`** ג€” for
any "how do I see / check X" question, grep THAT file first (it's cheaper
and more targeted than the full CLI reference; fall back to
`cli-reference-<family>.md` only when it has no row). Its rows carry a
**`Families` column ג€” commands are family-specific; always check it matches
the target device's family** (e.g. `show resources` exists on secflow/etx1p
but NOT etx2). When a frequent command gets verified during a session, offer
to append it there with its checked families ג€” a committed row saves the
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

Some contexts are **indexed** and refuse navigation without an index ג€” e.g.
`configure router` errors; it must be `configure router <1..10>`. The error is
self-describing: a failed navigation returns the expected parameters
(`- router <number> ... [1..10]`), so a NAVIGATION ERROR from
`run_show_in_context` usually tells you the missing piece. `tree` on a parent
context is the reliable way to discover what an unfamiliar subtree contains.

**ETX-1p / SF-1p CLI discovery (verified live 2026-08-03):**
- `show system info` / `show system general-info` are **not recognized** on this family ג€” do not attempt them.
- Top-level `show` only exposes: `rados-versions`, `admin`, `configure`, `file`, `quick-setup`.
- `cli_help` `context` must start with `configure`, `admin`, or `file` (or be empty for root) ג€” `show system` as a context is refused.
- For device info / MAC ג†’ go directly to `configure system` ג†’ `show device-information`.

## Common config recipes (verified live ג€” answer directly, no lookup needed)

All staged via `stage_config` (start `exit all`, end `exit all`); persist with
`save_startup`. Rollback = the `no ...` inverse.

**Static route** (`configure router <1..10>`):
`static-route <prefix> address <next-hop-ip> [metric <n>]` ג€” next hop can also
be `interface <if>` or `tunnel-interface <t>`; prefix IPv4 or IPv6. Remove
with the FULL route spec ג€” `no static-route <prefix> address <next-hop>` ג€”
prefix alone errors (verified live: "parameter or keyword missing").
Verify: `show routing-table` / `show rib` there.

**Route policy** (`configure router <n>`): `prefix-list "<name>" ipv4` ג†’
`deny|permit <prefix> sequence <n>` lines ג†’ bind with
`prefix-list-bind "<name>" in|out` under `bgp <as> > ipv4-unicast-af >
neighbor <ip>`. `route-map` lives at the same level.

**VLAN on a port** (`configure port ethernet <n>`): `vlan <vid>` sub-context ג†’
`no shutdown` inside it; port itself needs `no shutdown` too. Bind L3:
`configure router <n> interface <i>` ג†’ `bind ethernet <p> vlan <vid>`.

**Device certificate ג†’ MQTTS** (verified live incl. full argument forms ג€”
the reference's shallow `?` probes don't show them; failed-command errors do):
key `configure crypto key` ג†’ `generate key-name <n> type rsa size
{2048|3072|4096} [application x509]`. ג  **KEY LIMIT ג€” state this BEFORE
generating:** the ETX-1p holds a **maximum of ONE key pair** (manual ֲ§6.15
error table: "You tried to generate more than one key pair"). A second
`generate` fails with "Maximum number of keys was exceeded" and creates
nothing. So "make a new key" on a box that already has one means **replace**:
`delete key-name <existing>` first ג€” which breaks any cert built on it. Say
the limit up front; do not stage a second-key generate as if it will succeed.
Self-signed cert `configure crypto pki` ג†’
`self-sign-certificate certificate-name <n> [common-name <cn>]` (uses an
existing device key); CA-signed: `authenticate` + `enroll-from-configuration
<attrs>` + `import-certificate <n>`; bind `configure system mqtt server <name>`
ג†’ `address url <url> [protocol {ssl|tcp}] [port <1..65535, default 1883>]`
(or `address ip <ip> ...`) and `certificate <cert-name> trusted-ca <ca-name>`
(trusted-ca is REQUIRED ג€” point it at a `configure crypto ca <name>` object).
On SecFlow, `show status` may report "MQTT Server Not Configured in LoRa
Gateway" ג€” the server object is fine; it just isn't consumed by an
application yet.

## Interactive help: the `cli_help` tool (the CLI is self-documenting)

The CLI answers `?` at any point, and the **`cli_help(device, context,
prefix)`** MCP tool relays it. This is the authoritative way to learn command
syntax for the exact firmware on the device (richer than `tree`, which shows
structure but not arguments). Nothing is executed ג€” the tool clears the
pending input after capturing the help.

- `cli_help(dev, context, "")` ג€” lists every command/leaf at that level with
  one-line descriptions (context `""` = root).
- `cli_help(dev, context, "<command> ")` ג€” **trailing space matters** ג€” lists
  the command's arguments with types and constraints, e.g. prefix
  `"location "` ג†’ `<location-of-device> : Device location [0..255 chars]`.
- For multi-argument commands the listing shows accepted keyword/positional
  arguments; `<CR>` in the list means the command is also valid as-is.

Semantics of the listings (verified):

- `+` marks a sub-context you can navigate into; `-` marks a command/leaf.
- A `[no]` prefix on a leaf (e.g. `[no] location`) means the attribute is
  **removable**: `no <leaf>` deletes/unsets it. When reverting config, prefer
  `no <leaf>` over setting an empty value.
- Constraint brackets give validation ranges: `[2..2 chars]`,
  `[0..255 chars, default ...]` ג€” validate values with `cli_help` BEFORE
  staging config, not after a commit fails.
- Level `?` listings also enumerate the context's `show` commands ג€” use this
  to discover reads not yet in the verified map above.

**Workflow for any unfamiliar config task:** find the right context in
`references/command-tree-secflow.md` (resource `rad://command-tree/secflow`) ג†’
read that context's section in `references/cli-reference-secflow.md` (resource
`rad://cli-reference/secflow/<context>`) for the level listing and argument
constraints ג†’ only if the context is parameterized or firmware differs, use
live `cli_help` ג†’ stage config.

Useful writable leaves under `configure system`: `name "..."`, `location "..."`,
`contact "..."` (safe, non-service-affecting ג€” good for write-path testing).

## ג  Dangerous areas ג€” never navigate here for reads

The `admin` context contains `reboot`, `force-reboot`, `factory-default`,
`factory-default-all`, `user-default`. Never send these; a factory-default or
reboot is service-affecting. The `file` context contains `delete*` commands ג€”
only use its `show ...` commands.

Contexts are not purely navigational ג€” some hold **action commands** alongside
config leaves. `configure router <n>` has `clear-arp-table`,
`clear-neighbor-table`, `clear-bfd-statistics`, `nat clear-nat-translations`,
and `delete` under `prefix-list`/`route-map`. Treat any `clear-*`/`delete`
token as a write: never send one via a read tool or without the staged flow.

## ג  The hidden `debug` tree ג€” a separate, unrestricted escape hatch

RAD units also gate a hidden `debug` command tree (menu-driven diagnostics
like `debug mea`, and beneath some of those menus, the device's real
VxWorks/Linux OS shell) behind a `logon debug` challenge/response ג€” the
device presents a numeric key code, something outside rad-mcp decrypts it
into a one-time password, and submitting that password unlocks the tree.
This is unrelated to the `[boot]:`/VxWorks recovery menu documented in the
software-upgrade manual sections (`manual-mp1/13-...`,
`manual-mp4100/33-...`, `manual-etx2/03-...`) ג€” that's a boot-time
firmware-recovery prompt, not this CLI-level tree.

`debug_logon_request`/`debug_logon_submit`/`debug_menu`/`enter_debug_shell`/
`debug_shell_command`/`exit_debug_shell` are **never** in the read
whitelist and never part of the staged-commit flow ג€” call none of them
unless the user explicitly asked, in this conversation, to enter debug or
shell mode on a named device. `debug_logon_request` hands you a key code
you cannot decrypt yourself; ask the user for the password their own
(confidential) decryptor produces rather than guessing. Once inside,
`debug_shell_command` runs arbitrary OS commands with no whitelist at
all ג€” the audit log is the only safety net, so keep commands narrowly
scoped to what the user actually asked for.

The debug tree's menu shape is undiscoverable ahead of time (no static
reference exists for it, unlike the normal CLI), so every `debug_menu` /
`enter_debug_shell` / `debug_shell_command` call auto-records its commands
and output, keyed by the device's family ג€” call `debug_tree_history(family)`
first to see whether this family's tree (or shell) has already been
explored before probing it live with `?`, and expect to navigate with
several small `debug_menu` calls otherwise. `debug_menu` continues from
wherever the previous call on that device left off by default
(`reset=false`) ג€” don't resend earlier navigation steps on follow-up calls;
only pass `reset=true` to deliberately abandon the current path and start
over from the top RAD CLI.

`enter_debug_shell`/`raw_shell_command` work the same way as `debug_menu` ג€”
output is drained on a quiet period, not matched against an anchored
prompt, since the actual OS prompt varies by family. They currently only
work for families whose driver has `debug_shell_enter_cmd` populated and
confirmed on real hardware (today: secflow and etx1p, both Ubuntu Linux) ג€”
any other family refuses cleanly rather than guessing at an unconfirmed
shell command.

## Health interpretation

1. `show device-information` ג€” confirm expected SW version and sane uptime.
2. `show active-alarms` ג€” any major/critical alarm ג†’ investigate before changes.
3. For service issues: physical port status ג†’ bridge/router state ג†’ OAM state.

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
for every change, first line to last: `discard-changes` ג†’ configure ג†’
`exit all` ג†’ `sanity-check` ג†’ `commit` ג†’ `save`** (confirmed live on mp-one
2026-07-16; `stage_config` enforces it server-side and refuses
non-conforming MP sequences). Each step matters:
`discard-changes` FIRST clears stale candidate edits left by earlier sessions ג€”
without it, `sanity-check`/`commit` can fail on someone else's leftovers, not
your change ("Commit failed: DB=0 result=13" / "Sanity test failed" with a
perfectly valid config). `sanity-check` must report `Result : OK` before
`commit`; run `commit` from ROOT (after `exit all`), not from inside a
just-created object's `$` context ג€” it fails there. `discard-changes` outside
this recipe is still not casual: it resets the whole candidate to running,
discarding YOUR uncommitted work too. On the other families, changes affect the **running** config
immediately; on all families nothing survives reboot until `save_startup` ג€”
a revert is just staging the previous value back.
Verify after commit by re-running the relevant context `info` or `show`.
Rollback: stage the inverse commands or restore from the pre-commit backup
(path is in the commit_config output).

**Check documented limits BEFORE staging a bounded/additive write.** When a
write *creates one more of something* ג€” a key, certificate, MQTT/OPC-UA server,
zone, neighbor, SNMP target ג€” the device caps the count, and the cap lives in
the **manual**, not the `?` help. Before staging, grep `manual-<family>/` for
the scaling/limit statement (or the error-reference table) and **state the
limit to the user up front**; if they're already at it, say so and offer the
replace path rather than staging a doomed "add" that only fails at commit.
Known caps: ETX-1p = **1 key pair**, **2 MQTT servers** (manual ֲ§6.9/ֲ§6.15).
This is a hard lesson ג€” the "add a second key" case was discovered at commit
instead of warned in advance; don't repeat it.

