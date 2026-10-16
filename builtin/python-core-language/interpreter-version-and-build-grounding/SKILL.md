---
name: interpreter-version-and-build-grounding
description: "Use when \"interpreter version and build grounding\" is the work. assuming a walrus operator, tomllib, or except is available without checking the minimum supported version."
---

# Interpreter Version and Build Grounding

assuming a walrus operator, tomllib, or except is available without checking the minimum supported version.

1. Do not: assuming a walrus operator, tomllib, or except is available without checking the minimum supported.
2. Do not: conflating python and python3 on systems where they point to different installs.

Example:
```bash
python3 --version
```

Check: Do not: assuming a walrus operator, tomllib, or except is available without checking the minimum supported version.
