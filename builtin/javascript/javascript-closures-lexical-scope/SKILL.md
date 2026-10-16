---
name: javascript-closures-lexical-scope
description: "Use when \"javascript closures lexical scope\" is the work. Closures retain bindings rather than frozen copies of values."
---

# JavaScript Closures & Lexical Scope

Closures retain bindings rather than frozen copies of values.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
function counter() {
let value = 0;
return () => ++value;
```

Check: Do not edit the assert to match a surprising result.
