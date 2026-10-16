---
name: consumer-group-rebalancing-and-partition-assignment
description: "Use when \"consumer group rebalancing and partition assignment\" is the work. using auto-commit with a short interval, acknowledging messages before processing actually completes and risking loss on crash."
---

# Consumer Group Rebalancing and Partition Assignment

using auto-commit with a short interval, acknowledging messages.

1. Do not: using auto-commit with a short interval, acknowledging messages before processing actually completes and risking.
2. Do not: not testing rebalance behavior under real scaling/deploy events, discovering processing gaps only in production.

Example:
```bash
identify the acknowledgement mode, retention, and ordering guarantee in config
```

Check: Do not: using auto-commit.
