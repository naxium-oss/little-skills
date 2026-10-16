---
name: revert-versus-reset-decision-making
description: "Use when \"revert versus reset decision making\" is the work. Prefer a history-preserving revert on shared branches; obtain authorization before destructive reset."
---

# Revert versus Reset Decision-Making

Prefer a history-preserving revert on shared branches; obtain authorization before destructive reset.

1. Inspect working tree, index, branch, remotes, and repository instructions.
2. Preserve uncommitted work and identify a recovery point.

Example:
```text
Inspect working tree, index, branch, remotes, and repository instructions.
```

Check: Check the staged diff, secret scans, test results, final history, and recovery instructions; never discard unrelated user work.
