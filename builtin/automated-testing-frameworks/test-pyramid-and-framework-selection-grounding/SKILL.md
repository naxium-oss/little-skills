---
name: test-pyramid-and-framework-selection-grounding
description: "Use when \"test pyramid and framework selection grounding\" is the work. writing tests using Jest-specific globals (jest.fn()) in a project that migrated to Vitest, causing silent no-ops or import."
---

# Test Pyramid and Framework Selection Grounding

writing tests using Jest-specific.

1. Do not: writing tests using Jest-specific globals (jest.fn()) in a project that migrated to Vitest, causing.
2. Do not: over-investing in slow E2E tests for logic better covered by fast unit tests.

Example:
```bash
read the runner config and the test script in the manifest
```

Check: Do not: writing tests.
