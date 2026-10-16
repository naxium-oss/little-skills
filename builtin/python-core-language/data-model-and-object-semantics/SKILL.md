---
name: data-model-and-object-semantics
description: "Use when \"data model and object semantics\" is the work. relying on integer/string interning across versions or implementations."
---

# Data Model and Object Semantics

relying on integer/string interning across versions or implementations.

1. Do not: relying on integer/string interning across versions or implementations.
2. Do not: using == when identity is intended for singletons like None.

Example:
```bash
python3 --version
python3 -c "import sys; print(sys.version_info, sys.implementation.name)"
```

Check: Do not: relying on integer/string interning across versions or implementations.
