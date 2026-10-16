---
name: remote-environment-parity-verification
description: "Use when \"remote environment parity verification\" is the work. Compare runtime, PATH, locale, shell startup, libraries, permissions, and filesystem behavior across hosts."
---

# Remote Environment Parity Verification

Compare runtime, PATH, locale, shell startup, libraries, permissions, and filesystem behavior across hosts.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
