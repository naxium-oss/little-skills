---
name: context-managers-and-resource-safety
description: "Use when \"context managers and resource safety\" is the work. forgetting that __exit__ returning True silently suppresses exceptions."
---

# Context Managers and Resource Safety

forgetting that __exit__ returning True silently suppresses exceptions.

1. Do not: forgetting that __exit__ returning True silently suppresses exceptions.
2. Do not: opening files without with and leaking file descriptors under error paths.

Example:
```bash
python3 --version
python3 -c "import sys; print(sys.version_info, sys.implementation.name)"
```

Check: Do not: forgetting that __exit__ returning True silently suppresses exceptions.
