---
name: network-byte-order-port-fields
description: "Use when \"network byte order port fields\" is the work. Network byte order is big-endian for common internet protocol integer fields."
---

# Network Byte Order & Port Fields

Network byte order is big-endian for common internet protocol integer fields.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import struct
port = 443
raw = struct.pack("!H", port)
```

Check: Do not edit the assert to match a surprising result.
