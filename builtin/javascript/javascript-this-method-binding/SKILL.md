---
name: javascript-this-method-binding
description: "Use when \"javascript this method binding\" is the work. The call site determines this for ordinary functions."
---

# JavaScript this & Method Binding

The call site determines this for ordinary functions.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```javascript
const account = {
balance: 4,
read() { return this.balance; }
```

Check: Do not edit the assert to match a surprising result.
