---
name: monorepo-workspace-dependency-management
description: "Use when \"monorepo workspace dependency management\" is the work. Validate workspace ranges, hoisting assumptions, package boundaries, and isolated consumer installation."
---

# Monorepo Workspace Dependency Management

Validate workspace ranges, hoisting assumptions, package boundaries, and isolated consumer installation.

1. Identify the package manager and exact resolver version.
2. Inspect manifests, lockfiles, dependency graphs, hashes, and platform markers.
3. Reproduce installation in an isolated target-matching environment.

Example:
```text
Identify the package manager and exact resolver version.
```

Check: Verify package contents, import behavior, signatures where supported, and offline reproducibility; generate an SBOM from actual artifacts.
