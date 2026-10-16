---
name: line-endings-byte-order-marks
description: "Use when \"line endings byte order marks\" is the work. BOM handling depends on encoding and protocol."
---

# Line Endings & Byte Order Marks

BOM handling depends on encoding and protocol.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
raw = b"\xef\xbb\xbfhello\r\nworld\r\n"
text = raw.decode("utf-8-sig")
assert text.splitlines() == ["hello", "world"]
```

Check: Do not edit the assert to match a surprising result.
