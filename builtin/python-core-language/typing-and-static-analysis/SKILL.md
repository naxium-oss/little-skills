---
name: typing-and-static-analysis
description: "Use when \"typing and static analysis\" is the work. trusting hints as runtime guarantees."
---

# Typing and Static Analysis

trusting hints as runtime guarantees.

1. Do not: trusting hints as runtime guarantees.
2. Do not: using new typing constructs unsupported by the pinned checker version, causing CI-only failures.

Example:
```bash
python3 --version
python3 -c "import sys; print(sys.version_info, sys.implementation.name)"
```

Check: Do not: trusting hints as runtime guarantees.
