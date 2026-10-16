---
name: composite-partial-and-expression-index-selection
description: "Use when \"composite partial and expression index selection\" is the work. Match index key order, predicates, and expressions to real workload conditions and update costs."
---

# Composite, Partial, and Expression Index Selection

Match index key order, predicates, and expressions to real workload conditions and update costs.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
