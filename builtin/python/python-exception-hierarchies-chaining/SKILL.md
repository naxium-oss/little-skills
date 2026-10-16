---
name: python-exception-hierarchies-chaining
description: "Use when \"python exception hierarchies chaining\" is the work. Catch the narrowest meaningful exception and chain translated failures with from."
---

# Python Exception Hierarchies & Chaining

Catch the narrowest meaningful exception and chain translated failures with from.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
class InvalidQuantity(ValueError):
pass
def quantity(text):
```

Check: Do not edit the assert to match a surprising result.
