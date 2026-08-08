"""Untrusted device-output boundary (plan 02).

Every piece of device-originated text that becomes part of a tool result is
wrapped, at this single seam, in a delimiter block:

    <device-output device="sf-163-187" family="secflow" command="show alarms" trust="untrusted">...verbatim payload...</device-output>

The payload is NEVER altered — no stripping, escaping, or normalisation
(operators need byte-exact output; the harvest pipeline depends on it, though
it talks Netmiko directly and never passes through this seam). Unwrapping is
exact: the payload is the bytes between the opening tag's ``>`` and the
closing ``</device-output>`` — no framing newlines are added.

If the payload itself contains the closing tag, a randomised nonce is added
to the tag name for that call (``<device-output-a7f3 ...>``), closing the
obvious tag-injection escape.

Trust levels:
- ``untrusted``      — normal device CLI / SNMP output
- ``untrusted-root`` — debug OS-shell channel output (the highest-risk channel)

This module also carries the mechanism-2 state: a monotonically increasing
device-read sequence number, bumped on every wrap. ``stage_config`` records
the current sequence in the stage; ``commit_config`` with ``confirm=true``
refuses when device output has been read since staging (an injected
read-then-commit chain inside one agent turn always trips this; the
legitimate stage -> human approves -> commit sequence structurally cannot).
Kill switch: ``RAD_MCP_STRICT_COMMIT_GUARD=false``.

Decomposition note: this boundary belongs in the shared rad_core library
(docs/plan/DECOMPOSITION.md) so every future server inherits it.
"""
from __future__ import annotations

import os
import secrets
import threading

# Mechanism 2 kill switch — default ON; set RAD_MCP_STRICT_COMMIT_GUARD=false
# to disable the commit guard (mechanism 1's wrapping is unconditional).
STRICT_COMMIT_GUARD = os.environ.get(
    "RAD_MCP_STRICT_COMMIT_GUARD", "true"
).lower() not in ("0", "false", "no")

_read_seq = 0
_lock = threading.Lock()


def device_read_seq() -> int:
    """The number of device-output blocks returned so far this process."""
    return _read_seq


def _note_device_read() -> None:
    global _read_seq
    with _lock:
        _read_seq += 1


def _attr(value: object) -> str:
    """Escape a tag-attribute value (metadata only — never the payload)."""
    return (str(value).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def wrap_device_output(text: object, *, device: str, family: str,
                       command: str, trust: str = "untrusted") -> str:
    """Wrap device-originated text in the untrusted-output delimiter block.

    The payload passes through byte-identical; only the surrounding tag is
    added. Every call counts as one device read for the commit guard.
    """
    _note_device_read()
    payload = text if isinstance(text, str) else str(text)
    tag = "device-output"
    while f"</{tag}>" in payload:
        tag = f"device-output-{secrets.token_hex(2)}"
    return (
        f'<{tag} device="{_attr(device)}" family="{_attr(family)}" '
        f'command="{_attr(command)}" trust="{_attr(trust)}">'
        f"{payload}</{tag}>"
    )
