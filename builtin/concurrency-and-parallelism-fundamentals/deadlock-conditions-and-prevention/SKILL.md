---
name: deadlock-conditions-and-prevention
description: "Use when \"deadlock conditions and prevention\" is the work. acquiring locks in different orders in different functions operating on the same pair of resources, creating a circular-wait."
---

# Deadlock Conditions and Prevention

acquiring locks in different orders in different functions operating on the.

1. Do not: acquiring locks in different orders in different functions operating on the same pair of.
2. Do not: using a single global lock as a blunt "fix," reintroducing serialization bottlenecks.

Example:
```bash
identify every shared mutable resource and its guard
```

Check: Do not: acquiring locks in different orders in different functions operating on the same pair of resources, creating.
