---
name: ssh-host-key-verification
description: "Use when \"ssh host key verification\" is the work. Confirm host fingerprints through an independent trusted source and investigate unexpected key changes."
---

# SSH Host Key Verification

Confirm host fingerprints through an independent trusted source and investigate unexpected key changes.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.
3. Preview transfers and validate quoting, permissions, exposure, and exit-code propagation.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
