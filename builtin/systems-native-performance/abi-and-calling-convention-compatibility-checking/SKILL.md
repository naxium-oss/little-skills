---
name: abi-and-calling-convention-compatibility-checking
description: "Use when \"abi and calling convention compatibility checking\" is the work. Match binary format, data layout, symbol naming, calling convention, and runtime library boundaries."
---

# ABI and Calling Convention Compatibility Checking

Match binary format, data layout, symbol naming, calling convention, and runtime library boundaries.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
