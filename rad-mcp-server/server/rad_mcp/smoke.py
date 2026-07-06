"""Smoke test: connect to one inventory device and exercise the read path.

Usage:  python -m rad_mcp.smoke <device-name> [extra show command ...]

Connects over SSH, prints the prompt, runs the driver's health commands plus
any extra commands given, and writes a full transcript to logs/smoke-<device>.txt
so driver command sets can be grounded against real output.
"""
from __future__ import annotations

import sys
from pathlib import Path

from netmiko import ConnectHandler

from .drivers import get_driver
from .inventory import get_device

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    name = sys.argv[1]
    extra = sys.argv[2:]

    dev = get_device(name)
    driver = get_driver(dev.family)
    print(f"Connecting to {dev.name} ({dev.host}:{dev.port}) as netmiko '{driver.netmiko_device_type}' ...")

    conn = ConnectHandler(
        device_type=driver.netmiko_device_type,
        host=dev.host,
        port=dev.port,
        username=dev.username,
        password=dev.password,
        timeout=30,
        conn_timeout=15,
    )
    transcript: list[str] = []
    try:
        prompt = conn.find_prompt()
        print(f"Connected. Prompt: {prompt!r}\n")
        transcript.append(f"PROMPT: {prompt!r}")

        for cmd in list(driver.health_sequence) + extra:
            print(f"### {cmd}")
            out = conn.send_command_timing(cmd, read_timeout=30)
            print(out)
            print("-" * 60)
            transcript.append(f"### {cmd}\n{out}")
    finally:
        conn.disconnect()

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"smoke-{dev.name}.txt"
    log_path.write_text("\n\n".join(transcript), encoding="utf-8")
    print(f"\nTranscript saved: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
