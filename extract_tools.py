#!/usr/bin/env python3
import re

with open('rad-mcp-server/server/rad_mcp/server.py') as f:
    content = f.read()

matches = re.findall(r'@mcp\.tool\(\)\s*\ndef\s+(\w+)\(', content)

print("=" * 70)
print("ALL MCP TOOLS FROM server.py")
print("=" * 70)
for i, tool in enumerate(matches, 1):
    print(f"{i:2d}. {tool}")

print(f"\nTotal: {len(matches)} tools")
