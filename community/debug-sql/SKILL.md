---
name: debug-sql
description: "Use when \"sql Query suddenly slow\", \"Query suddenly slow\". Not when explaining working sql code."
---

# Debug sql

Reproduce the sql failure with the project command, then change one thing.

1. Query suddenly slow: Run `EXPLAIN ANALYZE`: a Seq Scan on a large table means a missing.
2. Wrong row counts: A join fanning out on one side; `SELECT DISTINCT` hiding it. Count each.
3. NULL comparisons return nothing: `NULL = NULL` is not true; use `IS NULL` and `COALESCE` deliberately.

Example:
```text
Run the sql tests.
```

Check: The same command that failed has to pass.
