---
name: java-memory-model-and-volatile-synchronized-visibility
description: "Use when \"java memory model and volatile synchronized visibility\" is the work. reading/writing a shared field without volatile or synchronization and assuming the JVM guarantees prompt cross-thread visibility, when the."
---

# Java Memory Model and Volatile/Synchronized Visibility

reading/writing a shared field without.

1. Do not: reading/writing a shared field without volatile or synchronization and assuming the JVM guarantees prompt.
2. Do not: using volatile for compound operations (counter++) that aren't actually atomic despite the field itself.

Example:
```java
public class FlagHolder {
```

Check: Do not: reading/writing a shared field without volatile or.
