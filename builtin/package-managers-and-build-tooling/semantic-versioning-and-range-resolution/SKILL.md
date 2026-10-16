---
name: semantic-versioning-and-range-resolution
description: "Use when \"semantic versioning and range resolution\" is the work."
---

# Semantic Versioning and Range Resolution

assuming ^1.3.0 guarantees safety.

1. Do not: assuming ^1.3.0 guarantees safety from breaking changes, when the maintainer violates semver (common in.
2. Do not: never checking npm outdated/npm ls, missing that a wide-open range has silently pulled in.

Example:
```bash
read the lockfile format and the declared manager in the manifest
```

Check: Do not: assuming ^1.3.0.
