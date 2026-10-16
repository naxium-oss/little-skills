---
name: cache-key-ttl-and-invalidation-design
description: "Use when \"cache key ttl and invalidation design\" is the work. Define namespace, serialization, ownership, expiry, invalidation triggers, and stale-read tolerance."
---

# Cache Key, TTL, and Invalidation Design

Define namespace, serialization, ownership, expiry.

1. Verify server, client, topology, persistence, and eviction settings.
2. Define key ownership, TTL, invalidation, and atomicity requirements.

Example:
```text
Verify server, client, topology, persistence, and eviction settings.
```

Check: Check cluster multi-key restrictions, script behavior, data-loss windows, ACLs, exposure, and recovery rather than assuming standalone semantics.
