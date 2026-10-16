---
name: react-hydration-mismatch-diagnosis
description: "Use when \"react hydration mismatch diagnosis\" is the work. Compare server and first-client output for time, randomness, locale, browser-only values, and invalid markup."
---

# React Hydration Mismatch Diagnosis

Compare server and first-client output for time, randomness, locale, browser-only values, and invalid markup.

1. Verify framework, compiler, router, and plugin versions together.
2. Identify state ownership and render boundaries.

Example:
```text
Verify framework, compiler, router, and plugin versions together.
```

Check: Test mount, update, unmount, navigation, hydration where applicable, and production builds; inspect stale closures and cleanup paths.
