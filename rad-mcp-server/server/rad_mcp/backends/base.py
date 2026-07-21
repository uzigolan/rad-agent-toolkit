"""Backend ABC: how bytes reach a device (SSH now, RADview NB API later)."""
from __future__ import annotations

from abc import ABC, abstractmethod

from ..inventory import Device


class Backend(ABC):
    @abstractmethod
    def execute(self, device: Device, command: str, timeout: int = 30) -> str:
        """Run one read command, return raw output."""

    @abstractmethod
    def push_config(self, device: Device, lines: list[str], timeout: int = 60) -> str:
        """Send a sequence of configuration lines, return the session transcript."""

    def interactive_help(self, device: Device, navigation: list[str], prefix: str,
                         timeout: int = 30) -> str:
        """Send `<prefix>?` (no newline) and return the CLI's interactive help.

        Optional capability: only interactive-terminal backends (SSH) can do
        this; API backends (RADview) have no `?` keypress to relay.
        """
        raise NotImplementedError(f"{type(self).__name__} does not support interactive help")

    def debug_logon_request(self, device: Device, timeout: int = 15) -> str:
        """Send `logon debug` and return the raw numeric key-code
        challenge. Decryption happens outside the backend — see
        debug_logon_submit. Optional capability: only interactive-terminal
        backends (SSH) can relay this challenge/response.
        """
        raise NotImplementedError(f"{type(self).__name__} does not support debug_logon_request")

    def debug_logon_submit(self, device: Device, password: str, timeout: int = 15) -> None:
        """Submit the password for a pending debug_logon_request challenge,
        unlocking the device's hidden `debug` command tree. Optional
        capability."""
        raise NotImplementedError(f"{type(self).__name__} does not support debug_logon_submit")

    def debug_menu(self, device: Device, commands: list[str], timeout: int = 30,
                   reset: bool = False) -> str:
        """Run commands inside the already-unlocked `debug` tree. By default
        continues from wherever the previous call left off (no
        re-grounding); reset=True forces `exit all` back to the top RAD CLI
        first. Optional capability."""
        raise NotImplementedError(f"{type(self).__name__} does not support debug_menu")

    def enter_debug_shell(self, device: Device, timeout: int = 15) -> str:
        """Drop an already-debug_logon'd session into the device's real OS
        shell (VxWorks/Linux, per driver). Optional capability."""
        raise NotImplementedError(f"{type(self).__name__} does not support enter_debug_shell")

    def raw_shell_command(self, device: Device, command: str, timeout: int = 30) -> str:
        """Run one command inside an already-entered OS shell, no whitelist.
        Optional capability."""
        raise NotImplementedError(f"{type(self).__name__} does not support raw_shell_command")

    def exit_debug_shell(self, device: Device, timeout: int = 15) -> str:
        """Leave the OS shell, returning to the normal RAD CLI. Optional
        capability."""
        raise NotImplementedError(f"{type(self).__name__} does not support exit_debug_shell")
