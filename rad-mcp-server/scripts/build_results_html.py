"""Render tests/eval-coverage-report.json as a self-contained tests/RESULTS.html.

Same data as build_results_md.py, styled as a standalone page — IBM Plex
fonts (scripts/assets/fonts/) embedded as base64 @font-face data URIs, no
external requests at view time. Zero device I/O.

Usage: python scripts/build_results_html.py
"""
import base64
import json
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parents[1]
FONTS = Path(__file__).resolve().parent / "assets" / "fonts"
results = json.loads((REPO / "tests/eval-coverage-report.json").read_text(encoding="utf-8"))

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
    rep = cases[0]
    rows.append({
        "num": source_row,
        "category": rep["category"],
        "cli_path": rep["cli_path"],
        "show_command": rep["show_command"],
        "full_cli": rep["expected_cli_command"],
        "classic_prompts": [c["prompt"] for c in cases if c["prompt_type"] == "classic"],
        "implicit_prompts": [c["prompt"] for c in cases if c["prompt_type"] == "implicit"],
        "t5_prompt": next((c["wrapped_prompt"] for c in cases if c["prompt_type"] == "classic"), cases[0]["wrapped_prompt"]),
        "t1": rep["prior_test_results"]["test1_baseline"] or "",
        "t2": rep["prior_test_results"]["test2_post_training"] or "",
        "t3": rep["prior_test_results"]["test3_optimized_prompts"] or "",
        "verdict": PASS_FAIL[rep["coverage"]],
        "reason": reason_for(rep),
        "detail": rep["detail"],
        "prior_comments": (rep["prior_comments"] or "").strip(),
    })
rows.sort(key=lambda r: r["num"])

n_pass = sum(1 for r in rows if r["verdict"] == "PASS")
n_fail_found = sum(1 for r in rows if r["verdict"] == "FAIL" and r["reason"] == "FOUND")
n_fail_license = sum(1 for r in rows if r["verdict"] == "FAIL" and r["reason"] == "LICENSE")
n_fail_missing = sum(1 for r in rows if r["verdict"] == "FAIL" and r["reason"] == "MISSING")
n_fail = n_fail_found + n_fail_license + n_fail_missing


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def font_b64(filename):
    return base64.b64encode((FONTS / filename).read_bytes()).decode("ascii")


MONO400 = font_b64("ibm-plex-mono-400.woff2")
MONO500 = font_b64("ibm-plex-mono-500.woff2")
MONO600 = font_b64("ibm-plex-mono-600.woff2")
SANS400 = font_b64("ibm-plex-sans-400.woff2")
COND600 = font_b64("ibm-plex-sans-condensed-600.woff2")
COND700 = font_b64("ibm-plex-sans-condensed-700.woff2")

PILL_CLASS = {"PASS": "pill pill--pass", "FAIL": "pill pill--fail",
              "FOUND": "pill pill--found", "LICENSE": "pill pill--license",
              "MISSING": "pill pill--missing"}
DOT_CLASS = {"PASS": "dot dot--pass", "PASS*": "dot dot--pass",
             "FAIL": "dot dot--fail", "FAIL*": "dot dot--fail", "": "dot"}


def t_dot(val):
    if not val:
        return '<span class="tmini tmini--empty">—</span>'
    cls = DOT_CLASS.get(val, "dot")
    return f'<span class="tmini"><span class="{cls}"></span>{esc(val)}</span>'


def pill(val):
    if not val:
        return ""
    cls = PILL_CLASS.get(val, "pill")
    return f'<span class="{cls}">{esc(val)}</span>'


row_html = []
for r in rows:
    stripe = "stripe--pass" if r["verdict"] == "PASS" else "stripe--fail"
    comment_html = (f'<div class="comment">{esc(r["prior_comments"])}</div>'
                     if r["prior_comments"] else "")
    classic_cell = "<br>".join(esc(x) for x in r["classic_prompts"]) or "&mdash;"
    implicit_cell = "<br>".join(esc(x) for x in r["implicit_prompts"]) or "&mdash;"
    row_html.append(f'''
      <tr class="{stripe}">
        <td class="num">{r["num"]}</td>
        <td class="cat">{esc(r["category"])}</td>
        <td class="code code--small">{esc(r["show_command"])}</td>
        <td class="prompt">{classic_cell}</td>
        <td class="prompt">{implicit_cell}</td>
        <td class="tcol">{t_dot(r["t1"])}</td>
        <td class="tcol">{t_dot(r["t2"])}</td>
        <td class="tcol">{t_dot(r["t3"])}</td>
        <td class="verdict">{pill(r["verdict"])}</td>
        <td class="reason">{pill(r["reason"])}</td>
        <td class="detail">{esc(r["detail"])}{comment_html}</td>
      </tr>''')

HTML = f'''<title>RAD CLI vs Fusion CLI — STR coverage results</title>
<style>
@font-face {{ font-family: 'Plex Mono'; font-weight: 400; font-style: normal;
  src: url(data:font/woff2;base64,{MONO400}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Plex Mono'; font-weight: 500; font-style: normal;
  src: url(data:font/woff2;base64,{MONO500}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Plex Mono'; font-weight: 600; font-style: normal;
  src: url(data:font/woff2;base64,{MONO600}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Plex Sans'; font-weight: 400; font-style: normal;
  src: url(data:font/woff2;base64,{SANS400}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Plex Cond'; font-weight: 600; font-style: normal;
  src: url(data:font/woff2;base64,{COND600}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Plex Cond'; font-weight: 700; font-style: normal;
  src: url(data:font/woff2;base64,{COND700}) format('woff2'); font-display: swap; }}

:root {{
  --bg: #eef1ee;
  --surface: #ffffff;
  --surface-2: #f5f7f4;
  --ink: #1c2621;
  --ink-soft: #55645c;
  --ink-faint: #8a9690;
  --line: #d7ddd6;
  --accent: #c65a1f;
  --accent-soft: #f3e3d3;
  --pass: #1f7a4f;
  --pass-soft: #dcefe3;
  --fail: #b23a3a;
  --fail-soft: #f6dede;
  --license: #a8621a;
  --license-soft: #f2e2cd;
  --found: #8a6d0f;
  --found-soft: #f1e7c2;
  --shadow: 0 1px 2px rgba(28,38,33,.06), 0 8px 24px -12px rgba(28,38,33,.18);
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #12181a;
    --surface: #182120;
    --surface-2: #1d2726;
    --ink: #e8ece7;
    --ink-soft: #a3b0aa;
    --ink-faint: #718079;
    --line: #2a3532;
    --accent: #e2894c;
    --accent-soft: #3a2a1c;
    --pass: #57bb87;
    --pass-soft: #1c3327;
    --fail: #e17d76;
    --fail-soft: #3a2323;
    --license: #dba053;
    --license-soft: #3a2c19;
    --found: #d9c25a;
    --found-soft: #362f16;
    --shadow: 0 1px 2px rgba(0,0,0,.3), 0 8px 24px -12px rgba(0,0,0,.5);
  }}
}}
:root[data-theme="dark"] {{
  --bg: #12181a; --surface: #182120; --surface-2: #1d2726; --ink: #e8ece7;
  --ink-soft: #a3b0aa; --ink-faint: #718079; --line: #2a3532; --accent: #e2894c;
  --accent-soft: #3a2a1c; --pass: #57bb87; --pass-soft: #1c3327; --fail: #e17d76;
  --fail-soft: #3a2323; --license: #dba053; --license-soft: #3a2c19;
  --found: #d9c25a; --found-soft: #362f16;
  --shadow: 0 1px 2px rgba(0,0,0,.3), 0 8px 24px -12px rgba(0,0,0,.5);
}}
:root[data-theme="light"] {{
  --bg: #eef1ee; --surface: #ffffff; --surface-2: #f5f7f4; --ink: #1c2621;
  --ink-soft: #55645c; --ink-faint: #8a9690; --line: #d7ddd6; --accent: #c65a1f;
  --accent-soft: #f3e3d3; --pass: #1f7a4f; --pass-soft: #dcefe3; --fail: #b23a3a;
  --fail-soft: #f6dede; --license: #a8621a; --license-soft: #f2e2cd;
  --found: #8a6d0f; --found-soft: #f1e7c2;
  --shadow: 0 1px 2px rgba(28,38,33,.06), 0 8px 24px -12px rgba(28,38,33,.18);
}}

* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; background: var(--bg); }}
body {{
  font-family: 'Plex Sans', ui-sans-serif, system-ui, sans-serif;
  color: var(--ink);
  padding: clamp(20px, 4vw, 56px);
  line-height: 1.5;
}}
.wrap {{ max-width: none; width: 100%; margin: 0; display: flex; flex-direction: column; gap: 28px; }}

.eyebrow {{
  font-family: 'Plex Cond', sans-serif; font-weight: 700; font-size: 12.5px;
  letter-spacing: .12em; text-transform: uppercase; color: var(--accent);
}}
h1 {{
  font-family: 'Plex Cond', sans-serif; font-weight: 700;
  font-size: clamp(26px, 3.4vw, 38px); line-height: 1.12; margin: 6px 0 0;
  text-wrap: balance; letter-spacing: -.01em;
}}
.scope {{
  color: var(--ink-soft); font-size: 14.5px; max-width: 68ch; margin: 12px 0 0;
}}
.scope b {{ color: var(--ink); font-weight: 500; }}

.card {{
  background: var(--surface); border-radius: 10px;
}}

.summary {{ padding: 22px 26px; display: flex; flex-wrap: wrap; gap: 28px; align-items: stretch; }}
.stat {{ display: flex; flex-direction: column; gap: 4px; min-width: 120px; }}
.stat-label {{
  font-family: 'Plex Cond', sans-serif; font-size: 11.5px; letter-spacing: .1em;
  text-transform: uppercase; color: var(--ink-faint);
}}
.stat-value {{
  font-family: 'Plex Mono', monospace; font-weight: 600; font-size: 30px;
  font-variant-numeric: tabular-nums; line-height: 1;
}}
.stat-value.v-pass {{ color: var(--pass); }}
.stat-value.v-fail {{ color: var(--fail); }}
.stat-sub {{ font-size: 12.5px; color: var(--ink-soft); }}
.divider {{ width: 1px; background: var(--line); align-self: stretch; margin: 2px 0; }}
.breakdown {{ display: flex; flex-direction: column; gap: 8px; justify-content: center; }}
.breakdown-row {{ display: flex; align-items: baseline; gap: 10px; font-size: 13.5px; }}
.breakdown-row .pill {{ min-width: 66px; text-align: center; }}
.breakdown-row .n {{
  font-family: 'Plex Mono', monospace; font-weight: 500; font-variant-numeric: tabular-nums;
  color: var(--ink-soft);
}}
.breakdown-row .why {{ color: var(--ink-faint); }}

.pill {{
  display: inline-flex; align-items: center; justify-content: center;
  font-family: 'Plex Mono', monospace; font-weight: 600; font-size: 11.5px;
  letter-spacing: .03em; padding: 3px 9px; border-radius: 5px; line-height: 1.3;
  white-space: nowrap;
}}
.pill--pass {{ background: var(--pass-soft); color: var(--pass); }}
.pill--fail {{ background: var(--fail-soft); color: var(--fail); }}
.pill--found {{ background: var(--found-soft); color: var(--found); }}
.pill--license {{ background: var(--license-soft); color: var(--license); }}
.pill--missing {{ background: var(--fail-soft); color: var(--fail); }}

.legend {{ padding: 20px 26px; display: grid; gap: 14px; grid-template-columns: repeat(3, 1fr); }}
.legend dt {{
  font-family: 'Plex Cond', sans-serif; font-weight: 600; font-size: 13px;
  letter-spacing: .02em; color: var(--ink); margin: 0 0 4px;
}}
.legend dd {{ margin: 0; font-size: 13px; color: var(--ink-soft); }}
.legend code {{ font-family: 'Plex Mono', monospace; font-size: 12px; }}
@media (max-width: 860px) {{ .legend {{ grid-template-columns: 1fr; }} }}

.table-card {{ overflow: hidden; }}
.table-scroll {{ overflow-x: auto; }}
table {{ width: 100%; border-collapse: collapse; font-size: 13px; table-layout: fixed; }}
col.c-num {{ width: 3.4%; }}
col.c-cat {{ width: 5.5%; }}
col.c-show {{ width: 9%; }}
col.c-prompt {{ width: 14%; }}
td.prompt {{ font-size: 12px; line-height: 1.45; }}
col.c-t {{ width: 3.6%; }}
col.c-t5 {{ width: 5%; }}
col.c-reason {{ width: 7%; }}
col.c-detail {{ width: 22%; }}
thead th {{
  position: sticky; top: 0; background: var(--surface-2); z-index: 1;
  text-align: left; font-family: 'Plex Cond', sans-serif; font-weight: 600;
  font-size: 11px; letter-spacing: .06em; text-transform: uppercase;
  color: var(--ink-faint); padding: 11px 12px; border-bottom: 1px solid var(--line);
}}
tbody td {{ padding: 10px 12px; border-bottom: 1px solid var(--line); vertical-align: top; overflow-wrap: anywhere; }}
tbody tr {{ border-left: 3px solid transparent; }}
tbody tr.stripe--pass {{ border-left-color: var(--pass); }}
tbody tr.stripe--fail {{ border-left-color: var(--fail); }}
tbody tr:hover {{ background: var(--surface-2); }}
tbody tr:last-child td {{ border-bottom: none; }}

td.num {{
  font-family: 'Plex Mono', monospace; color: var(--ink-faint); font-variant-numeric: tabular-nums;
  white-space: nowrap;
}}
td.cat {{
  font-family: 'Plex Cond', sans-serif; font-size: 10.5px; letter-spacing: .04em;
  text-transform: uppercase; color: var(--ink-soft);
}}
td.code {{ font-family: 'Plex Mono', monospace; font-size: 12.5px; }}
td.code--small {{ font-size: 10.5px; line-height: 1.35; }}
td.code--muted {{ color: var(--ink-soft); }}
td.detail {{ color: var(--ink-soft); font-size: 12.5px; }}
.comment {{ margin-top: 5px; font-style: italic; color: var(--ink-faint); font-size: 12px; }}

.tmini {{ display: inline-flex; align-items: center; gap: 5px; font-size: 12px; color: var(--ink-soft); white-space: nowrap; }}
.tmini--empty {{ color: var(--ink-faint); }}
.dot {{ width: 7px; height: 7px; border-radius: 50%; background: var(--ink-faint); flex: none; }}
.dot--pass {{ background: var(--pass); }}
.dot--fail {{ background: var(--fail); }}

footer {{ color: var(--ink-faint); font-size: 12px; padding: 4px 2px 0; }}
footer a {{ color: var(--accent); }}
</style>

<div class="wrap">
  <div>
    <div class="eyebrow">rad-cli-operations skill · knowledge-coverage eval</div>
    <h1>RAD CLI failures (T1&ndash;T3) vs Fusion CLI (T5)</h1>
    <p class="scope">
      <b>Scope:</b> <code>ETX-2i_Show_Commands_enhanced.xlsx</code>, sheet <code>STR</code>,
      has 182 total rows. This report covers only the <b>35 rows</b> a separate, external
      testing app/process marked <b>Test3 FAIL</b> when it originally generated that
      spreadsheet &mdash; the other 147 rows, where that app&rsquo;s own Test3 already
      passed, are not analyzed here.
    </p>
  </div>

  <section class="card summary">
    <div class="stat">
      <span class="stat-label">Fusion CLI (T5) &middot; Pass</span>
      <span class="stat-value v-pass">{n_pass}/35</span>
      <span class="stat-sub">answers correctly from the reference alone</span>
    </div>
    <div class="divider"></div>
    <div class="stat">
      <span class="stat-label">Fusion CLI (T5) &middot; Fail</span>
      <span class="stat-value v-fail">{n_fail}/35</span>
      <span class="stat-sub">not confirmed &mdash; see reason breakdown</span>
    </div>
    <div class="divider"></div>
    <div class="breakdown">
      <div class="breakdown-row">{pill('FOUND')}<span class="n">{n_fail_found}/35</span><span class="why">navigation known, exact syntax unconfirmed</span></div>
      <div class="breakdown-row">{pill('LICENSE')}<span class="n">{n_fail_license}/35</span><span class="why">device-confirmed license gate, no code fix closes it</span></div>
      <div class="breakdown-row">{pill('MISSING')}<span class="n">{n_fail_missing}/35</span><span class="why">command genuinely not found at the claimed context</span></div>
    </div>
  </section>

  <section class="card legend">
    <div>
      <dt>T1 / T2 / T3</dt>
      <dd>Three prior test rounds against the real device, each already PASS/FAIL,
        carried through unchanged from the source spreadsheet. Run by
        <b>RAD CLI</b> &mdash; a prior AI/tool &mdash; not by this project. (A T4
        &ldquo;Post-Training Re-test&rdquo; column also existed but is omitted here.)</dd>
    </div>
    <div>
      <dt>Fusion CLI (T5)</dt>
      <dd>The next round in that lineage, run by <b>this project</b> instead: does the
        <code>rad-cli-operations</code> skill&rsquo;s harvested etx2 CLI reference
        actually contain the row&rsquo;s expected command? Zero device I/O either way.</dd>
    </div>
    <div>
      <dt>Reason (on FAIL)</dt>
      <dd><b>FOUND</b> &mdash; path is real, leaf unconfirmed. <b>LICENSE</b> &mdash;
        device refused with &ldquo;License required.&rdquo; <b>MISSING</b> &mdash;
        command not found anywhere at the claimed context.</dd>
    </div>
  </section>

  <section class="card table-card">
    <div class="table-scroll">
      <table>
        <colgroup>
          <col class="c-num"><col class="c-cat"><col class="c-show">
          <col class="c-prompt"><col class="c-prompt"><col class="c-t"><col class="c-t"><col class="c-t">
          <col class="c-t5"><col class="c-reason"><col class="c-detail">
        </colgroup>
        <thead>
          <tr>
            <th>#</th><th>Category</th><th>Show Command</th>
            <th>RAD CLI classic prompt (T1&ndash;T3)</th>
            <th>RAD CLI implicit variants (T1&ndash;T3)</th>
            <th>T1</th><th>T2</th><th>T3</th>
            <th>Fusion (T5)</th><th>Reason</th><th>Detail</th>
          </tr>
        </thead>
        <tbody>{"".join(row_html)}
        </tbody>
      </table>
    </div>
  </section>

  <section class="card">
    <p><b>Prompt columns:</b> the phrasings RAD CLI (T1&ndash;T3) was driven with.
      <b>Fusion (T5) used no prompt</b> &mdash; its verdict is a mechanical lookup of the
      row&rsquo;s expected command in the harvested reference, identical for every
      phrasing (0 mixed rows). A per-phrasing end-to-end round (each wrapped as
      &ldquo;abayev, &lt;phrasing&gt; on etx2i&rdquo; to a live agent) is prepared in the
      dataset but not yet run.</p>
  </section>

  <footer>35 rows &middot; generated from <code>tests/eval-coverage-report.json</code> &middot; see <code>tests/eval-report.md</code> for full method &middot; zero device execution</footer>
</div>
'''

out = REPO / "tests" / "RESULTS.html"
out.write_text(HTML, encoding="utf-8")
print(f"wrote {out} ({len(rows)} rows, {len(HTML)} chars)")
