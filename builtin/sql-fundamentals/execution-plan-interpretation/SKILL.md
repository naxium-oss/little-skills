---
name: execution-plan-interpretation
description: "Use when \"execution plan interpretation\" is the work. Compare estimated and actual rows, join choices, scan types, sorting, and resource consumption."
---

# Execution Plan Interpretation

Compare estimated and actual rows, join choices, scan types, sorting, and resource consumption.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
