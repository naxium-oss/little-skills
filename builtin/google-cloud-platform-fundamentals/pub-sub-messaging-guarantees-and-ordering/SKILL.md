---
name: pub-sub-messaging-guarantees-and-ordering
description: "Use when \"pub sub messaging guarantees and ordering\" is the work."
---

# Pub/Sub Messaging Guarantees and Ordering

assuming default Pub/Sub delivery preserves.

1. Do not: assuming default Pub/Sub delivery preserves message order across a topic without enabling ordering keys.
2. Do not: enabling exactly-once delivery and assuming it removes all need for idempotent consumer logic, when.

Example:
```bash
gcloud pubsub topics create orders --message-storage-policy-allowed-regions=us-central1
```

Check: Do not: assuming default.
