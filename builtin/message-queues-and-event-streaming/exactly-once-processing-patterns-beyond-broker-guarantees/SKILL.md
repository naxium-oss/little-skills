---
name: exactly-once-processing-patterns-beyond-broker-guarantees
description: "Use when \"exactly once processing patterns beyond broker guarantees\" is the work."
---

# Exactly-Once Processing Patterns Beyond Broker Guarantees

assuming a broker's "exactly-once" configuration.

1. Do not: assuming a broker's "exactly-once" configuration eliminates the need for any application-level idempotency handling for.
2. Do not: checking for a duplicate and performing the actual side effect as two separate non-transactional.

Example:
```bash
identify the acknowledgement mode, retention, and ordering guarantee in config
```

Check: Do not: assuming a.
