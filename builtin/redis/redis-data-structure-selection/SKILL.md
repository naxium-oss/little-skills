---
name: redis-data-structure-selection
description: "Use when \"redis data structure selection\" is the work. Select structures by access patterns, atomicity needs, cardinality, encoding, and memory overhead."
---

# Redis Data Structure Selection

Select structures by access patterns, atomicity needs, cardinality, encoding, and memory overhead.

1. Verify server, client, topology, persistence, and eviction settings.
2. Define key ownership, TTL, invalidation, and atomicity requirements.

Example:
```text
Verify server, client, topology, persistence, and eviction settings.
```

Check: Check cluster multi-key restrictions, script behavior, data-loss windows, ACLs, exposure, and recovery rather than assuming standalone semantics.
