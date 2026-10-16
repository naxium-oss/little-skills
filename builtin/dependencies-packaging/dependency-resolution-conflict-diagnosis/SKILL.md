---
name: dependency-resolution-conflict-diagnosis
description: "Use when \"dependency resolution conflict diagnosis\" is the work. Trace incompatible constraints to their sources and compare minimal supported resolution alternatives."
---

# Dependency Resolution Conflict Diagnosis

Trace incompatible constraints to their sources and compare minimal supported resolution alternatives.

1. Identify the package manager and exact resolver version.
2. Inspect manifests, lockfiles, dependency graphs, hashes, and platform markers.
3. Reproduce installation in an isolated target-matching environment.

Example:
```text
Identify the package manager and exact resolver version.
```

Check: Verify package contents, import behavior, signatures where supported, and offline reproducibility; generate an SBOM from actual artifacts.
