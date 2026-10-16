---
name: csharp-span-range-based-processing
description: "Use when \"c span range based processing\" is the work. Span is a view, not an owned copy."
---

# C# Span & Range-Based Processing

Span is a view, not an owned copy.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
int[] values = { 1, 2, 3 };
Span<int> middle = values.AsSpan(1, 1);
middle[0] = 9;
```

Check: Do not edit the assert to match a surprising result.
