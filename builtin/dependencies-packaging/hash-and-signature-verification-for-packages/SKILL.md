---
name: hash-and-signature-verification-for-packages
description: "Use when \"hash and signature verification for packages\" is the work. Verify hashes against trusted metadata and signatures against an independently established trust root."
---

# Hash and Signature Verification for Packages

Verify hashes against trusted metadata and signatures against an independently established trust root.

1. Identify the package manager and exact resolver version.
2. Inspect manifests, lockfiles, dependency graphs, hashes, and platform markers.
3. Reproduce installation in an isolated target-matching environment.

Example:
```text
Identify the package manager and exact resolver version.
```

Check: Verify package contents, import behavior, signatures where supported, and offline reproducibility; generate an SBOM from actual artifacts.
