---
description: Run a health check on one RAD device or a group and summarize findings. Also use when addressed via "abayev" / "noam" / "rad agent" — e.g. "abayev, run a health check on lab-sf1p", "rad agent, check the lab group"
argument-hint: <device-name | group-name>
---

Run a health sweep on: $ARGUMENTS

1. If the argument matches a group, `list_devices(group=...)` and health-check each; otherwise treat it as a device name. With no argument, list devices and ask which.
2. For each device call `health_check` and, if alarms need more context, targeted `run_show` commands.
3. Summarize as a table: device, reachability, active alarms (by severity), anything abnormal in the summary output.
4. Flag any major/critical alarm prominently and suggest the next diagnostic step. Do not make any configuration changes.
