---
name: php-datetimeimmutable-time-zones
description: "Use when \"php datetimeimmutable time zones\" is the work. Use immutable date objects when callers must not share accidental mutation."
---

# PHP DateTimeImmutable & Time Zones

Use immutable date objects when callers must not share accidental mutation.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```php
$start = new DateTimeImmutable("2024-02-28", new DateTimeZone("UTC"));
$next = $start->modify("+1 day");
```

Check: Do not edit the assert to match a surprising result.
