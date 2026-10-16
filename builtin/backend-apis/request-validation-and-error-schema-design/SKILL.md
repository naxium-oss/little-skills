---
name: request-validation-and-error-schema-design
description: "Use when \"request validation and error schema design\" is the work. Reject invalid types, bounds, unknown fields per policy, and expose stable non-sensitive error schemas."
---

# Request Validation and Error Schema Design

Reject invalid types, bounds, unknown fields per policy, and expose stable non-sensitive error schemas.

1. Define request, response, error, and authorization contracts.
2. Validate untrusted inputs at boundaries.

Example:
```text
Define request, response, error, and authorization contracts.
```

Check: Check object-level authorization, stable pagination, status semantics, replay windows, and backward compatibility with real contract fixtures.
