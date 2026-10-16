---
name: debug-zig
description: "Use when \"zig Index out of bounds panic\", \"Index out of bounds panic\". Not when explaining working zig code."
---

# Debug zig

Reproduce the zig failure with the project command, then change one thing.

1. Index out of bounds panic: The safety check names the slice and index; check loop bounds.
2. Memory leaks: Zig has no GC, every allocator call needs matching free/deinit; use `std.testing.allocator` in tests.
3. comptime errors: The compiler explains the comptime value; make the branch comptime-known or restructure to runtime.

Example:
```text
zig build test
```

Check: The same command that failed has to pass.
