---
name: checked-exceptions-and-exception-hierarchy-design
description: "Use when \"checked exceptions and exception hierarchy design\" is the work. catching Exception broadly to satisfy the compilers checked-exception requirement, accidentally swallowing unrelated runtime bugs."
---

# Checked Exceptions and Exception Hierarchy Design

catching Exception broadly to satisfy the compiler's.

1. Do not: catching Exception broadly to satisfy the compiler's checked-exception requirement, accidentally swallowing unrelated runtime bugs.
2. Do not: overusing checked exceptions for conditions that are really unrecoverable programming errors, forcing boilerplate try/catch.

Example:
```java
public class InsufficientFundsException extends Exception {   // checked: caller must decide how to handle
```

Check: Do not: catching Exception broadly to satisfy the.
