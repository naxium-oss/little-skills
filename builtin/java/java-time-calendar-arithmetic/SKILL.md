---
name: java-time-calendar-arithmetic
description: "Use when \"java time calendar arithmetic\" is the work. An Instant is a timeline point, while LocalDate has no time zone."
---

# Java Time & Calendar Arithmetic

An Instant is a timeline point, while LocalDate has no time zone.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
LocalDate date = LocalDate.of(2024, 2, 28);
assert date.plusDays(1).equals(LocalDate.of(2024, 2, 29));
```

Check: Do not edit the assert to match a surprising result.
