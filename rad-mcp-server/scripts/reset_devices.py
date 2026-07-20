"""Reset the device inventory: remove ALL devices and ALL device secrets.

Called by the MCP-server installers when the user chooses "reset" instead of
reusing the existing devices; safe to run standalone too. Stdlib only.

What it does (both files get a timestamped .bak backup first):
  - inventory.yaml  -> rewritten as an empty inventory (`devices:`)
  - server/.env     -> every credential/community key removed:
        RAD_MCP_*_USERNAME / RAD_MCP_*_PASSWORD   (incl. the globals)
        any RAD_MCP_* key containing  _SNMP_       (v1/v2c communities, v3 user)
    Server configuration keys are PRESERVED (RAD_MCP_TOKENS,
    RAD_MCP_WRITE_TOKENS, RAD_MCP_TLS_*, RAD_MCP_SERVER_NAME,
    RAD_MCP_READONLY, RAD_MCP_INVENTORY, ...).

Usage:
  python scripts/reset_devices.py [--dry-run]
"""
from __future__ import annotations

import os
import re
import shutil
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
INVENTORY = Path(os.environ.get("RAD_MCP_INVENTORY") or REPO / "inventory.yaml")
ENV_FILE = REPO / "server" / ".env"

DEVICE_LINE = re.compile(r"^\s*-\s*name\s*:", re.M)
# a key is a device secret if it ends in _USERNAME/_PASSWORD or names SNMP
SECRET_KEY = re.compile(r"^RAD_MCP_(?:.+_)?(?:USERNAME|PASSWORD)$|^RAD_MCP_.*_SNMP_.*$|^RAD_MCP_SNMP_.+$")


def main(dry_run: bool) -> None:
    stamp = time.strftime("%Y%m%d-%H%M%S")

    n_devices = 0
    if INVENTORY.exists():
        n_devices = len(DEVICE_LINE.findall(INVENTORY.read_text(encoding="utf-8")))

    dropped: list[str] = []
    kept_lines: list[str] = []
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            key = line.split("=", 1)[0].strip() if ("=" in line and not line.lstrip().startswith("#")) else None
            if key and SECRET_KEY.match(key):
                dropped.append(key)
            else:
                kept_lines.append(line)

    print(f"inventory: {INVENTORY} ({n_devices} device(s))")
    print(f".env     : {ENV_FILE} ({len(dropped)} secret key(s) to remove)")
    for k in dropped:
        print(f"  - {k}")
    if dry_run:
        print("dry run — nothing changed.")
        return

    if INVENTORY.exists():
        shutil.copy2(INVENTORY, INVENTORY.with_name(f"{INVENTORY.name}.bak-{stamp}"))
    INVENTORY.parent.mkdir(parents=True, exist_ok=True)
    INVENTORY.write_text("devices:\n", encoding="utf-8")

    if ENV_FILE.exists():
        shutil.copy2(ENV_FILE, ENV_FILE.with_name(f".env.bak-{stamp}"))
        ENV_FILE.write_text("\n".join(kept_lines) + ("\n" if kept_lines else ""), encoding="utf-8")

    print(f"done: inventory emptied ({n_devices} device(s) removed), "
          f"{len(dropped)} secret key(s) stripped from .env; "
          f"backups saved as *.bak-{stamp}")


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv[1:])
