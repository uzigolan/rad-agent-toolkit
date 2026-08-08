"""debug group — the hidden `debug` command tree.

The highest-blast-radius group: menu-driven diagnostics, the logon key-code
challenge, and the raw OS shell beneath it (reboot/factory-reset/root access
live here). debug_tree_history is a read-only log lookup and is always
registered with the group; everything else is write-gated AND confirm-gated.
Off by default in the lean profile (RAD_MCP_DEBUG_TOOLS=true to enable).
Future home: the rad-debug server (plan 09).
"""
from __future__ import annotations

from fastmcp.exceptions import ToolError

from .. import debug_tree_log
from ..audit import audit, redact
from ..backends import get_backend
from ..drivers import get_driver
from ..inventory import get_device
from ..runtime import _DEMO_DEVICES, _demo_confirm_bypass, _demo_state


def register_debug_tools(mcp, *, write_enabled: bool) -> None:
    """Register the 8 debug-tree tools (7 of them only when `write_enabled`)."""

    @mcp.tool()
    def debug_tree_history(family: str, limit: int = 20) -> list[dict]:
        """Look up what's already been discovered in a family's hidden `debug`
        tree — both the menu-driven diagnostics (debug_menu) and the raw OS
        shell beneath it (enter_debug_shell/debug_shell_command) — before
        probing it live.

        Neither is hardcoded or pre-documented anywhere in this codebase — every
        debug_menu / enter_debug_shell / debug_shell_command call auto-records
        its commands and output here, keyed by family (each entry's `kind` is
        "menu" or "shell"), so a later session (or a later step in this one) can
        check prior navigation instead of rediscovering the same path blind.
        Returns the most recent entries first; empty if nothing's been recorded
        yet for this family. For safety, the recorded source-device name is not
        returned to callers (history is path evidence, not a target-device list).
        Read-only, no write scope required.
        """
        get_driver(family)  # raises with the valid-family list if unknown
        rows = debug_tree_log.history(family, limit=limit)
        # Never leak historical source-device names through this read path.
        out: list[dict] = []
        for r in rows:
            rr = dict(r)
            rr.pop("device", None)
            out.append(rr)
        return out

    if not write_enabled:
        return

    from ..runtime import _require_write_scope

    @mcp.tool()
    def debug_logon_request(device: str, confirm: bool = False) -> dict:
        """Start unlocking a device's hidden `debug` command tree: sends
        `logon debug` and returns the device's numeric key-code challenge.
        This tool does NOT decrypt it — compute the password for the
        returned key_code (however that's done — the algorithm is
        confidential and lives outside this server) and pass it to
        debug_logon_submit to finish.

        The device is left waiting at its `password>` prompt; don't run
        other tools against it until debug_logon_submit (or a failure)
        clears that. The debug tree includes dangerous commands (reboot,
        factory reset, the raw OS shell) — write-gated + confirm=true like
        commit_config.
        """
        _require_write_scope()
        if not confirm and not _demo_confirm_bypass(device):
            return {"status": "REFUSED: debug_logon_request requires confirm=true — this begins unlocking reboot/shell/factory-reset access."}
        dev = get_device(device)
        if _demo_state(dev.name):
            state = _demo_state(dev.name) or {}
            key_code = state.get("debug_key_code", "424242")
            audit("debug_logon_request", device, detail="demo key code issued", ok=True)
            return {
                "key_code": key_code,
                "next_step": f"Call debug_logon_submit('{device}', password=<value>) to unlock demo debug mode.",
            }
        key_code = get_backend().debug_logon_request(dev)
        audit("debug_logon_request", device, detail="key code issued", ok=True)
        return {
            "key_code": key_code,
            "next_step": f"Compute the password for this key_code, then call "
                         f"debug_logon_submit('{device}', password=<value>, confirm=true).",
        }

    @mcp.tool()
    def debug_logon_submit(device: str, password: str, confirm: bool = False) -> str:
        """Finish a debug_logon_request challenge: submits `password` (the
        value computed for the key_code that call returned) and confirms
        the device is back at its normal CLI prompt, debug mode unlocked.
        The password is never logged."""
        _require_write_scope()
        if not confirm and not _demo_confirm_bypass(device):
            return "REFUSED: debug_logon_submit requires confirm=true."
        dev = get_device(device)
        if _demo_state(dev.name):
            _DEMO_DEVICES[dev.name]["debug_unlocked"] = True
            audit("debug_logon_submit", device, detail="demo debug mode unlocked", ok=True)
            return f"Debug mode unlocked on {device}. (demo)"
        get_backend().debug_logon_submit(dev, password)
        audit("debug_logon_submit", device, detail="debug mode unlocked", ok=True)
        return f"Debug mode unlocked on {device}."

    @mcp.tool()
    def debug_access_preflight(
        device: str,
        target: str = "mea",
        commands: list[str] | None = None,
        confirm: bool = False,
        reset: bool = False,
    ) -> dict:
        """Dedicated unlock-first flow for debug operations.

        Tries one targeted action using the current session first (reuses an
        existing unlock if someone already opened debug recently). If that
        action fails, issues a fresh debug key-code challenge immediately so
        the caller can submit a new password via debug_logon_submit.

        target:
          - mea   -> probe via debug_menu (default command: ["debug mea"])
          - menu  -> probe via debug_menu (default command: ["debug"])
          - shell -> probe via enter_debug_shell

        For target=mea/menu, pass `commands` to test a specific bundle.
        For target=shell, `commands` is ignored.
        """
        _require_write_scope()
        if not confirm and not _demo_confirm_bypass(device):
            return {
                "status": "REFUSED: debug_access_preflight requires confirm=true.",
                "target": target,
            }

        dev = get_device(device)
        mode = (target or "mea").strip().lower()
        if mode not in ("mea", "menu", "shell"):
            raise ToolError("target must be one of: mea, menu, shell")

        probe_commands = list(commands or (["debug mea"] if mode == "mea" else ["debug"]))

        if _demo_state(dev.name):
            state = _demo_state(dev.name) or {}
            if state.get("debug_unlocked"):
                audit("debug_access_preflight", device, detail=f"demo target={mode} reused unlock", ok=True)
                return {
                    "status": "ready",
                    "target": mode,
                    "used_existing_unlock": True,
                    "next_step": "Run your debug action directly (debug already unlocked).",
                }
            key_code = state.get("debug_key_code", "424242")
            audit("debug_access_preflight", device, detail=f"demo target={mode} key issued", ok=True)
            return {
                "status": "unlock_required",
                "target": mode,
                "used_existing_unlock": False,
                "key_code": key_code,
                "next_step": (
                    f"Call debug_logon_submit('{device}', password=<value>, confirm=true), "
                    f"then retry your {mode} action."
                ),
            }

        backend = get_backend()
        try:
            if mode == "shell":
                output = backend.enter_debug_shell(dev)
                action = "enter_debug_shell"
            else:
                output = backend.debug_menu(dev, probe_commands, reset=reset)
                action = "debug_menu"

            out = redact(output)
            audit("debug_access_preflight", device,
                  detail=f"target={mode} action={action} reused unlock", ok=True)
            if mode == "shell":
                next_step = "Debug shell is active; run debug_shell_command or exit_debug_shell."
            else:
                next_step = "Debug access is ready; continue with your targeted debug_menu commands."
            return {
                "status": "ready",
                "target": mode,
                "used_existing_unlock": True,
                "action": action,
                "probe_commands": [] if mode == "shell" else probe_commands,
                "output": out,
                "next_step": next_step,
            }
        except Exception as exc:
            # Any failed probe is treated as stale/locked debug access: request
            # a fresh key challenge so callers can continue immediately.
            reason = str(exc)
            try:
                key_code = backend.debug_logon_request(dev)
            except Exception as unlock_exc:
                audit("debug_access_preflight", device,
                      detail=f"target={mode} probe failed and key request failed: {reason}", ok=False)
                raise ToolError(
                    f"debug preflight failed ({reason}) and key request also failed ({unlock_exc})"
                ) from unlock_exc

            audit("debug_access_preflight", device,
                  detail=f"target={mode} probe failed; key issued", ok=True)
            return {
                "status": "unlock_required",
                "target": mode,
                "used_existing_unlock": False,
                "probe_commands": [] if mode == "shell" else probe_commands,
                "probe_error": reason,
                "key_code": key_code,
                "next_step": (
                    f"Compute password for key_code and call "
                    f"debug_logon_submit('{device}', password=<value>, confirm=true), "
                    f"then retry your {mode} action."
                ),
            }

    @mcp.tool()
    def debug_menu(device: str, commands: list[str], confirm: bool = False,
                   reset: bool = False) -> str:
        """Run commands inside the already-unlocked `debug` tree (call
        debug_logon_request/submit first).

        By default (reset=False) this CONTINUES from wherever the previous
        debug_menu call on this device left off — no re-grounding. Submenu
        trees (mea/alarms/db/...) are family- and FPGA-specific, undocumented,
        and not whitelisted like run_show, so expect to explore them with
        `?` one command at a time (e.g. call 1: ["debug mea"], call 2:
        ["?"], call 3: ["version"] once you see the right subcommand) —
        each call picks up right where the last one left off, so probing
        step by step does NOT cost you your place in the menu. Pass
        reset=True only when you want to abandon the current navigation and
        force `exit all` back to the top RAD CLI first.
        """
        _require_write_scope()
        if not confirm and not _demo_confirm_bypass(device):
            return "REFUSED: debug_menu requires confirm=true."
        dev = get_device(device)
        if _demo_state(dev.name):
            state = _demo_state(dev.name) or {}
            if not state.get("debug_unlocked"):
                return "REFUSED: demo debug mode is locked; call debug_logon_request then debug_logon_submit first."
            out = "DEMO DEBUG OK\n" + "\n".join(f"{cmd}\nOK" for cmd in commands)
            audit("debug_menu", device, detail=f"demo reset={reset} " + "\\n".join(commands))
            debug_tree_log.record(dev.family, device, commands, out, reset)
            return out
        out = get_backend().debug_menu(dev, commands, reset=reset)
        audit("debug_menu", device, detail=f"reset={reset} " + "\n".join(commands))
        out = redact(out)
        debug_tree_log.record(dev.family, device, commands, out, reset)
        return out

    @mcp.tool()
    def enter_debug_shell(device: str, confirm: bool = False) -> str:
        """Drop an already-debug_logon'd session into the device's real OS
        shell (VxWorks or Ubuntu Linux, depending on family — currently
        confirmed for secflow and etx1p; other families refuse cleanly
        until their driver's debug_shell_enter_cmd is populated and
        confirmed on real hardware). Once inside, use debug_shell_command
        to run raw commands and exit_debug_shell to return to the normal
        CLI. Like debug_menu, every call auto-records to that family's
        debug-tree log — check debug_tree_history(family) first.
        """
        _require_write_scope()
        if not confirm and not _demo_confirm_bypass(device):
            return "REFUSED: enter_debug_shell requires confirm=true — this is unrestricted OS-level access."
        dev = get_device(device)
        if _demo_state(dev.name):
            state = _demo_state(dev.name) or {}
            if not state.get("debug_unlocked"):
                return "REFUSED: demo debug mode is locked; unlock it first with debug_logon_request/debug_logon_submit."
            _DEMO_DEVICES[dev.name]["debug_in_shell"] = True
            out = "Entered debug shell on demo device."
            audit("enter_debug_shell", device, detail="demo")
            enter_cmd = get_driver(dev.family).debug_shell_enter_cmd
            debug_tree_log.record(dev.family, device, [enter_cmd], out, reset=False, kind="shell")
            return out
        out = get_backend().enter_debug_shell(dev)
        audit("enter_debug_shell", device)
        out = redact(out)
        enter_cmd = get_driver(dev.family).debug_shell_enter_cmd
        debug_tree_log.record(dev.family, device, [enter_cmd], out, reset=False, kind="shell")
        return out or f"Entered debug shell on {device}."

    @mcp.tool()
    def debug_shell_command(device: str, command: str, confirm: bool = False) -> str:
        """Run one raw command inside an already-entered debug OS shell
        (call enter_debug_shell first). No whitelist — this is the device's
        real VxWorks/Linux shell, use with care. Auto-recorded to that
        family's debug-tree log, same as debug_menu."""
        _require_write_scope()
        if not confirm and not _demo_confirm_bypass(device):
            return "REFUSED: debug_shell_command requires confirm=true."
        dev = get_device(device)
        if _demo_state(dev.name):
            state = _demo_state(dev.name) or {}
            if not state.get("debug_in_shell"):
                return "REFUSED: demo debug shell is not active; call enter_debug_shell first."
            out = f"DEMO SHELL OK\n$ {command}\nOK"
            audit("debug_shell_command", device, detail=f"demo::{command}")
            debug_tree_log.record(dev.family, device, [command], out, reset=False, kind="shell")
            return out
        out = get_backend().raw_shell_command(dev, command)
        audit("debug_shell_command", device, detail=command)
        out = redact(out)
        debug_tree_log.record(dev.family, device, [command], out, reset=False, kind="shell")
        return out

    @mcp.tool()
    def exit_debug_shell(device: str) -> str:
        """Leave the debug OS shell, returning the session to the normal
        RAD CLI. Always safe to call."""
        _require_write_scope()
        dev = get_device(device)
        out = get_backend().exit_debug_shell(dev)
        audit("exit_debug_shell", device)
        return redact(out) or f"Exited debug shell on {device}."
