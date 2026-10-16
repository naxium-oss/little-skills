---
name: hermetic-dependency-installation
description: "Use when \"hermetic dependency installation\" is the work. Use immutable locks and verified artifacts while controlling registries, caches, and install scripts."
---

# Hermetic Dependency Installation

Use immutable locks and verified artifacts while controlling registries, caches, and install scripts.

1. Identify the package manager and exact resolver version.
2. Inspect manifests, lockfiles, dependency graphs, hashes, and platform markers.
3. Reproduce installation in an isolated target-matching environment.

Example:
```text
Identify the package manager and exact resolver version.
```

Check: Verify package contents, import behavior, signatures where supported, and offline reproducibility; generate an SBOM from actual artifacts.
