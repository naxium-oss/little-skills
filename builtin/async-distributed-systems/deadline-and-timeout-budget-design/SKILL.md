---
name: deadline-and-timeout-budget-design
description: "Use when \"deadline and timeout budget design\" is the work. Allocate a total deadline across hops and retries using monotonic time where available."
---

# Deadline and Timeout Budget Design

Allocate a total deadline across hops and retries using monotonic time where available.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.
3. Inject delayed, duplicated, lost, and reordered operations in an isolated test environment.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
