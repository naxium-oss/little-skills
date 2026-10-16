---
name: code-review
description: "Use when \"review the diff\", \"code review\", or \"before merge\". Not when review this design."
---

# Review the diff

Will this do what it claims, without breaking the rest?

1. Read the diff next to the claim.
2. Hunt correctness, then regressions, then the new error paths.
3. Each finding names a location, the problem, and the fix.

Example:
```text
catch on line 42 swallows ENOENT. Rethrow it.
```

Check: Verify a finding before you change code for it.
