---
name: atomic-commit-construction
description: "Use when \"atomic commit construction\" is the work. Stage one coherent behavior change and inspect the exact staged diff before committing."
---

# Atomic Commit Construction

Stage one coherent behavior change and inspect the exact staged diff before committing.

1. Inspect working tree, index, branch, remotes, and repository instructions.
2. Preserve uncommitted work and identify a recovery point.
3. Preview the intended diff before any history-changing action.

Example:
```text
Inspect working tree, index, branch, remotes, and repository instructions.
```

Check: Check the staged diff, secret scans, test results, final history, and recovery instructions; never discard unrelated user work.
