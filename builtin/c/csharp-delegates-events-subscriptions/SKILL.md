---
name: csharp-delegates-events-subscriptions
description: "Use when \"c delegates events subscriptions\" is the work. Events restrict external invocation and assignment."
---

# C# Delegates, Events & Subscriptions

Events restrict external invocation and assignment.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```csharp
class Clock {
public event Action? Tick;
public void Pulse() => Tick?.Invoke();
```

Check: Do not edit the assert to match a surprising result.
