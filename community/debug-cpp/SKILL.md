---
name: debug-cpp
description: "Use when \"cpp Segfault\", \"Segfault\". Not when explaining working cpp code."
---

# Debug cpp

Reproduce the cpp failure with the project command, then change one thing.

1. Segfault: Build with ASan + debug symbols, run the repro under gdb, and read the stack.
2. Wrong values, no crash: Check for uninitialized variables, integer overflow, and `unsigned` wrapping before pointer math.
3. Works in Debug, breaks in Release: Optimizer exposes UB (uninitialized reads, signed overflow, aliasing); build Release.

Example:
```text
cmake --build build
```

Check: The same command that failed has to pass.
