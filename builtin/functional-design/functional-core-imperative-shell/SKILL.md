---
name: functional-core-imperative-shell
description: "Use when \"functional core imperative shell\" is the work. Compute an explicit action plan from supplied state, then let a shell execute it."
---

# Functional Core & Imperative Shell

Compute an explicit action plan from supplied state, then let a shell execute it.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def plan_restock(stock, threshold):
return [(sku, threshold - count) for sku, count in sorted(stock.items()) if count < threshold]
```

Check: Do not edit the assert to match a surprising result.
