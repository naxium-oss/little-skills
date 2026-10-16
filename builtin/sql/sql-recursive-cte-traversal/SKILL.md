---
name: sql-recursive-cte-traversal
description: "Use when \"sql recursive cte traversal\" is the work. Separate the seed term from the recursive step."
---

# SQL Recursive CTE Traversal

Separate the seed term from the recursive step.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
WITH RECURSIVE numbers(n) AS (
VALUES (1)
UNION ALL
```

Check: Do not edit the assert to match a surprising result.
