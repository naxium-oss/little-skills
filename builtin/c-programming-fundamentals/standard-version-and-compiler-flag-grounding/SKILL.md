---
name: standard-version-and-compiler-flag-grounding
description: "Use when \"standard version and compiler flag grounding\" is the work. assuming -std=c++20 alone guarantees a specific library feature is implemented by the actual standard library shipped with the."
---

# Standard Version and Compiler Flag Grounding

assuming -std=c++20 alone guarantees.

1. Do not: assuming -std=c++20 alone guarantees a specific library feature is implemented by the actual standard.
2. Do not: mixing object files compiled with different standard versions or ABI-incompatible compiler flags.

Example:
```bash
cmake --build build
```

Check: Do not: assuming -std=c++20 alone guarantees a specific library.
