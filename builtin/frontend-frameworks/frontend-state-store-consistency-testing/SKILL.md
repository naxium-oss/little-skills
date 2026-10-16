---
name: frontend-state-store-consistency-testing
description: "Use when \"frontend state store consistency testing\" is the work. Check derived-state invariants, transaction boundaries, selector behavior, and persistence synchronization."
---

# Frontend State Store Consistency Testing

Check derived-state invariants, transaction boundaries, selector behavior, and persistence synchronization.

1. Verify framework, compiler, router, and plugin versions together.
2. Identify state ownership and render boundaries.
3. Isolate the smallest component that reproduces the observed lifecycle or rendering behavior.

Example:
```text
Verify framework, compiler, router, and plugin versions together.
```

Check: Test mount, update, unmount, navigation, hydration where applicable, and production builds; inspect stale closures and cleanup paths.
