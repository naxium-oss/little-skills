---
name: debug-java
description: "Use when \"java NullPointerException\", \"NullPointerException\". Not when explaining working java code."
---

# Debug java

Reproduce the java failure with the project command, then change one thing.

1. NullPointerException: The stack frame names the exact line; find which expression is null and where it.
2. Caused by chain hides the real error: Read the innermost `Caused by` first, the outer frames.
3. ClassNotFoundException: Dependency version conflict on the classpath; `mvn dependency:tree` / `gradle dependencies` to find the duplicate.

Example:
```text
./mvnw test
```

Check: The same command that failed has to pass.
