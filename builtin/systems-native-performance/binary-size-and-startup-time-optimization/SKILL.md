---
name: binary-size-and-startup-time-optimization
description: "Use when \"binary size and startup time optimization\" is the work. Measure section sizes and startup phases and verify that optimization preserves compatibility and behavior."
---

# Binary Size and Startup Time Optimization

Measure section sizes and startup phases and verify that optimization preserves compatibility and behavior.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
