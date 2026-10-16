---
name: php-generators-lazy-traversal
description: "Use when \"php generators lazy traversal\" is the work. Calling a generator function creates a Generator."
---

# PHP Generators & Lazy Traversal

Calling a generator function creates a Generator.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
function squares(iterable $values): Generator {
foreach ($values as $value) { yield $value * $value; }
}
```

Check: Do not edit the assert to match a surprising result.
