---
name: sql-relational-keys-functional-dependencies
description: "Use when \"sql relational keys functional dependencies\" is the work. A candidate key minimally determines each row."
---

# SQL Relational Keys & Functional Dependencies

A candidate key minimally determines each row.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
CREATE TABLE account (
id bigint PRIMARY KEY,
email text NOT NULL UNIQUE,
```

Check: Do not edit the assert to match a surprising result.
