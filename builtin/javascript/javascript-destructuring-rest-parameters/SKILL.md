---
name: javascript-destructuring-rest-parameters
description: "Use when \"javascript destructuring rest parameters\" is the work. Destructuring defaults apply to undefined, not null."
---

# JavaScript Destructuring & Rest Parameters

Destructuring defaults apply to undefined, not null.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
const { name = "Guest", ...extra } = { role: "reader" };
console.assert(name === "Guest");
console.assert(extra.role === "reader");
```

Check: Do not edit the assert to match a surprising result.
