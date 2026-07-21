---
description: List devices in the rad-mcp inventory, with optional group or family filter. Also use when addressed via "abayev" / "noam" / "rad agent" — e.g. "rad agent, list devices", "noam, show all lab devices", "abayev, list etx2 devices", "rad agent, what devices do I have?"
argument-hint: [<group-name> | family=<family>]
---

List devices from the inventory: $ARGUMENTS

Parse the argument (optional):
- If the argument starts with `family=`, treat the remainder as a family filter
  (e.g. `family=etx2`).
- Otherwise treat the argument as a group filter (e.g. `lab`, `prod`).
- No argument: list all devices.

1. Call `list_devices(group=<group>, family=<family>)` with the parsed filters.

2. **If the inventory is empty** (empty list returned): say so clearly and point
   the user at the `rad-device-mng` skill — e.g. *"No devices yet. Say
   'rad agent, add my device' to register your first unit."*

3. **Otherwise**, render a markdown table:

   | Name | Host | Family | Transport | Port | Groups | Description |
   |---|---|---|---|---|---|---|
   | … | … | … | … | … | … | … |

   Follow with a one-line count: *"N device(s) shown."* (or *"N of M device(s)
   match \<filter\>."* if a filter was applied).

4. **Never** print, log, or mention credentials. The table contains only the
   `summary()` fields — name, host, family, transport, port, groups,
   description — never username or password.

5. If the user follows up with an inventory change ("add", "update", "remove"),
   load the **`rad-device-mng`** skill and follow its full intake workflow.
