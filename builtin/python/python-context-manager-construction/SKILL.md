---
name: python-context-manager-construction
description: "Use when \"python context manager construction\" is the work. Put release logic in finally."
---

# Python Context Manager Construction

Put release logic in finally.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from contextlib import contextmanager
@contextmanager
def tracked(events):
```

Check: Do not edit the assert to match a surprising result.
