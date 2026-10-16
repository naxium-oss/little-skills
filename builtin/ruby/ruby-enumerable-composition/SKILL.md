---
name: ruby-enumerable-composition
description: "Use when \"ruby enumerable composition\" is the work. Enumerable methods derive behavior from each."
---

# Ruby Enumerable Composition

Enumerable methods derive behavior from each.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
result = [1, 2, 3, 4].select(&:even?).map { |n| n * 10 }
raise unless result == [20, 40]
result = (1..).lazy.select(&:even?).first(3)
```

Check: Do not edit the assert to match a surprising result.
