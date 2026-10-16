---
name: software-bill-of-materials-generation
description: "Use when \"software bill of materials generation\" is the work. Generate the bill of materials from the resolved and shipped artifacts, including transitive components."
---

# Software Bill of Materials Generation

Generate the bill of materials from the resolved and shipped artifacts, including transitive components.

1. Identify the package manager and exact resolver version.
2. Inspect manifests, lockfiles, dependency graphs, hashes, and platform markers.
3. Reproduce installation in an isolated target-matching environment.

Example:
```text
Identify the package manager and exact resolver version.
```

Check: Verify package contents, import behavior, signatures where supported, and offline reproducibility; generate an SBOM from actual artifacts.
