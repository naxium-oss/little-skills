---
name: php-namespaces-autoload-structure
description: "Use when \"php namespaces autoload structure\" is the work. Namespace names and filesystem layouts are related by the selected autoloader, not by PHP syntax alone."
---

# PHP Namespaces & Autoload Structure

Namespace names and filesystem layouts are related by the selected autoloader, not by PHP syntax alone.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
<?php
namespace App\Domain;
final class Price {
```

Check: Do not edit the assert to match a surprising result.
