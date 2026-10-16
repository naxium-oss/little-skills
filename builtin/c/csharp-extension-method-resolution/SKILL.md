---
name: csharp-extension-method-resolution
description: "Use when \"c extension method resolution\" is the work. Extension methods are static methods resolved at compile time."
---

# C# Extension Method Resolution

Extension methods are static methods resolved at compile time.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
static class TextExtensions {
public static string OrGuest(this string? text) =>
string.IsNullOrWhiteSpace(text) ? "Guest" : text;
```

Check: Do not edit the assert to match a surprising result.
