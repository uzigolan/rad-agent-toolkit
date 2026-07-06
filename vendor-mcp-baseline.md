# Vendor MCP / Automation Server Directory — Baseline Reference

> Compiled July 2026. Use this as baseline context for building or choosing an MCP server (or Claude Code skill) to automate network/infra devices across the vendor platforms below. Each entry is a real public GitHub repo (or vendor doc page) found via web search — not verified end-to-end, so review auth model, write-scope, and audit logging before pointing anything at production equipment.
>
> Legend: **[OFFICIAL]** = lives under the vendor's own GitHub org. **[COMMUNITY]** = independent/third-party project. ⚠ = flagged caution (alpha, unaudited, write-access, no built-in guardrails, etc.)

---

## Arista EOS
`device_type: arista_eos`

- **[OFFICIAL-ADJACENT] Arista CloudVision MCP server** — bridges Claude/agents to CloudVision's REST API (connectivity monitor data, Studio/dashboard tags, fabric-wide state). Built on FastMCP.
  https://playbooks.com/mcp/noredistribution-arista-cloudvision
- **[COMMUNITY] jotasantos/arista-mcp-automation** — wraps mcp-netmiko-server for Arista labs; TOML device inventory; show/VLAN/BGP/LLDP queries; health-check prompts across spine/leaf fleets.
  https://github.com/jotasantos/arista-mcp-automation
- **[COMMUNITY] upa/mcp-netmiko-server** — generic Netmiko MCP server; supports `arista_eos` alongside Cisco/Juniper/Nokia device_types. stdio or SSE transport.
  https://github.com/upa/mcp-netmiko-server
- **[OFFICIAL] aristanetworks/EosSdk** — native EOS SDK (C++/Python) for agents running directly on-switch. Not MCP — the underlying programmability layer CloudVision/AVA build on.
  https://github.com/aristanetworks/EosSdk

---

## Cisco IOS / IOS-XE / NX-OS
`device_type: cisco_ios`

Widest coverage of any vendor. RADKit is Cisco's official remote-automation SDK (free with a support contract). pyATS/Genie gives structured parsed output instead of raw CLI text.

- **[OFFICIAL] CiscoDevNet/radkit-mcp-server-community** — FastMCP server over Cisco RADKit; device inventory, CLI execution, config commits via RADKit's certificate-based auth. Labelled "not an official product" but lives under the CiscoDevNet org.
  https://github.com/CiscoDevNet/radkit-mcp-server-community
- **[COMMUNITY] ponchotitlan/radkit-loves-agenticops** — low-code AgenticOps workflows: n8n + MCP + RADKit, with Slack/Webex integration. Good fit if you're already running n8n.
  https://github.com/ponchotitlan/radkit-loves-agenticops
- **[COMMUNITY] automateyournetwork/pyATS_MCP** — wraps pyATS + Genie; structured show-command parsing, config push, JSON-RPC over stdio. 85 unit tests, Docker image included.
  https://github.com/automateyournetwork/pyATS_MCP
- **[COMMUNITY] automateyournetwork/MCPyATS** — fuller "VibeOps" stack: pyATS MCP + LangGraph agent + Streamlit UI + A2A protocol, bundled with filesystem/email/Mermaid/GitHub MCP tools.
  https://github.com/automateyournetwork/MCPyATS
- **[COMMUNITY] Ringertz/MCP-Claude-Cisco** — lighter-weight network-assistant MCP server for routing policy / device-health lookups. Good template to read, not production-grade.
  https://github.com/Ringertz/MCP-Claude-Cisco

---

## Fortinet FortiOS
`device_type: fortinet`

Note: FortiOS 8.0 has native *visibility* into MCP/A2A traffic at the firewall level — separate from the MCP servers below, which let an agent *manage* the box.

- **[COMMUNITY] paoloamato2/fortinet-mcp-server** — full REST API coverage for FortiOS 7.6.x; 204+ typed tools + 5 generic pass-through tools covering all 1,536 endpoints. Async httpx client.
  https://github.com/paoloamato2/fortinet-mcp-server
- **[COMMUNITY] alpadalar/fortigate-mcp-server** — async Python, persistent HTTP pooling, security-first defaults. Tools split by domain: firewall policy, network objects, routing, virtual IPs.
  https://github.com/alpadalar/fortigate-mcp-server
- **[COMMUNITY] rstierli/fortimanager-mcp** ⚠ — centralized policy/device management via FortiManager JSON-RPC API. Built-in safety checks (blocks overly-permissive policies, dangerous CLI script commands) but beta — can create/modify/delete config; test in non-prod first.
  https://github.com/rstierli/fortimanager-mcp

---

## Huawei VRP
`device_type: huawei`

⚠ **Gap:** no mature MCP server exists for physical VRP hardware. Best path is your own thin MCP wrapper around Netmiko (`huawei_vrp` / `huawei_vrpv8`) or the NAPALM driver below.

- **[COMMUNITY] napalm-automation-community/napalm-huawei-vrp** — NAPALM driver for VRP5/VRP8; get_facts, get_config, arp/mac tables, LLDP neighbors, merge/replace config with contextual diffing. The building block to wrap.
  https://github.com/napalm-automation-community/napalm-huawei-vrp
- **[COMMUNITY] l-sw-4/ensp-cli-mcp** ⚠ — Telnet-based MCP server for Huawei's eNSP *simulator*, not live production hardware.
  https://lobehub.com/mcp/l-sw-4-ensp-cli-mcp
- **[OFFICIAL, cloud only] HuaweiCloudDeveloper/mcp-server** — official Huawei Cloud MCP servers (ECS, OBS, GaussDB, EIP). Manages cloud resources, not on-prem VRP network hardware.
  https://github.com/HuaweiCloudDeveloper/mcp-server

---

## Juniper Junos
`device_type: junos`

Best-supported vendor after Cisco — Juniper maintains an **official** MCP server in their own org.

- **[OFFICIAL] Juniper/junos-mcp-server** ⚠ — official bridge between MCP clients and Junos devices. stdio + streamable-http transports, Docker image, token-based auth for remote deployments. Supports operational queries and config load/commit. Vendor explicitly recommends SSH-key auth (not passwords) in production.
  https://github.com/Juniper/junos-mcp-server
- **[OFFICIAL] Juniper/routing-director-mcp-server** — MCP server for Juniper Routing Director (formerly Paragon Automation); routing/assurance/optimization at controller level, not per-device CLI.
  https://github.com/Juniper/routing-director-mcp-server
- **[COMMUNITY] dpajin/mcp-server-junos** — built on junos-eznc (PyEZ) + FastMCP. Tools: get_fact, show_command, apply_config, list_devices. Tested with VS Code/Copilot as MCP client too.
  https://github.com/dpajin/mcp-server-junos
- **[COMMUNITY] kbedford/Junos-MCP-Server-on-a-Linux-Bastion** — deployment recipe running Juniper's own junos-mcp-server centrally on a Linux bastion, with a jmcp_cli operator helper. Good reference for self-hosted setups.
  https://github.com/kbedford/Junos-MCP-Server-on-a-Linux-Bastion-

---

## Linux / Unix
`device_type: linux` — host/OS shell access, not a network vendor

- **[COMMUNITY] tufantunc/ssh-mcp** — remote SSH execution for Linux *and* Windows targets; password or key auth, sudo/su elevation, configurable timeouts.
  https://github.com/tufantunc/ssh-mcp
- **[COMMUNITY] tumf/mcp-shell-server** — whitelisted-command execution with safe argv pipelines (no raw shell string exec), contained redirection, structured audit logging with secret redaction. Most security-conscious option.
  https://github.com/tumf/mcp-shell-server
- **[COMMUNITY] MladenSU/cli-mcp-server** — command + flag whitelisting, path traversal prevention, shell-operator injection protection, execution timeouts.
  https://github.com/MladenSU/cli-mcp-server
- **[COMMUNITY] blazickjp/shell-mcp-server** — directory-scoped shell execution, multi-shell support (bash/zsh).
  https://github.com/blazickjp/shell-mcp-server
- **[COMMUNITY] patrickomatik/mcp-bash** ⚠ — minimal, unrestricted bash execution. No whitelist/sandboxing; author explicitly flags this as risky, personal-use only.
  https://github.com/patrickomatik/mcp-bash

---

## MikroTik RouterOS
`device_type: mikrotik`

Most crowded field here. Unusual option: RouterOS 7.22+ can run an MCP server *as a container on the router itself*.

- **[COMMUNITY] AliKarami/MikroMCP** — most production-minded option: 117 typed tools, dry-run previews, per-router circuit breakers, RBAC, audit logs, rollback-aware writes.
  https://github.com/AliKarami/MikroMCP
- **[COMMUNITY] tikoci/rosetta** — not device-control; a documentation/RAG server (SQLite FTS5) for RouterOS docs/commands/changelogs. Deployable as a RouterOS `/app` container on supported hardware (CCR, RB5009, hAP ax, CHR).
  https://github.com/tikoci/rosetta
- **[COMMUNITY] jeff-nasseri/mikrotik-mcp** — registered in the official MCP Registry; installable via `claude mcp add`. VLANs, firewall, DHCP, wireless, backups.
  https://github.com/jeff-nasseri/mikrotik-mcp
- **[COMMUNITY] sevaepsteyn/routeros_mcp** — API + SSH with automatic fallback; YAML device inventory; smart export falls back to SSH when API perms insufficient.
  https://github.com/sevaepsteyn/routeros_mcp
- **[COMMUNITY] ramanarupa/mcp-mikrotik** — Node.js, targets RouterOS 7 API; interfaces, IP/firewall/DHCP, arbitrary command execution tool included.
  https://github.com/ramanarupa/mcp-mikrotik
- **[COMMUNITY] dospuntos-dev/mikrotik-mcp** ⚠ — REST API-based, auto-discovers branch routers over VPN peers. Explicitly alpha, not security-audited, no MCP-endpoint auth by default.
  https://github.com/dospuntos-dev/mikrotik-mcp

---

## Palo Alto Networks PAN-OS
`device_type: palo_alto`

Palo Alto Networks publishes an official server — but it's a security *relay/proxy* for MCP traffic, not a PAN-OS device-management tool.

- **[OFFICIAL] PaloAltoNetworks/pan-mcp-relay** — Prisma AIRS MCP Security Relay; scans MCP tool descriptions/params/responses for prompt injection, malicious URLs, data-loss risk. Sits in front of other MCP servers rather than talking to firewalls directly.
  https://github.com/PaloAltoNetworks/pan-mcp-relay
- **[COMMUNITY] vlanviking/panos-mcp-server** — read-only mode toggle (`PANOS_READONLY=true`), regex-validated inputs against XPath injection, explicit two-step write→commit flow, full audit logging. Best safety posture of the PAN-OS options.
  https://github.com/vlanviking/panos-mcp-server
- **[COMMUNITY] apius-tech/Palo-MCP** — TypeScript, Desktop Extension (.mcpb) support, OS-keychain credential storage, proxy support for jump-host/SOCKS5 access.
  https://github.com/apius-tech/Palo-MCP
- **[COMMUNITY] cdot65/pan-os-mcp** — FastMCP-based, XML API, supports Panorama device groups and shared objects. Dedicated docs site (cdot65.github.io/pan-os-mcp).
  https://github.com/cdot65/pan-os-mcp
- **[COMMUNITY] edoscars/pan-os-mcp** — separate, similarly-named XML-API MCP server; smaller/simpler alternative to cdot65's version.
  https://github.com/edoscars/pan-os-mcp

---

## RAD Data Communications
`device_type: rad` (e.g. `rad_etx` via Netmiko)

⚠ **No MCP server — official or community — exists for RAD Data Communications equipment.** Search results for "RAD" surface unrelated projects: RAD Security (Kubernetes/cloud security, different company), Cisco RADKit (different product, see Cisco section), Radicle (peer-to-peer git), radare2 (reverse-engineering).

Practical path: same as Huawei — wrap Netmiko's `rad_etx` device_type in your own thin MCP server following the `mcp-netmiko-server` pattern used for Arista/Cisco above.

---

## Windows Command Prompt & PowerShell
`device_type: windows_cmd / windows_powershell` — host/OS shell access, not a network vendor

- **[COMMUNITY] yotsuda/PowerShell.MCP** ⚠ — distinctive design: you and the AI share the *same live PowerShell console*, so commands are visible and human-interruptible in real time (e.g. type an MFA code mid-flow). Cross-platform via pwsh. Sibling project `ripple` generalizes this to bash/Python REPL/SQL console/debuggers. Full PowerShell access — author warns trusted-environments-only.
  https://github.com/yotsuda/PowerShell.MCP
- **[COMMUNITY] simon-ami/win-cli-mcp-server** — multi-shell: PowerShell, CMD, *and* Git Bash, plus remote SSH execution. Command blocklists, path restrictions, working-directory validation, history/logging.
  https://github.com/simon-ami/win-cli-mcp-server
- **[COMMUNITY] cezarypiatek/PoshMCP** — whitelist-only cmdlet exposure, no dynamic/arbitrary execution. Auto-generates MCP tool schemas from PowerShell's own cmdlet help/reflection. Safest PowerShell option if you want a fixed, auditable tool surface.
  https://mcpservers.org/servers/cezarypiatek/poshmcp
- **[COMMUNITY] gunjanjp/powershell-mcp** — Node.js-based; ships config-recovery/backup/merge tooling to avoid clobbering an existing Claude Desktop config on install.
  https://github.com/gunjanjp/powershell-mcp
- **[COMMUNITY] tufantunc/ssh-mcp** — same server as listed under Linux; also supports remote Windows targets via SSH, including sudo/su-equivalent elevation flags.
  https://github.com/tufantunc/ssh-mcp
- **[COMMUNITY] CursorTouch/Windows-MCP** — a level up from shell access: full Windows UI automation (clicks, window control, app launching), with an optional PowerShell tool alongside. 2M+ users via Claude Desktop extensions per the repo.
  https://github.com/CursorTouch/Windows-MCP

---

## Cross-vendor notes

- **Strongest vendor-official coverage:** Juniper (`junos-mcp-server`), Cisco (RADKit ecosystem), Palo Alto (Prisma AIRS relay).
- **No vendor-official or mature community MCP server:** Huawei VRP (physical hardware), RAD Data Communications.
- **Safety patterns worth copying when building your own:** read-only env-var toggles (Fortinet, Palo Alto), dry-run/diff-before-commit flows (MikroMCP, Junos PyEZ apply_config), whitelisted commands over raw shell strings (mcp-shell-server, PoshMCP), audit logging with secret redaction (mcp-shell-server).
- **For your own multi-vendor wrapper:** Netmiko/NAPALM device_type strings map directly to most of the above — `arista_eos`, `cisco_ios`/`cisco_nxos`, `huawei_vrp`, `junos`, `rad_etx` are all supported Netmiko platforms, so a single `mcp-netmiko-server`-style wrapper can cover Arista, Cisco, Huawei, Juniper, and RAD from one codebase if you don't need vendor-specific REST/XML API depth.
