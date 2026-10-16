---
name: ruby-object-identity-copying
description: "Use when \"ruby object identity copying\" is the work. == checks value behavior chosen by the class; equal?"
---

# Ruby Object Identity & Copying

== checks value behavior chosen by the class; equal?

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
a = ["hello"]
b = a.dup
raise unless a == b
```

Check: Do not edit the assert to match a surprising result.
