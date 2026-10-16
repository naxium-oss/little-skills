---
name: lockfile-semantics-across-package-managers
description: "Use when \"lockfile semantics across package managers\" is the work. committing both package-lock.json and yarn.lock after switching tools, causing confusion about which is authoritative."
---

# Lockfile Semantics Across Package Managers

committing both package-lock.json and yarn.lock after switching.

1. Do not: committing both package-lock.json and yarn.lock after switching tools, causing confusion about which is authoritative.
2. Do not: using npm install in CI instead of npm ci, allowing dependency drift between local.

Example:
```bash
read the lockfile format and the declared manager in the manifest
```

Check: Do not: committing both.
