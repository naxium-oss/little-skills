---
name: testing-with-pytest-fixtures-and-parametrization
description: "Use when \"testing with pytest fixtures and parametrization\" is the work. naming test files without a test_ prefix and having them silently skipped."
---

# Testing with pytest: Fixtures and Parametrization

naming test files without a test_ prefix and having them silently skipped.

1. Do not: naming test files without a test_ prefix and having them silently skipped.
2. Do not: fixture scope leaking state between tests when marked session incorrectly.

Example:
```bash
python3 -c "import importlib.metadata as m; print(m.version('pip'))"
python3 -m pip --version
```

Check: Do not: naming test files without a test_ prefix and having them silently skipped.
