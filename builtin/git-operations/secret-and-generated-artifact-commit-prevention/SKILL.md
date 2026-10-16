---
name: secret-and-generated-artifact-commit-prevention
description: "Use when \"secret and generated artifact commit prevention\" is the work. Inspect staged content and generated artifacts; remove exposed secrets and follow rotation procedures."
---

# Secret and Generated-Artifact Commit Prevention

Inspect staged content and generated artifacts; remove exposed secrets and follow rotation procedures.

1. Inspect working tree, index, branch, remotes, and repository instructions.
2. Preserve uncommitted work and identify a recovery point.

Example:
```text
Inspect working tree, index, branch, remotes, and repository instructions.
```

Check: Check the staged diff, secret scans, test results, final history, and recovery instructions; never discard unrelated user work.
