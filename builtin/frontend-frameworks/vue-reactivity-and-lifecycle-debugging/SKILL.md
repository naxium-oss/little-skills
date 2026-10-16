---
name: vue-reactivity-and-lifecycle-debugging
description: "Use when \"vue reactivity and lifecycle debugging\" is the work. Inspect tracked dependencies, proxy boundaries, computed values, watchers, and lifecycle cleanup."
---

# Vue Reactivity and Lifecycle Debugging

Inspect tracked dependencies, proxy boundaries, computed values, watchers, and lifecycle cleanup.

1. Verify framework, compiler, router, and plugin versions together.
2. Identify state ownership and render boundaries.
3. Isolate the smallest component that reproduces the observed lifecycle or rendering behavior.

Example:
```text
Verify framework, compiler, router, and plugin versions together.
```

Check: Test mount, update, unmount, navigation, hydration where applicable, and production builds; inspect stale closures and cleanup paths.
