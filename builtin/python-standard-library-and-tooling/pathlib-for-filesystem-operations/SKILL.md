---
name: pathlib-for-filesystem-operations
description: "Use when \"pathlib for filesystem operations\" is the work. mixing os.path.join string outputs with Path objects inconsistently."
---

# pathlib for Filesystem Operations

mixing os.path.join string outputs with Path objects inconsistently.

1. Do not: mixing os.path.join string outputs with Path objects inconsistently.
2. Do not: assuming Path.resolve() behaves identically across OSes for symlink cycles.

Example:
```bash
python3 -c "import importlib.metadata as m; print(m.version('pip'))"
python3 -m pip --version
```

Check: Do not: mixing os.path.join string outputs with Path objects inconsistently.
