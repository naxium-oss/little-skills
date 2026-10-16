---
name: ruby-blocks-procs-lambdas
description: "Use when \"ruby blocks procs lambdas\" is the work. A lambda returns from itself and checks arity more strictly than an ordinary proc."
---

# Ruby Blocks, Procs & Lambdas

A lambda returns from itself and checks arity more strictly than an ordinary proc.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
double = ->(value) { value * 2 }
raise unless double.call(3) == 6
```

Check: Do not edit the assert to match a surprising result.
