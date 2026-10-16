---
name: constant-time-secret-comparison
description: "Use when \"constant time secret comparison\" is the work. Use a vetted constant-time comparison primitive for compatible byte sequences."
---

# Constant-Time Secret Comparison

Use a vetted constant-time comparison primitive for compatible byte sequences.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import hmac
expected = b"0123456789abcdef"
assert hmac.compare_digest(expected, b"0123456789abcdef")
```

Check: Do not edit the assert to match a surprising result.
