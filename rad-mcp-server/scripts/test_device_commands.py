#!/usr/bin/env python3
"""
Test all 499 extracted commands against the Raviv-Etx2-Telnet device.

Uses the server's own Netmiko infrastructure (credentials from server/.env,
context navigation via "exit all -> context -> command", same as run_show_in_context).
Groups test cases by unique CLI context to minimise navigation overhead.

Usage (run from rad-mcp-server/server/ so rad_mcp is on the path):
  cd rad-mcp-server/server && python ../scripts/test_device_commands.py
  python scripts/test_device_commands.py --only-classic
  python scripts/test_device_commands.py --limit 20

Output:
  tests/eval-etx2-device-results.json
  tests/eval-etx2-device-results.csv
  tests/eval-etx2-device-report.md
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# Add server/ to sys.path so "import rad_mcp" works regardless of cwd
SERVER_DIR = Path(__file__).resolve().parents[1] / "server"
if str(SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(SERVER_DIR))

REPO    = Path(__file__).resolve().parents[1]   # rad-mcp-server/
OUT_DIR = REPO / "tests"
DATASET_JSON = OUT_DIR / "eval-etx2-full-dataset.json"
DEVICE_NAME  = "RavivETX2-SSH"

# ── cli_path → context string ("exit all; <ctx>"; "" = root) ────────────────
CLI_PATH_CONTEXT: dict[str, str] = {
    "ETX-2i>":                                                            "",
    "ETX-2i>file#":                                                       "file",
    "ETX-2i>admin>license#":                                              "admin license",
    "ETX-2i>admin>scheduler#":                                            "admin scheduler",
    "ETX-2i>config>bridge(n)#":                                           "configure bridge 1",
    "ETX-2i>config>chassis#":                                             "configure chassis",
    "ETX-2i>config>mngmnt#":                                              "configure management",
    "ETX-2i>config>mngmnt>radius#":                                       "configure management radius",
    "ETX-2i>config>mngmnt>snmp#":                                         "configure management snmp",
    "ETX-2i>config>oam>cfm#":                                             "configure oam cfm",
    "ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)#":                         "configure oam cfm maintenance-domain 1 maintenance-association 1 mep 1",
    "ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)#":              "configure oam cfm maintenance-domain 1 maintenance-association 1 mep 1 service 1",
    "ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)>service(n)>dest-ne(n)#":   "configure oam cfm maintenance-domain 1 maintenance-association 1 mep 1 service 1 dest-ne 1",
    "ETX-2i>config>oam>twamp>controller(n)#":                             "configure oam twamp controller 1",
    "ETX-2i>config>oam>twamp>controller(n)>peer(ip)#":                    "configure oam twamp controller 1 peer 1.1.1.1",
    "ETX-2i>config>oam>twamp>responder(n)#":                              "configure oam twamp responder 1",
    "ETX-2i>config>port#":                                                "configure port",
    "ETX-2i>config>port>e1(slot/port)#":                                  "configure port ds1 0/1",
    "ETX-2i>config>port>eth(port)#":                                      "configure port ethernet 0/1",
    "ETX-2i>config>port>eth(port)>lldp#":                                 "configure port ethernet 0/1 lldp",
    "ETX-2i>config>port>gfp(n)#":                                         "configure port gfp 1",
    "ETX-2i>config>port>lag(n)#":                                         "configure port lag 1",
    "ETX-2i>config>port>log-mac(n)#":                                     "configure port logical-mac 1",
    "ETX-2i>config>port>pcs(n)#":                                         "configure port pcs 1",
    "ETX-2i>config>port>ppp(n)#":                                         "configure port ppp 1",
    "ETX-2i>config>port>ppp(n)>pppoe#":                                   "configure port ppp 1 pppoe",
    "ETX-2i>config>port>shdsl(slot/port)#":                               "configure port shdsl 0/1",
    "ETX-2i>config>port>vdsl2(slot/port)#":                               "configure port vdsl2 0/1",
    "ETX-2i>config>pwe#":                                                 "configure pwe",
    "ETX-2i>config>pwe>pw(n)#":                                           "configure pwe pw 1",
    "ETX-2i>config>qos>envelope-profile(n)#":                             "configure qos envelope-profile 1",
    "ETX-2i>config>qos>policer-profile(n)#":                              "configure qos policer-profile 1",
    "ETX-2i>config>qos>shaper-profile(name)#":                            "configure qos shaper-profile 1",
    "ETX-2i>config>reporting#":                                           "configure reporting",
    "ETX-2i>config>router(n)#":                                           "configure router 1",
    "ETX-2i>config>router(n)>bgp(n)#":                                    "configure router 1 bgp 1",
    "ETX-2i>config>router(n)>bgp(n)>ipv4-unicast-af>neighbor(ip)#":       "configure router 1 bgp 1 ipv4-unicast-af neighbor 1.1.1.1",
    "ETX-2i>config>router(n)>bgp(n)>ipv6-unicast-af>neighbor(ip)#":       "configure router 1 bgp 1 ipv6-unicast-af neighbor ::1",
    "ETX-2i>config>router(n)>interface(n)#":                              "configure router 1 interface 1",
    "ETX-2i>config>system#":                                              "configure system",
    "ETX-2i>config>system>clock>domain(n)>source(n)#":                    "configure system clock domain 1 source 1",
    "ETX-2i>config>system>clock>recovered(port/ptp)#":                    "configure system clock recovered 0/1",
    "ETX-2i>config>test>l3sat>generator(name)#":                          "configure test l3sat generator 1",
    "ETX-2i>config>test>l3sat>generator(name)>peer(ip)#":                 "configure test l3sat generator 1 peer 1.1.1.1",
    "ETX-2i>config>test>l3sat>responder(name)#":                          "configure test l3sat responder 1",
    "ETX-2i>config>test>rfc2544>test(n)#":                                "configure test rfc2544 test 1",
    "ETX-2i>config>test>y1564>generator(n)#":                             "configure test y1564 generator 1",
    "ETX-2i>config>test>y1564>responder(n)#":                             "configure test y1564 responder 1",
}

ERROR_PATTERNS = [
    "cli error",
    "invalid command",
    "syntax error",
    "unknown command",
    "license required",
]


# ── helpers ──────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--only-classic", action="store_true",
                   help="Test classic prompts only (skip implicit variants)")
    p.add_argument("--limit", type=int, default=0,
                   help="Stop after N test cases (0 = all)")
    return p.parse_args()


def load_dataset(only_classic: bool, limit: int) -> list[dict]:
    if not DATASET_JSON.exists():
        sys.exit(f"ERROR: {DATASET_JSON} not found — run test_all_commands_on_device.py first")
    with open(DATASET_JSON, encoding="utf-8") as f:
        cases: list[dict] = json.load(f)
    if only_classic:
        cases = [c for c in cases if c.get("prompt_type") == "classic"]
    if limit:
        cases = cases[:limit]
    return cases


def extract_show_command(expected: str) -> str:
    """'ETX-2i>config>port# show summary' → 'show summary'"""
    m = re.search(r"(?:#|>)\s*(show\b.+)", expected, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    parts = expected.rsplit(">", 1)
    return parts[-1].strip() if len(parts) > 1 else expected.strip()


# ── main test runner ──────────────────────────────────────────────────────────

def run_tests(cases: list[dict]) -> list[dict]:
    from netmiko import ConnectHandler
    from rad_mcp.inventory import get_device
    from rad_mcp.drivers import get_driver

    dev    = get_device(DEVICE_NAME)
    driver = get_driver(dev.family)
    dtype  = driver.netmiko_device_type + ("_telnet" if dev.transport == "telnet" else "")

    print(f"Connecting to {DEVICE_NAME} ({dev.host}:{dev.port}) [{dtype}] …")
    conn = ConnectHandler(
        device_type=dtype,
        host=dev.host,
        port=dev.port,
        username=dev.username,
        password=dev.password,
        timeout=30,
        conn_timeout=15,
    )
    print(f"Connected  →  {conn.find_prompt()!r}\n")

    # Group by context; unknown paths get a SKIP result immediately
    by_ctx: dict[str, list[dict]] = defaultdict(list)
    results: list[dict] = []

    for case in cases:
        cli_path = case.get("cli_path", "ETX-2i>")
        if cli_path not in CLI_PATH_CONTEXT:
            results.append({**case,
                             "device_result": "SKIP",
                             "device_reason": f"no_context_map:{cli_path}",
                             "device_output": "",
                             "tested_at": datetime.now().isoformat()})
        else:
            by_ctx[CLI_PATH_CONTEXT[cli_path]].append(case)

    total_ctx = len(by_ctx)
    for ctx_idx, (ctx, ctx_cases) in enumerate(by_ctx.items(), 1):
        label = f'"{ctx}"' if ctx else "(root)"
        print(f"  [{ctx_idx}/{total_ctx}] context {label}  ({len(ctx_cases)} cases)")

        # ── navigate to context ───────────────────────────────────────────
        nav_ok = True
        try:
            conn.send_command_timing("exit all", read_timeout=10)
            if ctx:
                nav_out = conn.send_command_timing(ctx, read_timeout=10)
                if any(p in nav_out.lower() for p in ERROR_PATTERNS):
                    nav_ok = False
                    nav_err = nav_out[:120].strip()
        except Exception as e:
            nav_ok = False
            nav_err = str(e)

        if not nav_ok:
            for case in ctx_cases:
                results.append({**case,
                                 "device_result": "FAIL",
                                 "device_reason": f"NAV_ERROR:{nav_err}",
                                 "device_output": "",
                                 "tested_at": datetime.now().isoformat()})
            continue

        # ── run commands (deduplicate within context) ─────────────────────
        cmd_cache: dict[str, str] = {}
        for case in ctx_cases:
            cmd = extract_show_command(case.get("expected_cli_command", ""))
            if not cmd:
                results.append({**case,
                                 "device_result": "SKIP",
                                 "device_reason": "parse_failed",
                                 "device_output": "",
                                 "tested_at": datetime.now().isoformat()})
                continue

            if cmd not in cmd_cache:
                try:
                    cmd_cache[cmd] = conn.send_command_timing(cmd, read_timeout=15)
                except Exception as e:
                    cmd_cache[cmd] = f"EXCEPTION:{e}"

            out   = cmd_cache[cmd]
            error = next((p for p in ERROR_PATTERNS if p in out.lower()), None)
            results.append({**case,
                             "device_result": "FAIL" if error else "PASS",
                             "device_reason": error or "ok",
                             "device_output": out[:600],
                             "tested_at": datetime.now().isoformat()})

    conn.send_command_timing("exit all", read_timeout=10)
    conn.disconnect()
    return results


# ── output ────────────────────────────────────────────────────────────────────

def save_results(results: list[dict]) -> None:
    # JSON
    jp = OUT_DIR / "eval-etx2-device-results.json"
    with open(jp, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # CSV (key fields only)
    cp = OUT_DIR / "eval-etx2-device-results.csv"
    fields = ["id","source_row","category","cli_path","prompt_type",
              "expected_cli_command","device_result","device_reason"]
    with open(cp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(results)

    # Markdown report
    total   = len(results)
    passed  = sum(1 for r in results if r["device_result"] == "PASS")
    failed  = sum(1 for r in results if r["device_result"] == "FAIL")
    skipped = sum(1 for r in results if r["device_result"] == "SKIP")
    pct = lambda n: f"{100*n//total}%" if total else "0%"

    by_cat: dict[str, dict] = defaultdict(lambda: {"PASS":0,"FAIL":0,"SKIP":0})
    for r in results:
        by_cat[r.get("category","?")][r["device_result"]] += 1

    md = [
        f"# ETX-2 Device Test Results  —  {DEVICE_NAME}",
        f"",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  ",
        f"**Total:** {total}",
        f"",
        f"| Status | Count | % |",
        f"|--------|-------|---|",
        f"| PASS   | {passed} | {pct(passed)} |",
        f"| FAIL   | {failed} | {pct(failed)} |",
        f"| SKIP   | {skipped} | {pct(skipped)} |",
        f"",
        f"## By category",
        f"",
        f"| Category | Pass | Fail | Skip |",
        f"|----------|------|------|------|",
    ]
    for cat in sorted(by_cat):
        s = by_cat[cat]
        md.append(f"| {cat} | {s['PASS']} | {s['FAIL']} | {s['SKIP']} |")

    failures = [r for r in results if r["device_result"] == "FAIL"]
    if failures:
        md += ["", "## Failures", ""]
        for r in failures:
            md.append(f"- **{r['id']}** `{r.get('expected_cli_command','')}` — _{r['device_reason']}_")

    (OUT_DIR / "eval-etx2-device-report.md").write_text("\n".join(md), encoding="utf-8")

    print(f"\n{'='*50}")
    print(f"PASS  {passed}/{total}  ({pct(passed)})")
    print(f"FAIL  {failed}/{total}  ({pct(failed)})")
    print(f"SKIP  {skipped}/{total}  ({pct(skipped)})")
    print(f"\nOutputs in tests/:")
    print(f"  {jp.name}")
    print(f"  {cp.name}")
    print(f"  eval-etx2-device-report.md")


# ── entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    args = parse_args()
    cases = load_dataset(args.only_classic, args.limit)
    print(f"Dataset: {len(cases)} test cases")
    results = run_tests(cases)
    save_results(results)


if __name__ == "__main__":
    main()
