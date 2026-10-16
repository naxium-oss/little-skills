---
name: higher-order-functions-and-function-composition
description: "Use when \"higher order functions and function composition\" is the work. chaining many .map().filter().reduce() calls over huge datasets without profiling, incurring multiple full traversals where one loop would suffice."
---

# Higher-Order Functions and Function Composition

chaining many .map().filter().reduce() calls.

1. Do not: chaining many .map().filter().reduce() calls over huge datasets without profiling, incurring multiple full traversals where.
2. Do not: composing functions with mismatched arity/argument order, silently passing wrong values downstream.

Example:
```bash
locate the effects: I/O, clock, randomness, mutation
```

Check: Do not: chaining many.
