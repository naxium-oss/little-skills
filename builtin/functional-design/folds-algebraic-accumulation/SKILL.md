---
name: folds-algebraic-accumulation
description: "Use when \"folds algebraic accumulation\" is the work. State the accumulator invariant."
---

# Folds & Algebraic Accumulation

State the accumulator invariant.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from functools import reduce
assert reduce(lambda total, x: total + x, [1, 2, 3], 0) == 6
assert reduce(lambda total, x: total + x, [], 0) == 0
```

Check: Do not edit the assert to match a surprising result.
