---
name: utf-8-encoding-decode-error-policies
description: "Use when \"utf 8 encoding decode error policies\" is the work. Strict decoding rejects malformed input."
---

# UTF-8 Encoding & Decode Error Policies

Strict decoding rejects malformed input.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
raw = "café".encode("utf-8")
assert raw == b"caf\xc3\xa9"
assert raw.decode("utf-8") == "café"
```

Check: Do not edit the assert to match a surprising result.
