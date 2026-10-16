---
name: python-imports-package-boundaries
description: "Use when \"python imports package boundaries\" is the work. Keep command-line execution behind a main guard."
---

# Python Imports & Package Boundaries

Keep command-line execution behind a main guard.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def double(value):
return value * 2
from .math_ops import double
```

Check: Do not edit the assert to match a surprising result.
