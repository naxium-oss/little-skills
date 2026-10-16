---
name: hmac-message-authentication
description: "Use when \"hmac message authentication\" is the work. Both parties need the same secret and byte-level message definition."
---

# HMAC Message Authentication

Both parties need the same secret and byte-level message definition.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import hmac, hashlib
key = b"fixture-key-not-for-production"
message = b"amount=10"
```

Check: Do not edit the assert to match a surprising result.
