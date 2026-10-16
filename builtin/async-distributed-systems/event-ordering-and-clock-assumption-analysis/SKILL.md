---
name: event-ordering-and-clock-assumption-analysis
description: "Use when \"event ordering and clock assumption analysis\" is the work. Separate event time, processing time, logical ordering, and wall-clock synchronization assumptions."
---

# Event Ordering and Clock Assumption Analysis

Separate event time, processing time, logical ordering, and wall-clock synchronization assumptions.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
