---
name: openapi-contract-validation
description: "Use when \"openapi contract validation\" is the work. Validate request and response examples against the pinned OpenAPI version and actual implementation."
---

# OpenAPI Contract Validation

Validate request and response examples against the pinned OpenAPI version and actual implementation.

1. Define request, response, error, and authorization contracts.
2. Validate untrusted inputs at boundaries.
3. Test normal, malformed, unauthorized, duplicate, and concurrent requests against the actual service stack.

Example:
```text
Define request, response, error, and authorization contracts.
```

Check: Check object-level authorization, stable pagination, status semantics, replay windows, and backward compatibility with real contract fixtures.
