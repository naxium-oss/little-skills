---
name: cryptographic-hashes-content-digests
description: "Use when \"cryptographic hashes content digests\" is the work. An unkeyed hash detects changes relative to a trusted digest but cannot prove who supplied the bytes."
---

# Cryptographic Hashes & Content Digests

An unkeyed hash detects changes relative to a trusted digest but cannot prove who supplied the bytes.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import hashlib
digest = hashlib.sha256(b"hello").hexdigest()
assert digest == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
```

Check: Do not edit the assert to match a surprising result.
