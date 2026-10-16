---
name: tcp-byte-stream-message-framing
description: "Use when \"tcp byte stream message framing\" is the work. TCP preserves byte order, not message boundaries."
---

# TCP Byte-Stream Message Framing

TCP preserves byte order, not message boundaries.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import struct
def consume(buffer):
messages = []
```

Check: Do not edit the assert to match a surprising result.
