---
name: cryptographic-randomness-token-entropy
description: "Use when \"cryptographic randomness token entropy\" is the work. Use a cryptographic generator, not a simulation PRNG."
---

# Cryptographic Randomness & Token Entropy

Use a cryptographic generator, not a simulation PRNG.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import secrets
raw = secrets.token_bytes(32)
assert len(raw) == 32
```

Check: Do not edit the assert to match a surprising result.
