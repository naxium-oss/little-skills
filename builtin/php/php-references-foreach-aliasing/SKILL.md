---
name: php-references-foreach-aliasing
description: "Use when \"php references foreach aliasing\" is the work. A by-reference foreach leaves the loop variable bound to the last element."
---

# PHP References & foreach Aliasing

A by-reference foreach leaves the loop variable bound to the last element.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
$values = [1, 2, 3];
foreach ($values as &$value) { $value *= 2; }
unset($value);
```

Check: Do not edit the assert to match a surprising result.
