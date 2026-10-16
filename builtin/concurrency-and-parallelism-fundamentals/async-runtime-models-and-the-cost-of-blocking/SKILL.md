---
name: async-runtime-models-and-the-cost-of-blocking
description: "Use when \"async runtime models and the cost of blocking\" is the work."
---

# Async Runtime Models and the Cost

calling a synchronous, blocking library.

1. Do not: calling a synchronous, blocking library function (a non-async DB driver, requests.get) inside an async.
2. Do not: assuming await-ing a function makes it non-blocking regardless of what it does internally.

Example:
```bash
identify every shared mutable resource and its guard
```

Check: Do not: calling a.
