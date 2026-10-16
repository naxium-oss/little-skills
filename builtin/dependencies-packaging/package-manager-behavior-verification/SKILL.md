---
name: package-manager-behavior-verification
description: "Use when \"package manager behavior verification\" is the work. Pin manager versions and verify install, update, script execution, and lockfile semantics."
---

# Package Manager Behavior Verification

Pin manager versions and verify install, update, script execution, and lockfile semantics.

1. Identify the package manager and exact resolver version.
2. Inspect manifests, lockfiles, dependency graphs, hashes, and platform markers.
3. Reproduce installation in an isolated target-matching environment.

Example:
```text
Identify the package manager and exact resolver version.
```

Check: Verify package contents, import behavior, signatures where supported, and offline reproducibility; generate an SBOM from actual artifacts.
