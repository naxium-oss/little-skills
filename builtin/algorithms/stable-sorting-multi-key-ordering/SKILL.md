---
name: stable-sorting-multi-key-ordering
description: "Use when \"stable sorting multi key ordering\" is the work. A stable sort retains input order for equal keys."
---

# Stable Sorting & Multi-Key Ordering

A stable sort retains input order for equal keys.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
rows = [("Ada", 2), ("Grace", 1), ("Lin", 2)]
result = sorted(rows, key=lambda row: row[1])
```

Check: Do not edit the assert to match a surprising result.
