---
name: change-streams-for-real-time-reactivity
description: "Use when \"change streams for real time reactivity\" is the work. running change streams against a standalone (non-replica-set) instance, which doesnt support them."
---

# Change Streams for Real-Time Reactivity

running change streams against a standalone.

1. Do not: running change streams against a standalone (non-replica-set) instance, which doesn't support them.
2. Do not: not persisting resume tokens, causing every consumer restart to either miss events or require.

Example:
```javascript
const changeStream = db.collection("orders").watch([{ $match: { operationType: "insert" } }]);
```

Check: Do not: running.
