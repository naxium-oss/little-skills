---
name: partial-failure-and-network-partition-testing
description: "Use when \"partial failure and network partition testing\" is the work. Inject isolated dependency failures and verify bounded resource use, degraded behavior, and recovery."
---

# Partial Failure and Network Partition Testing

Inject isolated dependency failures and verify bounded resource use, degraded behavior, and recovery.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
