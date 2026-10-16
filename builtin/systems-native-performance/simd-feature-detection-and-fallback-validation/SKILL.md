---
name: simd-feature-detection-and-fallback-validation
description: "Use when \"simd feature detection and fallback validation\" is the work. Detect CPU support at runtime and test safe dispatch to a verified scalar fallback."
---

# SIMD Feature Detection and Fallback Validation

Detect CPU support at runtime and test safe dispatch to a verified scalar fallback.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
