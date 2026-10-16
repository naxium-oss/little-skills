---
name: php-closures-arrow-function-capture
description: "Use when \"php closures arrow function capture\" is the work. Arrow functions capture referenced outer variables by value."
---

# PHP Closures & Arrow Function Capture

Arrow functions capture referenced outer variables by value.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
$value = 1;
$snapshot = fn() => $value;
$live = function () use (&$value) { return $value; };
```

Check: Do not edit the assert to match a surprising result.
