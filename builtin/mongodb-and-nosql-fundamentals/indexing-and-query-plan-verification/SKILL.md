---
name: indexing-and-query-plan-verification
description: "Use when \"indexing and query plan verification\" is the work. creating an index whose field order doesnt match the querys equality-then-sort-then-range pattern (ESR rule), causing it to be."
---

# Indexing and Query Plan Verification

creating an index whose field.

1. Do not: creating an index whose field order doesn't match the query's equality-then-sort-then-range pattern (ESR rule).
2. Do not: assuming an index exists in production because it exists in a local dev database.

Example:
```javascript
db.orders.createIndex({ customerId: 1, createdAt: -1 });
```

Check: Do not: creating an.
