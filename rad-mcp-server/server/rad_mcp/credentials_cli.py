"""rad-mcp-set-credentials — CLI replacement for the removed
set_device_credentials MCP tool (plan 01).

Credential provisioning is a human action on the server host, not an agent
capability: leaving it callable over MCP meant a prompt-injection path could
end at "rotate the credentials on this device". This CLI writes the same
RAD_MCP_<NAME>_* keys into server/.env that the tool used to, effective on
the server's next connection to the device.

Usage (run in the server venv, on the server host):

  rad-mcp-set-credentials <device> --username admin            # prompts for password
  rad-mcp-set-credentials <device> --snmp-v1-community public
  rad-mcp-set-credentials <device> --snmp-v3-user monitor \
      --snmp-v3-auth-key ... --snmp-v3-priv-key ...

Passwords/keys can be given as flags for scripting, but interactive prompts
(getpass, never echoed) are the default when --username is given without
--password. Values are never printed back.
"""
from __future__ import annotations

import argparse
import getpass
import sys

from .audit import audit
from .inventory import set_device_credentials


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="rad-mcp-set-credentials",
        description=(
            "Set (or rotate) an inventory device's secrets — CLI login and/or "
            "SNMP communities/USM keys — in the server's own server/.env. The "
            "device must already exist in the inventory (add_device first). "
            "Effective on the server's next connection; a long-running server "
            "process picks NEW keys up automatically, CHANGED keys need a "
            "server restart."
        ),
    )
    p.add_argument("device", help="inventory device name (as in list_devices)")
    p.add_argument("--username", default="", help="CLI username (prompts for the password unless --password is given)")
    p.add_argument("--password", default="", help="CLI password (omit to be prompted securely)")
    p.add_argument("--snmp-community", default="", help="SNMPv2c community")
    p.add_argument("--snmp-v1-community", default="", help="SNMPv1 community")
    p.add_argument("--snmp-v1-communities", default="",
                   help="SNMPv1 CSV fallback list, tried left->right")
    p.add_argument("--snmp-v3-user", default="", help="SNMPv3 USM user (alone = noAuthNoPriv)")
    p.add_argument("--snmp-v3-auth-key", default="", help="SNMPv3 auth key (>=8 chars; adds authNoPriv)")
    p.add_argument("--snmp-v3-priv-key", default="", help="SNMPv3 priv key (>=8 chars; adds authPriv, needs auth key)")
    p.add_argument("--snmp-v3-auth-protocol", default="",
                   help="md5/sha/sha224/sha256/sha384/sha512 (default sha)")
    p.add_argument("--snmp-v3-priv-protocol", default="",
                   help="des/3des/aes/aes192/aes256 (default aes)")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    password = args.password
    if args.username and not password:
        password = getpass.getpass(f"CLI password for '{args.device}': ")
    try:
        res = set_device_credentials(
            args.device, args.username, password,
            snmp_community=args.snmp_community,
            snmp_v1_community=args.snmp_v1_community,
            snmp_v1_communities=args.snmp_v1_communities,
            snmp_v3_user=args.snmp_v3_user,
            snmp_v3_auth_key=args.snmp_v3_auth_key,
            snmp_v3_priv_key=args.snmp_v3_priv_key,
            snmp_v3_auth_protocol=args.snmp_v3_auth_protocol,
            snmp_v3_priv_protocol=args.snmp_v3_priv_protocol,
        )
    except (KeyError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    audit("set_device_credentials_cli", args.device,
          detail=f"keys {'+'.join(res['created'] + res['replaced'])} (values redacted)")
    action = "rotated" if res["replaced"] else "created"
    changed = ", ".join(k.removeprefix(res["prefix"] + "_")
                        for k in res["created"] + res["replaced"])
    print(f"Secrets for '{args.device}' {action} in {res['env_file']} ({changed}).")
    if res["replaced"]:
        print("Rotated keys were already loaded — restart a running server "
              "process for the change to take effect.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
