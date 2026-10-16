---
name: filesystem-atomicity-and-crash-consistency-testing
description: "Use when \"filesystem atomicity and crash consistency testing\" is the work. Test crash windows around write, fsync, rename, and directory persistence on the actual filesystem."
---

# Filesystem Atomicity and Crash Consistency Testing

Test crash windows around write, fsync, rename, and directory persistence on the actual filesystem.

1. Capture compiler, linker, target triple, ABI, libc, and build flags.
2. Inspect symbols and ownership boundaries.

Example:
```text
Capture compiler, linker, target triple, ABI, libc, and build flags.
```

Check: Test unsupported CPU features, sanitizer blind spots, crashes, handle leaks, partial writes, and binary compatibility across supported targets.
