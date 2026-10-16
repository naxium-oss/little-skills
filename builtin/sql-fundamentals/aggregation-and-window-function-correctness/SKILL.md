---
name: aggregation-and-window-function-correctness
description: "Use when \"aggregation and window function correctness\" is the work. Verify grouping grain, frame bounds, partition keys, and deterministic window ordering."
---

# Aggregation and Window Function Correctness

Verify grouping grain, frame bounds, partition keys, and deterministic window ordering.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
