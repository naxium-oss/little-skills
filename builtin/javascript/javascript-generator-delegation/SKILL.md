---
name: javascript-generator-delegation
description: "Use when \"javascript generator delegation\" is the work. A generator function returns an iterator without running its body immediately."
---

# JavaScript Generator Delegation

A generator function returns an iterator without running its body immediately.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
function* sequence() {
yield 1;
yield* [2, 3];
```

Check: Do not edit the assert to match a surprising result.
