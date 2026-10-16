---
name: backward-compatible-api-evolution
description: "Use when \"backward compatible api evolution\" is the work. Test old consumers against additive and breaking changes and publish migration and deprecation plans."
---

# Backward-Compatible API Evolution

Test old consumers against additive and breaking changes and publish migration and deprecation plans.

1. Define request, response, error, and authorization contracts.
2. Validate untrusted inputs at boundaries.
3. Test normal, malformed, unauthorized, duplicate, and concurrent requests against the actual service stack.

Example:
```text
Define request, response, error, and authorization contracts.
```

Check: Check object-level authorization, stable pagination, status semantics, replay windows, and backward compatibility with real contract fixtures.
