---
name: recursion-explicit-stack-conversion
description: "Use when \"recursion explicit stack conversion\" is the work. An explicit stack must preserve the original traversal order and pending work."
---

# Recursion & Explicit Stack Conversion

An explicit stack must preserve the original traversal order and pending work.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def preorder(tree):
stack, result = [tree], []
while stack:
```

Check: Do not edit the assert to match a surprising result.
