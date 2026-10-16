---
name: rebase-conflict-resolution
description: "Use when \"rebase conflict resolution\" is the work. Preserve intended commit boundaries and inspect each replayed patch for changed assumptions."
---

# Rebase Conflict Resolution

Preserve intended commit boundaries and inspect each replayed patch for changed assumptions.

1. Inspect working tree, index, branch, remotes, and repository instructions.
2. Preserve uncommitted work and identify a recovery point.
3. Preview the intended diff before any history-changing action.

Example:
```text
Inspect working tree, index, branch, remotes, and repository instructions.
```

Check: Check the staged diff, secret scans, test results, final history, and recovery instructions; never discard unrelated user work.
