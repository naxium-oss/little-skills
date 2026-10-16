---
name: unicode-normalization-canonical-equality
description: "Use when \"unicode normalization canonical equality\" is the work. NFC combines canonical equivalents, while compatibility normalization can erase distinctions."
---

# Unicode Normalization & Canonical Equality

NFC combines canonical equivalents, while compatibility normalization can erase distinctions.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import unicodedata
a, b = "é", "e\u0301"
assert a != b
```

Check: Do not edit the assert to match a surprising result.
