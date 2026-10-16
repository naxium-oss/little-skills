---
name: producer-acknowledgment-and-durability-tradeoffs
description: "Use when \"producer acknowledgment and durability tradeoffs\" is the work. using acks=1 (leader-only acknowledgment) for critical financial events, risking data loss on leader failure before replication."
---

# Producer Acknowledgment and Durability Tradeoffs

using acks=1 (leader-only acknowledgment) for critical financial events.

1. Do not: using acks=1 (leader-only acknowledgment) for critical financial events, risking data loss on leader failure.
2. Do not: leaving producer retries enabled without enable_idempotence, risking duplicate message delivery on retry.

Example:
```bash
identify the acknowledgement mode, retention, and ordering guarantee in config
```

Check: Do not: using acks=1.
