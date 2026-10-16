---
name: retry-policy-and-jitter-design
description: "Use when \"retry policy and jitter design\" is the work. Retry only safe transient failures with capped attempts, jitter, and a shared deadline."
---

# Retry Policy and Jitter Design

Retry only safe transient failures with capped attempts, jitter, and a shared deadline.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
