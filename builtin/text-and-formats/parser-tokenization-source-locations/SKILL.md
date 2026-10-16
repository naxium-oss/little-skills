---
name: parser-tokenization-source-locations
description: "Use when \"parser tokenization source locations\" is the work. Require every input character to be consumed or explicitly skipped."
---

# Parser Tokenization & Source Locations

Require every input character to be consumed or explicitly skipped.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import re
def tokenize(text):
pattern = re.compile(r"\s+|[0-9]+|[+()]")
```

Check: Do not edit the assert to match a surprising result.
