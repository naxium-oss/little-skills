---
name: engine-and-dialect-version-grounding
description: "Use when \"engine and dialect version grounding\" is the work. writing PostgreSQL-specific syntax (ILIKE, RETURNING) against a MySQL connection and getting a syntax error."
---

# Engine and Dialect Version Grounding

writing PostgreSQL-specific syntax (ILIKE, RETURNING) against a.

1. Do not: writing PostgreSQL-specific syntax (ILIKE, RETURNING) against a MySQL connection and getting a syntax error.
2. Do not: assuming a feature available in the latest docs is present in an older pinned.

Example:
```sql
SELECT version();                          -- PostgreSQL
```

Check: Do not: writing PostgreSQL-specific syntax (ILIKE, RETURNING) against a MySQL connection and getting a syntax error.
