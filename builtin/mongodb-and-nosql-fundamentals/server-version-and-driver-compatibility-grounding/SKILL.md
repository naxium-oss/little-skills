---
name: server-version-and-driver-compatibility-grounding
description: "Use when \"server version and driver compatibility grounding\" is the work."
---

# Server Version and Driver Compatibility Grounding

assuming multi-document transactions work on a standalone (non-replica-set).

1. Do not: assuming multi-document transactions work on a standalone (non-replica-set) deployment, they require a replica set.
2. Do not: using an aggregation operator introduced in a newer server version than what's deployed.

Example:
```bash
db.collection.find(...).explain("executionStats")
```

Check: Do not: assuming multi-document.
