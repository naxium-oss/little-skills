---
name: python-dataclasses-value-objects
description: "Use when \"python dataclasses value objects\" is the work. Frozen dataclasses prevent field reassignment, not mutation of referenced objects."
---

# Python Dataclasses & Value Objects

Frozen dataclasses prevent field reassignment, not mutation of referenced objects.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from dataclasses import dataclass
@dataclass(frozen=True)
class Point:
```

Check: Do not edit the assert to match a surprising result.
