"""Harvest a RAD device's complete interactive `?` help into a skill reference.

Re-runnable and firmware-drift-aware:
  1. Captures a FRESH `tree` from the device (root) — so commands added or
     removed by a firmware version are discovered automatically — and
     regenerates references/command-tree-<family>.md.
  2. Walks that live tree; for every context captures the level `?` listing,
     for every leaf the `<command> ?` argument help — using the exact same
     execute-nothing mechanic as the server's cli_help tool: type `<prefix>?`
     WITHOUT Enter, read the help, then Ctrl-U to discard the pending line.
  3. Diffs the new captures against the previous run (added / removed /
     changed), prints the report, and rewrites the canonical JSONL — git
     history then tracks CLI evolution across firmware versions.

The only lines ever sent with Enter are context navigation (`configure`,
`system`, ...), `exit`, `exit all` and `tree`. Names on the DANGEROUS_ENTER
list are never sent with Enter regardless of how the tree classifies them.

Usage (run with the server venv python):
  python scripts/harvest_cli.py probe   lab-sf1p            # inspect prompt/error shapes
  python scripts/harvest_cli.py harvest lab-sf1p            # full run (safe to repeat)
  python scripts/harvest_cli.py harvest lab-sf1p --branch configure   # partial refresh
  python scripts/harvest_cli.py harvest lab-sf1p --branch "configure crypto"  # one subtree
  python scripts/harvest_cli.py render  lab-sf1p            # re-render md from jsonl

Output (both under skills/rad-cli-operations/references/ — knowledge assets,
committed to git and readable by the server's rad://cli-reference resources):
  cli-help-<family>.jsonl        # canonical captures, rewritten (sorted) each run
  cli-reference-<family>.md      # rendered, grep-friendly
  command-tree-<family>.md       # regenerated from the live `tree` each run
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

# Never sent with Enter, even if the tree shows children under them.
DANGEROUS_ENTER = {
    "reboot", "force-reboot", "factory-default", "factory-default-all",
    "install", "undo-install", "user-default", "send", "login", "logout",
    "startup-confirm-required", "software-confirm-required", "save", "copy",
    "exec", "delete", "shutdown",
}
DANGEROUS_PREFIXES = ("clear-", "blacklist-clear")

# Parameterized contexts we never auto-create even when the CLI allows it:
# identity / credential / security-material objects.
CREATE_EXCLUDE = {"login-user", "user", "community", "isakmp-key", "access-list"}

# A string-named instance parameter, e.g. "[1..20 chars]" or "[string]".
PARAM_STR_RE = re.compile(r"\[1\.\.(\d+) chars|\[string\]")
TMP_NAME = "zzz-hrvst"

MORE_RE = re.compile(r"-+\s*more\s*-+\s*$", re.IGNORECASE)

Key = tuple[str, str]  # (context, prefix); prefix "" = the level `?` capture


# ------------------------------------------------------------------ tree


@dataclass
class Node:
    name: str
    children: list["Node"] = field(default_factory=list)

    @property
    def is_context(self) -> bool:
        return bool(self.children)


def parse_tree_text(text: str) -> Node:
    """Parse `tree` output: nodes are '+---name' lines indented 4 chars/level."""
    root = Node("")
    stack = [root]
    for line in text.splitlines():
        idx = line.find("+---")
        if idx < 0:
            continue
        depth = idx // 4
        name = line[idx + 4:].strip()
        if not name:
            continue
        node = Node(name)
        while len(stack) > depth + 1:
            stack.pop()
        stack[depth].children.append(node)
        stack.append(node)
    return root


def capture_tree(conn) -> str:
    """Run root `tree` and return the raw hierarchy text."""
    nav(conn, "exit all")
    out = conn.send_command_timing("tree", last_read=2.0, read_timeout=180)
    lines = out.splitlines()
    if lines and lines[0].strip() == "tree":
        lines = lines[1:]
    while lines and (not lines[-1].strip() or lines[-1].rstrip().endswith("#")):
        lines = lines[:-1]
    return "\n".join(lines).rstrip()


def write_tree_md(family: str, device_label: str, tree_text: str) -> Path:
    path = REFERENCE_DIR / f"command-tree-{family}.md"
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    md = (
        f"# {family} command tree (family: {family})\n\n"
        f"Captured live from {device_label} via the root `tree` command on {date}\n"
        "by scripts/harvest_cli.py — re-run `harvest` after firmware upgrades; the\n"
        "tree is re-captured fresh each run. Use it to locate which context holds a\n"
        f"feature, then cli-reference-{family}.md / the cli_help tool for exact,\n"
        "firmware-current argument syntax.\n\n"
        "Legend from the CLI's own `?` listings: `+` = sub-context you can enter,\n"
        "`-` = command/leaf, `[no]` prefix = removable with `no <leaf>`.\n\n"
        "```\n" + tree_text + "\n```\n"
    )
    path.write_text(md, encoding="utf-8")
    return path


# ------------------------------------------------------------------ device


BASE_PROMPT = ""  # set on connect; anchors reads on the device prompt


def connect(device_name: str):
    global BASE_PROMPT
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
    BASE_PROMPT = conn.base_prompt
    return dev, conn


def capture_help(conn, prefix: str, timeout: float = 15.0) -> str:
    """Type `<prefix>?` without Enter, read help, Ctrl-U the pending line."""
    # After the help the CLI reprints `<prompt> <prefix>` as the pending
    # line — that is the end-of-help signature, so reads can stop there
    # instead of waiting out a quiet-period timer.
    end_re = re.compile(re.escape(BASE_PROMPT) + r"[^\n]*[#\$] ?"
                        + re.escape(prefix.rstrip()) + r" ?$") if BASE_PROMPT else None
    conn.write_channel(prefix + "?")
    output = ""
    deadline = time.monotonic() + timeout
    quiet = 0.0
    while time.monotonic() < deadline:
        time.sleep(0.1)
        chunk = conn.read_channel()
        if chunk:
            output += chunk
            quiet = 0.0
            last = output.strip().splitlines()[-1] if output.strip() else ""
            if MORE_RE.search(last):
                conn.write_channel(" ")  # advance pager
            elif end_re and end_re.search(last):
                break
        elif output:
            quiet += 0.1
            if quiet >= 0.6:  # fallback when the signature never matched
                break
    conn.write_channel("\x15")  # Ctrl-U: discard re-echoed pending input
    drain_deadline = time.monotonic() + 2.0
    while time.monotonic() < drain_deadline:  # drain the redraw fully so no
        time.sleep(0.1)                       # residue leaks into the next read
        if not conn.read_channel():
            break
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
    if BASE_PROMPT:
        try:
            return conn.send_command(
                line, expect_string=re.escape(BASE_PROMPT) + r"[^\n]*[#\$] ?$",
                strip_prompt=False, strip_command=False, read_timeout=timeout)
        except Exception:
            # Prompt pattern didn't show — drain passively, NEVER re-send
            # (the line may already have executed).
            output = ""
            deadline = time.monotonic() + 3.0
            while time.monotonic() < deadline:
                time.sleep(0.1)
                chunk = conn.read_channel()
                if not chunk and output:
                    break
                output += chunk
            return output
    return conn.send_command_timing(line, last_read=0.8, read_timeout=timeout)


# ------------------------------------------------------------------ crawl


class Harvester:
    def __init__(self, conn, scratch_path: Path, log=print):
        self.conn = conn
        self.records: dict[Key, dict] = {}
        # Crash scratch: streamed as we go so an interrupted run loses nothing.
        self.scratch = scratch_path.open("w", encoding="utf-8")
        self.log = log
        self.parameterized: list[str] = []
        self.entered_existing: list[str] = []
        self.created: list[str] = []
        self.rolled_back: list[tuple[str, str]] = []

    def record(self, kind: str, context: str, prefix: str, text: str):
        entry = {"kind": kind, "context": context, "prefix": prefix, "text": text}
        self.records[(context, prefix)] = entry
        self.scratch.write(json.dumps(entry, ensure_ascii=False) + "\n")
        self.scratch.flush()

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

    def level_info(self, timeout: float = 60.0) -> str:
        """Run `info` at the current level (pager-aware) to find existing
        instances of parameterized child contexts."""
        end_re = re.compile(re.escape(BASE_PROMPT) + r"[^\n]*[#\$] ?$") if BASE_PROMPT else None
        self.conn.write_channel("info\n")
        output = ""
        deadline = time.monotonic() + timeout
        quiet = 0.0
        while time.monotonic() < deadline:
            time.sleep(0.1)
            chunk = self.conn.read_channel()
            if chunk:
                output += chunk
                quiet = 0.0
                last = output.strip().splitlines()[-1] if output.strip() else ""
                if MORE_RE.search(last):
                    self.conn.write_channel(" ")
                elif end_re and end_re.search(last):
                    break  # prompt reprinted — dump complete
            elif output:
                quiet += 0.1
                if quiet >= 0.8:
                    break
        return output

    @staticmethod
    def existing_instance(info_text: str, name: str) -> str | None:
        """First existing instance of a parameterized child in `info` output.

        Only single-token instance args are accepted so a mismatched info line
        can never be assembled into an executable set-command.
        """
        for line in info_text.splitlines():
            m = re.match(rf"^{re.escape(name)}\s+(\S+)\s*$", line.strip())
            if m and m.group(1) != "?":
                return m.group(1)
        return None

    def enter_and_crawl(self, child: Node, path: list[str], labels: list[str],
                        nav_line: str, prompt_parent: str, rollback: str | None) -> bool:
        """Enter a parameterized context via `nav_line`; harvest inside under a
        stable NAME placeholder; roll back the instance if we created it."""
        nav(self.conn, nav_line)
        if self.conn.find_prompt() == prompt_parent:
            return False  # entry refused (bad name, second arg required, ...)
        where = " ".join(path)
        if rollback:
            self.created.append(f"{where} > {nav_line}")
        self.crawl(child, path + [nav_line], labels + [f"{child.name} NAME"])
        nav(self.conn, "exit")
        if self.conn.find_prompt() != prompt_parent:
            self.resync(path)
        if rollback:
            out = nav(self.conn, rollback)
            self.rolled_back.append((f"{where} > {rollback}", out.strip()))
        else:
            self.entered_existing.append(f"{where} > {nav_line}")
        return True

    def try_enter_parameterized(self, child: Node, path: list[str], labels: list[str],
                                level_help: str, arg_help: str, info_text: str,
                                prompt_here: str) -> bool:
        """Harvest inside a parameterized context when it is safe:
        an existing instance (pure navigation), or a string-named [no]-removable
        object created with a temp name and rolled back right after."""
        inst = self.existing_instance(info_text, child.name)
        if inst is not None and self.enter_and_crawl(
                child, path, labels, f"{child.name} {inst}", prompt_here, rollback=None):
            return True
        m = PARAM_STR_RE.search(arg_help)
        removable = re.search(rf"\[no\]\s+{re.escape(child.name)}\b", level_help)
        if m and removable and child.name not in CREATE_EXCLUDE:
            tmp = TMP_NAME[: max(1, int(m.group(1)))] if m.group(1) else TMP_NAME
            return self.enter_and_crawl(
                child, path, labels, f"{child.name} {tmp}", prompt_here,
                rollback=f"no {child.name} {tmp}")
        return False

    def crawl(self, node: Node, path: list[str], labels: list[str] | None = None):
        labels = path if labels is None else labels
        ctx = " ".join(labels) or "<root>"
        prompt_here = self.conn.find_prompt()
        level = capture_help(self.conn, "")
        self.record("level", ctx, "", level)
        self.log(f"[{len(self.records):4d}] level  {ctx}", flush=True)

        info_text = None  # fetched lazily, once per level, on first param child
        for child in node.children:
            if child.is_context and not self.enter_forbidden(child.name):
                nav(self.conn, child.name)
                if self.conn.find_prompt() == prompt_here:
                    # Prompt didn't move — usually parameterized, but stray
                    # buffered output can fake this on a plain context (lost
                    # `configure crypto` once). Re-ground and retry before
                    # classifying.
                    self.resync(path)
                    nav(self.conn, child.name)
                if self.conn.find_prompt() == prompt_here:
                    # Prompt still didn't move: needs an argument (parameterized).
                    arg = capture_help(self.conn, child.name + " ")
                    entered = False
                    if path and path[0] == "configure":  # never under quick-setup etc.
                        if info_text is None:
                            info_text = self.level_info()
                        entered = self.try_enter_parameterized(
                            child, path, labels, level, arg, info_text, prompt_here)
                    if entered:
                        self.record("args-param", ctx, child.name, arg)
                        self.log(f"[{len(self.records):4d}] param+ {ctx} > {child.name} (entered)", flush=True)
                    else:
                        self.parameterized.append(f"{ctx} > {child.name}")
                        self.record("args-noenter", ctx, child.name, arg)
                        self.log(f"[{len(self.records):4d}] param  {ctx} > {child.name}", flush=True)
                    continue
                self.crawl(child, path + [child.name], labels + [child.name])
                nav(self.conn, "exit")
                if self.conn.find_prompt() != prompt_here:
                    self.resync(path)  # lost position — renavigate from root
            else:
                arg = capture_help(self.conn, child.name + " ")
                self.record("args", ctx, child.name, arg)
                self.log(f"[{len(self.records):4d}] args   {ctx} > {child.name}", flush=True)


# ------------------------------------------------------- merge / diff / io


def jsonl_path_for(family: str) -> Path:
    return REFERENCE_DIR / f"cli-help-{family}.jsonl"


def load_records(family: str) -> dict[Key, dict]:
    path = jsonl_path_for(family)
    if not path.exists():
        return {}
    out: dict[Key, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            e = json.loads(line)
            out[(e["context"], e["prefix"])] = e
    return out


def write_records(family: str, records: dict[Key, dict]):
    def sort_key(k: Key):
        ctx, prefix = k
        return (ctx != "<root>", ctx, prefix != "", prefix)  # root first, level before args
    path = jsonl_path_for(family)
    with path.open("w", encoding="utf-8") as f:
        for k in sorted(records, key=sort_key):
            f.write(json.dumps(records[k], ensure_ascii=False) + "\n")


def diff_report(old: dict[Key, dict], new: dict[Key, dict], in_scope) -> str:
    """Human summary of what this run changed, scoped to what was re-crawled."""
    old_scoped = {k: v for k, v in old.items() if in_scope(k[0])}
    added = [k for k in new if k not in old_scoped]
    removed = [k for k in old_scoped if k not in new]
    changed = [k for k in new if k in old_scoped
               and (new[k]["text"] != old_scoped[k]["text"]
                    or new[k]["kind"] != old_scoped[k]["kind"])]

    def fmt(keys):
        return "".join(f"    {ctx} :: {prefix or '<level>'}\n" for ctx, prefix in sorted(keys)[:40]) \
            + (f"    ... and {len(keys) - 40} more\n" if len(keys) > 40 else "")

    if not old_scoped:
        return f"First harvest for this scope: {len(new)} captures recorded.\n"
    lines = [f"Diff vs previous harvest (scope: {len(old_scoped)} old / {len(new)} new captures):"]
    lines.append(f"  ADDED   {len(added)}\n" + fmt(added) if added else "  ADDED   0")
    lines.append(f"  REMOVED {len(removed)}\n" + fmt(removed) if removed else "  REMOVED 0")
    lines.append(f"  CHANGED {len(changed)}\n" + fmt(changed) if changed else "  CHANGED 0")
    if not (added or removed or changed):
        lines.append("  No CLI changes detected — firmware behavior identical for this scope.")
    return "\n".join(lines)


# ------------------------------------------------------------------ render


def render(family: str, device_label: str) -> Path:
    entries = list(load_records(family).values())
    out = [
        f"# {family} CLI reference (harvested `?` help)",
        "",
        f"Captured live from {device_label} on "
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%d')} by scripts/harvest_cli.py",
        "(re-run `harvest` after firmware upgrades — it diffs and updates in place).",
        "Every section is a CLI context: first the level `?` listing (commands +",
        "descriptions), then per-command argument help (`<command> ?`). Sections",
        "ending in NAME are parameterized contexts harvested through one instance",
        "(an existing one, or a temp object created and rolled back) — NAME stands",
        "for any instance. Entries marked *(not entered)* could not be harvested",
        "safely — their inner structure is in command-tree-" + family + ".md; use",
        "cli_help with a real index for inner argument syntax.",
        "",
    ]
    contexts: dict[str, list[dict]] = {}
    for e in entries:
        contexts.setdefault(e["context"], []).append(e)
    for ctx, ctx_entries in contexts.items():
        out.append(f"## {ctx}")
        out.append("")
        for e in ctx_entries:
            if e["kind"] == "level":
                out.append("Level help (`?`):")
            elif e["kind"] == "args-noenter":
                out.append(f"### {e['prefix']} *(not entered — parameterized context)*")
            elif e["kind"] == "args-param":
                out.append(f"### {e['prefix']} *(parameterized — inner help harvested "
                           f"under \"{ctx} {e['prefix']} NAME\")*")
            else:
                out.append(f"### {e['prefix']}")
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
    ap.add_argument("--branch", default="",
                    help="only re-crawl this subtree, top-level or nested "
                         "(e.g. configure, or \"configure crypto\")")
    args = ap.parse_args()

    dev = get_device(args.device)
    family = dev.family
    label = f"{dev.name} ({dev.description})"

    if args.mode == "render":
        print(f"Rendered: {render(family, label)}")
        return

    if args.mode == "probe":
        _, conn = connect(args.device)
        try:
            print("PROMPT root:", repr(conn.find_prompt()))
            print("ENTER configure system ->", repr(nav(conn, "configure system")))
            print("PROMPT in-context:", repr(conn.find_prompt()))
            print("EXIT ->", repr(nav(conn, "exit all")))
            print("PROMPT after exit all:", repr(conn.find_prompt()))
            print("LEVEL HELP at root:", repr(capture_help(conn, "")[:400]))
            print("PROMPT after help capture:", repr(conn.find_prompt()))
        finally:
            conn.disconnect()
        return

    # ---- harvest: live tree -> crawl -> diff -> canonical rewrite -> render
    REFERENCE_DIR.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    _, conn = connect(args.device)
    scratch = jsonl_path_for(family).with_suffix(".jsonl.partial")
    try:
        print("Capturing live `tree` ...", flush=True)
        tree_text = capture_tree(conn)
        tree = parse_tree_text(tree_text)
        if not tree.children:
            raise SystemExit("Live `tree` capture came back empty — aborting, nothing overwritten.")
        write_tree_md(family, label, tree_text)
        print(f"Tree: {sum(1 for _ in iter_nodes(tree))} nodes.", flush=True)

        if args.branch:
            node = tree  # prune to the single chain leading to the branch
            for part in args.branch.split():
                nxt = next((c for c in node.children if c.name == part), None)
                if nxt is None:
                    raise SystemExit(f"Branch '{args.branch}' not found in the live tree.")
                node.children = [nxt]
                node = nxt

        h = Harvester(conn, scratch)
        h.crawl(tree, [])
        h.scratch.close()
    finally:
        conn.disconnect()

    old = load_records(family)
    if args.branch:
        # Scope excludes <root>: the filtered tree hides the other root leaves,
        # so treating root as in-scope would falsely report them as removed.
        b = args.branch
        def in_scope(ctx: str) -> bool:
            return ctx == b or ctx.startswith(b + " ")
    else:
        def in_scope(ctx: str) -> bool:
            return True

    new_scoped = {k: v for k, v in h.records.items() if in_scope(k[0])}
    report = diff_report(old, new_scoped, in_scope)
    merged = {k: v for k, v in old.items() if not in_scope(k[0])}
    merged.update(h.records)  # branch replaced; re-captured root keys refreshed too
    write_records(family, merged)
    scratch.unlink(missing_ok=True)

    mins = (time.monotonic() - started) / 60
    print(f"\nDone: {len(h.records)} captures in {mins:.1f} min "
          f"-> {jsonl_path_for(family)} ({len(merged)} total records)")
    print(report)
    if h.entered_existing:
        print(f"\nParameterized entered via EXISTING instance ({len(h.entered_existing)}):")
        for line in h.entered_existing:
            print(f"    {line}")
    if h.created:
        print(f"\nParameterized entered via TEMP object ({len(h.created)}):")
        for line in h.created:
            print(f"    {line}")
        print("  Rollback results:")
        for cmd, out in h.rolled_back:
            print(f"    {cmd} -> {out or 'ok'}")
        leftovers = len(h.created) - len(h.rolled_back)
        if leftovers:
            print(f"  WARNING: {leftovers} temp object(s) without a recorded rollback — verify on device!")
    if h.parameterized:
        print(f"\nParameterized (not entered): {len(h.parameterized)}")
    print(f"Rendered: {render(family, label)}")


def iter_nodes(node: Node):
    for c in node.children:
        yield c
        yield from iter_nodes(c)


if __name__ == "__main__":
    main()
