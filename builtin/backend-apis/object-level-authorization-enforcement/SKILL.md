---
name: object-level-authorization-enforcement
description: "Use when \"object level authorization enforcement\" is the work. Authorize the requested object and action using trusted identity and ownership data on every path."
---

# Object-Level Authorization Enforcement

Authorize the requested object and action using trusted identity and ownership data on every path.

1. Define request, response, error, and authorization contracts.
2. Validate untrusted inputs at boundaries.
3. Test normal, malformed, unauthorized, duplicate, and concurrent requests against the actual service stack.

Example:
```text
Define request, response, error, and authorization contracts.
```

Check: Check object-level authorization, stable pagination, status semantics, replay windows, and backward compatibility with real contract fixtures.
