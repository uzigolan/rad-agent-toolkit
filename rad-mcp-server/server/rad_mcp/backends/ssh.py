"""SSH backend built on Netmiko's `rad_etx` (and future RAD) device types."""
from __future__ import annotations

import re
import threading
import time
from contextlib import contextmanager

from netmiko import ConnectHandler

from ..drivers import get_driver
from ..inventory import Device
from .base import Backend


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
        self._guard = threading.Lock()

    def _lock(self, device: Device) -> threading.Lock:
        with self._guard:
            return self._locks.setdefault(device.name, threading.Lock())

    def _connect(self, device: Device, timeout: int):
        driver = get_driver(device.family)
        # RAD units refuse a new SSH session while the previous one is still
        # being torn down (Paramiko surfaces this as "No existing session"),
        # so retry connection setup with a short backoff.
        last_exc: Exception | None = None
        for attempt in range(3):
            if attempt:
                time.sleep(2.0 * attempt)
            try:
                return ConnectHandler(
                    device_type=driver.netmiko_device_type,
                    host=device.host,
                    port=device.port,
                    username=device.username,
                    password=device.password,
                    timeout=timeout,
                    conn_timeout=15,
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
            if conn is not None:
                try:
                    conn.read_channel()  # drop residue from a previous call
                    conn.find_prompt()   # liveness probe — raises if it died
                    self._run(conn, "exit all", 10)
                except Exception:
                    try:
                        conn.disconnect()
                    except Exception:
                        pass
                    conn = None
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
                raise
            else:
                self._conns[device.name] = conn

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
