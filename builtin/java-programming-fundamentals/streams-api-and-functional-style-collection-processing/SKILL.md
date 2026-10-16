---
name: streams-api-and-functional-style-collection-processing
description: "Use when \"streams api and functional style collection processing\" is the work. reaching for parallelStream() on a small collection or I/O-bound operation, adding overhead without benefit and potentially introducing thread-safety."
---

# Streams API and Functional-Style Collection Processing

reaching for parallelStream() on a.

1. Do not: reaching for parallelStream() on a small collection or I/O-bound operation, adding overhead without benefit.
2. Do not: chaining an excessively long stream pipeline that sacrifices readability for a marginal functional-style preference.

Example:
```java
List<String> activeUserEmails = users.stream()
```

Check: Do not: reaching for.
