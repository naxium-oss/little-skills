---
name: python-descriptors-attribute-lookup
description: "Use when \"python descriptors attribute lookup\" is the work. Data descriptors take precedence over instance dictionaries."
---

# Python Descriptors & Attribute Lookup

Data descriptors take precedence over instance dictionaries.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
class Celsius:
def __init__(self, value):
self.value = value
```

Check: Do not edit the assert to match a surprising result.
