"""Render tests/eval-coverage-report.json as tests/RESULTS.md.

RAD CLI (T1-T3, a prior AI/tool's three test rounds) vs Fusion CLI (T5, this
project's single knowledge-coverage check) for the 35 Test3-FAIL rows from
the source spreadsheet. Zero device I/O — see scripts/check_eval_coverage.py
(run that first) and tests/eval-report.md for full method.

Usage: python scripts/build_results_md.py
"""
import json
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parents[1]
results = json.loads((REPO / "tests/eval-coverage-report.json").read_text(encoding="utf-8"))

# Fusion CLI's own verdict, in the same PASS/FAIL vocabulary as T1-T3 (which
# are RAD CLI's — the prior AI/tool's — test rounds, not ours). When FAIL,
# the reason tag says which of three states caused it: FOUND (the command's
# context/navigation path is real and harvested, just not independently
# confirmed at the exact leaf — no live instance existed at harvest time),
# LICENSE (harvester's own diagnostic probe got a device-confirmed "License
# required" refusal — not fixable by any code change), or MISSING (the
# command was not found anywhere at the claimed context).
PASS_FAIL = {
    "FOUND": "PASS",
    "FOUND_IN_LEVEL_LISTING": "PASS",
    "CONTEXT_EXISTS_NOT_ENTERED": "FAIL",
    "CONTEXT_ENTERED_COMMAND_MISSING": "FAIL",
}
REASON_TAG = {
    "CONTEXT_EXISTS_NOT_ENTERED": "FOUND",
    "CONTEXT_ENTERED_COMMAND_MISSING": "MISSING",
}


def reason_for(rep):
    tag = REASON_TAG.get(rep["coverage"])
    if tag == "FOUND" and "license required" in rep["detail"].lower():
        return "LICENSE"
    return tag


by_row = defaultdict(list)
for r in results:
    by_row[r["source_row"]].append(r)

rows = []
for source_row, cases in by_row.items():
    # coverage is uniform per row (verified) -- take the first case as representative
    rep = cases[0]
    n_classic = sum(1 for c in cases if c["prompt_type"] == "classic")
    n_implicit = sum(1 for c in cases if c["prompt_type"] == "implicit")
    classic_prompts = [c["prompt"] for c in cases if c["prompt_type"] == "classic"]
    implicit_prompts = [c["prompt"] for c in cases if c["prompt_type"] == "implicit"]
    rows.append({
        "num": source_row,
        "category": rep["category"],
        "cli_path": rep["cli_path"],
        "show_command": rep["show_command"],
        "full_cli": rep["expected_cli_command"],
        "classic_prompts": classic_prompts,
        "implicit_prompts": implicit_prompts,
        "t5_prompt": next((c["wrapped_prompt"] for c in cases if c["prompt_type"] == "classic"), cases[0]["wrapped_prompt"]),
        "t1": rep["prior_test_results"]["test1_baseline"],
        "t2": rep["prior_test_results"]["test2_post_training"],
        "t3": rep["prior_test_results"]["test3_optimized_prompts"],
        "n_prompts": f"{n_classic}c+{n_implicit}i",
        "verdict": PASS_FAIL[rep["coverage"]],
        "reason": reason_for(rep),
        "detail": rep["detail"],
        "prior_comments": rep["prior_comments"] or "",
    })

rows.sort(key=lambda r: r["num"])

n_pass = sum(1 for r in rows if r["verdict"] == "PASS")
n_fail_found = sum(1 for r in rows if r["verdict"] == "FAIL" and r["reason"] == "FOUND")
n_fail_license = sum(1 for r in rows if r["verdict"] == "FAIL" and r["reason"] == "LICENSE")
n_fail_missing = sum(1 for r in rows if r["verdict"] == "FAIL" and r["reason"] == "MISSING")
n_fail = n_fail_found + n_fail_license + n_fail_missing

COLOR = {"PASS": "green", "FAIL": "red", "FOUND": "yellow", "MISSING": "red",
         "LICENSE": "orange"}


def colorize(val):
    if not val:
        return ""
    base = val.rstrip("*")  # PASS* / FAIL* keep the asterisk, still colored
    color = COLOR.get(base)
    if not color:
        return val
    return f'<span style="color:{color}">{val}</span>'


lines = [
    "# RESULTS — RAD CLI failures (T1-3) + Fusion CLI (T5)",
    "",
    "**Scope:** `ETX-2i_Show_Commands_enhanced.xlsx`, sheet `STR`, has 182",
    "total rows. This report covers ONLY the 35 rows that a separate,",
    "external testing app/process marked as **Test3 FAIL** when it originally",
    "generated that spreadsheet — the other 147 rows (where that app's own",
    "Test3 passed) are not analyzed here at all.",
    "",
    "## Fusion CLI (T5) summary",
    "",
    "Base is 35, not 182: this counts only the rows the original testing",
    "app/process marked Test3 FAIL — it says nothing about the other 147",
    "rows in `STR` that app already passed, which were never re-checked here.",
    "",
    "| Result | Reason | Count |",
    "|---|---|---|",
    f"| {colorize('PASS')} |  | {n_pass}/35 |",
    f"| {colorize('FAIL')} | {colorize('FOUND')} | {n_fail_found}/35 |",
    f"| {colorize('FAIL')} | {colorize('LICENSE')} | {n_fail_license}/35 |",
    f"| {colorize('FAIL')} | {colorize('MISSING')} | {n_fail_missing}/35 |",
    f"| {colorize('FAIL')} | **total** | {n_fail}/35 |",
    "",
    "## Legend",
    "",
    "- **T1 / T2 / T3** — three separate prior test rounds against the real",
    "  device, each already PASS/FAIL, carried through unchanged from the",
    "  original spreadsheet. These were run by **RAD CLI** (a prior AI/tool),",
    "  *not* by this project. (A T4 \"Post-Training Re-test\" column also",
    "  existed in the source sheet but is omitted here — not relevant to this",
    "  report.)",
    "- **Fusion CLI (T5)** — the next round in that same test lineage, but",
    "  run by **Fusion CLI** (this project) instead: does our",
    "  **rad-cli-operations** skill's harvested etx2 CLI reference actually",
    "  contain the row's expected command? `PASS` = yes, confirmed. `FAIL` =",
    "  not confirmed — zero device I/O either way; see `tests/eval-report.md`",
    "  for full method.",
    "- **Reason** (only shown on FAIL) — `FOUND`: the command's",
    "  context/menu path is real and harvested, just not independently",
    "  confirmed at the exact leaf (no live instance of that context existed",
    "  when the reference was harvested). `LICENSE`: the harvester's own",
    "  diagnostic probe got a device-confirmed \"License required\" refusal —",
    "  not fixable by any code change, needs a real license on the unit.",
    "  `MISSING`: the command was not found anywhere at the claimed context",
    "  at all.",
    "",
    "| # | Category | Show Command | RAD CLI classic prompt (T1-T3) | RAD CLI implicit variants (T1-T3) | T1 | T2 | T3 | Prior comment | **Fusion (T5)** | **Reason** | **Detail** |",
    "|---|---|---|---|---|---|---|---|---|---|---|---|",
]
for r in rows:
    def esc(s):
        return str(s).replace("|", "\\|").replace("\n", " ")
    classic = "<br>".join(esc(x) for x in r["classic_prompts"]) or "—"
    implicit = "<br>".join(esc(x) for x in r["implicit_prompts"]) or "—"
    lines.append(
        f"| {r['num']} | {esc(r['category'])} | `{esc(r['show_command'])}` | "
        f"{classic} | {implicit} | {colorize(r['t1'])} | "
        f"{colorize(r['t2'])} | {colorize(r['t3'])} | {esc(r['prior_comments'])[:60]} | "
        f"{colorize(r['verdict'])} | {colorize(r['reason'])} | {esc(r['detail'])[:120]} |"
    )

lines += [
    "",
    "Prompt columns: the phrasings RAD CLI (T1-T3) was driven with — classic "
    "(bold in the source) and implicit variants (one per line). "
    "**Fusion (T5) used NO prompt**: its verdict is a mechanical lookup of the "
    "row's expected command in the harvested reference, so it is identical for "
    "every phrasing (verified: 0 mixed rows). A per-phrasing end-to-end round "
    "(each wrapped as \"abayev, <phrasing> on etx2i\" to a live agent) is "
    "prepared in the dataset but not yet run.",
]

out = REPO / "tests" / "RESULTS.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(f"wrote {out} ({len(rows)} rows)")
