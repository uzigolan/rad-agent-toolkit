"""rad-mcp MCP server (stdio).

Tools are product-agnostic verbs; the device's `family` field selects a
driver (CLI dialect), and the backend handles transport. Write tools follow
the staged-commit flow: stage_config -> (human reviews diff) -> commit_config.

Set RAD_MCP_READONLY=true to disable all write tools at registration time.
"""
from __future__ import annotations

import os
import secrets
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import FastMCP

from . import __version__
from .audit import audit, redact
from .backends import get_backend
from .drivers import get_driver
from .inventory import get_device, load_inventory

READONLY = os.environ.get("RAD_MCP_READONLY", "").lower() in ("1", "true", "yes")
BACKUP_DIR = Path(__file__).resolve().parent.parent / "backups"

mcp = FastMCP(
    "rad-mcp",
    instructions=(
        "Operate RAD Data Communications devices (ETX-2 family and beyond). "
        "Always run health_check or test_connectivity before configuration work. "
        "Writes are staged: stage_config returns a stage_id and preview; nothing "
        "touches the device until commit_config is called with confirm=true. "
        "A running-config backup is taken automatically before every commit."
    ),
)

# In-memory staging area: stage_id -> {device, lines, created}
_STAGES: dict[str, dict] = {}


# ---------------------------------------------------------------- inventory

@mcp.tool()
def list_devices(group: str = "", family: str = "") -> list[dict]:
    """List devices from the inventory, optionally filtered by group or product family."""
    devices = load_inventory().values()
    out = []
    for d in devices:
        if group and group not in d.groups:
            continue
        if family and d.family != family:
            continue
        out.append(d.summary())
    return out


@mcp.tool()
def test_connectivity(device: str) -> str:
    """Verify SSH reachability and authentication against a device (runs no user commands)."""
    dev = get_device(device)
    try:
        get_backend().execute(dev, "", timeout=20)
        audit("test_connectivity", device, ok=True)
        return f"OK: SSH session to {dev.name} ({dev.host}) established and closed."
    except Exception as e:  # noqa: BLE001 — report, don't crash the server
        audit("test_connectivity", device, detail=str(e), ok=False)
        return f"FAILED: {redact(str(e))}"


# --------------------------------------------------------------------- read

@mcp.tool()
def run_show(device: str, command: str) -> str:
    """Run a whitelisted read-only command (show/info/help/ping...) on a device."""
    dev = get_device(device)
    driver = get_driver(dev.family)
    if not driver.is_show_allowed(command):
        allowed = ", ".join(driver.show_whitelist)
        return f"REFUSED: '{command}' is not whitelisted for {dev.family}. Allowed prefixes: {allowed}"
    out = get_backend().execute(dev, command)
    audit("run_show", device, detail=command)
    return out


@mcp.tool()
def get_config(device: str) -> str:
    """Export the device's current configuration."""
    dev = get_device(device)
    driver = get_driver(dev.family)
    out = get_backend().execute(dev, driver.config_export_command, timeout=60)
    audit("get_config", device)
    return out


@mcp.tool()
def health_check(device: str) -> dict[str, str]:
    """Run the driver-defined health sweep (device info, active alarms, ...) over one session."""
    dev = get_device(device)
    driver = get_driver(dev.family)
    results = get_backend().execute_many(dev, list(driver.health_sequence))
    audit("health_check", device)
    # Drop the navigation lines (empty output) from the result for readability
    return {cmd: out for cmd, out in results if out.strip()}


@mcp.tool()
def run_show_in_context(device: str, context: str, command: str) -> str:
    """Run a whitelisted read command inside a CLI context (RAD CLIs scope `show` to contexts).

    context: space-separated navigation path, e.g. "configure reporting" or
    "configure port ethernet 1". Only level names/indexes — never commands
    that set values. command: a whitelisted read command, e.g. "show active-alarms".
    """
    dev = get_device(device)
    driver = get_driver(dev.family)
    if not driver.is_show_allowed(command):
        allowed = ", ".join(driver.show_whitelist)
        return f"REFUSED: '{command}' is not whitelisted for {dev.family}. Allowed prefixes: {allowed}"

    tokens = context.strip().lower().split()
    if not tokens or tokens[0] not in ("configure", "admin", "file"):
        return "REFUSED: context must start with 'configure', 'admin' or 'file'."
    if tokens[0] == "configure" and len(tokens) > 1 and driver.configure_contexts \
            and tokens[1] not in driver.configure_contexts:
        known = ", ".join(driver.configure_contexts)
        return f"REFUSED: unknown configure context '{tokens[1]}'. Known: {known}"
    if any(not t.replace("-", "").replace("/", "").replace(".", "").isalnum() for t in tokens):
        return "REFUSED: context tokens may only contain letters, digits, '-', '/', '.'"

    sequence = ["exit all", context.strip(), command.strip(), "exit all"]
    results = get_backend().execute_many(dev, sequence)
    audit("run_show_in_context", device, detail=f"{context} :: {command}")
    nav_errors = [out for cmd, out in results if cmd != command.strip() and "cli error" in out.lower()]
    if nav_errors:
        return "NAVIGATION ERROR:\n" + "\n".join(nav_errors)
    return next((out for cmd, out in results if cmd == command.strip()), "")


@mcp.tool()
def cli_help(device: str, context: str = "", prefix: str = "") -> str:
    """Query the device's interactive `?` help — the authoritative, firmware-exact
    syntax reference. Use it to discover commands and validate arguments BEFORE
    staging config.

    context: navigation path ("configure system") or "" for root-level help.
    prefix: "" lists every command at that level with descriptions; a command
    name ending with a space ("location ") lists that command's arguments,
    types and constraints (e.g. [2..2 chars]). Nothing is executed on the
    device — the pending input is cleared after the help is captured.
    """
    dev = get_device(device)
    driver = get_driver(dev.family)

    if any(ord(c) < 32 for c in prefix) or any(ch in prefix for ch in ("|", ";")):
        return "REFUSED: prefix must be plain text (no control characters, '|' or ';')."
    navigation = ["exit all"]
    ctx = context.strip()
    if ctx:
        tokens = ctx.lower().split()
        if tokens[0] not in ("configure", "admin", "file"):
            return "REFUSED: context must start with 'configure', 'admin' or 'file' (or be empty for root)."
        if tokens[0] == "configure" and len(tokens) > 1 and driver.configure_contexts \
                and tokens[1] not in driver.configure_contexts:
            known = ", ".join(driver.configure_contexts)
            return f"REFUSED: unknown configure context '{tokens[1]}'. Known: {known}"
        if any(not t.replace("-", "").replace("/", "").replace(".", "").isalnum() for t in tokens):
            return "REFUSED: context tokens may only contain letters, digits, '-', '/', '.'"
        navigation.append(ctx)

    out = get_backend().interactive_help(dev, navigation, prefix)
    audit("cli_help", device, detail=f"{ctx or '<root>'} :: {prefix or '<level>'}?")
    # Trim the echoed keystrokes and the re-displayed trailing prompt line.
    lines = out.splitlines()
    if lines and lines[0].strip().endswith("?"):
        lines = lines[1:]
    while lines and (not lines[-1].strip() or lines[-1].rstrip().endswith(("#", "# " + prefix.strip(), prefix))):
        lines = lines[:-1]
    return "\n".join(lines).strip() or out.strip()


@mcp.tool()
def backup_config(device: str) -> str:
    """Export the device configuration and save it to the local backup archive."""
    dev = get_device(device)
    path = _take_backup(dev)
    return f"Backup saved: {path}"


def _take_backup(dev) -> Path:
    driver = get_driver(dev.family)
    config = get_backend().execute(dev, driver.config_export_command, timeout=60)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = BACKUP_DIR / f"{dev.name}-{stamp}.cfg"
    path.write_text(config, encoding="utf-8")
    audit("backup_config", dev.name, detail=str(path))
    return path


# ---------------------------------------------------------------- resources

REPO_ROOT = Path(__file__).resolve().parents[2]
REFERENCE_DIR = REPO_ROOT / "skills" / "rad-cli-operations" / "references"


@mcp.resource("rad://inventory")
def inventory_resource() -> str:
    """The device inventory (names, hosts, families, groups — no credentials)."""
    path = Path(os.environ.get("RAD_MCP_INVENTORY") or REPO_ROOT / "inventory.yaml")
    return path.read_text(encoding="utf-8")


@mcp.resource("rad://backups")
def backups_resource() -> str:
    """List of configuration backups in the local archive, newest first."""
    if not BACKUP_DIR.exists():
        return "(no backups yet)"
    entries = sorted(BACKUP_DIR.glob("*.cfg"), key=lambda p: p.name, reverse=True)
    return "\n".join(f"{p.name}\t{p.stat().st_size} bytes" for p in entries) or "(no backups yet)"


@mcp.resource("rad://backups/{name}")
def backup_resource(name: str) -> str:
    """Contents of one backup file from the archive (by file name)."""
    path = (BACKUP_DIR / name).resolve()
    if path.parent != BACKUP_DIR.resolve() or path.suffix != ".cfg":
        return "REFUSED: name must be a .cfg file from the backup archive."
    if not path.exists():
        return f"Unknown backup '{name}'. See rad://backups for the list."
    return path.read_text(encoding="utf-8")


@mcp.resource("rad://command-tree/{family}")
def command_tree_resource(family: str) -> str:
    """Captured CLI command tree for a product family (from live `tree`/`?` sweeps)."""
    path = (REFERENCE_DIR / f"command-tree-{family}.md").resolve()
    if path.parent != REFERENCE_DIR.resolve():
        return "REFUSED: invalid family name."
    if not path.exists():
        known = ", ".join(p.stem.removeprefix("command-tree-") for p in REFERENCE_DIR.glob("command-tree-*.md"))
        return f"No captured tree for '{family}'. Available: {known or '(none yet)'}"
    return path.read_text(encoding="utf-8")


# -------------------------------------------------------------------- write

if not READONLY:

    @mcp.tool()
    def stage_config(device: str, lines: list[str], purpose: str) -> dict:
        """Stage configuration lines for review. Nothing is sent to the device.

        Returns a stage_id and a preview. Present the preview to the user and
        only call commit_config after they explicitly approve.
        """
        dev = get_device(device)  # validates the device exists
        stage_id = secrets.token_hex(4)
        _STAGES[stage_id] = {
            "device": dev.name,
            "lines": lines,
            "purpose": purpose,
            "created": datetime.now(timezone.utc).isoformat(),
        }
        audit("stage_config", device, detail=f"{stage_id}: {purpose}")
        return {
            "stage_id": stage_id,
            "device": dev.name,
            "purpose": purpose,
            "preview": lines,
            "next_step": "Show this preview to the user; commit_config(stage_id, confirm=true) only after explicit approval.",
        }

    @mcp.tool()
    def commit_config(stage_id: str, confirm: bool = False) -> str:
        """Apply a staged config after user approval. Auto-backs-up the running config first."""
        if stage_id not in _STAGES:
            return f"Unknown stage_id '{stage_id}'. Stage the change first with stage_config."
        if not confirm:
            return "REFUSED: commit_config requires confirm=true after the user has approved the staged preview."
        stage = _STAGES.pop(stage_id)
        dev = get_device(stage["device"])
        backup_path = _take_backup(dev)
        transcript = get_backend().push_config(dev, stage["lines"])
        audit("commit_config", dev.name, detail=f"{stage_id}: {stage['purpose']}\n{transcript}")
        return (
            f"Committed stage {stage_id} to {dev.name}. Pre-commit backup: {backup_path}\n"
            f"--- session transcript ---\n{redact(transcript)}"
        )

    @mcp.tool()
    def save_startup(device: str, confirm: bool = False) -> str:
        """Persist the running configuration to startup (survives reboot)."""
        if not confirm:
            return "REFUSED: save_startup requires confirm=true after user approval."
        dev = get_device(device)
        driver = get_driver(dev.family)
        out = get_backend().execute(dev, driver.save_command)
        audit("save_startup", device)
        return out or "Saved."


def main() -> None:
    mode = "READ-ONLY" if READONLY else "read-write (staged commits)"
    audit("server_start", "-", detail=f"v{__version__} {mode}")
    mcp.run()  # stdio


if __name__ == "__main__":
    main()
