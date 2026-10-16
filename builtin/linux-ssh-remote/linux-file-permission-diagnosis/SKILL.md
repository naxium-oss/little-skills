---
name: linux-file-permission-diagnosis
description: "Use when \"linux file permission diagnosis\" is the work. Inspect user identity, ownership, groups, mode bits, ACLs, mount options, and parent-directory access."
---

# Linux File Permission Diagnosis

Inspect user identity, ownership, groups, mode bits, ACLs, mount options, and parent-directory access.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
