---
name: merkle-trees-inclusion-proofs
description: "Use when \"merkle trees inclusion proofs\" is the work. Use domain separation for leaf and internal-node hashing and define odd-leaf handling."
---

# Merkle Trees & Inclusion Proofs

Use domain separation for leaf and internal-node hashing and define odd-leaf handling.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import hashlib
def leaf(data): return hashlib.sha256(b"\x00" + data).digest()
```

Check: Do not edit the assert to match a surprising result.
