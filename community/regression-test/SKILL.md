---
name: regression-test
description: "Use when \"regression test\", \"doesn't come back\", or \"add a test for the bug\". Not when write tests for a new feature."
---

# Lock the bug

The bug's test fails on the old code and passes on the fix.

1. Turn the repro into a test.
2. See it fail.
3. Apply the fix and see that test pass.

Example:
```text
test_empty_cart failed on None, then passed after the guard.
```

Check: A test written after the fix proves nothing until you see it fail.
