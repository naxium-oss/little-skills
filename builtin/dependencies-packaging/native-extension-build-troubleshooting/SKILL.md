---
name: native-extension-build-troubleshooting
description: "Use when \"native extension build troubleshooting\" is the work. Compare ABI, compiler, headers, architecture, libc, and build logs before selecting a workaround."
---

# Native Extension Build Troubleshooting

Compare ABI, compiler, headers, architecture, libc, and build logs before selecting a workaround.

1. Identify the package manager and exact resolver version.
2. Inspect manifests, lockfiles, dependency graphs, hashes, and platform markers.
3. Reproduce installation in an isolated target-matching environment.

Example:
```text
Identify the package manager and exact resolver version.
```

Check: Verify package contents, import behavior, signatures where supported, and offline reproducibility; generate an SBOM from actual artifacts.
