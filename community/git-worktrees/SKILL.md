---
name: git-worktrees
description: "Use when \"git worktree\", \"isolate this branch\", or \"do not dirty\". Not when commit message."
---

# Use a worktree

Put a long change on its own worktree.

1. git worktree add a new directory and branch.
2. Do the work there.
3. Leave the user's current checkout as it was.

Example:
```text
git worktree add ../app-feature feature/login
```

Check: Do not commit secrets. Do not rewrite published history.
