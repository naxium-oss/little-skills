---
name: environment-variables-and-client-server-exposure-boundaries
description: "Use when \"environment variables and client server exposure boundaries\" is the work."
---

# Environment Variables and Client/Server Exposure Boundaries

prefixing a secret (API key.

1. Do not: prefixing a secret (API key, DB credential) with NEXT_PUBLIC_ out of habit or copy-paste.
2. Do not: assuming a non-prefixed variable is safe to reference in client component code, when it.

Example:
```bash
DATABASE_URL=postgres://...          # server-only, never bundled to the client
```

Check: Do not: prefixing a.
