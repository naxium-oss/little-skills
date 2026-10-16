---
name: python-collections-comprehensions
description: "Use when \"python collections comprehensions\" is the work. Preserve ordering deliberately and separate deduplication from sorting."
---

# Python Collections & Comprehensions

Preserve ordering deliberately and separate deduplication from sorting.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
pairs = [("a", 1), ("b", 2)]
lookup = {key: value for key, value in pairs}
assert lookup["b"] == 2
```

Check: Do not edit the assert to match a surprising result.
