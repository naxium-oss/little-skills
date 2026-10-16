---
name: ssh-key-and-agent-configuration
description: "Use when \"ssh key and agent configuration\" is the work. Check key permissions, agent forwarding exposure, selected identity, and actual authentication traces."
---

# SSH Key and Agent Configuration

Check key permissions, agent forwarding exposure, selected identity, and actual authentication traces.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
