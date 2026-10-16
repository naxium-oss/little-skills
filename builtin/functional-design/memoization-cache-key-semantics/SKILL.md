---
name: memoization-cache-key-semantics
description: "Use when \"memoization cache key semantics\" is the work. A cache key must include every input affecting the result."
---

# Memoization & Cache Key Semantics

A cache key must include every input affecting the result.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from functools import lru_cache
@lru_cache(maxsize=128)
def fib(n):
```

Check: Do not edit the assert to match a surprising result.
