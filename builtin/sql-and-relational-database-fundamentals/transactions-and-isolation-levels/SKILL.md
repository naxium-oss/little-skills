---
name: transactions-and-isolation-levels
description: "Use when \"transactions and isolation levels\" is the work. assuming SERIALIZABLE prevents all race conditions without handling serialization-failure retries."
---

# Transactions and Isolation Levels

assuming SERIALIZABLE prevents all race conditions without handling serialization-failure retries.

1. Do not: assuming SERIALIZABLE prevents all race conditions without handling serialization-failure retries.
2. Do not: forgetting FOR UPDATE row locking when implementing a read-then-write balance update, causing lost-update races.

Example:
```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;   -- row lock to prevent lost update
```

Check: Do not: assuming SERIALIZABLE prevents all race conditions without handling serialization-failure retries.
