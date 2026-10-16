---
name: rate-limiting-strategies-and-client-communication
description: "Use when \"rate limiting strategies and client communication\" is the work. implementing rate limiting with in-process memory state behind a load balancer, allowing the effective limit to multiply by."
---

# Rate Limiting Strategies and Client Communication

implementing rate limiting with in-process.

1. Do not: implementing rate limiting with in-process memory state behind a load balancer, allowing the effective.
2. Do not: omitting Retry-After/X-RateLimit- headers, forcing clients to guess at backoff timing and often retry too.

Example:
```bash
curl -sS -D - <endpoint> -o /dev/null
```

Check: Do not: implementing rate.
