---
name: lock-contention-and-deadlock-analysis
description: "Use when \"lock contention and deadlock analysis\" is the work. Build a wait-for graph from active sessions and locks and identify the transaction holding progress."
---

# Lock Contention and Deadlock Analysis

Build a wait-for graph from active sessions and locks and identify the transaction holding progress.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.
3. Test proposed changes under realistic concurrency and transaction boundaries.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
