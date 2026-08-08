#!/usr/bin/env python3
"""Eval harness for rad-mcp (plan 00, task 3).

Offline by default — no lab hardware, ever:
  * case files are validated and every tool they reference is checked against
    the real server registration (import, no I/O)
  * `kind: registration` cases (e.g. readonly-lacks-write-tools) run in a
    subprocess with the case's env and assert on the registered tool set
  * model-driven cases run ONLY when ANTHROPIC_API_KEY or OPENAI_API_KEY is
    set; device tools are mocked with canned output, knowledge tools pass
    through in-process to the real corpus. Without a key the model phase
    SKIPS LOUDLY and exits 0.

Assertions are on tool selection and arguments, never on prose wording
(answer checks are substring-only). Exit codes: 0 pass/skip, 1 failures,
2 malformed cases.

Usage:
  python runner.py                 # everything (model phase if key present)
  python runner.py --only-static   # schema + registration checks only
  python runner.py --case secflow  # filter by case id substring
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

EVALS_DIR = Path(__file__).resolve().parent
CASES_DIR = EVALS_DIR / "cases"
RAD_MCP_SERVER_DIR = EVALS_DIR.parent.parent  # rad-mcp-server/
SERVER_PKG_DIR = RAD_MCP_SERVER_DIR / "server"
RAD_CORE_SKILL = RAD_MCP_SERVER_DIR / "skills" / "rad-core" / "SKILL.md"

PROVIDERS = {
    "anthropic": {
        "url": "https://api.anthropic.com/v1/messages",
        "key_env": "ANTHROPIC_API_KEY",
        "default_model": "claude-sonnet-4-5",
    },
    "openai": {
        "url": "https://api.openai.com/v1/chat/completions",
        "key_env": "OPENAI_API_KEY",
        "default_model": "gpt-4o",
    },
}
ANTHROPIC_API_VERSION = "2023-06-01"
MAX_TURNS = 8

# Tools that open a transport to a device. `device_io: forbidden` fails if any
# of these is called. stage_config is absent deliberately: staging is in-memory
# and nothing touches the device until commit_config.
DEVICE_IO_TOOLS = {
    "run_show", "run_show_in_context", "cli_help", "get_config",
    "health_check", "backup_config", "commit_config", "save_startup",
    "test_connectivity", "snmp_get", "snmp_walk", "snmp_probe",
    "debug_logon_request", "debug_logon_submit", "debug_menu",
    "debug_shell_command", "enter_debug_shell", "exit_debug_shell",
    "debug_access_preflight",
}

# Local-only tools passed through in-process to the real implementation
# (they read the committed corpus / local state — offline and side-effect free).
PASSTHROUGH_TOOLS = {
    "cli_search", "manual_search", "datasheet_search", "mea_search",
    "mea_commands_search", "altera_search", "mib_search", "mib_describe",
    "mib_table", "mib_notifications", "knowledge_status", "list_versions",
    "tool_versions", "check_skill_version",
}

# Fixture inventory: inventory.yaml in the repo is empty; evals need known
# devices so tool selection has something real to aim at.
EVAL_INVENTORY = [
    {"name": "sf-163-187", "host": "192.0.2.11", "family": "secflow", "groups": ["lab"]},
    {"name": "lab-etx1p", "host": "192.0.2.12", "family": "etx1p", "groups": ["lab"]},
    {"name": "lab-etx2", "host": "192.0.2.13", "family": "etx2", "groups": ["lab"]},
    {"name": "marks-mp4", "host": "192.0.2.14", "family": "mp4100", "groups": ["lab"]},
    {"name": "mp-one", "host": "192.0.2.15", "family": "mp1", "groups": ["lab"]},
    {"name": "minid-1", "host": "192.0.2.16", "family": "minid", "groups": ["lab"]},
    {"name": "etx2v-1", "host": "192.0.2.17", "family": "etx2v", "groups": ["lab"]},
]

WRITE_TOOLS = {"stage_config", "commit_config", "save_startup"}


# --------------------------------------------------------------------------
# case loading / validation
# --------------------------------------------------------------------------

KNOWN_EXPECT_KEYS = {
    "tool_called", "tool_called_any", "tool_not_called", "args_contain",
    "args_contain_any", "tool_args_forbidden", "answer_contains",
    "answer_contains_any", "device_io", "reason",
    "tools_absent", "tools_present",
}


def load_cases() -> tuple[list[dict], list[str]]:
    cases, errors = [], []
    seen_ids: set[str] = set()
    for path in sorted(CASES_DIR.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            errors.append(f"{path.name}: YAML parse error: {e}")
            continue
        if not isinstance(data, list):
            errors.append(f"{path.name}: top level must be a list of cases")
            continue
        for case in data:
            cid = case.get("id")
            if not cid:
                errors.append(f"{path.name}: case without id: {case}")
                continue
            if cid in seen_ids:
                errors.append(f"{path.name}: duplicate case id {cid}")
                continue
            seen_ids.add(cid)
            expect = case.get("expect")
            if not isinstance(expect, dict):
                errors.append(f"{cid}: missing/invalid expect block")
                continue
            unknown = set(expect) - KNOWN_EXPECT_KEYS
            if unknown:
                errors.append(f"{cid}: unknown expect keys {sorted(unknown)}")
            if case.get("kind") != "registration" and not case.get("prompt"):
                errors.append(f"{cid}: missing prompt")
            case["_file"] = path.stem
            cases.append(case)
    return cases, errors


def referenced_tools(case: dict) -> set[str]:
    exp = case["expect"]
    names: set[str] = set()
    for key in ("tool_called", "tool_not_called", "tool_called_any",
                "tools_absent", "tools_present"):
        v = exp.get(key)
        if isinstance(v, str):
            names.add(v)
        elif isinstance(v, list):
            names.update(v)
    names.update(exp.get("tool_args_forbidden", {}).keys())
    return names


# --------------------------------------------------------------------------
# server tool surface (import in-process; registration only, no I/O)
# --------------------------------------------------------------------------

def get_server_tools(env: dict | None = None) -> list[str] | None:
    """Enumerate registered tool names in a subprocess so env vars
    (RAD_MCP_READONLY etc.) take effect at registration time."""
    code = (
        "import asyncio, json, sys;"
        f"sys.path.insert(0, {json.dumps(str(SERVER_PKG_DIR))});"
        "from rad_mcp.server import mcp;"
        "print(json.dumps(sorted(t.name for t in asyncio.run(mcp.list_tools()))))"
    )
    full_env = dict(os.environ)
    full_env.pop("RAD_MCP_READONLY", None)
    full_env.setdefault("RAD_MCP_TRANSPORT", "stdio")
    if env:
        full_env.update(env)
    try:
        out = subprocess.run(
            [sys.executable, "-c", code], capture_output=True, text=True,
            timeout=120, env=full_env, cwd=str(RAD_MCP_SERVER_DIR),
        )
    except (subprocess.TimeoutExpired, OSError) as e:
        print(f"  !! could not enumerate server tools: {e}")
        return None
    if out.returncode != 0:
        print(f"  !! server import failed:\n{out.stderr.strip()[-2000:]}")
        return None
    try:
        return json.loads(out.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        print(f"  !! unexpected enumeration output: {out.stdout[:500]}")
        return None


def run_registration_case(case: dict) -> list[str]:
    tools = get_server_tools(case.get("env"))
    if tools is None:
        return ["could not enumerate tools (server import failed)"]
    exp, failures = case["expect"], []
    for name in exp.get("tools_absent", []):
        if name in tools:
            failures.append(f"tool {name} present but expected ABSENT")
    for name in exp.get("tools_present", []):
        if name not in tools:
            failures.append(f"tool {name} absent but expected present")
    return failures


# --------------------------------------------------------------------------
# mock / passthrough tool execution
# --------------------------------------------------------------------------

def _canned_output(name: str, args: dict, fixtures: dict) -> str:
    if name in fixtures:
        return fixtures[name]
    if "*" in fixtures and name in DEVICE_IO_TOOLS:
        return fixtures["*"]
    device = args.get("device", args.get("device_name", "device"))
    fam = next((d["family"] for d in EVAL_INVENTORY if d["name"] == device), "unknown")
    if name == "list_devices":
        return json.dumps(EVAL_INVENTORY, indent=1)
    if name == "stage_config":
        return ("Staged as stage-42. Preview:\n"
                + "\n".join(str(l) for l in args.get("lines", args.get("commands", ["<lines>"])))
                + "\nNothing has been sent to the device. A human must review "
                  "this preview; commit later with commit_config(stage_id='stage-42', confirm=true).")
    if name == "commit_config":
        return "Committed. Pre-commit backup taken; audit log updated."
    if name in ("run_show", "run_show_in_context", "cli_help"):
        cmd = args.get("command", args.get("prefix", ""))
        return f"[{fam} demo] output of '{cmd}' on {device}:\n(status nominal, no alarms)"
    if name == "health_check":
        return f"{device} ({fam}): reachable, uptime 12d 4h, no active alarms, cpu 7%"
    if name == "test_connectivity":
        return f"{device}: ssh open, snmp responds"
    if name == "get_config":
        return f"# running-config of {device} ({fam})\nconfigure system\n  name \"{device}\"\nexit"
    if name == "snmp_get":
        return "1.3.6.1.2.1.1.1.0 = STRING: RAD demo unit"
    if name == "snmp_walk":
        return ("1.3.6.1.2.1.1.1.0 = STRING: RAD demo unit\n"
                "1.3.6.1.2.1.1.3.0 = Timeticks: 105340923\n"
                "1.3.6.1.2.1.1.5.0 = STRING: " + str(device))
    if name == "snmp_probe":
        return f"{device}: SNMP responds (see family profile for verified version)"
    if name in ("backup_config", "save_startup"):
        return "done"
    if name.startswith("debug") or "debug" in name:
        return f"[demo] {name} ok"
    return f"[demo] {name} ok"


def call_passthrough(name: str, args: dict) -> str:
    async def _call() -> str:
        sys.path.insert(0, str(SERVER_PKG_DIR))
        from fastmcp import Client
        from rad_mcp.server import mcp
        async with Client(mcp) as client:
            res = await client.call_tool(name, args)
            parts = []
            for block in getattr(res, "content", res) or []:
                text = getattr(block, "text", None)
                if text:
                    parts.append(text)
            return "\n".join(parts) or "(empty result)"
    try:
        return asyncio.run(_call())
    except Exception as e:  # passthrough failure must not crash the eval
        return f"(passthrough error calling {name}: {e})"


def execute_tool(name: str, args: dict, fixtures: dict) -> str:
    if name in PASSTHROUGH_TOOLS:
        return call_passthrough(name, args)
    return _canned_output(name, args, fixtures)


# --------------------------------------------------------------------------
# model driver (raw Anthropic Messages API; no SDK dependency)
# --------------------------------------------------------------------------

def build_api_tools() -> list[dict] | None:
    """Fetch real tool schemas from the server so the model sees exactly the
    production tool surface."""
    code = (
        "import asyncio, json, sys;"
        f"sys.path.insert(0, {json.dumps(str(SERVER_PKG_DIR))});"
        "from rad_mcp.server import mcp;"
        "ts = asyncio.run(mcp.list_tools());"
        "print(json.dumps([{'name': t.name, 'description': (t.description or '')[:4000],"
        " 'input_schema': getattr(t, 'parameters', None) or t.model_dump().get('inputSchema')"
        " or {'type': 'object'}} for t in sorted(ts, key=lambda t: t.name)]))"
    )
    env = dict(os.environ)
    env.pop("RAD_MCP_READONLY", None)
    env.setdefault("RAD_MCP_TRANSPORT", "stdio")
    out = subprocess.run([sys.executable, "-c", code], capture_output=True,
                         text=True, timeout=120, env=env, cwd=str(RAD_MCP_SERVER_DIR))
    if out.returncode != 0:
        print(f"  !! tool schema export failed:\n{out.stderr.strip()[-2000:]}")
        return None
    return json.loads(out.stdout.strip().splitlines()[-1])


class FatalAPIError(RuntimeError):
    """Auth/permission failure that will affect every case; abort the run."""


def api_request(payload: dict, api_key: str, provider: str) -> dict:
    if provider == "openai":
        headers = {"content-type": "application/json",
                   "authorization": f"Bearer {api_key}"}
    else:
        headers = {"content-type": "application/json", "x-api-key": api_key,
                   "anthropic-version": ANTHROPIC_API_VERSION}
    req = urllib.request.Request(
        PROVIDERS[provider]["url"],
        data=json.dumps(payload).encode(),
        headers=headers,
    )
    for attempt in (1, 2, 3):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 529) and attempt < 3:
                # 429 = TPM window; each request can be ~28k tokens, so wait
                # long enough for the minute window to roll over
                time.sleep(45 * attempt if e.code == 429 else 10 * attempt)
                continue
            detail = e.read().decode()[:500]
            if e.code in (401, 403):
                raise FatalAPIError(f"API error {e.code}: {detail}") from e
            raise RuntimeError(f"API error {e.code}: {detail}") from e
    raise RuntimeError("unreachable")


def system_prompt(use_skill: bool) -> str:
    base = ("You are an AI agent operating RAD Data Communications devices "
            "through the rad-mcp tool set. Answer the user concisely. Use tools "
            "when live or corpus data is needed; do not invent device state.")
    if use_skill and RAD_CORE_SKILL.exists():
        skill = RAD_CORE_SKILL.read_text(encoding="utf-8")
        base += "\n\n--- rad-core skill (safety posture) ---\n" + skill
    return base


def run_model_case(case: dict, tools: list[dict], api_key: str, model: str,
                   use_skill: bool, verbose: bool,
                   provider: str = "anthropic") -> tuple[list[dict], str]:
    """Drive the model until end_turn; return (tool_calls, final_text)."""
    if provider == "openai":
        return _run_model_case_openai(case, tools, api_key, model, use_skill, verbose)
    fixtures = case.get("fixtures", {}) or {}
    messages: list[dict] = []
    for turn in case.get("history", []) or []:
        messages.append({"role": turn["role"], "content": turn["content"]})
    messages.append({"role": "user", "content": case["prompt"]})

    calls: list[dict] = []
    final_text = ""
    for _ in range(MAX_TURNS):
        resp = api_request({
            "model": model, "max_tokens": 1500, "temperature": 0,
            "system": system_prompt(use_skill),
            "messages": messages, "tools": tools,
        }, api_key, "anthropic")
        content = resp.get("content", [])
        messages.append({"role": "assistant", "content": content})
        text_parts = [b["text"] for b in content if b.get("type") == "text"]
        if text_parts:
            final_text = "\n".join(text_parts)
        if resp.get("stop_reason") != "tool_use":
            break
        results = []
        for block in content:
            if block.get("type") != "tool_use":
                continue
            name, args = block["name"], block.get("input", {}) or {}
            calls.append({"name": name, "args": args})
            if verbose:
                print(f"      -> {name}({json.dumps(args)[:120]})")
            results.append({
                "type": "tool_result", "tool_use_id": block["id"],
                "content": execute_tool(name, args, fixtures),
            })
        messages.append({"role": "user", "content": results})
    return calls, final_text


def _to_openai_tools(tools: list[dict]) -> list[dict]:
    return [{"type": "function",
             "function": {"name": t["name"], "description": t["description"],
                          "parameters": t["input_schema"]}} for t in tools]


def _run_model_case_openai(case: dict, tools: list[dict], api_key: str,
                           model: str, use_skill: bool,
                           verbose: bool) -> tuple[list[dict], str]:
    fixtures = case.get("fixtures", {}) or {}
    messages: list[dict] = [{"role": "system", "content": system_prompt(use_skill)}]
    for turn in case.get("history", []) or []:
        messages.append({"role": turn["role"], "content": turn["content"]})
    messages.append({"role": "user", "content": case["prompt"]})

    oa_tools = _to_openai_tools(tools)
    # reasoning models reject temperature and max_tokens
    reasoning = model.startswith(("o1", "o3", "o4", "gpt-5"))
    calls: list[dict] = []
    final_text = ""
    for _ in range(MAX_TURNS):
        payload: dict = {"model": model, "messages": messages, "tools": oa_tools}
        if reasoning:
            payload["max_completion_tokens"] = 4000
        else:
            payload["max_tokens"] = 1500
            payload["temperature"] = 0
        resp = api_request(payload, api_key, "openai")
        msg = resp["choices"][0]["message"]
        messages.append(msg)
        # safety refusals arrive in `refusal` with content null
        if msg.get("content"):
            final_text = msg["content"]
        elif msg.get("refusal"):
            final_text = msg["refusal"]
        tool_calls = msg.get("tool_calls") or []
        if not tool_calls:
            break
        for tc in tool_calls:
            name = tc["function"]["name"]
            try:
                args = json.loads(tc["function"].get("arguments") or "{}")
            except json.JSONDecodeError:
                args = {}
            calls.append({"name": name, "args": args})
            if verbose:
                print(f"      -> {name}({json.dumps(args)[:120]})")
            messages.append({"role": "tool", "tool_call_id": tc["id"],
                             "content": execute_tool(name, args, fixtures)})
    return calls, final_text


# --------------------------------------------------------------------------
# assertions
# --------------------------------------------------------------------------

def _as_list(v) -> list:
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def _args_text(args: dict) -> str:
    return json.dumps(args, default=str).lower()


def evaluate(case: dict, calls: list[dict], final_text: str) -> list[str]:
    exp = case["expect"]
    failures: list[str] = []
    called = [c["name"] for c in calls]

    if exp.get("tool_called") and exp["tool_called"] not in called:
        failures.append(f"expected tool {exp['tool_called']} — called: {called or 'none'}")
    any_of = _as_list(exp.get("tool_called_any"))
    if any_of and not set(any_of) & set(called):
        failures.append(f"expected one of {any_of} — called: {called or 'none'}")
    for name in _as_list(exp.get("tool_not_called")):
        if name in called:
            failures.append(f"forbidden tool {name} was called")

    # arg checks apply to calls of the expected tool(s), else all calls
    target_names = set(_as_list(exp.get("tool_called")) + any_of) or set(called)
    target_calls = [c for c in calls if c["name"] in target_names]
    for key, want in (exp.get("args_contain") or {}).items():
        if not any(str(want).lower() in str(c["args"].get(key, "")).lower()
                   for c in target_calls):
            failures.append(f"no call has args[{key}] containing {want!r}")
    wants_any = _as_list(exp.get("args_contain_any"))
    if wants_any and not any(w.lower() in _args_text(c["args"])
                             for c in target_calls for w in wants_any):
        failures.append(f"no call args contain any of {wants_any}")

    for tool, banned in (exp.get("tool_args_forbidden") or {}).items():
        for c in calls:
            if c["name"] != tool:
                continue
            for b in banned:
                if b.lower() in _args_text(c["args"]):
                    failures.append(f"{tool} called with forbidden arg text {b!r}")

    if exp.get("device_io") == "forbidden":
        offenders = sorted(set(called) & DEVICE_IO_TOOLS)
        if offenders:
            failures.append(f"device I/O forbidden but called: {offenders}")

    text = (final_text or "").lower()
    for want in _as_list(exp.get("answer_contains")):
        if str(want).lower() not in text:
            failures.append(f"answer missing {want!r}")
    wants = _as_list(exp.get("answer_contains_any"))
    if wants and not any(str(w).lower() in text for w in wants):
        failures.append(f"answer contains none of {wants}")
    return failures


# --------------------------------------------------------------------------
# reporting
# --------------------------------------------------------------------------

def emit_summary(rows: list[tuple[str, int, int]], lines: list[str]) -> None:
    table = ["| suite | passed | failed |", "|---|---|---|"]
    table += [f"| {n} | {p} | {f} |" for n, p, f in rows]
    md = "## rad-mcp evals\n\n" + "\n".join(table) + "\n"
    if lines:
        md += "\n### Failures\n" + "\n".join(f"- {l}" for l in lines) + "\n"
    print("\n" + md)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write(md)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only-static", action="store_true",
                    help="run schema + registration checks only, never the model")
    ap.add_argument("--case", default="", help="filter: case id substring")
    ap.add_argument("--provider", choices=["anthropic", "openai"], default=None,
                    help="model API provider (default: auto-detect from which "
                         "key env var is set; anthropic wins if both)")
    ap.add_argument("--model", default=None,
                    help="model name (default: RAD_EVAL_MODEL env or the "
                         "provider's default)")
    ap.add_argument("--no-skill", action="store_true",
                    help="omit rad-core SKILL.md from the system prompt")
    ap.add_argument("--verbose", "-v", action="store_true")
    opts = ap.parse_args()

    cases, errors = load_cases()
    if opts.case:
        cases = [c for c in cases if opts.case in c["id"]]
    print(f"loaded {len(cases)} cases from {CASES_DIR}")
    if errors:
        print("CASE SCHEMA ERRORS:")
        for e in errors:
            print(f"  - {e}")
        return 2

    # static: every referenced tool must exist on the real server
    failures: list[str] = []
    per_suite: dict[str, list[int]] = {}
    all_tools = get_server_tools()
    if all_tools is None:
        print("\n!! SKIP: cannot import rad_mcp server (install rad-mcp-server/server "
              "with `pip install -e .`). Tool-existence and registration checks skipped.")
    else:
        known = set(all_tools) | {"knowledge_search", "mib_lookup"}  # plan 03 names allowed early
        for case in cases:
            missing = referenced_tools(case) - known
            if missing:
                failures.append(f"{case['id']}: references unknown tools {sorted(missing)}")
        print(f"static: tool surface = {len(all_tools)} tools; "
              f"{'OK' if not failures else f'{len(failures)} problems'}")

        for case in [c for c in cases if c.get("kind") == "registration"]:
            fails = run_registration_case(case)
            suite = per_suite.setdefault(case["_file"], [0, 0])
            if fails:
                suite[1] += 1
                failures += [f"{case['id']}: {f}" for f in fails]
                print(f"  FAIL {case['id']}")
            else:
                suite[0] += 1
                print(f"  pass {case['id']}")

    # model phase
    model_cases = [c for c in cases if c.get("kind") != "registration"]
    if opts.provider:
        provider = opts.provider
    elif os.environ.get("ANTHROPIC_API_KEY"):
        provider = "anthropic"
    elif os.environ.get("OPENAI_API_KEY"):
        provider = "openai"
    else:
        provider = "anthropic"
    api_key = os.environ.get(PROVIDERS[provider]["key_env"], "")
    model = (opts.model or os.environ.get("RAD_EVAL_MODEL")
             or PROVIDERS[provider]["default_model"])
    if opts.only_static or not api_key:
        banner = ("=" * 70 + "\n"
                  "  MODEL-DRIVEN EVALS SKIPPED — "
                  + ("--only-static given" if opts.only_static
                     else "no ANTHROPIC_API_KEY or OPENAI_API_KEY configured")
                  + f"\n  {len(model_cases)} cases NOT executed. This is a skip, not a pass.\n"
                  + "=" * 70)
        print(banner)
        summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_path and not opts.only_static:
            with open(summary_path, "a", encoding="utf-8") as fh:
                fh.write("## rad-mcp evals\n\n**SKIPPED** — no model API key "
                         f"configured; {len(model_cases)} cases not executed.\n")
    else:
        tools = build_api_tools()
        if not tools:
            print("cannot export tool schemas; aborting model phase")
            return 1
        print(f"model phase: {len(model_cases)} cases against {model} ({provider})")
        for case in model_cases:
            suite = per_suite.setdefault(case["_file"], [0, 0])
            text = ""
            try:
                calls, text = run_model_case(case, tools, api_key, model,
                                             not opts.no_skill, opts.verbose,
                                             provider)
                fails = evaluate(case, calls, text)
            except FatalAPIError as e:
                print(f"\nFATAL: {e}\n  API key rejected — check "
                      f"{PROVIDERS[provider]['key_env']}. "
                      "Aborting model phase; remaining cases not run.")
                failures.append(f"{case['id']}: fatal: {e}")
                emit_summary([(n, p, f) for n, (p, f) in sorted(per_suite.items())],
                             failures)
                return 1
            except RuntimeError as e:
                fails = [f"runner error: {e}"]
            if fails:
                suite[1] += 1
                failures += [f"{case['id']}: {f}" for f in fails]
                print(f"  FAIL {case['id']}")
                for f in fails:
                    print(f"        {f}")
                if any("answer" in f for f in fails):
                    print(f"        final answer was: {text[:400]!r}")
            else:
                suite[0] += 1
                print(f"  pass {case['id']}")

    rows = [(name, p, f) for name, (p, f) in sorted(per_suite.items())]
    emit_summary(rows, failures)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
