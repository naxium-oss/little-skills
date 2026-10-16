---
name: sql-dialect-and-engine-version-verification
description: "Use when \"sql dialect and engine version verification\" is the work. Capture server version, dialect mode, extensions, collation, and driver behavior before choosing syntax."
---

# SQL Dialect and Engine Version Verification

Capture server version, dialect mode, extensions, collation, and driver behavior before choosing syntax.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
