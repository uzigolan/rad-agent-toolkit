"""CLI backend built on Netmiko's `rad_etx` (and future RAD) device types.

Speaks SSH by default; a device with `transport: telnet` in the inventory is
driven over Netmiko's `<device_type>_telnet` variant instead — same session
caching, prompt anchoring, and command semantics on both transports."""
from __future__ import annotations

import re
import threading
import time
from contextlib import contextmanager

from fastmcp.exceptions import ToolError
from netmiko import ConnectHandler

from ..drivers import get_driver
from ..inventory import Device
from .base import Backend

# Trailing \s*\n is required (not just \s*(\d+)) so a key code that arrives
# split across two channel reads can't get matched — and its digits
# captured — before the rest of the number has actually landed.
_KEY_CODE_RE = re.compile(r"Key code:\s*(\d+)\s*\n")
# Regex that never matches — forces _read_until_re to always fall through to
# its quiet-period drain, for callers with no anchored end-of-output pattern.
_NEVER_MATCH = re.compile(r"(?!)")


class SSHBackend(Backend):
    """One persistent CLI session per device, reused across tool calls.

    Opening a RAD SSH session costs several seconds, and the unit refuses a
    new session while a previous one is still being torn down — so tearing
    the connection down after every tool call made each call pay both costs.
    Instead, sessions are cached per device and re-grounded (`exit all`) at
    the start of every operation; a session that died in between is replaced
    transparently. Reads are anchored on the device prompt so they return
    the moment the CLI is ready instead of waiting out a quiet-period timer.
    """

    def __init__(self) -> None:
        self._conns: dict[str, object] = {}
        self._locks: dict[str, threading.Lock] = {}
        self._last_used: dict[str, float] = {}
        self._guard = threading.Lock()
        # Devices whose cached connection currently sits inside the debug OS
        # shell (VxWorks/Linux), not the normal RAD CLI — while set, _session
        # must not send RAD-CLI re-grounding ("exit all") into a foreign shell.
        self._in_debug_shell: dict[str, bool] = {}
        # Devices sitting at the `password>` prompt after debug_logon_request,
        # waiting for debug_logon_submit — _session must not reground here
        # either, since the CLI isn't back at its normal prompt yet.
        self._awaiting_debug_password: dict[str, bool] = {}
        # Devices whose cached connection is parked mid-navigation inside the
        # unlocked `debug` menu tree (e.g. an FPGA submenu) after a debug_menu
        # call — _session must not reground here either, or the next
        # debug_menu call silently loses its place (exit all bounces it back
        # to the top RAD CLI). Cleared by debug_menu(reset=true).
        self._in_debug_menu: dict[str, bool] = {}

    def _lock(self, device: Device) -> threading.Lock:
        with self._guard:
            return self._locks.setdefault(device.name, threading.Lock())

    def _connect(self, device: Device, timeout: int):
        driver = get_driver(device.family)
        # Per-family SSH tuning (legacy KEX/ciphers, timeouts, keepalive for old
        # or unstable links). The driver's options override this baseline.
        # (Keys are BaseConnection params, so the telnet variant accepts them
        # too — SSH-only ones are simply ignored there.)
        opts = {"conn_timeout": 15, **getattr(driver, "ssh_connect_options", {})}
        device_type = driver.netmiko_device_type
        if device.transport == "telnet":
            device_type += "_telnet"
        # RAD units refuse a new SSH session while the previous one is still
        # being torn down (Paramiko surfaces this as "No existing session"),
        # so retry connection setup with a backoff — both tunable per family.
        attempts = max(1, getattr(driver, "connect_attempts", 3))
        backoff = getattr(driver, "connect_backoff", 2.0)
        last_exc: Exception | None = None
        for attempt in range(attempts):
            if attempt:
                time.sleep(backoff * attempt)
            try:
                return ConnectHandler(
                    device_type=device_type,
                    host=device.host,
                    port=device.port,
                    username=device.username,
                    password=device.password,
                    timeout=timeout,
                    **opts,
                )
            except Exception as exc:
                last_exc = exc
        raise last_exc

    @staticmethod
    def _prompt_re(conn) -> str:
        # RAD prompts always end the output: "SF-1p-187>config>crypto#" or
        # "...server(name)$" for uncommitted objects.
        return re.escape(conn.base_prompt) + r"[^\n]*[#\$] ?$"

    def _run(self, conn, command: str, timeout: int) -> str:
        """Send one line and read until the prompt reappears."""
        try:
            # strip_prompt/strip_command stay at their True defaults so output
            # keeps the old send_command_timing shape (no echo, no trailing
            # prompt) — config backups and stage previews depend on that.
            return conn.send_command(
                command,
                expect_string=self._prompt_re(conn),
                read_timeout=timeout,
            )
        except Exception:
            # The prompt pattern didn't show (unusual output shape). Drain
            # passively — never re-send, the command may already have run.
            return self._drain(conn, quiet=0.5, limit=5.0)

    @staticmethod
    def _drain(conn, quiet: float = 0.2, limit: float = 2.0) -> str:
        out = ""
        deadline = time.monotonic() + limit
        idle = 0.0
        while time.monotonic() < deadline:
            time.sleep(0.1)
            chunk = conn.read_channel()
            if chunk:
                out += chunk
                idle = 0.0
            else:
                idle += 0.1
                if idle >= quiet:
                    break
        return out

    @contextmanager
    def _session(self, device: Device, timeout: int):
        with self._lock(device):
            conn = self._conns.pop(device.name, None)
            # Inside the debug OS shell, or mid-way through the logon debug
            # challenge (sitting at "password>"), "exit all" and RAD-style
            # liveness probing are meaningless (or harmful) — the caller
            # drives the channel directly instead.
            skip_reground = (
                self._in_debug_shell.get(device.name, False)
                or self._awaiting_debug_password.get(device.name, False)
                or self._in_debug_menu.get(device.name, False)
            )
            if conn is not None:
                try:
                    conn.read_channel()  # drop residue from a previous call
                    if not skip_reground:
                        if time.monotonic() - self._last_used.get(device.name, 0.0) > 60:
                            conn.find_prompt()  # liveness probe — raises if it died
                        self._run(conn, "exit all", 10)
                except Exception:
                    try:
                        conn.disconnect()
                    except Exception:
                        pass
                    conn = None
                    self._in_debug_shell.pop(device.name, None)
                    self._awaiting_debug_password.pop(device.name, None)
                    self._in_debug_menu.pop(device.name, None)
            if conn is None:
                conn = self._connect(device, timeout)
                self._run(conn, "exit all", 10)
            try:
                yield conn
            except Exception:
                # Unknown session state — retire it; next call reconnects.
                try:
                    conn.disconnect()
                except Exception:
                    pass
                self._in_debug_shell.pop(device.name, None)
                self._awaiting_debug_password.pop(device.name, None)
                self._in_debug_menu.pop(device.name, None)
                raise
            else:
                self._conns[device.name] = conn
                self._last_used[device.name] = time.monotonic()

    def execute(self, device: Device, command: str, timeout: int = 30) -> str:
        with self._session(device, timeout) as conn:
            return self._run(conn, command, timeout)

    def execute_many(self, device: Device, commands: list[str], timeout: int = 30) -> list[tuple[str, str]]:
        """Run several commands over ONE session, preserving order and duplicates."""
        with self._session(device, timeout) as conn:
            return [(cmd, self._run(conn, cmd, timeout)) for cmd in commands]

    def interactive_help(self, device: Device, navigation: list[str], prefix: str,
                         timeout: int = 30) -> str:
        """Relay the RAD CLI's `?` help: navigate, type `<prefix>?` without
        Enter, collect the help text, then clear the pending line (Ctrl-U) so
        nothing is ever executed."""
        with self._session(device, timeout) as conn:
            for line in navigation:
                self._run(conn, line, timeout)
            # After the help, the CLI reprints the prompt plus the pending
            # input — that line is the end-of-help signature.
            end_re = re.compile(
                re.escape(conn.base_prompt) + r"[^\n]*[#\$] ?"
                + re.escape(prefix.rstrip()) + r" ?$"
            )
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
                    tail = output.rstrip()
                    if tail and end_re.search(tail.splitlines()[-1]):
                        break
                elif output:
                    quiet += 0.1
                    if quiet >= 0.6:  # fallback: help printed, channel quiet
                        break
            conn.write_channel("\x15")  # Ctrl-U: discard the re-echoed pending input
            self._drain(conn)  # swallow the redraw fully before the next call
            return output

    def push_config(self, device: Device, lines: list[str], timeout: int = 60) -> str:
        with self._session(device, timeout) as conn:
            transcript = []
            for line in lines:
                out = self._run(conn, line, timeout)
                transcript.append(f"> {line}\n{out}")
            return "\n".join(transcript)

    @staticmethod
    def _read_until_re(conn, pattern: re.Pattern, timeout: float) -> str:
        """Poll the channel until `pattern` matches the accumulated output,
        or give up once output has gone quiet for a bit. Same shape as
        interactive_help's loop, generalized to an arbitrary end pattern
        instead of one fixed end-of-help signature."""
        output = ""
        deadline = time.monotonic() + timeout
        quiet = 0.0
        while time.monotonic() < deadline:
            time.sleep(0.1)
            chunk = conn.read_channel()
            if chunk:
                output += chunk
                quiet = 0.0
                if pattern.search(output):
                    break
            elif output:
                quiet += 0.1
                if quiet >= 0.6:
                    break
        return output

    def debug_logon_request(self, device: Device, timeout: int = 15) -> str:
        """Send `logon debug` and return the raw numeric key-code challenge.
        Decryption is NOT done here — the caller (the model, or whoever/
        whatever it hands the code to) computes the password out-of-band
        and returns it via debug_logon_submit.

        The connection is left parked at the device's `password>` prompt,
        cached under this device's name same as any other session — the
        awaiting-password flag just tells _session not to reground it in
        the meantime. Nothing else should be run against this device until
        debug_logon_submit (or a failure) clears that flag."""
        with self._session(device, timeout) as conn:
            conn.write_channel("logon debug\n")
            challenge = self._read_until_re(conn, _KEY_CODE_RE, timeout)
            match = _KEY_CODE_RE.search(challenge)
            if not match:
                raise ToolError(
                    "logon debug did not present a 'Key code:' challenge — unexpected CLI response"
                )
            self._awaiting_debug_password[device.name] = True
            return match.group(1)

    def debug_logon_submit(self, device: Device, password: str, timeout: int = 15) -> None:
        """Submit the password for a pending debug_logon_request challenge
        and confirm the CLI is back at its normal prompt."""
        if not self._awaiting_debug_password.get(device.name):
            raise ToolError(
                f"{device.name} has no pending debug logon challenge — call debug_logon_request first"
            )
        with self._session(device, timeout) as conn:
            conn.write_channel(password + "\n")
            prompt_re = re.compile(self._prompt_re(conn))
            confirm = self._read_until_re(conn, prompt_re, timeout)
            self._awaiting_debug_password.pop(device.name, None)
            if not prompt_re.search(confirm):
                raise ToolError(
                    "logon debug password was not accepted (CLI did not return to its normal prompt)"
                )

    def debug_menu(self, device: Device, commands: list[str], timeout: int = 30,
                   reset: bool = False) -> str:
        """Run a sequence of commands inside the already-unlocked `debug`
        tree. By default (reset=False) CONTINUES from wherever the previous
        debug_menu call left off — no re-grounding — so a submenu entered
        by one call (e.g. `debug mea` dropping into an FPGA console) is
        still current on the next call, letting the caller probe one
        command at a time without losing its place. Pass reset=True to
        force `exit all` back to the top RAD CLI first (e.g. to abandon a
        wrong navigation path). Submenu prompts (e.g. `FPGA>>`,
        `FPGA>MEA>>`) are family/FPGA-specific and don't contain
        conn.base_prompt, so each line is drained on a quiet period rather
        than matched against an expected prompt."""
        if reset:
            self._in_debug_menu.pop(device.name, None)
        with self._session(device, timeout) as conn:
            transcript = []
            for cmd in commands:
                conn.write_channel(cmd + "\n")
                out = self._read_until_re(conn, _NEVER_MATCH, min(timeout, 5.0))
                transcript.append(f"> {cmd}\n{out}")
            self._in_debug_menu[device.name] = True
            return "\n".join(transcript)

    def enter_debug_shell(self, device: Device, timeout: int = 15) -> str:
        """Send the family's debug-tree shell-entry command (e.g. `debug
        shell`) and drain the response. Same shape as debug_menu: the
        resulting OS prompt (VxWorks `->`, a Linux `root@host:~#`, etc.) is
        family-specific and not matched against an expected regex — this
        just gets you in and hands back whatever the device printed."""
        driver = get_driver(device.family)
        if not driver.debug_shell_enter_cmd:
            raise ToolError(
                f"debug shell not yet supported for family '{device.family}' — "
                "populate debug_shell_enter_cmd/exit_cmd on its driver once confirmed"
            )
        with self._session(device, timeout) as conn:
            conn.write_channel(driver.debug_shell_enter_cmd + "\n")
            output = self._read_until_re(conn, _NEVER_MATCH, min(timeout, 5.0))
            self._in_debug_shell[device.name] = True
            self._in_debug_menu.pop(device.name, None)
            return output

    def raw_shell_command(self, device: Device, command: str, timeout: int = 30) -> str:
        """Run one command inside an already-entered debug OS shell — no
        whitelist, no anchored prompt, just drained like debug_menu."""
        if not self._in_debug_shell.get(device.name):
            raise ToolError(f"{device.name} is not inside a debug shell — call enter_debug_shell first")
        with self._session(device, timeout) as conn:
            conn.write_channel(command + "\n")
            return self._read_until_re(conn, _NEVER_MATCH, min(timeout, 5.0))

    def exit_debug_shell(self, device: Device, timeout: int = 15) -> str:
        driver = get_driver(device.family)
        with self._session(device, timeout) as conn:
            output = ""
            if driver.debug_shell_exit_cmd:
                conn.write_channel(driver.debug_shell_exit_cmd + "\n")
                output = self._read_until_re(conn, re.compile(self._prompt_re(conn)), timeout)
            self._in_debug_shell.pop(device.name, None)
            self._run(conn, "exit all", 10)  # re-ground now that we're back in the RAD CLI
            return output
