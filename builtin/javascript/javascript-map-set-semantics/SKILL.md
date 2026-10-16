---
name: javascript-map-set-semantics
description: "Use when \"javascript map set semantics\" is the work. Map object keys compare by identity, not structural equality."
---

# JavaScript Map & Set Semantics

Map object keys compare by identity, not structural equality.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
const key = { id: 1 };
const values = new Map([[key, "found"]]);
console.assert(values.get(key) === "found");
```

Check: Do not edit the assert to match a surprising result.
