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

VALID_TRANSPORTS = ("ssh", "telnet")


def default_port(transport: str) -> int:
    return 23 if transport == "telnet" else 22


@dataclass
class Device:
    name: str
    host: str
    family: str = "etx2"
    transport: str = "ssh"
    port: int | None = None   # resolved to the transport default when unset
    groups: list[str] = field(default_factory=list)
    description: str = ""

    def __post_init__(self) -> None:
        if self.transport not in VALID_TRANSPORTS:
            raise ValueError(
                f"Invalid transport '{self.transport}' for device '{self.name}': "
                f"use one of {', '.join(VALID_TRANSPORTS)}"
            )
        if self.port is None:
            self.port = default_port(self.transport)

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
            "transport": self.transport,
            "port": self.port,
            "groups": self.groups,
            "description": self.description,
        }


def load_inventory(path: str | Path | None = None) -> dict[str, Device]:
    inv_path = Path(path or os.environ.get("RAD_MCP_INVENTORY") or DEFAULT_INVENTORY)
    if not inv_path.exists():
        # Fresh install: create an empty personal inventory on first use.
        inv_path.parent.mkdir(parents=True, exist_ok=True)
        # Use block-list form to keep first append operations straightforward.
        inv_path.write_text("devices:\n", encoding="utf-8")
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

SERVER_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


def _env_quote(value: str) -> str:
    """Quote a value for a dotenv line. Single quotes are literal in dotenv;
    fall back to double quotes (with escaping) when the value contains one."""
    if "'" not in value:
        return f"'{value}'"
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def set_device_credentials(name: str, username: str = "", password: str = "",
                           snmp_community: str = "", snmp_v1_community: str = "",
                           snmp_v1_communities: str = "", snmp_v3_user: str = "",
                           env_path: str | Path | None = None) -> dict:
    """Write a device's secrets (CLI login and/or SNMP communities) into
    server/.env ON THIS HOST and refresh the process environment, so the
    change is effective on the next connection — including rotation of an
    existing value (the os.environ update overrides the loaded-at-startup
    value, closing the 'changed keys need a restart' gap for this path).

    Only the fields provided are written; username/password must come as a
    pair. The device must already exist in the inventory (add_device first).
    Values are never returned or logged by this function.
    """
    get_device(name)  # raises KeyError with the known-device list if unknown
    prefix = "RAD_MCP_" + name.upper().replace("-", "_")
    keys: dict[str, str] = {}
    if username or password:
        if not (username and password):
            raise ValueError("username and password must be provided together")
        keys[f"{prefix}_USERNAME"] = username
        keys[f"{prefix}_PASSWORD"] = password
    for suffix, value in (("_SNMP_COMMUNITY", snmp_community),
                          ("_SNMP_V1_COMMUNITY", snmp_v1_community),
                          ("_SNMP_V1_COMMUNITIES", snmp_v1_communities),
                          ("_SNMP_V3_USER", snmp_v3_user)):
        if value:
            keys[prefix + suffix] = value
    if not keys:
        raise ValueError("nothing to set — provide username+password and/or "
                         "an SNMP field (snmp_community, snmp_v1_community, "
                         "snmp_v1_communities, snmp_v3_user)")

    env_file = Path(env_path or SERVER_ENV_PATH)
    env_file.parent.mkdir(parents=True, exist_ok=True)
    lines = env_file.read_text(encoding="utf-8").splitlines() if env_file.exists() else []
    replaced = set()
    out = []
    for line in lines:
        key = line.split("=", 1)[0].strip() if "=" in line else None
        if key in keys:
            out.append(f"{key}={_env_quote(keys[key])}")
            replaced.add(key)
        else:
            out.append(line)
    appended = [k for k in keys if k not in replaced]
    out.extend(f"{k}={_env_quote(keys[k])}" for k in appended)
    env_file.write_text("\n".join(out) + "\n", encoding="utf-8")

    # effective immediately for this server process, even for rotation
    for k, v in keys.items():
        os.environ[k] = v
    return {"env_file": str(env_file), "prefix": prefix,
            "replaced": sorted(replaced), "created": sorted(appended)}


def add_device_entry(
    name: str,
    host: str,
    family: str,
    transport: str = "ssh",
    port: int | None = None,
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
    if transport not in VALID_TRANSPORTS:
        raise ValueError(
            f"Invalid transport '{transport}': use one of {', '.join(VALID_TRANSPORTS)}"
        )
    if port is None:
        port = default_port(transport)
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
        + (f"    transport: {transport}\n" if transport != "ssh" else "")
        + (f"    port: {port}\n" if port != default_port(transport) else "")
        + f"    groups: {groups_yaml}\n"
        f'    description: "{desc_escaped}"\n'
    )

    existing = inv_path.read_text(encoding="utf-8")
    # Normalize the one-line empty-list shorthand before appending the first
    # entry. Appending a list item under "devices: []" would create invalid YAML
    # (a root-level list item after an inline list mapping value).
    if re.search(r"(?m)^\s*devices:\s*\[\s*\]\s*$", existing):
        existing = re.sub(
            r"(?m)^\s*devices:\s*\[\s*\]\s*$",
            "devices:",
            existing,
            count=1,
        )
        inv_path.write_text(existing, encoding="utf-8")

    # Defensive: if a hand-edited file somehow dropped the top-level key,
    # restore it so appended entries remain valid.
    if not re.search(r"(?m)^\s*devices:\s*$", existing):
        if existing and not existing.endswith("\n"):
            existing += "\n"
        existing += "devices:\n"
        inv_path.write_text(existing, encoding="utf-8")

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
    transport: str | None = None,
    port: int | None = None,
    groups: list[str] | None = None,
    description: str | None = None,
) -> Device:
    """Update a subset of an existing device's fields (unset params keep
    their current value). Implemented as remove + re-add so the on-disk
    formatting stays identical to a fresh add_device_entry call."""
    inv_path = Path(path or os.environ.get("RAD_MCP_INVENTORY") or DEFAULT_INVENTORY)
    current = get_device(name, inv_path)
    new_transport = transport if transport is not None else current.transport
    new_port = port
    if new_port is None:
        # Keep the current port — unless the transport is changing and the
        # port was just the old transport's default (22 <-> 23), in which
        # case re-resolve to the new transport's default.
        if new_transport != current.transport and current.port == default_port(current.transport):
            new_port = default_port(new_transport)
        else:
            new_port = current.port
    merged = Device(
        name=name,
        host=host if host is not None else current.host,
        family=family if family is not None else current.family,
        transport=new_transport,
        port=new_port,
        groups=groups if groups is not None else current.groups,
        description=description if description is not None else current.description,
    )
    remove_device_entry(name, path=inv_path)
    add_device_entry(
        merged.name, merged.host, merged.family, transport=merged.transport,
        port=merged.port, groups=merged.groups, description=merged.description,
        path=inv_path,
    )
    return merged
