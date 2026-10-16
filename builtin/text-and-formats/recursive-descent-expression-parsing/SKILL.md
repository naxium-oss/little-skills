---
name: recursive-descent-expression-parsing
description: "Use when \"recursive descent expression parsing\" is the work. Encode precedence in grammar layers instead of relying on operator order in code."
---

# Recursive-Descent Expression Parsing

Encode precedence in grammar layers instead of relying on operator order in code.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def parse_sum(text):
parts = text.split("+")
if not parts or any(not p.strip().isdigit() for p in parts):
```

Check: Do not edit the assert to match a surprising result.
