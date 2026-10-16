---
name: commit-from-diff
description: "Use when \"commit message\", \"git commit\", or \"make a commit\". Not when commit hash or which commit."
---

# Commit from the diff

The message says why, and it matches the diff.

1. Read git status and git diff.
2. Stage only the files for this change.
3. Write one message about why, then commit.

Example:
```text
git diff shows the null guard. Message: fix empty cart total.
```

Check: Do not commit secrets, lockfile noise, or files you did not mean.
