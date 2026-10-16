---
name: packaging-a-distributable-project-with-pyproject-toml
description: "Use when \"packaging a distributable project with pyproject toml\" is the work. publishing a package that only works because of files present in the dev checkout but excluded from the."
---

# Packaging a Distributable Project with pyproject.toml

publishing a package that.

1. Do not: publishing a package that only works because of files present in the dev checkout.
2. Do not: mismatched requires-python versus features actually used in the code.

Example:
```bash
python3 -c "import importlib.metadata as m; print(m.version('pip'))"
```

Check: Do not: publishing a package that only works because.
