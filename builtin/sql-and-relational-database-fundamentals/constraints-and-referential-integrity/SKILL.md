---
name: constraints-and-referential-integrity
description: "Use when \"constraints and referential integrity\" is the work. relying solely on application-level validation for uniqueness/referential integrity, allowing a race condition to insert duplicate or orphaned rows."
---

# Constraints and Referential Integrity

relying solely on application-level.

1. Do not: relying solely on application-level validation for uniqueness/referential integrity, allowing a race condition to insert.
2. Do not: adding a foreign key with ON DELETE CASCADE without realizing it will silently delete.

Example:
```sql
ALTER TABLE orders ADD CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(id);
```

Check: Do not: relying solely on application-level validation for uniqueness/referential.
