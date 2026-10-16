---
name: persistent-data-structural-sharing
description: "Use when \"persistent data structural sharing\" is the work. Structural sharing requires shared nodes to remain immutable."
---

# Persistent Data & Structural Sharing

Structural sharing requires shared nodes to remain immutable.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from dataclasses import dataclass
@dataclass(frozen=True)
class Node:
```

Check: Do not edit the assert to match a surprising result.
