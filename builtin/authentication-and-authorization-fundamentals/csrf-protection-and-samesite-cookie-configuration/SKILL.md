---
name: csrf-protection-and-samesite-cookie-configuration
description: "Use when \"csrf protection and samesite cookie configuration\" is the work. relying solely on SameSite=Lax without server-side CSRF token validation for high-value state-changing actions."
---

# CSRF Protection and SameSite Cookie Configuration

relying solely on SameSite=Lax without server-side.

1. Do not: relying solely on SameSite=Lax without server-side CSRF token validation for high-value state-changing actions.
2. Do not: setting SameSite=None for cross-site embedding convenience without understanding it disables this specific protection layer.

Example:
```bash
identify the token format and expiry policy from config, not memory
```

Check: Do not: relying.
