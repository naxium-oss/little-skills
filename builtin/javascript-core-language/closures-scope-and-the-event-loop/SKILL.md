---
name: closures-scope-and-the-event-loop
description: "Use when \"closures scope and the event loop\" is the work. assuming setTimeout(fn, 0) runs immediately."
---

# Closures, Scope, and the Event Loop

assuming setTimeout(fn, 0) runs immediately.

1. Do not: assuming setTimeout(fn, 0) runs immediately.
2. Do not: forgetting process.nextTick starves the event loop if recursively scheduled.

Example:
```javascript
console.log("start");
setTimeout(() => console.log("timeout"), 0);
Promise.resolve().then(() => console.log("promise"));
```

Check: Do not: assuming setTimeout(fn, 0) runs immediately.
