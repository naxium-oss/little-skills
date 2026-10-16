---
name: next-js-server-client-boundary-validation
description: "Use when \"next js server client boundary validation\" is the work. Keep secrets and server-only dependencies outside client bundles and validate serialized boundary values."
---

# Next.js Server–Client Boundary Validation

Keep secrets and server-only dependencies outside client bundles and validate serialized boundary values.

1. Verify framework, compiler, router, and plugin versions together.
2. Identify state ownership and render boundaries.

Example:
```text
Verify framework, compiler, router, and plugin versions together.
```

Check: Test mount, update, unmount, navigation, hydration where applicable, and production builds; inspect stale closures and cleanup paths.
