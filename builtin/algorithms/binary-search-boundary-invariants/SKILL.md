---
name: binary-search-boundary-invariants
description: "Use when \"binary search boundary invariants\" is the work. Maintain that all positions below lo are too small and all positions at or beyond hi qualify."
---

# Binary Search & Boundary Invariants

Maintain that all positions below lo are too small and all positions at or beyond hi qualify.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def lower_bound(values, target):
lo, hi = 0, len(values)
while lo < hi:
```

Check: Do not edit the assert to match a surprising result.
