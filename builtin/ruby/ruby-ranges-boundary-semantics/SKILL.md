---
name: ruby-ranges-boundary-semantics
description: "Use when \"ruby ranges boundary semantics\" is the work. Two-dot ranges include the end, while three-dot ranges exclude it."
---

# Ruby Ranges & Boundary Semantics

Two-dot ranges include the end, while three-dot ranges exclude it.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
raise unless (1..3).to_a == [1, 2, 3]
raise unless (1...3).to_a == [1, 2]
```

Check: Do not edit the assert to match a surprising result.
