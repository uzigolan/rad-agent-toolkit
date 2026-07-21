"""Auto-captured log of hidden `debug`-tree navigation, per device family.

The debug command tree (menu-driven diagnostics beneath `logon debug`, e.g.
FPGA submenus) is family/FPGA-specific and deliberately NOT hardcoded
anywhere in this codebase — see docs/architecture.md item 8. The normal
`?`-help harvester can't reach it either (it's gated behind a challenge/
response, out of scope for that read-only crawl).

Instead, every debug_menu call is recorded here automatically, keyed only
by the device's family — nothing in this module names a specific family,
command, or submenu. Over time this turns live, one-off exploration into a
reusable history: a later session can check what's already been
discovered on a family before probing blind via `?` again.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

_RAD = Path(__file__).resolve().parents[2]  # rad-mcp-server/
_DIR = _RAD / "skills" / "rad-cli-operations" / "references"


def _log_path(family: str) -> Path:
    safe = "".join(c for c in family if c.isalnum() or c in "-_") or "unknown"
    return _DIR / f"debug-tree-{safe}.jsonl"


def record(family: str, device: str, commands: list[str], output: str, reset: bool,
           kind: str = "menu") -> None:
    """Append one debug-tree call's transcript to this family's log.

    `kind` distinguishes the menu-driven debug tree ("menu", e.g. debug_menu)
    from the raw OS shell beneath it ("shell", e.g. debug_shell_command) —
    both share the same log/lookup mechanism, since neither is documented
    anywhere ahead of time."""
    _DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": time.time(),
        "device": device,
        "kind": kind,
        "reset": reset,
        "commands": commands,
        "output": output[:4000],
    }
    with _log_path(family).open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def history(family: str, limit: int = 20) -> list[dict]:
    """Return this family's most recently recorded debug-tree calls (menu
    navigation and/or raw shell commands), newest first. Empty list if
    nothing has ever been recorded for it."""
    path = _log_path(family)
    if not path.exists():
        return []
    entries = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return list(reversed(entries[-limit:]))
