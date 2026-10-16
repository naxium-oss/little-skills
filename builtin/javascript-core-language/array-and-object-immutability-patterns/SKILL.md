---
name: array-and-object-immutability-patterns
description: "Use when \"array and object immutability patterns\" is the work. calling .sort() directly on state arrays in React/Vue, mutating them in place and breaking change detection."
---

# Array and Object Immutability Patterns

calling .sort() directly on state arrays in React/Vue.

1. Do not: calling .sort() directly on state arrays in React/Vue, mutating them in place and breaking.
2. Do not: assuming Object.freeze is deep (it is shallow).

Example:
```javascript
const original = [3, 1, 2];
```

Check: Do not: calling .sort() directly on state arrays in.
