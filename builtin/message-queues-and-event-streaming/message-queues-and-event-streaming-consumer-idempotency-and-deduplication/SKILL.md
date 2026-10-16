---
name: message-queues-and-event-streaming-consumer-idempotency-and-deduplication
description: "Use when \"consumer idempotency and deduplication\" is the work. writing consumer logic that assumes each message arrives exactly once, causing duplicate charges/emails/side-effects on redelivery after a consumer."
---

# Consumer Idempotency and Deduplication

writing consumer logic that.

1. Do not: writing consumer logic that assumes each message arrives exactly once, causing duplicate charges/emails/side-effects on.
2. Do not: storing deduplication state only in memory, losing it on consumer restart and allowing duplicates.

Example:
```bash
identify the acknowledgement mode, retention, and ordering guarantee in config
```

Check: Do not: writing consumer logic that assumes each message.
