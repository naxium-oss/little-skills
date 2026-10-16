---
name: schema-migration-reversibility-assessment
description: "Use when \"schema migration reversibility assessment\" is the work. Assess data-loss reversibility separately from schema syntax reversal and test both migration directions."
---

# Schema Migration Reversibility Assessment

Assess data-loss reversibility separately from schema syntax reversal and test both migration directions.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
