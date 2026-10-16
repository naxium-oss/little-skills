---
name: php-classes-interfaces-traits
description: "Use when \"php classes interfaces traits\" is the work. Interfaces define required behavior; traits supply reusable implementations."
---

# PHP Classes, Interfaces & Traits

Interfaces define required behavior; traits supply reusable implementations.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
interface Named { public function name(): string; }
trait Label { public function name(): string { return "Ada"; } }
class User implements Named { use Label; }
```

Check: Do not edit the assert to match a surprising result.
