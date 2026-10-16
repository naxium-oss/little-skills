---
name: ruby-modules-method-lookup
description: "Use when \"ruby modules method lookup\" is the work. include inserts a module into the ancestor chain; prepend places it ahead of the class."
---

# Ruby Modules & Method Lookup

include inserts a module into the ancestor chain; prepend places it ahead of the class.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
module Label
def name; "[#{super}]"; end
end
```

Check: Do not edit the assert to match a surprising result.
