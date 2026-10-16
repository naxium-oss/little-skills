---
name: javascript-equality-coercion
description: "Use when \"javascript equality coercion\" is the work. Prefer strict equality for ordinary comparisons."
---

# JavaScript Equality & Coercion

Prefer strict equality for ordinary comparisons.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
console.assert(0 !== "0");
console.assert(Number("42") === 42);
console.assert(Number.isNaN(Number("hello")));
```

Check: Do not edit the assert to match a surprising result.
