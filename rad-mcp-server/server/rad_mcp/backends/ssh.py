"""SSH backend built on Netmiko's `rad_etx` (and future RAD) device types."""
from __future__ import annotations

import time
from contextlib import contextmanager

from netmiko import ConnectHandler

from ..drivers import get_driver
from ..inventory import Device
from .base import Backend


class SSHBackend(Backend):
    @contextmanager
    def _session(self, device: Device, timeout: int):
        driver = get_driver(device.family)
        conn = ConnectHandler(
            device_type=driver.netmiko_device_type,
            host=device.host,
            port=device.port,
            username=device.username,
            password=device.password,
            timeout=timeout,
            conn_timeout=15,
        )
        try:
            yield conn
        finally:
            conn.disconnect()

    def execute(self, device: Device, command: str, timeout: int = 30) -> str:
        with self._session(device, timeout) as conn:
            # send_command_timing: ETX prompts are not always cleanly matched
            # by expect_string-based send_command on first contact.
            return conn.send_command_timing(command, read_timeout=timeout)

    def execute_many(self, device: Device, commands: list[str], timeout: int = 30) -> list[tuple[str, str]]:
        """Run several commands over ONE session, preserving order and duplicates."""
        results: list[tuple[str, str]] = []
        with self._session(device, timeout) as conn:
            for cmd in commands:
                results.append((cmd, conn.send_command_timing(cmd, read_timeout=timeout)))
        return results

    def interactive_help(self, device: Device, navigation: list[str], prefix: str,
                         timeout: int = 30) -> str:
        """Relay the RAD CLI's `?` help: navigate, type `<prefix>?` without
        Enter, collect the help text, then clear the pending line (Ctrl-U) so
        nothing is ever executed."""
        with self._session(device, timeout) as conn:
            for line in navigation:
                conn.send_command_timing(line, read_timeout=timeout)
            conn.write_channel(prefix + "?")
            output = ""
            deadline = time.monotonic() + timeout
            quiet = 0.0
            while time.monotonic() < deadline:
                time.sleep(0.3)
                chunk = conn.read_channel()
                if chunk:
                    output += chunk
                    quiet = 0.0
                elif output:
                    quiet += 0.3
                    if quiet >= 1.2:  # help printed and the channel went quiet
                        break
            conn.write_channel("\x15")  # Ctrl-U: discard the re-echoed pending input
            time.sleep(0.2)
            conn.read_channel()
            return output

    def push_config(self, device: Device, lines: list[str], timeout: int = 60) -> str:
        with self._session(device, timeout) as conn:
            transcript = []
            for line in lines:
                out = conn.send_command_timing(line, read_timeout=timeout)
                transcript.append(f"> {line}\n{out}")
            return "\n".join(transcript)
