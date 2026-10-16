---
name: postgresql-server-and-extension-version-verification
description: "Use when \"postgresql server and extension version verification\" is the work. Read server build, installed extension versions, available upgrades, and client/server compatibility."
---

# PostgreSQL Server and Extension Version Verification

Read server build, installed extension versions, available upgrades, and client/server compatibility.

1. Capture server, extension, pooler, and configuration versions.
2. Inspect catalog statistics and plans on representative data.
3. Test proposed changes under realistic concurrency and transaction boundaries.

Example:
```text
Capture server, extension, pooler, and configuration versions.
```

Check: Remember EXPLAIN ANALYZE executes the statement; use a safe environment for writes; validate restoration, lock impact, and rollback.
