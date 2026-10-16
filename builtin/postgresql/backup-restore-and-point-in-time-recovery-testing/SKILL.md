---
name: backup-restore-and-point-in-time-recovery-testing
description: "Use when \"backup restore and point in time recovery testing\" is the work. Restore into an isolated instance and verify application invariants at the intended recovery timestamp."
---

# Backup Restore and Point-in-Time Recovery Testing

Restore into an isolated instance and verify application invariants at the intended recovery timestamp.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
