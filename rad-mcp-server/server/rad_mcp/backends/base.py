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
