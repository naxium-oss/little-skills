---
name: safe-file-synchronization-with-dry-runs
description: "Use when \"safe file synchronization with dry runs\" is the work. Preview file additions, deletions, permissions, and symlinks before authorizing synchronization."
---

# Safe File Synchronization with Dry Runs

Preview file additions, deletions, permissions, and symlinks before authorizing synchronization.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
