---
name: repository-state-and-version-grounding
description: "Use when \"repository state and version grounding\" is the work. running git reset --hard without checking git status first, silently discarding uncommitted work."
---

# Repository State and Version Grounding

running git reset --hard without checking git status first, silently discarding uncommitted work.

1. Do not: running git reset --hard without checking git status first, silently discarding uncommitted work.
2. Do not: assuming the checked-out branch matches expectations without git branch --show-current.

Example:
```bash
git rev-parse HEAD
git status --short --branch
```

Check: Do not: running git reset --hard without checking git status first, silently discarding uncommitted work.
