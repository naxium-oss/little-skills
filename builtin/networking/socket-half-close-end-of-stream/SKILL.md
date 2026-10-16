---
name: socket-half-close-end-of-stream
description: "Use when \"socket half close end of stream\" is the work. For a stream socket, recv returning empty bytes means peer shutdown of its sending direction."
---

# Socket Half-Close & End-of-Stream

For a stream socket, recv returning empty bytes means peer shutdown of its sending direction.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import socket
a, b = socket.socketpair()
try:
```

Check: Do not edit the assert to match a surprising result.
