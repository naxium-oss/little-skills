---
name: offline-and-air-gapped-build-preparation
description: "Use when \"offline and air gapped build preparation\" is the work. Mirror all required artifacts and metadata, then prove the build succeeds without network access."
---

# Offline and Air-Gapped Build Preparation

Mirror all required artifacts and metadata, then prove the build succeeds without network access.

1. Identify the package manager and exact resolver version.
2. Inspect manifests, lockfiles, dependency graphs, hashes, and platform markers.
3. Reproduce installation in an isolated target-matching environment.

Example:
```text
Identify the package manager and exact resolver version.
```

Check: Verify package contents, import behavior, signatures where supported, and offline reproducibility; generate an SBOM from actual artifacts.
