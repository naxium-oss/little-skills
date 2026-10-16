---
name: csharp-linq-deferred-execution
description: "Use when \"c linq deferred execution\" is the work. Many LINQ operators defer work until enumeration."
---

# C# LINQ & Deferred Execution

Many LINQ operators defer work until enumeration.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
var values = new List<int> { 1, 2 };
var query = values.Where(x => x > 1);
values.Add(3);
```

Check: Do not edit the assert to match a surprising result.
