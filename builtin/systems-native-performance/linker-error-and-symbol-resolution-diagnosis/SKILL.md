---
name: linker-error-and-symbol-resolution-diagnosis
description: "Use when \"linker error and symbol resolution diagnosis\" is the work. Inspect missing and duplicate symbols, link order, visibility, name mangling, and library architecture."
---

# Linker Error and Symbol Resolution Diagnosis

Inspect missing and duplicate symbols, link order, visibility, name mangling, and library architecture.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
