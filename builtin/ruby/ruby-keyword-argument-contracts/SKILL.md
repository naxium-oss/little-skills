---
name: ruby-keyword-argument-contracts
description: "Use when \"ruby keyword argument contracts\" is the work. Use explicit keyword parameters and forwarding."
---

# Ruby Keyword Argument Contracts

Use explicit keyword parameters and forwarding.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```ruby
def connect(host, timeout: 3, **extra)
[host, timeout, extra]
end
```

Check: Do not edit the assert to match a surprising result.
