---
name: debug-ruby
description: "Use when \"ruby NoMethodError: undefined method for nil\", \"NoMethodError: undefined method for nil\". Not when explaining working ruby code."
---

# Debug ruby

Reproduce the ruby failure with the project command, then change one thing.

1. NoMethodError: undefined method for nil: The stack names the nil; find where the object should have.
2. LoadError: Gem version conflicts via `bundle check`; autoload (Zeitwerk) naming conventions must match file names exactly.
3. Tests pass alone, fail together: Shared state, ordering, and `let` memoization across examples; reset in `before`.

Example:
```text
bundle exec rspec
```

Check: The same command that failed has to pass.
