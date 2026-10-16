---
name: framework-and-plugin-compatibility-verification
description: "Use when \"framework and plugin compatibility verification\" is the work. Intersect every framework and plugin peer constraint and verify the resulting combination with a clean build."
---

# Framework and Plugin Compatibility Verification

Intersect every framework and plugin peer constraint and verify the resulting combination with a clean build.

1. Identify the actual executable or service endpoint used by the failing process.
2. Compare shell resolution with the application process.
3. Collect a machine-readable environment manifest.

Example:
```text
Identify the actual executable or service endpoint used by the failing process.
```

Check: Repeat the check in a clean shell and the real execution context; explain every mismatch.
