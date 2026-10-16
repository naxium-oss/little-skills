---
name: debug-python
description: "Use when \"pytest fails\", \"ModuleNotFoundError\", \"python ModuleNotFoundError\". Not when explaining working python code."
---

# Debug python

Reproduce the python failure with the project command, then change one thing.

1. ModuleNotFoundError: Check cwd vs package root, missing `__init__.py`, PYTHONPATH, and whether you are inside a venv.
2. Runs on my machine but not here: Compare Python version, venv, and `pip freeze`; check relative-path.
3. Stale behavior after edits: Delete `__pycache__`; restart the interpreter; check that the file you edited is.

Example:
```text
python -m pytest -x
```

Check: The same command that failed has to pass.
