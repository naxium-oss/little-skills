---
name: csharp-records-non-destructive-mutation
description: "Use when \"c records non destructive mutation\" is the work. Record equality is value-based for its fields, but reference-typed fields retain their own equality rules."
---

# C# Records & Non-Destructive Mutation

Record equality is value-based for its fields, but reference-typed fields retain their own equality rules.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
public record Point(int X, int Y);
```

Check: Do not edit the assert to match a surprising result.
