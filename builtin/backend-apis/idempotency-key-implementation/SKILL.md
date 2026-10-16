---
name: idempotency-key-implementation
description: "Use when \"idempotency key implementation\" is the work. Scope keys by caller and operation and atomically associate them with payload hashes and stored results."
---

# Idempotency Key Implementation

Scope keys by caller and operation and atomically associate them with payload hashes and stored results.

1. Define request, response, error, and authorization contracts.
2. Validate untrusted inputs at boundaries.
3. Test normal, malformed, unauthorized, duplicate, and concurrent requests against the actual service stack.

Example:
```text
Define request, response, error, and authorization contracts.
```

Check: Check object-level authorization, stable pagination, status semantics, replay windows, and backward compatibility with real contract fixtures.
