---
name: dataclasses-and-structured-records
description: "Use when \"dataclasses and structured records\" is the work. using a mutable default like [] directly in a field instead of default_factory."
---

# Dataclasses and Structured Records

using a mutable default like [] directly in a field instead of default_factory.

1. Do not: using a mutable default like [] directly in a field instead of default_factory.
2. Do not: assuming dataclasses are as fast as __slots__-only classes without verifying with a profiler.

Example:
```bash
python3 -c "import importlib.metadata as m; print(m.version('pip'))"
python3 -m pip --version
```

Check: Do not: using a mutable default like [] directly in a field instead of default_factory.
