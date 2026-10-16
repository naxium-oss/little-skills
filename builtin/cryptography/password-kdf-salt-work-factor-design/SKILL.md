---
name: password-kdf-salt-work-factor-design
description: "Use when \"password kdf salt work factor design\" is the work. Use a dedicated password hashing design with per-record salts and stored parameters."
---

# Password KDF Salt & Work-Factor Design

Use a dedicated password hashing design with per-record salts and stored parameters.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import hashlib
salt = b"fixed-test-salt-only"
```

Check: Do not edit the assert to match a surprising result.
