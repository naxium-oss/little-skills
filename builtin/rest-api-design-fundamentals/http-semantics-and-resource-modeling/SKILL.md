---
name: http-semantics-and-resource-modeling
description: "Use when \"http semantics and resource modeling\" is the work. using POST for operations that are actually idempotent updates, breaking safe-retry assumptions in clients/proxies."
---

# HTTP Semantics and Resource Modeling

using POST for operations that are actually.

1. Do not: using POST for operations that are actually idempotent updates, breaking safe-retry assumptions in clients/proxies.
2. Do not: returning 200 for a resource-creation endpoint instead of 201 with a Location header.

Example:
```bash
curl -sS -D - <endpoint> -o /dev/null
```

Check: Do not: using POST for operations that are.
