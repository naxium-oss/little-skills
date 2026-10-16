---
name: authentication-middleware-integration
description: "Use when \"authentication middleware integration\" is the work. Verify signature, issuer, audience, expiry, session state, and middleware ordering as applicable."
---

# Authentication Middleware Integration

Verify signature, issuer, audience, expiry, session state, and middleware ordering as applicable.

1. Define request, response, error, and authorization contracts.
2. Validate untrusted inputs at boundaries.
3. Test normal, malformed, unauthorized, duplicate, and concurrent requests against the actual service stack.

Example:
```text
Define request, response, error, and authorization contracts.
```

Check: Check object-level authorization, stable pagination, status semantics, replay windows, and backward compatibility with real contract fixtures.
