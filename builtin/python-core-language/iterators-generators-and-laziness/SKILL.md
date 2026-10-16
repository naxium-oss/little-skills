---
name: iterators-generators-and-laziness
description: "Use when \"iterators generators and laziness\" is the work. passing a generator to a function that iterates it more than once."
---

# Iterators, Generators, and Laziness

passing a generator to a function that iterates it more than once.

1. Do not: passing a generator to a function that iterates it more than once.
2. Do not: assuming generator expressions support indexing or len().

Example:
```bash
python3 --version
python3 -c "import sys; print(sys.version_info, sys.implementation.name)"
```

Check: Do not: passing a generator to a function that iterates it more than once.
