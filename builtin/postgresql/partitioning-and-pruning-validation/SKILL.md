---
name: partitioning-and-pruning-validation
description: "Use when \"partitioning and pruning validation\" is the work. Verify partition bounds, routing, pruning, uniqueness restrictions, and maintenance costs."
---

# Partitioning and Pruning Validation

Verify partition bounds, routing, pruning, uniqueness restrictions, and maintenance costs.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.
3. Test proposed changes under realistic concurrency and transaction boundaries.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
