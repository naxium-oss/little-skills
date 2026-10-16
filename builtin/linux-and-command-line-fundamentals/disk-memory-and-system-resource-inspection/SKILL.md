---
name: disk-memory-and-system-resource-inspection
description: "Use when \"disk memory and system resource inspection\" is the work. trusting du totals without -x when directories span multiple filesystems/mounts, causing double-counting."
---

# Disk, Memory, and System Resource Inspection

trusting du totals without -x when.

1. Do not: trusting du totals without -x when directories span multiple filesystems/mounts, causing double-counting.
2. Do not: ignoring inode exhaustion as a separate failure mode from byte capacity.

Example:
```bash
df -h                          # human-readable disk free per filesystem
```

Check: Do not: trusting du totals without -x when directories span multiple filesystems/mounts, causing double-counting.
