---
name: query-parameterization
description: "Use when \"query parameterization\" is the work. Bind values using the verified driver API and allowlist identifiers that cannot be parameterized."
---

# Query Parameterization

Bind values using the verified driver API and allowlist identifiers that cannot be parameterized.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
