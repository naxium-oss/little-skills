---
name: sql-normal-forms-decomposition
description: "Use when \"sql normal forms decomposition\" is the work. Separate attributes according to dependencies rather than visual repetition alone."
---

# SQL Normal Forms & Decomposition

Separate attributes according to dependencies rather than visual repetition alone.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```sql
CREATE TABLE department (id integer PRIMARY KEY, name text NOT NULL);
CREATE TABLE employee (
id integer PRIMARY KEY,
```

Check: Do not edit the assert to match a surprising result.
