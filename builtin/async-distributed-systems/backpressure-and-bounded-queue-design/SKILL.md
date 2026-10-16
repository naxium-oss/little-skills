---
name: backpressure-and-bounded-queue-design
description: "Use when \"backpressure and bounded queue design\" is the work. Bound producer concurrency and queue length and define overload rejection or slowing behavior."
---

# Backpressure and Bounded Queue Design

Bound producer concurrency and queue length and define overload rejection or slowing behavior.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.
3. Inject delayed, duplicated, lost, and reordered operations in an isolated test environment.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
