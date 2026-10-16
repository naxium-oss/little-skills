---
name: mvcc-vacuum-and-table-bloat-diagnosis
description: "Use when \"mvcc vacuum and table bloat diagnosis\" is the work. Inspect dead tuples, transaction age, vacuum progress, visibility, and long-lived snapshots."
---

# MVCC, Vacuum, and Table Bloat Diagnosis

Inspect dead tuples, transaction age, vacuum progress, visibility, and long-lived snapshots.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
