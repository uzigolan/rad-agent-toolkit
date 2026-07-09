# Eval report: `eval-etx2i-str-test3-fail` knowledge-coverage check

**What this tests:** for the 103 prompts where the source spreadsheet's
Test3 ("Optimized Prompts") failed, does our **harvested etx2 reference**
(`cli-help-etx2.jsonl`) actually contain the expected `show_command` at the
expected `cli_path`? This is a **knowledge-coverage** check — does the
skill's reference have the right answer available at all — not a live test;
per the etx2i override, nothing was executed on the device. Zero device I/O
was used to produce this report; every result comes from grepping/walking the
already-harvested reference.

Builder: `scripts/eval_coverage_check.py`-equivalent logic (see method below).
Full per-case detail: `tests/eval-coverage-report.json`.

## Results

**Updated across four re-harvests on 2026-07-09** as numeric auto-create was
built out in `scripts/harvest_cli.py`:

1. First harvest with `mep`/`lag`/`pw` allow-listed: `mep` closed, but via a
   real instance that already existed on the device
   (`maintenance-domain 1 maintenance-association 1 > mep 1`), not the new
   create logic. `lag 4`/`pw 64` were correctly picked but refused, falling
   back safely to "not entered" — no gain yet, but proved the mechanism
   doesn't damage anything.
2. Added a diagnostic: on refusal, probe `<name> <idx> ?` (read-only) and
   log what the CLI wanted. Result for `lag`/`pw`/`test`(rfc2544, newly
   added to the allow-list after checking the manual): all three showed
   `<CR>` — meaning the command was already syntactically complete, so
   "needs another argument" was the wrong theory.
3. Capturing the device's *actual* refusal text (not just detecting
   refusal) revealed the real reasons: `lag 4` → `Invalid LAG ID` (the
   CLI's own declared `[1..4]` range is wrong — real max is lower); `test
   9999` → `Test index must be between 1 to 8` (no range was declared at
   all, so the fallback guess was hugely oversized); `pw 64` → `PW type
   must be configured` (this one *does* need a second mandatory argument).
4. Switched from one guess at the top of the range to trying up to 6 free
   indices ascending from the bottom. Result: `lag 1` and `test 1` both
   entered and rolled back cleanly on the first try; `pw` still correctly
   refused at every index with the same "type must be configured" reason
   (a real second-argument gap, not an indexing problem).
5. Extended the same refusal-text capture to string-named creates too (it
   was only wired up for numeric ones) so the harvester's own evidence,
   not just the spreadsheet's comment, could confirm or refute the "twamp
   needs a license" theory. Result: `controller` and `profile` are
   genuinely license-gated (`cli error: License required`, device-confirmed)
   — but `responder` is not; it fails with `parameter or keyword missing or
   wrong` and a usage hint (`responder <name> [<number>] light
   [l2-probe]`), meaning it needs a second argument, same class of gap as
   `pw`, not a license issue.

Verified clean on the live device after every run (fresh-connection
`get_config` grep: zero `zzz-hrvst`, zero `lag`/`pw`/`test` residue at any
tried index).

| Coverage | Count | Meaning |
|---|---|---|
| **FOUND** | 65 (was 50) | Exact command captured at the exact context — the skill would answer this correctly straight from the reference, zero live lookup needed. |
| **CONTEXT_EXISTS_NOT_ENTERED** | 26 (was 41) | The navigation path is real (confirmed in the harvest as a genuine child context) but its *interior* was never captured. Remaining cases: `pw`/`responder` (need a second argument the harvester doesn't supply), `controller`/`profile` (device-confirmed license-gated on the lab unit, see below), and any context with no live instance and not on the allow-list. |
| **CONTEXT_ENTERED_COMMAND_MISSING** | 12 (4 unique) | The context *was* fully harvested, but this specific command isn't there. See breakdown below — most of these are genuine. |

Also fixed a bug in *this checker itself* (not the harvest) along the way:
`show lacp-status ethernet <port>` was truncating to `show lacp-status
ethernet`, which doesn't match the harvest's real bare leaf (`show
lacp-status` — `ethernet <port>` is an optional filter, not part of the
command name). `strip_args` now tries the fuller truncation first and falls
back to dropping one more trailing word only when a placeholder was
present, so a genuinely missing command with no placeholder at all (e.g.
`show report detailed`) is never over-truncated into a false match. Also
fixed the detail message itself: for the `twamp controller > peer` cases it
was reporting `peer` as the blocked token when the walk actually stops at
`controller` first — `peer` is never even reached, so blaming it was wrong.

**`controller`/`profile` under `configure oam twamp` are a device-confirmed
license gate, not a code gap:** the harvester's own diagnostic (not just the
spreadsheet's comment) captured `cli error: License required` on refusal.
No harvester change closes this — it needs a TWAMP license on the lab unit.
`responder`, by contrast, needs a second argument the harvester doesn't
supply — a fixable gap, same class as `pw`.

**103 total, 0 unmapped paths, 0 truly-unknown contexts** — every single
path in this dataset resolved to a real place in the etx2 CLI tree; none
were fabricated by the spreadsheet's author.

## The 4 genuinely missing commands (12 cases)

| `cli_path` | `show_command` | Verdict |
|---|---|---|
| `ETX-2i>` (root) | `show configure service` | **Likely wrong.** Zero hits anywhere in the harvest for this exact string; doesn't match this CLI's context-based syntax pattern (`show <x>` at root doesn't take a `configure` sub-target this way). Same category as the row-10 discrepancy flagged in `tests/README.md`. |
| `ETX-2i>config>router(n)#` | `show nat-statistics` | **Real command, wrong depth.** Confirmed it exists — but under `configure router NAME nat`, not directly under `configure router NAME` as the spreadsheet's `cli_path` claims. A one-hop navigation difference. |
| `ETX-2i>config>test>y1564>generator(n)#` | `show report detailed` | **Confirmed missing**, and not just from a harvest gap — this was live-verified earlier this session: `show ?` at this exact context lists only `status`. This command does not exist here. |
| `ETX-2i>config>test>l3sat>generator(name)>peer(ip)#` | `show summary-report` | **Likely missing** — the harvested peer-level leaf list is `activate`, `peer-profile`, `test-session`, `show status` only; no `show summary-report`. |

Two earlier false positives were caught and fixed before finalizing this
table: `show rib { ipv4 | ipv6 }` and `show alarm-information <source-type>
<alarm-list>` both looked "missing" on first pass because the spreadsheet
embeds argument-choice notation directly in the `show_command` cell — after
stripping that notation, both matched a real, exact leaf capture. Lesson
folded into the matcher, not just this report.

## Classic vs. implicit — coverage gaps are prompt-neutral

| Coverage | Classic | Implicit |
|---|---|---|
| FOUND | 22 | 43 |
| CONTEXT_EXISTS_NOT_ENTERED | 9 | 17 |
| CONTEXT_ENTERED_COMMAND_MISSING | 4 | 8 |

Roughly the same ~1:2 classic:implicit ratio holds across all three buckets
— confirming coverage gaps are a property of **what the harvest captured**,
independent of **how the prompt was phrased**. This is expected: whether a
context's interior got harvested has nothing to do with the natural-language
wording used to ask about it later.

## What this report does *not* test

This is a coverage check, not a full natural-language-understanding eval —
it doesn't verify that a given prompt's wording would actually lead to the
correct command being *selected* from among the ones the skill knows. The
**classic** prompts are close restatements of each command's own
description (e.g. "Show the current system date and time configured on the
device" → `show system-date`) and are low-risk for misinterpretation. The
**implicit** prompts are colloquial ("show me my hardware", "check chassis
temperature") and are exactly what the original Test3 was probing — that
dimension would need either a live sampled run through the skill itself or
a separate, more expensive judged pass; out of scope for this coverage-only
report per the "commands only, don't touch the device" instruction.

## Practical takeaway

- **26 of 103 cases (25%)** still hit a real harvest gap
  (`CONTEXT_EXISTS_NOT_ENTERED`) — down from 41 at the start of this
  session's harvester work. Of what's left: `pw`/`responder` need the
  harvester taught a second argument (`type <psn>` / `[<number>] light
  [l2-probe]`); `controller`/`profile` need an actual TWAMP license on the
  lab unit, not a code change (device-confirmed, not just inferred from the
  spreadsheet); the rest have no live instance and aren't (yet) on the
  numeric auto-create allow-list.
- **Only 3-4 cases are genuine "the command doesn't exist as claimed"** —
  the spreadsheet's ground truth is largely trustworthy; the earlier
  suspicion about `show configure service` (from `tests/README.md`) holds up
  as the most likely real inaccuracy in the source data.
