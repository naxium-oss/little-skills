---
name: java-generics-wildcard-variance
description: "Use when \"java generics wildcard variance\" is the work. A producer of T uses extends T; a consumer of T uses super T."
---

# Java Generics & Wildcard Variance

A producer of T uses extends T; a consumer of T uses super T.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
static double sum(List<? extends Number> values) {
double total = 0;
for (Number value : values) total += value.doubleValue();
```

Check: Do not edit the assert to match a surprising result.
