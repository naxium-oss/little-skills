---
name: cache-stampede-prevention
description: "Use when \"cache stampede prevention\" is the work. Use bounded regeneration or coordinated refresh and test concurrent misses and worker crashes."
---

# Cache Stampede Prevention

Use bounded regeneration or coordinated refresh and test concurrent misses and worker crashes.

1. Verify server, client, topology, persistence, and eviction settings.
2. Define key ownership, TTL, invalidation, and atomicity requirements.
3. Exercise expiration, contention, memory pressure, and failover in a disposable environment.

Example:
```text
Verify server, client, topology, persistence, and eviction settings.
```

Check: Check cluster multi-key restrictions, script behavior, data-loss windows, ACLs, exposure, and recovery rather than assuming standalone semantics.
