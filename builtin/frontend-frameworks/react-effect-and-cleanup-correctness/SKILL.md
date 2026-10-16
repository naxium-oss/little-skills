---
name: react-effect-and-cleanup-correctness
description: "Use when \"react effect and cleanup correctness\" is the work. Verify dependency arrays, subscription ownership, cleanup symmetry, and asynchronous cancellation."
---

# React Effect and Cleanup Correctness

Verify dependency arrays, subscription ownership, cleanup symmetry, and asynchronous cancellation.

1. Verify framework, compiler, router, and plugin versions together.
2. Identify state ownership and render boundaries.
3. Isolate the smallest component that reproduces the observed lifecycle or rendering behavior.

Example:
```text
Verify framework, compiler, router, and plugin versions together.
```

Check: Test mount, update, unmount, navigation, hydration where applicable, and production builds; inspect stale closures and cleanup paths.
