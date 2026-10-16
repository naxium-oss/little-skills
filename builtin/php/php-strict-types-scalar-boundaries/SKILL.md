---
name: php-strict-types-scalar-boundaries
description: "Use when \"php strict types scalar boundaries\" is the work. strict_types is declared per file and affects relevant calls made there."
---

# PHP Strict Types & Scalar Boundaries

strict_types is declared per file and affects relevant calls made there.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
<?php
declare(strict_types=1);
function twice(int $value): int { return $value * 2; }
```

Check: Do not edit the assert to match a surprising result.
