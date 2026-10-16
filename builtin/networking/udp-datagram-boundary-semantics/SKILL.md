---
name: udp-datagram-boundary-semantics
description: "Use when \"udp datagram boundary semantics\" is the work. A UDP receive consumes a datagram rather than a stream fragment."
---

# UDP Datagram Boundary Semantics

A UDP receive consumes a datagram rather than a stream fragment.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as receiver:
receiver.bind(("127.0.0.1", 0)); receiver.settimeout(1)
```

Check: Do not edit the assert to match a surprising result.
