---
name: binary-struct-packing-endianness
description: "Use when \"binary struct packing endianness\" is the work. Specify byte order and field widths."
---

# Binary Struct Packing & Endianness

Specify byte order and field widths.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import struct
raw = struct.pack(">HI", 7, 1024)
assert len(raw) == 6
```

Check: Do not edit the assert to match a surprising result.
