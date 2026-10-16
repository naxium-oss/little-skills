---
name: pure-functions-referential-transparency
description: "Use when \"pure functions referential transparency\" is the work. A pure function returns the same result for the same inputs and has no externally visible effects."
---

# Pure Functions & Referential Transparency

A pure function returns the same result for the same inputs and has no externally visible effects.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def subtotal(prices):
return sum(prices)
values = [10, 20]
```

Check: Do not edit the assert to match a surprising result.
