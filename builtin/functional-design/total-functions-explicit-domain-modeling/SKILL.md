---
name: total-functions-explicit-domain-modeling
description: "Use when \"total functions explicit domain modeling\" is the work. A total contract handles every admitted input and terminates."
---

# Total Functions & Explicit Domain Modeling

A total contract handles every admitted input and terminates.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def safe_head(values):
return (True, values[0]) if values else (False, None)
assert safe_head([0]) == (True, 0)
```

Check: Do not edit the assert to match a surprising result.
