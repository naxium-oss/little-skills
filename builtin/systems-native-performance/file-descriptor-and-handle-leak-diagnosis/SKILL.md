---
name: file-descriptor-and-handle-leak-diagnosis
description: "Use when \"file descriptor and handle leak diagnosis\" is the work. Stress repeated operations and inspect open handles before and after failure and cancellation paths."
---

# File Descriptor and Handle Leak Diagnosis

Stress repeated operations and inspect open handles before and after failure and cancellation paths.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
