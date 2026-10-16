---
name: null-and-empty
description: "Use when \"empty input\", \"NoneType\", \"null reference\", or \"undefined where\". Not when the value is a normal zero."
---

# Null and empty

Empty is a real input. Handle it before the happy path.

1. Find the line that assumes a value exists.
2. Decide the empty result: default, skip, or error.
3. Add that case to the test.

Example:
```text
items is None. Return 0 for an empty cart. Test both.
```

Check: A guard that hides a missing record is not a default.
