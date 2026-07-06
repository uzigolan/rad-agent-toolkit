"""Device inventory: YAML file for device facts, environment for credentials.

Credentials are NEVER stored in the inventory file. Resolution order:
  1. RAD_MCP_<DEVICENAME>_USERNAME / _PASSWORD  (per-device override, name upper-cased, dashes -> underscores)
  2. RAD_MCP_USERNAME / RAD_MCP_PASSWORD        (global pilot credentials)
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from dotenv import load_dotenv

# .env sits next to pyproject.toml (server/.env); also honor CWD .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
load_dotenv()

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
        user = os.environ.get(f"{self._env_prefix}_USERNAME") or os.environ.get("RAD_MCP_USERNAME")
        if not user:
            raise RuntimeError(
                f"No username for '{self.name}': set RAD_MCP_USERNAME (or {self._env_prefix}_USERNAME) in server/.env"
            )
        return user

    @property
    def password(self) -> str:
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
        raise FileNotFoundError(f"Inventory file not found: {inv_path}")
    raw = yaml.safe_load(inv_path.read_text(encoding="utf-8")) or {}
    devices: dict[str, Device] = {}
    for entry in raw.get("devices", []):
        dev = Device(**entry)
        devices[dev.name] = dev
    return devices


def get_device(name: str, path: str | Path | None = None) -> Device:
    devices = load_inventory(path)
    if name not in devices:
        known = ", ".join(sorted(devices)) or "(none)"
        raise KeyError(f"Unknown device '{name}'. Known devices: {known}")
    return devices[name]
