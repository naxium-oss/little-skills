---
name: csharp-value-reference-semantics
description: "Use when \"c value reference semantics\" is the work. Struct assignment copies the value; class assignment copies a reference."
---

# C# Value & Reference Semantics

Struct assignment copies the value; class assignment copies a reference.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
struct Point { public int X; }
var a = new Point { X = 1 };
var b = a; b.X = 2;
```

Check: Do not edit the assert to match a surprising result.
