---
name: pagination-and-stable-ordering-design
description: "Use when \"pagination and stable ordering design\" is the work. Use deterministic tie-breakers and define cursor behavior under concurrent inserts, updates, and deletes."
---

# Pagination and Stable Ordering Design

Use deterministic tie-breakers and define cursor behavior under concurrent inserts, updates, and deletes.

1. Define request, response, error, and authorization contracts.
2. Validate untrusted inputs at boundaries.

Example:
```text
Define request, response, error, and authorization contracts.
```

Check: Check object-level authorization, stable pagination, status semantics, replay windows, and backward compatibility with real contract fixtures.
