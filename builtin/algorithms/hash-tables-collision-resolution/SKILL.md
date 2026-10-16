---
name: hash-tables-collision-resolution
description: "Use when \"hash tables collision resolution\" is the work. Equal keys must hash consistently; collisions do not imply equality."
---

# Hash Tables & Collision Resolution

Equal keys must hash consistently; collisions do not imply equality.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
buckets = [[] for _ in range(4)]
def put(key, value):
bucket = buckets[hash(key) % len(buckets)]
```

Check: Do not edit the assert to match a surprising result.
