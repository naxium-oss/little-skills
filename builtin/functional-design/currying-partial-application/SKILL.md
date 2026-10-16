---
name: currying-partial-application
description: "Use when \"currying partial application\" is the work. Currying transforms a multi-argument function into nested unary functions."
---

# Currying & Partial Application

Currying transforms a multi-argument function into nested unary functions.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from functools import partial
def multiply(a, b): return a * b
double = partial(multiply, 2)
```

Check: Do not edit the assert to match a surprising result.
