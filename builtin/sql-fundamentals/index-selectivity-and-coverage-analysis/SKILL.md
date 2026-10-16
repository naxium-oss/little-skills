---
name: index-selectivity-and-coverage-analysis
description: "Use when \"index selectivity and coverage analysis\" is the work. Measure cardinality and workload predicates; include write overhead and index storage in the decision."
---

# Index Selectivity and Coverage Analysis

Measure cardinality and workload predicates; include write overhead and index storage in the decision.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
