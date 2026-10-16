---
name: futures-promises-and-cancellation-propagation
description: "Use when \"futures promises and cancellation propagation\" is the work. assuming cancelling a future/promise immediately halts all underlying work, when many implementations only stop awaiting the result while."
---

# Futures, Promises, and Cancellation Propagation

assuming cancelling a future/promise immediately.

1. Do not: assuming cancelling a future/promise immediately halts all underlying work, when many implementations only stop.
2. Do not: forgetting to catch and handle a cancellation exception in cleanup code, leaking resources on.

Example:
```bash
identify every shared mutable resource and its guard
```

Check: Do not: assuming cancelling a future/promise immediately halts all underlying work, when many implementations only stop awaiting the.
