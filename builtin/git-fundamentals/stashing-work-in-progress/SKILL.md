---
name: stashing-work-in-progress
description: "Use when \"stashing work in progress\" is the work. forgetting --include-untracked and losing new files from a stash."
---

# Stashing Work in Progress

forgetting --include-untracked and losing new files from a stash.

1. Do not: forgetting --include-untracked and losing new files from a stash.
2. Do not: letting stashes accumulate indefinitely, becoming an untracked second history nobody reviews.

Example:
```bash
git rev-parse HEAD
git status --short --branch
```

Check: Do not: forgetting --include-untracked and losing new files from a stash.
