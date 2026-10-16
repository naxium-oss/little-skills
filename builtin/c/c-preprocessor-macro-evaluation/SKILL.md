---
name: c-preprocessor-macro-evaluation
description: "Use when \"c preprocessor macro evaluation\" is the work. Parenthesize macro operands and the whole expression, but recognize this does not prevent repeated evaluation."
---

# C Preprocessor & Macro Evaluation

Parenthesize macro operands and the whole expression, but recognize this does not prevent repeated evaluation.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```c
assert(SQUARE(1 + 2) == 9);
static inline int square_int(int x) { return x * x; }
```

Check: Do not edit the assert to match a surprising result.
