---
name: nonce-initialization-vector-requirements
description: "Use when \"nonce initialization vector requirements\" is the work. Nonce and IV rules depend on the algorithm and mode."
---

# Nonce & Initialization Vector Requirements

Nonce and IV rules depend on the algorithm and mode.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
seen = set()
def reserve(nonce):
if nonce in seen: raise ValueError("nonce reused")
```

Check: Do not edit the assert to match a surprising result.
