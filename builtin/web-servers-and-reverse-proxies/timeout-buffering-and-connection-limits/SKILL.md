---
name: timeout-buffering-and-connection-limits
description: "Use when \"timeout buffering and connection limits\" is the work. setting a generous application-level upload limit while a stricter reverse-proxy or CDN default silently rejects large requests first."
---

# Timeout, Buffering, and Connection Limits

setting a generous application-level.

1. Do not: setting a generous application-level upload limit while a stricter reverse-proxy or CDN default silently.
2. Do not: assuming a single component's timeout setting controls end-to-end behavior when multiple layered timeouts exist.

Example:
```bash
nginx -T 2>/dev/null || caddy adapt --config <file> | head -40
```

Check: Do not: setting a.
