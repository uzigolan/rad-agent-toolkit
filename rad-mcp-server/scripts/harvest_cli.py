"""Harvest a RAD device's complete interactive `?` help into a skill reference.

Walks the captured command tree (references/command-tree-<family>.md), and for
every context captures the level `?` listing, and for every leaf the
`<command> ?` argument help — using the exact same execute-nothing mechanic as
the server's cli_help tool: type `<prefix>?` WITHOUT Enter, read the help,
then Ctrl-U to discard the pending line.

The only lines ever sent with Enter are context navigation (`configure`,
`system`, ...), `exit` and `exit all`. Names on the DANGEROUS_ENTER list are
never sent with Enter regardless of how the tree classifies them.

Usage (run with the server venv python):
  python scripts/harvest_cli.py probe   lab-sf1p            # inspect prompt/error shapes
  python scripts/harvest_cli.py harvest lab-sf1p            # full run
  python scripts/harvest_cli.py render  lab-sf1p            # re-render md from jsonl

Output:
  server/logs/harvest-<family>.jsonl                        # raw, appended as we go
  skills/rad-cli-operations/references/cli-reference-<family>.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SERVER = REPO / "server"
sys.path.insert(0, str(SERVER))

from netmiko import ConnectHandler  # noqa: E402

from rad_mcp.drivers import get_driver  # noqa: E402
from rad_mcp.inventory import get_device  # noqa: E402

REFERENCE_DIR = REPO / "skills" / "rad-cli-operations" / "references"
LOG_DIR = SERVER / "logs"

ERROR_MARKER = "cli error"

# Never sent with Enter, even if the tree shows children under them.
DANGEROUS_ENTER = {
    "reboot", "force-reboot", "factory-default", "factory-default-all",
    "install", "undo-install", "user-default", "send", "login", "logout",
    "startup-confirm-required", "software-confirm-required", "save", "copy",
    "exec", "delete", "shutdown",
}
DANGEROUS_PREFIXES = ("clear-", "blacklist-clear")

MORE_RE = re.compile(r"-+\s*more\s*-+\s*$", re.IGNORECASE)


# ------------------------------------------------------------------ tree


@dataclass
class Node:
    name: str
    children: list["Node"] = field(default_factory=list)

    @property
    def is_context(self) -> bool:
        return bool(self.children)


def parse_tree(family: str) -> Node:
    """Parse the +--- tree inside the fenced block of command-tree-<family>.md."""
    path = REFERENCE_DIR / f"command-tree-{family}.md"
    text = path.read_text(encoding="utf-8")
    m = re.search(r"```\n(.*?)```", text, re.DOTALL)
    if not m:
        raise SystemExit(f"No fenced tree block found in {path}")
    root = Node("")
    stack = [root]  # stack[d] = last node seen at depth d-1's parent chain
    for line in m.group(1).splitlines():
        idx = line.find("+---")
        if idx < 0:
            continue
        depth = idx // 4  # each level indents by '|   ' (4 chars)
        name = line[idx + 4:].strip()
        if not name:
            continue
        node = Node(name)
        while len(stack) > depth + 1:
            stack.pop()
        stack[depth].children.append(node)
        if len(stack) == depth + 1:
            stack.append(node)
        else:
            stack[depth + 1] = node
    return root


# ------------------------------------------------------------------ device


def connect(device_name: str):
    dev = get_device(device_name)
    driver = get_driver(dev.family)
    conn = ConnectHandler(
        device_type=driver.netmiko_device_type,
        host=dev.host,
        port=dev.port,
        username=dev.username,
        password=dev.password,
        timeout=30,
        conn_timeout=15,
    )
    return dev, conn


def capture_help(conn, prefix: str, timeout: float = 15.0) -> str:
    """Type `<prefix>?` without Enter, read help, Ctrl-U the pending line."""
    conn.write_channel(prefix + "?")
    output = ""
    deadline = time.monotonic() + timeout
    quiet = 0.0
    while time.monotonic() < deadline:
        time.sleep(0.2)
        chunk = conn.read_channel()
        if chunk:
            output += chunk
            quiet = 0.0
            if MORE_RE.search(output.strip().splitlines()[-1] if output.strip() else ""):
                conn.write_channel(" ")  # advance pager
        elif output:
            quiet += 0.2
            if quiet >= 0.8:
                break
    conn.write_channel("\x15")  # Ctrl-U: discard re-echoed pending input
    time.sleep(0.15)
    conn.read_channel()
    return clean_help(output, prefix)


def clean_help(out: str, prefix: str) -> str:
    lines = out.splitlines()
    if lines and lines[0].strip().endswith("?"):
        lines = lines[1:]
    while lines and (not lines[-1].strip() or lines[-1].rstrip().endswith("#")
                     or lines[-1].strip() == prefix.strip()):
        lines = lines[:-1]
    return "\n".join(lines).strip()


def nav(conn, line: str, timeout: int = 20) -> str:
    return conn.send_command_timing(line, last_read=0.8, read_timeout=timeout)


# ------------------------------------------------------------------ crawl


class Harvester:
    def __init__(self, conn, jsonl_path: Path, log=print):
        self.conn = conn
        self.jsonl = jsonl_path.open("a", encoding="utf-8")
        self.log = log
        self.captures = 0
        self.skipped: list[str] = []
        self.parameterized: list[str] = []

    def record(self, kind: str, context: str, prefix: str, text: str):
        self.jsonl.write(json.dumps(
            {"kind": kind, "context": context, "prefix": prefix, "text": text},
            ensure_ascii=False) + "\n")
        self.jsonl.flush()
        self.captures += 1

    @staticmethod
    def enter_forbidden(name: str) -> bool:
        first = name.split()[0]
        return (first in DANGEROUS_ENTER
                or any(first.startswith(p) for p in DANGEROUS_PREFIXES)
                or " " in name)  # multi-word nodes are commands, not contexts

    def resync(self, path: list[str]):
        """Return to a known position: root, then re-enter the full path."""
        nav(self.conn, "exit all")
        for step in path:
            nav(self.conn, step)

    def crawl(self, node: Node, path: list[str]):
        ctx = " ".join(path) or "<root>"
        prompt_here = self.conn.find_prompt()
        level = capture_help(self.conn, "")
        self.record("level", ctx, "", level)
        self.log(f"[{self.captures:4d}] level  {ctx}")

        for child in node.children:
            if child.is_context and not self.enter_forbidden(child.name):
                nav(self.conn, child.name)
                if self.conn.find_prompt() == prompt_here:
                    # Prompt didn't move: needs an argument (parameterized).
                    self.parameterized.append(f"{ctx} > {child.name}")
                    arg = capture_help(self.conn, child.name + " ")
                    self.record("args-noenter", ctx, child.name, arg)
                    self.log(f"[{self.captures:4d}] param  {ctx} > {child.name}")
                    continue
                self.crawl(child, path + [child.name])
                nav(self.conn, "exit")
                if self.conn.find_prompt() != prompt_here:
                    self.resync(path)  # lost position — renavigate from root
            else:
                if child.is_context:
                    self.skipped.append(f"{ctx} > {child.name}")
                arg = capture_help(self.conn, child.name + " ")
                self.record("args", ctx, child.name, arg)
                self.log(f"[{self.captures:4d}] args   {ctx} > {child.name}")


# ------------------------------------------------------------------ render


def render(family: str, device_label: str) -> Path:
    jsonl_path = LOG_DIR / f"harvest-{family}.jsonl"
    entries = [json.loads(l) for l in jsonl_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    # Last capture wins if a context was re-harvested.
    by_key: dict[tuple, dict] = {(e["kind"] != "level", e["context"], e["prefix"]): e for e in entries}

    out = [
        f"# {family} CLI reference (harvested `?` help)",
        "",
        f"Captured live from {device_label} on "
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%d')} by scripts/harvest_cli.py.",
        "Every section is a CLI context: first the level `?` listing (commands +",
        "descriptions), then per-command argument help (`<command> ?`). Entries",
        "marked *(not entered)* are parameterized contexts — their inner structure",
        "is in command-tree-" + family + ".md; use cli_help with a real index for",
        "inner argument syntax.",
        "",
    ]
    contexts: dict[str, list[dict]] = {}
    for e in entries:
        contexts.setdefault(e["context"], []).append(e)
    for ctx in contexts:
        seen = {}
        for e in contexts[ctx]:
            seen[(e["kind"], e["prefix"])] = e
        out.append(f"## {ctx}")
        out.append("")
        for (kind, prefix), e in seen.items():
            if kind == "level":
                out.append("Level help (`?`):")
            elif kind == "args-noenter":
                out.append(f"### {prefix} *(not entered — parameterized context)*")
            else:
                out.append(f"### {prefix}")
            out.append("```text")
            out.append(e["text"] or "(no help output captured)")
            out.append("```")
            out.append("")
    path = REFERENCE_DIR / f"cli-reference-{family}.md"
    path.write_text("\n".join(out), encoding="utf-8")
    return path


# ------------------------------------------------------------------ main


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mode", choices=["probe", "harvest", "render"])
    ap.add_argument("device")
    ap.add_argument("--branch", default="", help="only crawl this top-level branch (e.g. configure)")
    args = ap.parse_args()

    dev = get_device(args.device)
    family = dev.family

    if args.mode == "render":
        path = render(family, f"{dev.name} ({dev.description})")
        print(f"Rendered: {path}")
        return

    if args.mode == "probe":
        _, conn = connect(args.device)
        try:
            print("PROMPT root:", repr(conn.find_prompt()))
            print("ENTER configure system ->", repr(nav(conn, "configure system")))
            print("PROMPT in-context:", repr(conn.find_prompt()))
            print("EXIT ->", repr(nav(conn, "exit all")))
            print("PROMPT after exit all:", repr(conn.find_prompt()))
            print("ENTER configure port (parameterized?) ->", repr(nav(conn, "configure port")))
            print("PROMPT now:", repr(conn.find_prompt()))
            nav(conn, "exit all")
            print("LEVEL HELP at root:", repr(capture_help(conn, "")[:400]))
            print("PROMPT after help capture:", repr(conn.find_prompt()))
        finally:
            conn.disconnect()
        return

    # harvest
    tree = parse_tree(family)
    if args.branch:
        tree.children = [c for c in tree.children if c.name == args.branch]
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    jsonl_path = LOG_DIR / f"harvest-{family}.jsonl"
    started = time.monotonic()
    _, conn = connect(args.device)
    try:
        nav(conn, "exit all")
        h = Harvester(conn, jsonl_path)
        h.crawl(tree, [])
    finally:
        conn.disconnect()
    mins = (time.monotonic() - started) / 60
    print(f"\nDone: {h.captures} captures in {mins:.1f} min -> {jsonl_path}")
    if h.parameterized:
        print(f"Parameterized (not entered): {len(h.parameterized)}")
        for p in h.parameterized:
            print("  -", p)
    path = render(family, f"{dev.name} ({dev.description})")
    print(f"Rendered: {path}")


if __name__ == "__main__":
    main()
