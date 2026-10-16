---
name: build-reproducibility-and-hermetic-builds
description: "Use when \"build reproducibility and hermetic builds\" is the work. relying on a globally installed tool version (a system Python, a global npm package) that isnt declared anywhere."
---

# Build Reproducibility and Hermetic Builds

relying on a globally installed.

1. Do not: relying on a globally installed tool version (a system Python, a global npm package).
2. Do not: embedding build timestamps or unordered directory listings in build output, breaking bit-for-bit reproducibility verification.

Example:
```bash
read the lockfile format and the declared manager in the manifest
```

Check: Do not: relying on a globally installed tool version.
