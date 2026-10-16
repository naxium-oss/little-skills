---
name: test-writing
description: "Use when \"write tests\", \"add tests\", or \"improve tests\". Not when pytest fails."
---

# Write a test

One test names one behavior and fails if that behavior breaks.

1. Use the lowest level that would catch the bug.
2. Arrange, act, assert. Name the behavior, not the call.
3. Run it once against the old code so it fails for the right reason.

Example:
```text
test("rejects an expired token")
```

Check: Do not delete or weaken a failing test to get green.
