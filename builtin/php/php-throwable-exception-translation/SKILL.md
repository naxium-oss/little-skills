---
name: php-throwable-exception-translation
description: "Use when \"php throwable exception translation\" is the work. Exception and Error both implement Throwable."
---

# PHP Throwable & Exception Translation

Exception and Error both implement Throwable.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
function number(string $text): int {
if (!preg_match("/^[0-9]+$/D", $text)) {
throw new InvalidArgumentException("digits required");
```

Check: Do not edit the assert to match a surprising result.
