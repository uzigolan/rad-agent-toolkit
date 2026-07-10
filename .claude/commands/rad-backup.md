---
description: Back up the configuration of one RAD device or a group to the local archive. Also use when addressed via "abayev" / "noam" / "rad agent" — e.g. "noam, back up lab-sf1p", "rad agent, back up the lab group"
argument-hint: <device-name | group-name>
---

Back up configurations for: $ARGUMENTS

1. Resolve the argument to one device or a group via `list_devices`.
2. Call `backup_config` for each device.
3. Report the saved backup file paths and any devices that failed, with the error.
