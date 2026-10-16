---
name: transaction-isolation-anomaly-reproduction
description: "Use when \"transaction isolation anomaly reproduction\" is the work. Use coordinated concurrent sessions to reproduce anomalies at the configured isolation level."
---

# Transaction Isolation Anomaly Reproduction

Use coordinated concurrent sessions to reproduce anomalies at the configured isolation level.

1. Confirm engine and SQL dialect before selecting syntax.
2. Construct small fixtures with duplicates, nulls, and boundary values.
3. Inspect plans and transaction behavior using representative statistics.

Example:
```text
Confirm engine and SQL dialect before selecting syntax.
```

Check: Compare expected rows and counts; parameterize inputs; preview affected rows and prepare rollback before any bulk mutation.
