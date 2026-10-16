---
name: timestamp-parsing-offset-preservation
description: "Use when \"timestamp parsing offset preservation\" is the work. A timestamp without an offset is not an unambiguous instant."
---

# Timestamp Parsing & Offset Preservation

A timestamp without an offset is not an unambiguous instant.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from datetime import datetime, timezone
value = datetime.fromisoformat("2024-01-01T01:00:00+01:00")
assert value.astimezone(timezone.utc).hour == 0
```

Check: Do not edit the assert to match a surprising result.
