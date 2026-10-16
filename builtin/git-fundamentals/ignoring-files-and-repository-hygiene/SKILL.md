---
name: ignoring-files-and-repository-hygiene
description: "Use when \"ignoring files and repository hygiene\" is the work. adding a pattern to .gitignore and assuming already-tracked files are retroactively ignored."
---

# Ignoring Files and Repository Hygiene

adding a pattern to .gitignore and assuming already-tracked files are retroactively ignored.

1. Do not: adding a pattern to .gitignore and assuming already-tracked files are retroactively ignored.
2. Do not: committing secrets and only fixing .gitignore without purging history or rotating the leaked credential.

Example:
```bash
git rev-parse HEAD
git status --short --branch
```

Check: Do not: adding a pattern to .gitignore and assuming already-tracked files are retroactively ignored.
