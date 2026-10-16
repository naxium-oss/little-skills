---
name: function-composition-pipelines
description: "Use when \"function composition pipelines\" is the work. Composition order must be explicit."
---

# Function Composition & Pipelines

Composition order must be explicit.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def compose(f, g):
return lambda value: f(g(value))
normalize = compose(str.lower, str.strip)
```

Check: Do not edit the assert to match a surprising result.
