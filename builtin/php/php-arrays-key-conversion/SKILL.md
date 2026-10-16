---
name: php-arrays-key-conversion
description: "Use when \"php arrays key conversion\" is the work. Some numeric string keys convert to integers."
---

# PHP Arrays & Key Conversion

Some numeric string keys convert to integers.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
$values = ["1" => "one", "01" => "zero-one"];
assert($values[1] === "one");
assert($values["01"] === "zero-one");
```

Check: Do not edit the assert to match a surprising result.
