---
name: authenticated-encryption-associated-data
description: "Use when \"authenticated encryption associated data\" is the work. AEAD authenticates ciphertext and associated data."
---

# Authenticated Encryption & Associated Data

AEAD authenticates ciphertext and associated data.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
record = {"nonce": b"fixture", "ciphertext": b"opaque", "aad": b"tenant:7"}
assert record["aad"] == b"tenant:7"
```

Check: Do not edit the assert to match a surprising result.
