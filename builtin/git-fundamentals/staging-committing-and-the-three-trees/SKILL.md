---
name: staging-committing-and-the-three-trees
description: "Use when \"staging committing and the three trees\" is the work. using git add ."
---

# Staging, Committing, and the Three Trees

using git add .

1. Do not: using git add . blindly and committing unintended files (build artifacts, secrets).
2. Do not: confusing git restore (working tree) with git restore --staged (index) targets.

Example:
```bash
git rev-parse HEAD
git status --short --branch
```

Check: Do not: using git add .
