---
name: message-delivery-semantics-verification
description: "Use when \"message delivery semantics verification\" is the work. Verify acknowledgment, persistence, redelivery, ordering, and failure guarantees under actual broker settings."
---

# Message Delivery Semantics Verification

Verify acknowledgment, persistence, redelivery, ordering, and failure guarantees under actual broker settings.

1. Model delivery, ordering, clock, and failure assumptions explicitly.
2. Bound concurrency, queue sizes, retries, and deadlines.

Example:
```text
Model delivery, ordering, clock, and failure assumptions explicitly.
```

Check: Test cancellation propagation, retry amplification, poison messages, partitions, and recovery; document guarantees and their configuration dependencies.
