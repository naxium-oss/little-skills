---
name: csharp-generic-constraints-variance
description: "Use when \"c generic constraints variance\" is the work. Variance is available for qualifying interfaces and delegates, not arbitrary classes."
---

# C# Generic Constraints & Variance

Variance is available for qualifying interfaces and delegates, not arbitrary classes.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
interface ISource<out T> { T Get(); }
class Source<T> : ISource<T> {
readonly T value;
```

Check: Do not edit the assert to match a surprising result.
