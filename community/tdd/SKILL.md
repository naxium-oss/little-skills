---
name: tdd
description: "Use when \"test first\", \"failing test\", \"tdd\", or \"tests after\" before production code. Not when explain or how many."
---

# Test first

The first file is a test that fails for the right reason.

1. Write the test that names the behavior.
2. Run it and read the failure. A pass now means the test is wrong.
3. Write the smallest code that makes that failure pass.

Example:
```text
expect(slugify("A B")).toBe("a-b") fails. Then implement slugify.
```

Check: tests after still means test first. Do not skip the failing test.
