---
name: redis-streams-consumer-group-handling
description: "Use when \"redis streams consumer group handling\" is the work. Handle pending entries, acknowledgments, stalled consumers, reclamation, and poison messages."
---

# Redis Streams Consumer Group Handling

Handle pending entries, acknowledgments, stalled consumers, reclamation, and poison messages.

1. Verify server, client, topology, persistence, and eviction settings.
2. Define key ownership, TTL, invalidation, and atomicity requirements.

Example:
```text
Verify server, client, topology, persistence, and eviction settings.
```

Check: Check cluster multi-key restrictions, script behavior, data-loss windows, ACLs, exposure, and recovery rather than assuming standalone semantics.
