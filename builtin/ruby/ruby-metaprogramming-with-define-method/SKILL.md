---
name: ruby-metaprogramming-with-define-method
description: "Use when \"ruby metaprogramming with define method\" is the work. Prefer define_method with controlled names over unrestricted eval."
---

# Ruby Metaprogramming with define_method

Prefer define_method with controlled names over unrestricted eval.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
class Flags
[:ready, :active].each do |name|
define_method("#{name}?") { !!instance_variable_get("@#{name}") }
```

Check: Do not edit the assert to match a surprising result.
