---
name: undefined-behavior-and-sanitizer-verified-correctness
description: "Use when \"undefined behavior and sanitizer verified correctness\" is the work."
---

# Undefined Behavior and Sanitizer-Verified Correctness

treating "it ran without crashing".

1. Do not: treating "it ran without crashing" as proof of correctness for pointer/array code, when UB.
2. Do not: relying on signed integer overflow wrapping behavior, which is undefined (not guaranteed to wrap).

Example:
```bash
g++ -std=c++20 -fsanitize=address,undefined -g -O1 file.cpp -o file_sanitized
```

Check: Do not: treating "it.
