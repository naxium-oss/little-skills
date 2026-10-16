---
name: python-decorators-callable-metadata
description: "Use when \"python decorators callable metadata\" is the work. Use functools.wraps and forward positional and keyword arguments."
---

# Python Decorators & Callable Metadata

Use functools.wraps and forward positional and keyword arguments.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from functools import wraps
def tagged(fn):
@wraps(fn)
```

Check: Do not edit the assert to match a surprising result.
