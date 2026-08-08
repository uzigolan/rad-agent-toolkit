"""device group — inventory reads, CLI reads, and the staged-commit write flow.

The core operating surface: list/reach/read a device, plus the
stage_config -> (human review) -> commit_config -> save_startup write path.
The three write tools are registered only when writes are enabled
(RAD_MCP_READONLY unset; over HTTP also a write-scoped token). Future home:
the rad-device server (plan 09).
"""
from __future__ import annotations

import secrets
from datetime import datetime, timezone
from pathlib import Path

from fastmcp.exceptions import ToolError

from ..audit import audit, redact
from ..backends import get_backend
from ..drivers import get_driver
from ..inventory import get_device, load_inventory
from ..runtime import (_STAGES, _demo_config, _demo_confirm_bypass,
                       _demo_state, _write_backup_content)


def _take_backup(dev) -> Path:
    if _demo_state(dev.name):
        return _write_backup_content(dev, _demo_config(dev))
    driver = get_driver(dev.family)
    config = get_backend().execute(dev, driver.config_export_command, timeout=60)
    return _write_backup_content(dev, config)


def register_device_tools(mcp, *, write_enabled: bool) -> None:
    """Register the device read tools, plus the staged-write flow when
    `write_enabled` (readonly always wins — see runtime.WRITE_TOOLS_ENABLED)."""

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
        if _demo_state(dev.name):
            audit("test_connectivity", device, ok=True, detail="demo runtime")
            return f"OK: Demo session to {dev.name} ({dev.host}) is running."
        try:
            get_backend().execute(dev, "", timeout=20)
            audit("test_connectivity", device, ok=True)
            return f"OK: SSH session to {dev.name} ({dev.host}) established and closed."
        except Exception as e:  # noqa: BLE001 — report, don't crash the server
            audit("test_connectivity", device, detail=str(e), ok=False)
            return f"FAILED: {redact(str(e))}"

    @mcp.tool()
    def run_show(device: str, command: str) -> str:
        """Run a whitelisted read-only command (show/info/help/ping...) on a device."""
        dev = get_device(device)
        driver = get_driver(dev.family)
        if not driver.is_show_allowed(command):
            allowed = ", ".join(driver.show_whitelist)
            return f"REFUSED: '{command}' is not whitelisted for {dev.family}. Allowed prefixes: {allowed}"
        if _demo_state(dev.name):
            audit("run_show", device, detail=f"demo::{command}")
            return f"DEMO OK [{dev.family}] {command}\nNo active alarms."
        out = get_backend().execute(dev, command)
        audit("run_show", device, detail=command)
        return out

    @mcp.tool()
    def get_config(device: str) -> str:
        """Export the device's current configuration."""
        dev = get_device(device)
        if _demo_state(dev.name):
            audit("get_config", device, detail="demo")
            return _demo_config(dev)
        driver = get_driver(dev.family)
        out = get_backend().execute(dev, driver.config_export_command, timeout=60)
        audit("get_config", device)
        return out

    @mcp.tool()
    def health_check(device: str) -> dict[str, str]:
        """Run the driver-defined health sweep (device info, active alarms, ...) over one session."""
        dev = get_device(device)
        if _demo_state(dev.name):
            audit("health_check", device, detail="demo")
            return {
                "show device-information": f"Demo device {dev.name} ({dev.family})",
                "show active-alarms": "No active alarms",
                "show system": "System status: OK",
            }
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
        if _demo_state(dev.name):
            audit("run_show_in_context", device, detail=f"demo::{context} :: {command}")
            return f"DEMO OK [{context}] {command}\nNo active alarms."
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

        if _demo_state(dev.name):
            audit("cli_help", device, detail=f"demo::{ctx or '<root>'} :: {prefix or '<level>'}?")
            if prefix.endswith(" "):
                return "<CR>\n<string>"
            return "show active-alarms\nshow system\nexit"

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

    if not write_enabled:
        return

    from ..runtime import _require_write_scope

    @mcp.tool()
    def stage_config(device: str, lines: list[str], purpose: str) -> dict:
        """Stage configuration lines for review. Nothing is sent to the device.

        Returns a stage_id and a preview. Present the preview to the user and
        only call commit_config after they explicitly approve.
        """
        _require_write_scope()
        dev = get_device(device)  # validates the device exists
        # MP candidate-DB families (mp1/mp4100): enforce the verified write
        # recipe — discard-changes FIRST (clears stale candidate edits from
        # earlier sessions, which otherwise fail sanity/commit on config that
        # isn't yours), then sanity-check before commit, commit from root.
        # Verified live on mp-one 2026-07-16; requested as a hard rule.
        if dev.family in ("mp1", "mp4100"):
            toks = [l.strip().lower() for l in lines if l.strip()]
            first_real = next((t for t in toks if t != "exit all"), "")
            problems = []
            if first_real != "discard-changes":
                problems.append("BEGIN with 'discard-changes' (after an optional leading 'exit all')")
            if "sanity-check" not in toks:
                problems.append("include 'sanity-check' after the config lines (must report OK)")
            if "commit" not in toks:
                problems.append("include 'commit' (run from root — after an 'exit all', never inside a new object's $ context)")
            elif "sanity-check" in toks and toks.index("sanity-check") > toks.index("commit"):
                problems.append("put 'sanity-check' BEFORE 'commit'")
            if problems:
                raise ToolError(
                    f"REFUSED: {dev.family} uses the candidate-DB model; every staged "
                    "sequence must follow the verified MP write recipe — "
                    "discard-changes -> <config lines> -> exit all -> sanity-check -> "
                    "commit -> save. This sequence must: " + "; ".join(problems)
                )
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
        _require_write_scope()
        if stage_id not in _STAGES:
            return f"Unknown stage_id '{stage_id}'. Stage the change first with stage_config."
        stage = _STAGES[stage_id]
        if not confirm and not _demo_confirm_bypass(stage["device"]):
            return "REFUSED: commit_config requires confirm=true after the user has approved the staged preview."
        dev = get_device(stage["device"])
        backup_path = _take_backup(dev)
        if _demo_state(dev.name):
            transcript = "\n".join([f"{line}\nOK" for line in stage["lines"]])
        else:
            transcript = get_backend().push_config(dev, stage["lines"])
        # Only consume the stage once the push has succeeded, so a connection
        # failure can be retried with the same stage_id.
        _STAGES.pop(stage_id, None)
        audit("commit_config", dev.name, detail=f"{stage_id}: {stage['purpose']}\n{transcript}")
        return (
            f"Committed stage {stage_id} to {dev.name}. Pre-commit backup: {backup_path}\n"
            f"--- session transcript ---\n{redact(transcript)}"
        )

    @mcp.tool()
    def save_startup(device: str, confirm: bool = False) -> str:
        """Persist the running configuration to startup (survives reboot)."""
        _require_write_scope()
        if not confirm and not _demo_confirm_bypass(device):
            return "REFUSED: save_startup requires confirm=true after user approval."
        dev = get_device(device)
        if _demo_state(dev.name):
            audit("save_startup", device, detail="demo")
            return "Saved. (demo)"
        driver = get_driver(dev.family)
        out = get_backend().execute(dev, driver.save_command)
        audit("save_startup", device)
        return out or "Saved."
