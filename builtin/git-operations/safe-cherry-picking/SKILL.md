---
name: safe-cherry-picking
description: "Use when \"safe cherry picking\" is the work. Check prerequisites and duplicate changes, preserve attribution, and validate the resulting behavior."
---

# Safe Cherry-Picking

Check prerequisites and duplicate changes, preserve attribution, and validate the resulting behavior.

1. Inspect working tree, index, branch, remotes, and repository instructions.
2. Preserve uncommitted work and identify a recovery point.
3. Preview the intended diff before any history-changing action.

Example:
```text
Inspect working tree, index, branch, remotes, and repository instructions.
```

Check: Check the staged diff, secret scans, test results, final history, and recovery instructions; never discard unrelated user work.
