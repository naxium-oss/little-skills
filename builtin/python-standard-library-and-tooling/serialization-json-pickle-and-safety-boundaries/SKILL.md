---
name: serialization-json-pickle-and-safety-boundaries
description: "Use when \"serialization json pickle and safety boundaries\" is the work. using pickle for API payloads or cache values that cross a trust boundary."
---

# Serialization: json, pickle, and Safety Boundaries

using pickle for API payloads or cache values that cross a trust boundary.

1. Do not: using pickle for API payloads or cache values that cross a trust boundary.
2. Do not: assuming json.dumps handles datetime or Decimal without a custom encoder.

Example:
```bash
python3 -c "import importlib.metadata as m; print(m.version('pip'))"
```

Check: Do not: using pickle for API payloads or cache values that cross a trust boundary.
