---
name: equality-coercion-and-type-semantics
description: "Use when \"equality coercion and type semantics\" is the work. using == for null checks broadly (x == null is idiomatic for null-or-undefined, but confirm the codebases lint."
---

# Equality, Coercion, and Type Semantics

using == for null checks.

1. Do not: using == for null checks broadly (x == null is idiomatic for null-or-undefined, but.
2. Do not: comparing floats for exact equality without an epsilon.

Example:
```javascript
console.log(NaN === NaN);        // false
```

Check: Do not: using == for null checks broadly (x.
