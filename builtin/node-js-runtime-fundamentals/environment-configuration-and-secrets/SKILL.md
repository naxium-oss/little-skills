---
name: environment-configuration-and-secrets
description: "Use when \"environment configuration and secrets\" is the work. assuming dotenv auto-loads without explicit import dotenv/config."
---

# Environment Configuration and Secrets

assuming dotenv auto-loads without explicit import "dotenv/config".

1. Do not: assuming dotenv auto-loads without explicit import "dotenv/config".
2. Do not: hardcoding fallback secrets that silently work in dev and mask missing production config.

Example:
```bash
node --env-file=.env.production server.js
```

Check: Do not: assuming dotenv auto-loads without explicit import "dotenv/config".
