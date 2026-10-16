---
name: zero-trust-and-defense-in-depth-authorization-layering
description: "Use when \"zero trust and defense in depth authorization layering\" is the work."
---

# Zero Trust and Defense-in-Depth Authorization Layering

relying entirely on application-layer authorization.

1. Do not: relying entirely on application-layer authorization checks with no database or infrastructure-level backstop, so a.
2. Do not: treating internal-network services as inherently trusted, skipping authentication between them entirely.

Example:
```bash
identify the token format and expiry policy from config, not memory
```

Check: Do not: relying entirely.
