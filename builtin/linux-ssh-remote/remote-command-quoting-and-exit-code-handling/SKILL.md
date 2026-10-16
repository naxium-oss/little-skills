---
name: remote-command-quoting-and-exit-code-handling
description: "Use when \"remote command quoting and exit code handling\" is the work. Distinguish local and remote expansion and propagate remote failures without masking exit codes."
---

# Remote Command Quoting and Exit-Code Handling

Distinguish local and remote expansion and propagate remote failures without masking exit codes.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
