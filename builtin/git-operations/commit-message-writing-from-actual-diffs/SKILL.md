---
name: commit-message-writing-from-actual-diffs
description: "Use when \"commit message writing from actual diffs\" is the work. Describe actual behavior and rationale from the diff; do not claim unexecuted verification."
---

# Commit Message Writing from Actual Diffs

Describe actual behavior and rationale from the diff; do not claim unexecuted verification.

1. Inspect working tree, index, branch, remotes, and repository instructions.
2. Preserve uncommitted work and identify a recovery point.

Example:
```text
Inspect working tree, index, branch, remotes, and repository instructions.
```

Check: Check the staged diff, secret scans, test results, final history, and recovery instructions; never discard unrelated user work.
