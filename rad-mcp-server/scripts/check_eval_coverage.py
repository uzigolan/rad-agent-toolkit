"""Knowledge-coverage checker for tests/eval-etx2i-str-test3-fail.json.

For each eval case, walks the harvested etx2 CLI tree (cli-help-etx2.jsonl)
token-by-token along the case's cli_path, to determine whether the expected
show_command is actually present in our reference. Zero device I/O — this
answers "does the skill's knowledge base have the right answer available",
not "does it work live on the device" (see tests/eval-report.md for why that
second question is explicitly out of scope here).

Three-way classification per case:
  FOUND                       - exact command captured at the exact context.
  CONTEXT_EXISTS_NOT_ENTERED  - the navigation path is real (a genuine child
                                 context) but its interior was never
                                 harvested (no instance existed at harvest
                                 time) — same class of gap as `mep`/`lag`/`pw`.
  CONTEXT_ENTERED_COMMAND_MISSING - the context was fully harvested but this
                                 specific command isn't there — a real gap,
                                 or the spreadsheet's claim is wrong/at the
                                 wrong depth (see tests/eval-report.md).

Argument notation embedded in the spreadsheet's show_command text (e.g.
'show rib { ipv4 | ipv6 }', 'show alarm-information <source-type> ...') is
stripped before matching — the harvest captures bare command names.

Usage: python scripts/check_eval_coverage.py
Output: tests/eval-coverage-report.json
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
JSONL = REPO / "skills/rad-cli-operations/references/cli-help-etx2.jsonl"
CASES = REPO / "tests/eval-etx2i-str-test3-fail.json"
OUT = REPO / "tests/eval-coverage-report.json"

# cli_path (as written in the spreadsheet) -> real token sequence to walk
# from root. Update this map if the dataset gains new cli_path values.
PATH_TOKENS = {
    "ETX-2i>": [],
    "ETX-2i>admin>scheduler#": ["admin", "scheduler"],
    "ETX-2i>config>chassis#": ["configure", "chassis"],
    "ETX-2i>config>mngmnt>radius#": ["configure", "management", "radius"],
    "ETX-2i>config>mngmnt>snmp#": ["configure", "management", "snmp"],
    "ETX-2i>config>oam>cfm>md(n)>ma(n)>mep(n)#":
        ["configure", "oam", "cfm", "maintenance-domain", "maintenance-association", "mep"],
    "ETX-2i>config>oam>twamp>controller(n)>peer(ip)#":
        ["configure", "oam", "twamp", "controller", "peer"],
    "ETX-2i>config>oam>twamp>responder(n)#": ["configure", "oam", "twamp", "responder"],
    "ETX-2i>config>port#": ["configure", "port"],
    "ETX-2i>config>port>eth(port)#": ["configure", "port", "ethernet"],
    "ETX-2i>config>port>lag(n)#": ["configure", "port", "lag"],
    "ETX-2i>config>pwe#": ["configure", "pwe"],
    "ETX-2i>config>pwe>pw(n)#": ["configure", "pwe", "pw"],
    "ETX-2i>config>reporting#": ["configure", "reporting"],
    "ETX-2i>config>router(n)#": ["configure", "router"],
    "ETX-2i>config>test>l3sat>generator(name)>peer(ip)#":
        ["configure", "test", "l3sat", "generator", "peer"],
    "ETX-2i>config>test>rfc2544>test(n)#": ["configure", "test", "rfc2544", "test"],
    "ETX-2i>config>test>y1564>generator(n)#": ["configure", "test", "y1564", "generator"],
    "ETX-2i>file#": ["file"],
}


def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def strip_args_candidates(s: str) -> list[str]:
    """Progressively shorter truncations at embedded argument notation, e.g.
    'show rib { ipv4 | ipv6 }' -> ['show rib']. When a keyword names the
    placeholder ('show lacp-status ethernet <port>' -> the harvest's real
    leaf is bare 'show lacp-status', not '...ethernet'), also try dropping
    one more trailing bare word. Ordered longest-first so a genuinely missing
    command (no placeholder at all, e.g. 'show report detailed') is never
    over-truncated into a false match with something unrelated."""
    cut = re.split(r"\s*[{<]", s, maxsplit=1)[0].strip()
    if cut == s.strip():
        return [cut]  # no placeholder found -- do not guess further
    words = cut.split()
    return [cut] if len(words) < 2 else [cut, " ".join(words[:-1])]


def main() -> None:
    entries = [json.loads(l) for l in JSONL.read_text(encoding="utf-8").splitlines()]
    by_context: dict[str, list[dict]] = {}
    for e in entries:
        by_context.setdefault(e["context"], []).append(e)
    all_contexts = set(by_context)
    level_text = {e["context"]: e["text"] for e in entries if e["kind"] == "level"}

    def walk(tokens: list[str]) -> tuple[str, str, str | None]:
        """Walk tokens from root, trying 'ctx' then 'ctx NAME' at each step.
        Returns (status, ctx, failing_tok) — failing_tok is whichever token in
        the path actually blocked descent, which is NOT always the last token
        in the list (e.g. for 'twamp controller peer', 'controller' itself is
        never entered, so 'peer' is never even reached)."""
        ctx = "<root>"
        for tok in tokens:
            plain = (ctx + " " + tok).strip() if ctx != "<root>" else tok
            named = plain + " NAME"
            if plain in all_contexts:
                ctx = plain
                continue
            if named in all_contexts:
                ctx = named
                continue
            known_child = any(
                e["kind"] in ("args-noenter", "args-param")
                and normalize(e["prefix"]).split(" ")[0] == tok
                for e in by_context.get(ctx, [])
            )
            if known_child:
                return "KNOWN_BUT_NOT_ENTERED", ctx, tok
            return "UNKNOWN_TOKEN", f"{ctx} -> {tok}", tok
        return "FULLY_ENTERED", ctx, None

    def refusal_reason(ctx: str, tok: str) -> str | None:
        """Pull a short device-response snippet out of the harvest's own
        args-noenter text for (ctx, tok), if the harvester's diagnostic probe
        captured one (e.g. a 'cli error' line) — None if there's nothing more
        specific than a plain 'not entered'."""
        for e in by_context.get(ctx, []):
            if e["kind"] == "args-noenter" and normalize(e["prefix"]).split(" ")[0] == tok:
                m = re.search(r"cli error:.*", e["text"])
                return m.group(0).strip() if m else None
        return None

    cases = json.loads(CASES.read_text(encoding="utf-8"))
    results = []
    for c in cases:
        tokens = PATH_TOKENS.get(c["cli_path"])
        if tokens is None:
            results.append({**c, "coverage": "UNMAPPED_PATH", "detail": c["cli_path"]})
            continue

        status, ctx, failing_tok = walk(tokens)
        if status == "UNKNOWN_TOKEN":
            results.append({**c, "coverage": "CONTEXT_NOT_FOUND", "detail": ctx})
            continue
        if status == "KNOWN_BUT_NOT_ENTERED":
            reason = refusal_reason(ctx, failing_tok)
            detail = (f"'{failing_tok}' under '{ctx}': {reason}" if reason
                      else f"'{failing_tok}' is a real child of '{ctx}', no instance existed")
            results.append({**c, "coverage": "CONTEXT_EXISTS_NOT_ENTERED", "detail": detail})
            continue

        show_cmd_candidates = [normalize(c2) for c2 in strip_args_candidates(c["show_command"])]
        show_cmd = show_cmd_candidates[0]
        leaf_names = {normalize(strip_args_candidates(e["prefix"])[0])
                      for e in by_context.get(ctx, []) if e["kind"] != "level"}
        matched = next((cand for cand in show_cmd_candidates if cand in leaf_names), None)
        found_in_level = any(cand in normalize(level_text.get(ctx, ""))
                              for cand in show_cmd_candidates)
        if matched:
            results.append({**c, "coverage": "FOUND", "detail": f"leaf capture in '{ctx}'"})
        elif found_in_level:
            results.append({**c, "coverage": "FOUND_IN_LEVEL_LISTING",
                             "detail": f"in '{ctx}' level listing, no separate leaf capture"})
        else:
            results.append({**c, "coverage": "CONTEXT_ENTERED_COMMAND_MISSING",
                             "detail": f"'{ctx}' fully harvested but '{show_cmd}' not found there"})

    cnt = Counter(r["coverage"] for r in results)
    print("=== Coverage summary ===")
    for k, v in cnt.most_common():
        print(f"  {k}: {v}")
    OUT.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\n-> {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
