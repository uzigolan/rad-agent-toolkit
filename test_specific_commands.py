#!/usr/bin/env python3
"""Test specific failing commands with actual parameters on Yossi-ETX2"""

import sys
sys.path.insert(0, r"c:\Users\uzi_g\Downloads\ai-projects\fusion-cli\rad-mcp-server")

from netmiko import ConnectHandler
from rad_mcp.inventory import get_device
import json

# Load device config from inventory
device_info = get_device("Yossi-ETX2")
print(f"Connecting to {device_info.name} ({device_info.host}:{device_info.port})")

# Connect
conn = ConnectHandler(**device_info.conn_params())
print(f"Connected  →  {conn.find_prompt()!r}\n")

# Navigate to file context
print("=" * 70)
print("Testing File Commands in 'file' Context")
print("=" * 70)

conn.send_command_timing("exit all", read_timeout=10)
nav_out = conn.send_command_timing("file", read_timeout=10)
print(f"Navigated to context: {conn.find_prompt()!r}\n")

# Test commands
commands_to_test = [
    ("show file-details user-default-config", "Test with actual filename"),
    ("show user-dir user-default-config", "Test user-dir with actual filename"),
    ("show configuration-files", "List available files"),
    ("show banner-text", "Try without filename"),
    ("show rollback-config", "Try rollback"),
]

results = {}
for cmd, description in commands_to_test:
    print(f"\n[TEST] {description}")
    print(f"CMD:   {cmd}")
    try:
        output = conn.send_command_timing(cmd, read_timeout=15)
        # Check for errors
        if "cli error" in output.lower() or "command not recognized" in output.lower():
            results[cmd] = {
                "status": "FAIL",
                "error": output[:200].strip()
            }
            print(f"RESULT: FAIL")
            print(f"ERROR: {output[:200]}")
        else:
            results[cmd] = {
                "status": "PASS",
                "output_lines": len(output.split('\n'))
            }
            print(f"RESULT: PASS ({len(output.split(chr(10)))} lines)")
            print(f"OUTPUT (first 300 chars):\n{output[:300]}")
    except Exception as e:
        results[cmd] = {
            "status": "ERROR",
            "exception": str(e)
        }
        print(f"RESULT: ERROR - {e}")

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
for cmd, result in results.items():
    print(f"  {result['status']:6} - {cmd}")

# Save results
with open("test_specific_commands_results.json", "w") as f:
    json.dump(results, f, indent=2)
    
print("\nResults saved to test_specific_commands_results.json")

conn.disconnect()
