---
name: reverse-proxy-version-and-module-grounding
description: "Use when \"reverse proxy version and module grounding\" is the work. applying an Nginx directive that requires a module not compiled into the installed binary, causing a silent no-op."
---

# Reverse Proxy Version and Module Grounding

applying an Nginx directive that.

1. Do not: applying an Nginx directive that requires a module not compiled into the installed binary.
2. Do not: reloading a syntactically valid but logically wrong config without testing it against a staging.

Example:
```bash
nginx -T 2>/dev/null || caddy adapt --config <file> | head -40
```

Check: Do not: applying an Nginx directive that requires a.
