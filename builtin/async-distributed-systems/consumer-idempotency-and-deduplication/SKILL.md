---
name: consumer-idempotency-and-deduplication
description: "Use when \"consumer idempotency and deduplication\" is the work. Atomically bind deduplication records to side effects and define retention and replay behavior."
---

# Consumer Idempotency and Deduplication

Atomically bind deduplication records to side effects and define retention and replay behavior.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.
3. Inject delayed, duplicated, lost, and reordered operations in an isolated test environment.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
