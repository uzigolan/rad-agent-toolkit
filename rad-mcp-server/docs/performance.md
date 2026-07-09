# Performance record

Running log of measured performance for the three things that matter: **CLI
harvest** (per family), **manual ingestion**, and **using the
`rad-cli-operations` skill day to day** — the last one is the most important,
since it's what every real interaction pays for. Numbers are quoted from tool
output, real timed re-runs (`time.monotonic()`), and
`~/.claude/hooks/skill-metrics.log` — not estimates.

**One table shape used throughout**, so the three are comparable:

| Stage (local, zero device I/O) | Device access (SSH round trip) | Total | Notes |
|---|---|---|---|

- **Stage** = work done before/without touching the device: grepping the
  harvested reference, deciding the command, formatting the answer.
- **Device access** = actual wall-clock time inside an SSH round trip
  (connect, or a command over an already-open session).
- **Excluded everywhere**: the time a human takes to answer the [Execution
  gate](../skills/rad-cli-operations/SKILL.md) confirmation ("run this on the
  device now?"). That's user think-time, not system performance — none of
  the numbers below include it; each was measured with a scripted,
  non-interactive re-run of the same operation.

## 1. Using the `rad-cli-operations` skill — the main event

Real timed re-run (2026-07-09) of the two things a typical skill answer does:
look up syntax in the harvested reference (stage), then touch the device to
confirm/fetch state (device access).

| Stage (local grep) | Device access (SSH) | Total | Notes |
|---|---|---|---|
| **<0.001 s** | 6.875 s | 6.876 s | Cold: fresh process, first call — pays SSH connect+auth |
| **<0.001 s** | 0.328 s | 0.328 s | Warm: 2nd call, same session — the persistent-session backend's payoff |

**The stage is free; the device is everything.** Grepping a 6,600-line
harvested reference for a context header takes under a millisecond —
unmeasurable at this resolution. Once a device round-trip is needed, cold
SSH connect+auth (6.875s) dominates completely; a warm call on an
already-open session (0.328s) is **~21x faster** than cold. This is exactly
why the persistent-session backend (§3 below) matters more for this skill
than anywhere else in the toolkit — it's invoked on nearly every RAD-related
message, so paying the cold-connect cost once per *session* instead of once
per *call* is the highest-leverage fix available.

**Practical implication:** the live MCP server currently pays the cold cost
once per device per Claude Code session (not per call) — but a *new* device
(like `etx2i` before its first reload) pays it again on the fresh-process
fallback path every time, since that path has no persistent session. This is
the concrete cost of the credential-staleness gap flagged elsewhere in this
project: each `etx2i` fallback call this session paid ~6-7s it wouldn't have
paid through the live tool.

**Skill-run totals** (from `skill-metrics.log` — whole-turn duration,
includes stage + device access + response generation, still excludes user
confirm-wait since the hook only spans model-turn time):

| Timestamp | Skill | Duration | Tokens in | Tokens out | Cache read | Cache write |
|---|---|---|---|---|---|---|
| 2026-07-07 15:57:58 | `/rad-load-manual` | 142s | 1,349 | 11,403 | 8,629,494 | 27,151 |
| 2026-07-07 16:13:08 | rad-cli-operations (persona) | 48s | 2,774 | 4,314 | 551,440 | 1,358,650 |
| 2026-07-07 16:26:20 | rad-cli-operations (persona) | 70s | 14 | 7,027 | 3,426,023 | 9,122 |
| 2026-07-09 12:35:32 | rad-cli-operations (persona) | 165s | 52 | 20,114 | 16,627,154 | 37,922 |
| 2026-07-09 12:44:43 | rad-cli-operations (persona) | 28s | 8 | 2,032 | 2,601,640 | 3,000 |
| 2026-07-09 13:05:59 | rad-cli-operations (persona) | 41s | 10 | 3,534 | 3,500,017 | 3,167 |
| 2026-07-09 13:08:48 | rad-cli-operations (persona) | 84s | 16 | 3,275 | 5,622,997 | 4,922 |
| 2026-07-09 13:14:23 | rad-cli-operations (persona) | 16s | 4 | 1,374 | 1,431,992 | 2,636 |
| 2026-07-09 13:48:49 | rad-cli-operations (persona) | 31s | 8 | 3,356 | 3,129,514 | 14,486 |
| **Total (9 captured runs)** | | **625s (~10.4 min)** | **4,235** | **56,429** | **45,520,271** | **1,461,056** |

**Coverage caveat:** only runs triggered by an explicit `/command` or an
Abayev/Noam persona address are captured — plain-language turns without
either trigger are not logged, so this table undercounts total session
activity. Live/current data: `cat ~/.claude/hooks/skill-metrics.log`. Also
surfaced via the `statusLine` (latest run) and in-reply summaries.

**Fix applied (2026-07-09):** the 165s/20,114-output-token outlier above was
diagnosed as two things: an over-long response, and a redundant live
`cli_help` call re-confirming what the harvested reference already answered
— i.e. an avoidable extra "device access" hop on top of an already-answered
question. Both are now addressed by two configurable modes in `SKILL.md` —
*"Response & verification modes"* — defaulting to `concise` responses and
`trust-reference` lookups (skip the redundant device round-trip once the
reference already gives a complete, fresh answer). A separate later addition,
the **Execution gate** (ask "run this on the device now?" and stop, instead
of continuing to explain/verify), also shortens turns structurally. Either
mode reverts on request for the rest of a session.

**Re-measured (4 more runs, 2026-07-09 13:05-13:48):** 41s/84s/16s/31s,
output 3,534/3,275/1,374/3,356 tokens — all well under the 165s/20,114-token
outlier, none close to being a new one. Directionally consistent with the
fix, but an honest caveat: this isn't a controlled A/B test — the new runs
are different question types (DMVPN config, not a repeat of the outlier's
exact task), and three separate behavior changes (concise mode,
trust-reference mode, the execution gate) landed in the same window, so the
improvement can't be attributed to any single one of them individually.

## 2. CLI harvest performance (per family)

`scripts/harvest_cli.py` connects once (**stage**), then crawls the device's
entire `?`-help tree as hundreds of sequential command round-trips (**device
access**) — there is no per-question gate here since it's an unattended
background job, not an interactive skill answer.

| Stage (SSH connect+auth, one-time) | Device access (per capture, representative) | Notes |
|---|---|---|
| 6.516 s | 0.372 s/capture (5-capture sample) | Real timed re-run, 2026-07-09, lab-sf1p |

A full harvest's duration is therefore ≈ 6.5s stage + (captures × ~0.37s) —
e.g. etx2's 868 captures ≈ 6.5s + 321s ≈ 5.5 min at this per-capture rate;
the actual completed run took 12.2 min, reflecting slower contexts (large
`info` dumps, parameterized-context create+capture+rollback triads costing
3+ round-trips each) that a flat per-capture average doesn't show.

| Family | Run | Captures | Duration | Notes |
|---|---|---|---|---|
| **secflow** | full (2026-07-06, pre-speedup) | 336 | ~11 min | first-ever harvest, 44 contexts |
| secflow | full (post prompt-anchoring fix) | 466 (0 old→466 new) | 7.7 min | validation: **ADDED 0 / REMOVED 0 / CHANGED 8** — speedup changed timing, not content |
| secflow | full (parameterized-context entry added) | 547 (466→547) | 8.5 min | **ADDED 81** — NAME-placeholder sections |
| secflow | branch `configure crypto` | 65 (469 total) | 2.9 min | targeted fix validation |
| secflow | branch `configure router` | 130 (**674 total, final**) | 2.0 min | fixed the bug hiding `router 1`'s subtree |
| **etx1p** | full (first-ever) | **531 (final)** | 8.0 min | Device3, Sw 6.5.0.43 |
| **etx2** | full (first-ever, aborted attempt) | ~31 before kill | — | killed by a launch-backgrounding mistake; device left clean, no residue |
| etx2 | full (first-ever, completed) | **868 (final)** | 12.2 min | ETX-2I, Sw 6.8.5(1.116); tool-reported diff ADDED 11/REMOVED 1/CHANGED 33 against 858 pre-existing records — likely an artifact of the aborted attempt's scratch state, not fully reconciled |

**Throughput held steady across all three families** (~60-70 captures/min),
scaling with tree size rather than degrading on the larger ones:

| Family | Captures | Minutes | Captures/min |
|---|---|---|---|
| secflow | 547 | 8.5 | 64.4 |
| etx1p | 531 | 8.0 | 66.4 |
| etx2 | 868 | 12.2 | 71.1 |

**Final per-family knowledge size:**

| Family | CLI captures | `cli-reference-<family>.md` | Manual chapters | Manual size |
|---|---|---|---|---|
| secflow | 674 | 6,632 lines | 17 | 1,048 KB |
| etx1p | 531 | 5,106 lines | 14 | 960 KB |
| etx2 | 868 | 9,215 lines | 44 | 2,428 KB |

Every temp object (`zzz-hrvst`) created during any harvest rolled back
cleanly; every device verified free of residue after each run.

## 3. Manual ingestion performance

100% local (PDF → markdown) — **stage is the entire operation; device access
is always zero** by construction. Real timed re-run, 2026-07-09. (This section
is timing only — see `docs/manual-quality.md` for per-family ingestion
*quality*: chapter structure, cross-link coverage, and what etx2 specifically
required that etx1p/secflow didn't.)

| Family | Stage (parse+split+write) | Device access | Total |
|---|---|---|---|
| etx1p | 1.141 s | 0 s | 1.141 s |
| secflow | 1.203 s | 0 s | 1.203 s |
| etx2 | 3.078 s | 0 s | 3.078 s (largest PDF: 27.7 MB, 1,576 pages, 44 output chapters) |

| Family | Source PDF | Pages | Chapters out |
|---|---|---|---|
| etx1p | 12.0 MB | 726 | 14 |
| secflow | 12.7 MB | 793 | 17 |
| etx2 | 27.7 MB | 1,576 | 44 (after adaptive-split fix) |

etx2's manual was organized as 3 giant "parts" (up to 1,079 pages) instead of
per-topic chapters; the adaptive splitter (expand any unit >220 pages with
≥3 sub-sections, recursively) fixed this without touching etx1p/secflow —
verified byte-identical chapter counts on those two after the change, and
re-verified identical again during this timing re-run.

## 4. Live tool-call latency (device-bound floor)

Backend rewrite: one persistent SSH session per device (vs. reconnect per
call) + prompt-anchored reads (vs. quiet-period timers). This is the
mechanism behind §1's cold/warm gap. Measured warm, SF-1p over lab LAN:

| Operation | Before | After |
|---|---|---|
| Health ping | ~6-10 s | **0.14 s** |
| `cli_help`, 3 contexts deep | ~12 s | **0.7 s** |
| Root-level help | ~8 s | **0.4 s** |
| `get_config` | ~13 s | ~7-8 s (device-bound; export generation itself is the floor) |

## Keeping this current

- Re-run `/rad-harvest <device>` after a firmware upgrade or when adding a
  family — append its `Done:` line and diff to §2.
- Re-run `/rad-load-manual` when a manual updates — append to §3.
- Skill-run rows accumulate automatically in `skill-metrics.log`; re-copy the
  tail into §1 periodically (or read the log directly for live numbers).
- The stage-vs-device-access numbers in §1/§2/§3 are point-in-time re-runs,
  not auto-updating — re-time after any backend change that could move them
  (e.g. a new persistent-session optimization, a different lab network path).
