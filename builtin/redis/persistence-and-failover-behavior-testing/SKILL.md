---
name: persistence-and-failover-behavior-testing
description: "Use when \"persistence and failover behavior testing\" is the work. Test acknowledged-write survival and recovery time across configured persistence and failover modes."
---

# Persistence and Failover Behavior Testing

Test acknowledged-write survival and recovery time across configured persistence and failover modes.

1. Verify server, client, topology, persistence, and eviction settings.
2. Define key ownership, TTL, invalidation, and atomicity requirements.

Example:
```text
Verify server, client, topology, persistence, and eviction settings.
```

Check: Check cluster multi-key restrictions, script behavior, data-loss windows, ACLs, exposure, and recovery rather than assuming standalone semantics.
