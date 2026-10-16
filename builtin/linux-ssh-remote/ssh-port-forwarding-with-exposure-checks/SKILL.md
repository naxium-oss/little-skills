---
name: ssh-port-forwarding-with-exposure-checks
description: "Use when \"ssh port forwarding with exposure checks\" is the work. Inspect bind addresses and firewall rules to prove the tunnel exposes only the intended endpoint."
---

# SSH Port Forwarding with Exposure Checks

Inspect bind addresses and firewall rules to prove the tunnel exposes only the intended endpoint.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
