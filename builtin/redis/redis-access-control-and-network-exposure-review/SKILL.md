---
name: redis-access-control-and-network-exposure-review
description: "Use when \"redis access control and network exposure review\" is the work. Inspect bind addresses, transport protection, ACL users, command permissions, and secret handling."
---

# Redis Access Control and Network Exposure

Inspect bind addresses, transport protection, ACL.

1. Verify server, client, topology, persistence, and eviction settings.
2. Define key ownership, TTL, invalidation, and atomicity requirements.

Example:
```text
Verify server, client, topology, persistence, and eviction settings.
```

Check: Check cluster multi-key restrictions, script behavior, data-loss windows, ACLs, exposure, and recovery rather than assuming standalone semantics.
