---
name: replica-sets-and-read-write-concern-tuning
description: "Use when \"replica sets and read write concern tuning\" is the work."
---

# Replica Sets and Read/Write Concern Tuning

using w: 1 (default in.

1. Do not: using w: 1 (default in many client configs) for critical writes, risking data loss.
2. Do not: reading from secondaries without accounting for replication lag, serving stale data to users expecting.

Example:
```javascript
db.orders.insertOne(doc, { writeConcern: { w: "majority", wtimeout: 5000 } });
```

Check: Do not: using w.
