---
name: python-function-arguments-defaults
description: "Use when \"python function arguments defaults\" is the work. Defaults are evaluated when the function is defined."
---

# Python Function Arguments & Defaults

Defaults are evaluated when the function is defined.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def append_item(value, items=None):
result = [] if items is None else list(items)
result.append(value)
```

Check: Do not edit the assert to match a surprising result.
