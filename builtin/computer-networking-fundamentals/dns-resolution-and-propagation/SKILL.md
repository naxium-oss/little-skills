---
name: dns-resolution-and-propagation
description: "Use when \"dns resolution and propagation\" is the work. assuming a DNS record change is instantly visible everywhere, ignoring TTL-based caching delays."
---

# DNS Resolution and Propagation

assuming a DNS record change is instantly visible everywhere, ignoring TTL-based caching delays.

1. Do not: assuming a DNS record change is instantly visible everywhere, ignoring TTL-based caching delays.
2. Do not: testing only against a local machine's resolver cache instead of querying an authoritative nameserver.

Example:
```bash
resolve the name and confirm the address actually used
capture the exchange before theorizing
```

Check: Do not: assuming a DNS record change is instantly visible everywhere, ignoring TTL-based caching delays.
