---
name: cluster-hash-slot-and-multi-key-constraint-checking
description: "Use when \"cluster hash slot and multi key constraint checking\" is the work. Check key hash slots and tagged-key conventions before relying on multi-key operations."
---

# Cluster Hash Slot and Multi-Key Constraint

Check key hash slots and tagged-key.

1. Verify server, client, topology, persistence, and eviction settings.
2. Define key ownership, TTL, invalidation, and atomicity requirements.

Example:
```text
Verify server, client, topology, persistence, and eviction settings.
```

Check: Check cluster multi-key restrictions, script behavior, data-loss windows, ACLs, exposure, and recovery rather than assuming standalone semantics.
