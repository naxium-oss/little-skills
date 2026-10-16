---
name: dns-record-types-resolution-paths
description: "Use when \"dns record types resolution paths\" is the work. getaddrinfo can consult local configuration and caches, not just DNS."
---

# DNS Record Types & Resolution Paths

getaddrinfo can consult local configuration and caches, not just DNS.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import socket
results = socket.getaddrinfo("localhost", 80, type=socket.SOCK_STREAM)
assert results
```

Check: Do not edit the assert to match a surprising result.
