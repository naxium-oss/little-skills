---
name: regex-performance-profiling-and-precompilation
description: "Use when \"regex performance profiling and precompilation\" is the work. recompiling the same regex pattern from a string literal inside a hot loop or per-request handler instead of."
---

# Regex Performance Profiling and Precompilation

recompiling the same regex pattern.

1. Do not: recompiling the same regex pattern from a string literal inside a hot loop or.
2. Do not: testing regex performance only with short, typical inputs and missing catastrophic backtracking behavior that.

Example:
```bash
test the pattern against a positive and a negative fixture before using it
```

Check: Do not: recompiling the same regex pattern from a string literal inside a hot loop or per-request handler.
