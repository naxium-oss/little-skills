---
name: memory-ownership-and-allocator-boundary-auditing
description: "Use when \"memory ownership and allocator boundary auditing\" is the work. Define allocation and deallocation ownership across modules and enforce compatible allocator boundaries."
---

# Memory Ownership and Allocator Boundary Auditing

Define allocation and deallocation ownership across modules and enforce compatible allocator boundaries.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
