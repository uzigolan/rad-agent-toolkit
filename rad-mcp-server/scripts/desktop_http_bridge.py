"""stdio -> http bridge for clients whose config can only spawn commands.

Claude Desktop's config file is stdio-only (http entries are silently
ignored, verified 2026-07-10). This bridge lets such a client join a shared
rad-mcp http server anyway: the client spawns THIS script over stdio, and
the script proxies everything to the http server with the bearer header.

The http server itself must already be running — a bridge connects, it
never starts servers (see docs/remote-server.md "Run it").

Config entry shape (fix paths/URL/token):

    "rad-mcp": {
      "command": "<repo>/rad-mcp-server/server/.venv/Scripts/python.exe",
      "args": ["<repo>/rad-mcp-server/scripts/desktop_http_bridge.py"],
      "env": {
        "RAD_MCP_URL": "http://127.0.0.1:8080/mcp",
        "RAD_MCP_TOKEN": "<your-token>"
      }
    }
"""
import os
import sys

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from fastmcp.server import create_proxy


def main() -> None:
    url = os.environ.get("RAD_MCP_URL", "").strip()
    token = os.environ.get("RAD_MCP_TOKEN", "").strip()
    if not url or not token:
        print("desktop_http_bridge: RAD_MCP_URL and RAD_MCP_TOKEN env vars are required", file=sys.stderr)
        raise SystemExit(2)
    transport = StreamableHttpTransport(url=url, headers={"Authorization": f"Bearer {token}"})
    proxy = create_proxy(Client(transport), name="rad-mcp-bridge")
    proxy.run()  # stdio


if __name__ == "__main__":
    main()
