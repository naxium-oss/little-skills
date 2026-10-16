---
name: atomic-command-and-lua-script-correctness
description: "Use when \"atomic command and lua script correctness\" is the work. Keep operations atomic where required and account for script blocking, errors, and cluster constraints."
---

# Atomic Command and Lua Script Correctness

Keep operations atomic where required and account for script blocking, errors, and cluster constraints.

1. Verify server, client, topology, persistence, and eviction settings.
2. Define key ownership, TTL, invalidation, and atomicity requirements.

Example:
```text
Verify server, client, topology, persistence, and eviction settings.
```

Check: Check cluster multi-key restrictions, script behavior, data-loss windows, ACLs, exposure, and recovery rather than assuming standalone semantics.
