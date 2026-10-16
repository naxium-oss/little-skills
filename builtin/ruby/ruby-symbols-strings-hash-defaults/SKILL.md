---
name: ruby-symbols-strings-hash-defaults
description: "Use when \"ruby symbols strings hash defaults\" is the work. Symbols and strings are distinct keys."
---

# Ruby Symbols, Strings & Hash Defaults

Symbols and strings are distinct keys.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
groups = Hash.new { |hash, key| hash[key] = [] }
groups[:a] << 1
raise unless groups[:b] == []
```

Check: Do not edit the assert to match a surprising result.
