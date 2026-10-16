---
name: null-and-three-valued-logic-handling
description: "Use when \"null and three valued logic handling\" is the work. Trace UNKNOWN through predicates, joins, aggregates, and NOT IN using explicit null fixtures."
---

# NULL and Three-Valued Logic Handling

Trace UNKNOWN through predicates, joins, aggregates, and NOT IN using explicit null fixtures.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
