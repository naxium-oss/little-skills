---
name: prototypes-classes-and-this-binding
description: "Use when \"prototypes classes and this binding\" is the work. passing obj.method directly as a callback without binding."
---

# Prototypes, Classes, and `this` Binding

passing obj.method directly as a callback without binding.

1. Do not: passing obj.method directly as a callback without binding.
2. Do not: assuming class fields and prototype methods behave identically for memory (class fields allocate per-instance).

Example:
```javascript
class Counter {
count = 0;
incrementRegular() { this.count++; }
```

Check: Do not: passing obj.method directly as a callback without binding.
