---
name: sql-check-referential-constraint-design
description: "Use when \"sql check referential constraint design\" is the work. CHECK expressions that evaluate to unknown may pass."
---

# SQL CHECK & Referential Constraint Design

CHECK expressions that evaluate to unknown may pass.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
CREATE TABLE stock (
sku text PRIMARY KEY,
quantity integer NOT NULL CHECK (quantity >= 0)
```

Check: Do not edit the assert to match a surprising result.
