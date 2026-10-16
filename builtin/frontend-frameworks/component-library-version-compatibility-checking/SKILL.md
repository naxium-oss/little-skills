---
name: component-library-version-compatibility-checking
description: "Use when \"component library version compatibility checking\" is the work. Intersect peer requirements, style-system assumptions, component APIs, and framework support ranges."
---

# Component Library Version Compatibility Checking

Intersect peer requirements, style-system assumptions, component APIs, and framework support ranges.

1. Verify framework, compiler, router, and plugin versions together.
2. Identify state ownership and render boundaries.
3. Isolate the smallest component that reproduces the observed lifecycle or rendering behavior.

Example:
```text
Verify framework, compiler, router, and plugin versions together.
```

Check: Test mount, update, unmount, navigation, hydration where applicable, and production builds; inspect stale closures and cleanup paths.
