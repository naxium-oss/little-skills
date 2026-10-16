---
name: join-cardinality-and-duplicate-diagnosis
description: "Use when \"join cardinality and duplicate diagnosis\" is the work. Annotate each relations grain and expected join multiplicity and test duplicate-heavy fixtures."
---

# Join Cardinality and Duplicate Diagnosis

Annotate each relation's grain and expected join multiplicity and test duplicate-heavy fixtures.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
