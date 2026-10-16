---
name: greedy-versus-lazy-quantifiers
description: "Use when \"greedy versus lazy quantifiers\" is the work. using a greedy .+/."
---

# Greedy versus Lazy Quantifiers

using a greedy .+/.

1. Do not: using a greedy .+/. to match "up to the next delimiter" and unintentionally matching.
2. Do not: assuming lazy quantifiers are always "more correct," when greedy is actually intended for some.

Example:
```bash
test the pattern against a positive and a negative fixture before using it
```

Check: Do not: using a greedy .+/.
