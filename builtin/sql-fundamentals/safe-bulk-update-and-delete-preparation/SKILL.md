---
name: safe-bulk-update-and-delete-preparation
description: "Use when \"safe bulk update and delete preparation\" is the work. Preview the exact predicate and row count, back up affected data, and use controlled transactions."
---

# Safe Bulk Update and Delete Preparation

Preview the exact predicate and row count, back up affected data, and use controlled transactions.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
