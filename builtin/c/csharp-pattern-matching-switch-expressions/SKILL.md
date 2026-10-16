---
name: csharp-pattern-matching-switch-expressions
description: "Use when \"c pattern matching switch expressions\" is the work. Patterns can inspect types, constants, and properties."
---

# C# Pattern Matching & Switch Expressions

Patterns can inspect types, constants, and properties.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
static string Label(object? value) => value switch {
null => "missing",
int n when n < 0 => "negative",
```

Check: Do not edit the assert to match a surprising result.
