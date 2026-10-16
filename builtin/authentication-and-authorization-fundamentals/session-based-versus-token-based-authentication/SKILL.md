---
name: session-based-versus-token-based-authentication
description: "Use when \"session based versus token based authentication\" is the work. assuming JWT logout immediately invalidates the token everywhere."
---

# Session-Based versus Token-Based Authentication

assuming JWT "logout" immediately invalidates the token everywhere.

1. Do not: assuming JWT "logout" immediately invalidates the token everywhere.
2. Do not: storing JWTs in localStorage (accessible to any XSS payload) instead of an HttpOnly cookie.

Example:
```bash
identify the token format and expiry policy from config, not memory
```

Check: Do not: assuming JWT "logout" immediately invalidates the token everywhere.
