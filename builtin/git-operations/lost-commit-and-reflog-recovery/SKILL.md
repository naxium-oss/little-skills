---
name: lost-commit-and-reflog-recovery
description: "Use when \"lost commit and reflog recovery\" is the work. Locate candidate commits in reflogs and preserve them on a recovery branch before cleanup."
---

# Lost Commit and Reflog Recovery

Locate candidate commits in reflogs and preserve them on a recovery branch before cleanup.

1. Inspect working tree, index, branch, remotes, and repository instructions.
2. Preserve uncommitted work and identify a recovery point.
3. Preview the intended diff before any history-changing action.

Example:
```text
Inspect working tree, index, branch, remotes, and repository instructions.
```

Check: Check the staged diff, secret scans, test results, final history, and recovery instructions; never discard unrelated user work.
