---
name: sql-views-logical-data-interfaces
description: "Use when \"sql views logical data interfaces\" is the work. Ordinary views name a query rather than necessarily materializing data."
---

# SQL Views & Logical Data Interfaces

Ordinary views name a query rather than necessarily materializing data.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
CREATE TABLE item (id integer PRIMARY KEY, active boolean NOT NULL);
CREATE VIEW active_item AS SELECT id FROM item WHERE active;
```

Check: Do not edit the assert to match a surprising result.
