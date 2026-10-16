---
name: async-race
description: "Use when \"race condition\", \"forgot to await\", or \"unhandled promise\". Not when the code is synchronous."
---

# Await and races

An unawaited call finishes after you have already answered.

1. Find the promise that is not awaited or not ordered.
2. Await it, or cancel the stale one.
3. Test a slow response that returns out of order.

Example:
```text
Request 1 returns after request 2 and overwrites the newer state.
```

Check: Adding a sleep to hide the race is not a fix.
