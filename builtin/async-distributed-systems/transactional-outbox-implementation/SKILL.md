---
name: transactional-outbox-implementation
description: "Use when \"transactional outbox implementation\" is the work. Commit domain state and outbox records in one transaction and test dispatcher crash windows."
---

# Transactional Outbox Implementation

Commit domain state and outbox records in one transaction and test dispatcher crash windows.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.
3. Inject delayed, duplicated, lost, and reordered operations in an isolated test environment.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
