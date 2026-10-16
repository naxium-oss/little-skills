---
name: dead-letter-queues-and-poison-message-handling
description: "Use when \"dead letter queues and poison message handling\" is the work. retrying a poison message indefinitely without a DLQ, causing it to block a partition/queue and stall all subsequent."
---

# Dead Letter Queues and Poison Message

retrying a poison message indefinitely.

1. Do not: retrying a poison message indefinitely without a DLQ, causing it to block a partition/queue.
2. Do not: routing messages to a DLQ with no monitoring or alerting, letting critical failed events.

Example:
```bash
identify the acknowledgement mode, retention, and ordering guarantee in config
```

Check: Do not: retrying a poison message indefinitely without a.
