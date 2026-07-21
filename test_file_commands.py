#!/usr/bin/env python3
"""Test only file-level commands to verify str-21, str-23, str-27, str-31, str-32, str-33"""

import sys
import os

# Add rad-mcp-server to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "rad-mcp-server"))

from netmiko import ConnectHandler
from rad_mcp.inventory import get_device
from rad_mcp.drivers import get_driver
import json

dev = get_device("Yossi-ETX2")
driver = get_driver(dev.family)
dtype = driver.netmiko_device_type + ("_telnet" if dev.transport == "telnet" else "")

print(f"Connecting to {dev.name} ({dev.host}:{dev.port})")
conn = ConnectHandler(
    device_type=dtype,
    host=dev.host,
    port=dev.port,
    username=dev.username,
    password=dev.password,
    timeout=30,
    conn_timeout=15,
)

print(f"Connected: {conn.find_prompt()}\n")

# Navigate to file context
print("=" * 70)
print("Navigating to FILE context")
print("=" * 70)

conn.send_command_timing("exit all", read_timeout=10)
file_nav = conn.send_command_timing("file", read_timeout=10)
print(f"Context: {conn.find_prompt()}\n")

# Test file-level commands
test_cases = [
    ("str-21", "show banner-text", "Display the configured login banner message"),
    ("str-23", "show file-details user-default-config", "Show detailed information about a specific file"),
    ("str-27", "show rollback-config", "Show the saved rollback configuration file"),
    ("str-30", "show usb-status", "Display the status of the USB storage device"),
    ("str-31", "show user-default-config", "Show the user-defined default configuration file"),
    ("str-32", "show user-dir user-default-config", "display the contents of user text files"),
    ("str-33", "show user-script", "Show the user scripts stored on the device"),
]

results = {}

for case_id, command, description in test_cases:
    print(f"\n[{case_id}] {description}")
    print(f"  Command: {command}")
    
    try:
        output = conn.send_command_timing(command, read_timeout=15)
        
        # Check for errors
        if "cli error" in output.lower() or "command not recognized" in output.lower():
            # Extract error message
            error_lines = [line for line in output.split('\n') if 'cli error' in line.lower() or 'command not recognized' in line.lower()]
            error_msg = error_lines[0] if error_lines else output.split('\n')[0]
            
            results[case_id] = {
                "status": "FAIL",
                "command": command,
                "error": error_msg.strip()
            }
            print(f"  Result: FAIL")
            print(f"  Error: {error_msg.strip()}")
        else:
            output_lines = output.strip().split('\n')
            results[case_id] = {
                "status": "PASS",
                "command": command,
                "output_lines": len(output_lines)
            }
            print(f"  Result: PASS ({len(output_lines)} lines)")
            if len(output_lines) <= 5:
                print(f"  Output:\n{output}")
            else:
                print(f"  Output (first 3 lines):\n" + "\n".join(output_lines[:3]))
    
    except Exception as e:
        results[case_id] = {
            "status": "ERROR",
            "command": command,
            "exception": str(e)
        }
        print(f"  Result: ERROR")
        print(f"  Exception: {e}")

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

pass_count = sum(1 for r in results.values() if r["status"] == "PASS")
fail_count = sum(1 for r in results.values() if r["status"] == "FAIL")
error_count = sum(1 for r in results.values() if r["status"] == "ERROR")

print(f"PASS:  {pass_count}/7")
print(f"FAIL:  {fail_count}/7")
print(f"ERROR: {error_count}/7")

print("\nDetailed Results:")
for case_id in sorted(results.keys()):
    r = results[case_id]
    status_symbol = "✓" if r["status"] == "PASS" else "✗" if r["status"] == "FAIL" else "!"
    print(f"  [{status_symbol}] {case_id}: {r['status']}")
    if "error" in r:
        print(f"       {r['error']}")

# Save results
with open("test_file_commands_results.json", "w") as f:
    json.dump(results, f, indent=2)
    print(f"\nResults saved to test_file_commands_results.json")

conn.disconnect()
