"""Device inventory: YAML file for device facts, environment for credentials.

Credentials are NEVER stored in the inventory file. Resolution order:
  1. RAD_MCP_<DEVICENAME>_USERNAME / _PASSWORD  (per-device override, name upper-cased, dashes -> underscores)
  2. RAD_MCP_USERNAME / RAD_MCP_PASSWORD        (global pilot credentials)
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from dotenv import load_dotenv

# .env sits next to pyproject.toml (server/.env); also honor CWD .env
def _refresh_env() -> None:
    """Pick up .env keys added after process start (e.g. a just-added device's
    credentials) without a server restart. No override: values already in the
    process environment — including a changed .env value for an EXISTING key —
    keep their startup state; only genuinely new keys appear. Changing an
    existing credential still requires a restart."""
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    load_dotenv()


_refresh_env()

DEFAULT_INVENTORY = Path(__file__).resolve().parent.parent.parent / "inventory.yaml"


@dataclass
class Device:
    name: str
    host: str
    family: str = "etx2"
    port: int = 22
    groups: list[str] = field(default_factory=list)
    description: str = ""

    @property
    def _env_prefix(self) -> str:
        return "RAD_MCP_" + self.name.upper().replace("-", "_")

    @property
    def username(self) -> str:
        _refresh_env()
        user = os.environ.get(f"{self._env_prefix}_USERNAME") or os.environ.get("RAD_MCP_USERNAME")
        if not user:
            raise RuntimeError(
                f"No username for '{self.name}': set RAD_MCP_USERNAME (or {self._env_prefix}_USERNAME) in server/.env"
            )
        return user

    @property
    def password(self) -> str:
        _refresh_env()
        pw = os.environ.get(f"{self._env_prefix}_PASSWORD") or os.environ.get("RAD_MCP_PASSWORD")
        if not pw:
            raise RuntimeError(
                f"No password for '{self.name}': set RAD_MCP_PASSWORD (or {self._env_prefix}_PASSWORD) in server/.env"
            )
        return pw

    def summary(self) -> dict:
        """Credential-free view, safe to return to the model/user."""
        return {
            "name": self.name,
            "host": self.host,
            "family": self.family,
            "port": self.port,
            "groups": self.groups,
            "description": self.description,
        }


def load_inventory(path: str | Path | None = None) -> dict[str, Device]:
    inv_path = Path(path or os.environ.get("RAD_MCP_INVENTORY") or DEFAULT_INVENTORY)
    if not inv_path.exists():
        raise FileNotFoundError(
            f"Inventory file not found: {inv_path} — copy inventory.example.yaml "
            "there, or register your first device with add_device (it creates "
            "the file)."
        )
    raw = yaml.safe_load(inv_path.read_text(encoding="utf-8")) or {}
    devices: dict[str, Device] = {}
    # `devices:` with nothing under it parses as None — treat as empty, not an error
    for entry in raw.get("devices") or []:
        dev = Device(**entry)
        devices[dev.name] = dev
    return devices


def get_device(name: str, path: str | Path | None = None) -> Device:
    devices = load_inventory(path)
    if name not in devices:
        known = ", ".join(sorted(devices)) or "(none)"
        raise KeyError(f"Unknown device '{name}'. Known devices: {known}")
    return devices[name]


_NAME_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_-]*$")


def add_device_entry(
    name: str,
    host: str,
    family: str,
    port: int = 22,
    groups: list[str] | None = None,
    description: str = "",
    path: str | Path | None = None,
    overwrite: bool = False,
) -> Path:
    """Append a device to inventory.yaml — facts only, never credentials.

    Appends formatted text rather than round-tripping through yaml.dump, so
    the file's own header comment and existing entries' formatting survive
    untouched (PyYAML would silently drop comments on a full re-dump).
    """
    if not _NAME_RE.match(name):
        raise ValueError(
            f"Invalid device name '{name}': use letters/digits/hyphens/underscores "
            "only, starting with a letter or digit (it becomes part of an "
            "RAD_MCP_<NAME>_USERNAME/_PASSWORD env var name)."
        )
    inv_path = Path(path or os.environ.get("RAD_MCP_INVENTORY") or DEFAULT_INVENTORY)
    if not inv_path.exists():
        # Fresh clone: the personal inventory is gitignored — create it.
        inv_path.write_text(
            "# rad-mcp device inventory — facts only, NEVER credentials "
            "(those live in server/.env)\ndevices:\n",
            encoding="utf-8",
        )
    devices = load_inventory(inv_path)
    if name in devices and not overwrite:
        raise ValueError(
            f"Device '{name}' already exists in {inv_path.name}. "
            "Pass overwrite=true to replace it, or pick a different name."
        )
    if overwrite and name in devices:
        remove_device_entry(name, path=inv_path)

    groups = groups or []
    groups_yaml = "[" + ", ".join(groups) + "]"
    desc_escaped = description.replace('"', '\\"')
    block = (
        f"  - name: {name}\n"
        f"    host: {host}\n"
        f"    family: {family}\n"
        + (f"    port: {port}\n" if port != 22 else "")
        + f"    groups: {groups_yaml}\n"
        f'    description: "{desc_escaped}"\n'
    )
    existing = inv_path.read_text(encoding="utf-8")
    with inv_path.open("a", encoding="utf-8") as f:
        if existing and not existing.endswith("\n"):
            f.write("\n")
        f.write(block)
    return inv_path


def remove_device_entry(name: str, path: str | Path | None = None) -> Path:
    """Remove a device's block from inventory.yaml by exact `name:` match."""
    inv_path = Path(path or os.environ.get("RAD_MCP_INVENTORY") or DEFAULT_INVENTORY)
    text = inv_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    skipping = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- name:") and stripped.split(":", 1)[1].strip() == name:
            skipping = True
            continue
        if skipping and (stripped.startswith("- name:") or (stripped and not line.startswith((" ", "\t")))):
            skipping = False
        if skipping:
            continue
        out.append(line)
    inv_path.write_text("".join(out), encoding="utf-8")
    return inv_path


def update_device_entry(
    name: str,
    path: str | Path | None = None,
    host: str | None = None,
    family: str | None = None,
    port: int | None = None,
    groups: list[str] | None = None,
    description: str | None = None,
) -> Device:
    """Update a subset of an existing device's fields (unset params keep
    their current value). Implemented as remove + re-add so the on-disk
    formatting stays identical to a fresh add_device_entry call."""
    inv_path = Path(path or os.environ.get("RAD_MCP_INVENTORY") or DEFAULT_INVENTORY)
    current = get_device(name, inv_path)
    merged = Device(
        name=name,
        host=host if host is not None else current.host,
        family=family if family is not None else current.family,
        port=port if port is not None else current.port,
        groups=groups if groups is not None else current.groups,
        description=description if description is not None else current.description,
    )
    remove_device_entry(name, path=inv_path)
    add_device_entry(
        merged.name, merged.host, merged.family, port=merged.port,
        groups=merged.groups, description=merged.description, path=inv_path,
    )
    return merged
