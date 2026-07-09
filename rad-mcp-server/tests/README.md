# Skill eval datasets

## `eval-etx2i-str-test3-fail.{json,csv}`

**Source:** `<repo-root>/ETX-2i_Show_Commands_enhanced.xlsx`, sheet `STR` — a
prior manual AI-testing log: natural-language prompt → expected CLI command,
tested across 4 rounds (Test1 baseline, Test2 post-training, Test3
optimized-prompts, Test4 post-training retest). Built by
`scripts/build_eval_dataset.py` (re-run it if the spreadsheet gets a new test
round).

**Filter:** only rows where **Test3 ("Optimized Prompts") == FAIL** — cases
that still got the wrong CLI syntax even with tuned prompts. 35 such rows.

**Expansion:** each row's "Suggested AI Prompt" cell holds multiple
phrasings of the same ask, distinguished by **rich-text formatting, not just
line breaks** — the bold run(s) are the "classic" (direct/explicit) prompt;
the non-bold run(s) are "implicit" (colloquial) phrasings, which is what
Test3 "Optimized Prompts" was specifically probing. Each phrasing becomes its
own eval case (tagged `prompt_type: "classic"|"implicit"`), sharing the row's
expected answer — 103 cases total from 35 rows (1 classic + ~2 implicit per
row) — so the dataset tests phrasing robustness the same way Test3 itself did.

Extraction reads the cell's actual bold/non-bold rich-text runs (openpyxl
`rich_text=True`), not a naive line-split — one cell (row 10) had a stray
bold-flagged newline (a formatting slip: Enter pressed while still in bold
mode) sitting between two non-bold lines, which a naive "split by line,
group by run" approach concatenated into one garbled string with no
separator. Fixed by reconstructing lines first (newlines always split,
regardless of which run carries them) and classifying each line by its own
non-whitespace content's bold-state. Verified clean across all 103 cases
(scanned for sentence-boundary-with-no-space patterns — zero hits).

**Case shape:**
```json
{
  "id": "str-10-1",
  "source_row": 10,
  "category": "Root",
  "cli_path": "ETX-2i>",
  "expected_cli_command": "ETX-2i> show configure service",
  "show_command": "show configure service",
  "prompt": "Show all configured services and their current status",
  "wrapped_prompt": "abayev, Show all configured services and their current status on etx2i",
  "device": "etx2i",
  "prior_test_results": { "test1_baseline": "FAIL", ... },
  "prior_comments": "..."
}
```

**How to use:** feed `wrapped_prompt` to the skill (as-is — it's already
addressed to Abayev and names the device, which triggers the skill's
standing `etx2i` override: commands only, never executed) and compare the
response's CLI command against `expected_cli_command`. `prompt` (unwrapped)
is kept for reference / alternate framing.

**Known caveat — expected answers are not all independently verified.**
`expected_cli_command` reflects what the *original spreadsheet* claims is
correct, not necessarily what's confirmed in our own harvested
`cli-reference-etx2.md`. Spot-checked: most show commands in this set do
appear in the harvest (e.g. `show schedule-log`, `show scheduler`, `show
environment`, `show trap-sync` — all found). One exception: row 10's
`show configure service` has **zero hits** in the harvested etx2 reference —
either it's a real command the harvest never captured (a coverage gap, like
the MEF46-LL case), or the spreadsheet's claimed answer is itself wrong. When
a skill answer disagrees with `expected_cli_command`, check the harvested
reference and manual before assuming the skill is at fault — the spreadsheet
is a prior AI's test log, not a verified oracle.

## Coverage check + results

`scripts/check_eval_coverage.py` walks the eval dataset above against the
harvested `cli-help-etx2.jsonl` token-by-token (not fuzzy string matching —
that produced 41 false negatives on the first attempt, since it never
checked `args-noenter`/`args-param` prefixes stored under a parent context
for not-yet-entered children) and classifies each case `FOUND` /
`CONTEXT_EXISTS_NOT_ENTERED` / `CONTEXT_ENTERED_COMMAND_MISSING`, writing
`eval-coverage-report.json`. Zero device I/O — pure reference lookup.

- **`RESULTS.md`** / **`RESULTS.html`** — the 35 Test3-FAIL rows with the
  original spreadsheet's own T1–T3 columns (RAD CLI, a prior AI/tool's three
  test rounds) plus our own single check as **Fusion CLI (T5)**: `PASS`/`FAIL`
  and, on `FAIL`, a `FOUND` (path real, leaf unconfirmed) / `LICENSE`
  (device-confirmed license gate) / `MISSING` (not found anywhere) reason.
  `RESULTS.html` is the same data as a self-contained styled page (fonts in
  `scripts/assets/fonts/`, embedded as base64 data URIs — no external
  requests) — regenerate both by re-running `scripts/check_eval_coverage.py`
  then `scripts/build_results_md.py` / `scripts/build_results_html.py`.
- **`eval-report.md`** — full method, the 4 genuinely-missing commands
  individually verified, and the running log of what closed as
  `scripts/harvest_cli.py`'s numeric-indexed auto-create was built out this
  session (`mep`/`lag`/`test` closed; `pw`/`twamp responder` need a second
  argument the harvester doesn't supply yet; `twamp controller`/`profile`
  are a device-confirmed license gate, not a code fix). See
  `docs/architecture.md`'s harvest section for how the manual layer gates
  which numeric contexts are safe to auto-create in the first place.
