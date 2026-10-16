---
name: ruby-method-visibility-encapsulation
description: "Use when \"ruby method visibility encapsulation\" is the work. Visibility affects how methods can be invoked; it is not a security sandbox."
---

# Ruby Method Visibility & Encapsulation

Visibility affects how methods can be invoked; it is not a security sandbox.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
class Wallet
def balance; cents; end
private
```

Check: Do not edit the assert to match a surprising result.
