---
name: logical-replication-compatibility-checking
description: "Use when \"logical replication compatibility checking\" is the work. Check publisher/subscriber versions, replica identity, schema alignment, slots, and unsupported operations."
---

# Logical Replication Compatibility Checking

Check publisher/subscriber versions, replica identity, schema alignment, slots, and unsupported operations.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.
3. Test proposed changes under realistic concurrency and transaction boundaries.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
