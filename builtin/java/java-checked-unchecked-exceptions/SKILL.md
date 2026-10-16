---
name: java-checked-unchecked-exceptions
description: "Use when \"java checked unchecked exceptions\" is the work. Checked exceptions are part of the declared call contract."
---

# Java Checked & Unchecked Exceptions

Checked exceptions are part of the declared call contract.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```java
class InvalidConfig extends Exception {
InvalidConfig(String message, Throwable cause) { super(message, cause); }
}
```

Check: Do not edit the assert to match a surprising result.
