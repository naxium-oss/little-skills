---
name: ruby-pattern-matching-deconstruction
description: "Use when \"ruby pattern matching deconstruction\" is the work. Patterns bind variables and can invoke deconstruction protocols."
---

# Ruby Pattern Matching & Deconstruction

Patterns bind variables and can invoke deconstruction protocols.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
value = { status: :ok, data: [1, 2] }
result = case value
in { status: :ok, data: [first, *rest] } then [first, rest]
```

Check: Do not edit the assert to match a surprising result.
