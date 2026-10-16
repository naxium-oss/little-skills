---
name: base64-hex-encoding-boundaries
description: "Use when \"base64 hex encoding boundaries\" is the work. Base64 and hex are reversible encodings, not encryption."
---

# Base64 & Hex Encoding Boundaries

Base64 and hex are reversible encodings, not encryption.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import base64
raw = b"\x00\xff"
encoded = base64.b64encode(raw)
```

Check: Do not edit the assert to match a surprising result.
