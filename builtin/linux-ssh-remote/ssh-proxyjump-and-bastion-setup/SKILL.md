---
name: ssh-proxyjump-and-bastion-setup
description: "Use when \"ssh proxyjump and bastion setup\" is the work. Verify each hops identity and trust boundary and avoid leaking credentials to intermediate hosts."
---

# SSH ProxyJump and Bastion Setup

Verify each hop's identity and trust boundary and avoid leaking credentials to intermediate hosts.

1. Verify the remote host identity through an independent trusted channel.
2. Inspect effective SSH and shell configuration.

Example:
```text
Verify the remote host identity through an independent trusted channel.
```

Check: Never bypass host-key verification to make a connection work; confirm user, host, path, and dry-run output before destructive.
