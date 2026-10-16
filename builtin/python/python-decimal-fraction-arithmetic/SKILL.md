---
name: python-decimal-fraction-arithmetic
description: "Use when \"python decimal fraction arithmetic\" is the work. Construct decimals from strings."
---

# Python Decimal & Fraction Arithmetic

Construct decimals from strings.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from decimal import Decimal, ROUND_HALF_EVEN
price = Decimal("2.675")
assert price.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN) == Decimal("2.68")
```

Check: Do not edit the assert to match a surprising result.
