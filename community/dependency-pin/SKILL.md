---
name: dependency-pin
description: "Use when \"add a dependency\", \"npm install\", or \"pip install\". Not when the package is already in the lockfile."
---

# Pin a dependency

Add a package only when the repo cannot do the job.

1. Search for an existing helper first.
2. Add the package with the repo's package manager.
3. Pin the version the lockfile writes. Do not float it.

Example:
```text
npm install zod. Commit package.json and the lockfile.
```

Check: Do not invent a version you did not install.
