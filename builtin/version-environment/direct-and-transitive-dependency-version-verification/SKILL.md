---
name: direct-and-transitive-dependency-version-verification
description: "Use when \"direct and transitive dependency version verification\" is the work. Traverse direct and transitive nodes, retaining duplicate versions and platform-specific optional dependencies."
---

# Direct and Transitive Dependency Version Verification

Traverse direct and transitive nodes, retaining duplicate versions and platform-specific optional dependencies.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
