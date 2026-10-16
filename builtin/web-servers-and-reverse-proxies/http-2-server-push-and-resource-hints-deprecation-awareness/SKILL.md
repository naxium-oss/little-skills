---
name: http-2-server-push-and-resource-hints-deprecation-awareness
description: "Use when \"http 2 server push and resource hints deprecation awareness\" is the work."
---

# HTTP/2 Server Push and Resource Hints

implementing HTTP/2 Server Push based on outdated tutorials.

1. Do not: implementing HTTP/2 Server Push based on outdated tutorials, building infrastructure around a feature browsers.
2. Do not: overusing <link rel="preload"> for non-critical resources, competing for early bandwidth with genuinely critical resources.

Example:
```bash
nginx -T 2>/dev/null || caddy adapt --config <file> | head -40
```

Check: Do not: implementing HTTP/2.
