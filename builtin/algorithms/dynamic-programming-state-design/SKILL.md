---
name: dynamic-programming-state-design
description: "Use when \"dynamic programming state design\" is the work. Define exactly what each table cell means before writing transitions."
---

# Dynamic Programming State Design

Define exactly what each table cell means before writing transitions.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def minimum_coins(coins, target):
best = [0] + [float("inf")] * target
for amount in range(1, target + 1):
```

Check: Do not edit the assert to match a surprising result.
