---
name: csharp-nullable-value-types-lifted-operators
description: "Use when \"c nullable value types lifted operators\" is the work. Nullable value types distinguish absence from a stored default."
---

# C# Nullable Value Types & Lifted

Nullable value types distinguish absence from a stored default.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
int? value = null;
Debug.Assert((value + 1) is null);
Debug.Assert((value ?? 0) == 0);
```

Check: Do not edit the assert to match a surprising result.
