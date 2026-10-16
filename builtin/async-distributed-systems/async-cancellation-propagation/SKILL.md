---
name: async-cancellation-propagation
description: "Use when \"async cancellation propagation\" is the work. Propagate cancellation to child work and release resources without leaving detached operations."
---

# Async Cancellation Propagation

Propagate cancellation to child work and release resources without leaving detached operations.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.
3. Inject delayed, duplicated, lost, and reordered operations in an isolated test environment.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
