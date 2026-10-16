---
name: digital-signature-verification-contracts
description: "Use when \"digital signature verification contracts\" is the work. A valid signature proves possession of the signing key for the supplied message, not that the key belongs."
---

# Digital Signature Verification Contracts

A valid signature proves possession of the signing key for the supplied message, not that the key belongs to the claimed person.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
cases = [("original", "trusted-key", True),
```

Check: Do not edit the assert to match a surprising result.
