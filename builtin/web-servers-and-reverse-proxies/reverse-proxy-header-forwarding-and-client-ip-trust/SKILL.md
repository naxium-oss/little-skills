---
name: reverse-proxy-header-forwarding-and-client-ip-trust
description: "Use when \"reverse proxy header forwarding and client ip trust\" is the work."
---

# Reverse Proxy Header Forwarding and Client

forgetting to forward X-Forwarded-Proto, causing.

1. Do not: forgetting to forward X-Forwarded-Proto, causing the app to think all requests are HTTP even.
2. Do not: trusting X-Forwarded-For from any source without restricting to known proxy IPs, enabling trivial IP.

Example:
```bash
nginx -T 2>/dev/null || caddy adapt --config <file> | head -40
```

Check: Do not: forgetting to.
