---
name: breadth-first-graph-traversal
description: "Use when \"breadth first graph traversal\" is the work. Mark vertices when enqueuing to avoid duplicate work."
---

# Breadth-First Graph Traversal

Mark vertices when enqueuing to avoid duplicate work.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from collections import deque
def distances(graph, start):
result, queue = {start: 0}, deque([start])
```

Check: Do not edit the assert to match a surprising result.
