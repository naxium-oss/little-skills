---
name: javascript-prototypes-delegation
description: "Use when \"javascript prototypes delegation\" is the work. Property reads can traverse the prototype chain."
---

# JavaScript Prototypes & Delegation

Property reads can traverse the prototype chain.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
const parent = { kind: "shape" };
const child = Object.create(parent);
child.size = 4;
```

Check: Do not edit the assert to match a surprising result.
