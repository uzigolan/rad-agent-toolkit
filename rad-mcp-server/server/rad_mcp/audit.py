"""Append-only JSONL audit log with secret redaction."""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"

_SECRET_PATTERNS = [
    re.compile(r"(password\s+)(\S+)", re.IGNORECASE),
    re.compile(r"(secret\s+)(\S+)", re.IGNORECASE),
    re.compile(r"(community\s+)(\S+)", re.IGNORECASE),
]


def redact(text: str) -> str:
    # Note: the debug_logon_request/submit challenge/response (server.py,
    # backends/ssh.py) never passes the submitted password through audit()'s
    # `detail` in the first place — it's a plain tool argument that stays
    # local to the one call. Don't start threading it through here.
    for pat in _SECRET_PATTERNS:
        text = pat.sub(r"\1<redacted>", text)
    # Redact any literal occurrence of configured credentials
    for var in ("RAD_MCP_PASSWORD", "RAD_MCP_USERNAME"):
        val = os.environ.get(var)
        if val and val in text:
            text = text.replace(val, "<redacted>")
    return text


def audit(event: str, device: str, detail: str = "", ok: bool = True) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "device": device,
        "ok": ok,
        "detail": redact(detail)[:4000],
    }
    with (LOG_DIR / "audit.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
