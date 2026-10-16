---
name: key-derivation-domain-separation
description: "Use when \"key derivation domain separation\" is the work. Use a standardized KDF with distinct context labels for distinct purposes."
---

# Key Derivation & Domain Separation

Use a standardized KDF with distinct context labels for distinct purposes.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
labels = {"encryption": b"app:v1:encryption", "authentication": b"app:v1:authentication"}
assert len(set(labels.values())) == 2
```

Check: Do not edit the assert to match a surprising result.
