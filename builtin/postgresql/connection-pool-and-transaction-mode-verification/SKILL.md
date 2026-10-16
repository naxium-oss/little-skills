---
name: connection-pool-and-transaction-mode-verification
description: "Use when \"connection pool and transaction mode verification\" is the work. Confirm pooler version and session or transaction mode against prepared statements and session state."
---

# Connection Pool and Transaction Mode Verification

Confirm pooler version and session or transaction mode against prepared statements and session state.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.
3. Test proposed changes under realistic concurrency and transaction boundaries.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
