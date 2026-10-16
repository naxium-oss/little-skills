---
name: systemd-unit-debugging
description: "Use when \"systemd unit debugging\" is the work. Inspect the effective unit, overrides, environment, dependencies, logs, and restart behavior."
---

# systemd Unit Debugging

Inspect the effective unit, overrides, environment, dependencies, logs, and restart behavior.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.
3. Preview transfers and validate quoting, permissions, exposure, and exit-code propagation.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
