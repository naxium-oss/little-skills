---
name: logging-configuration
description: "Use when \"logging configuration\" is the work. calling logging.basicConfig multiple times expecting reconfiguration."
---

# Logging Configuration

calling logging.basicConfig multiple times expecting reconfiguration.

1. Do not: calling logging.basicConfig multiple times expecting reconfiguration.
2. Do not: logging secrets or PII in extra fields that reach shared log sinks.

Example:
```bash
python3 -c "import importlib.metadata as m; print(m.version('pip'))"
python3 -m pip --version
```

Check: Do not: calling logging.basicConfig multiple times expecting reconfiguration.
