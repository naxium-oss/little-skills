---
name: regular-expression-groups-full-matches
description: "Use when \"regular expression groups full matches\" is the work. search locates a substring, while fullmatch constrains the entire string."
---

# Regular Expression Groups & Full Matches

search locates a substring, while fullmatch constrains the entire string.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import re
pattern = re.compile(r"(?P<kind>[A-Z]+)-(?P<number>[0-9]+)")
```

Check: Do not edit the assert to match a surprising result.
