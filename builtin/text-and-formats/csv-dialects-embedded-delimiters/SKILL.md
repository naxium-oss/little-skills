---
name: csv-dialects-embedded-delimiters
description: "Use when \"csv dialects embedded delimiters\" is the work. CSV is not equivalent to splitting on commas."
---

# CSV Dialects & Embedded Delimiters

CSV is not equivalent to splitting on commas.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import csv, io
rows = list(csv.reader(io.StringIO('name,note\nAda,"hello, world"\n')))
assert rows[1] == ["Ada", "hello, world"]
```

Check: Do not edit the assert to match a surprising result.
