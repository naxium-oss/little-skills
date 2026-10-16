---
name: php-enums-match-expressions
description: "Use when \"php enums match expressions\" is the work. match compares strictly and must produce a value or throw when no arm matches."
---

# PHP Enums & match Expressions

match compares strictly and must produce a value or throw when no arm matches.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
enum Status: string { case Ready = "ready"; case Waiting = "waiting"; }
function label(Status $status): string {
```

Check: Do not edit the assert to match a surprising result.
