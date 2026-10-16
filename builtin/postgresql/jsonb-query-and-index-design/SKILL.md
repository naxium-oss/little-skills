---
name: jsonb-query-and-index-design
description: "Use when \"jsonb query and index design\" is the work. Match JSONB operators and operator classes to query shapes and validate index usage."
---

# JSONB Query and Index Design

Match JSONB operators and operator classes to query shapes and validate index usage.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.
3. Test proposed changes under realistic concurrency and transaction boundaries.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
