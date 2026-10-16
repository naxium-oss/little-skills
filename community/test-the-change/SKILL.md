---
name: test-the-change
description: "Use when \"make sure it works\", \"run the tests\", or \"did you test\". Not when are we done is the whole release."
---

# Test this change

Run the narrowest check that would fail if the edit was wrong.

1. Pick the test or command for the file you edited.
2. Run it.
3. Quote the pass or the failure.

Example:
```text
npm test -- cart. 1 passed.
```

Check: The whole suite is not required when one test proves the edit.
