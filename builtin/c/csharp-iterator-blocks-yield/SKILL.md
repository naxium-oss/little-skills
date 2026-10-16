---
name: csharp-iterator-blocks-yield
description: "Use when \"c iterator blocks yield\" is the work. Iterator bodies execute during enumeration, not when the method is called."
---

# C# Iterator Blocks & yield

Iterator bodies execute during enumeration, not when the method is called.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
static IEnumerable<int> Range(int count) {
if (count < 0) throw new ArgumentOutOfRangeException(nameof(count));
return Iterate(count);
```

Check: Do not edit the assert to match a surprising result.
