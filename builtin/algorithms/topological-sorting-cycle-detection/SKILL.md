---
name: topological-sorting-cycle-detection
description: "Use when \"topological sorting cycle detection\" is the work. Kahn’s algorithm removes zero-indegree vertices."
---

# Topological Sorting & Cycle Detection

Kahn’s algorithm removes zero-indegree vertices.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from collections import deque
def topo(graph):
degree = {node: 0 for node in graph}
```

Check: Do not edit the assert to match a surprising result.
