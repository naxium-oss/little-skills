---
name: argparse-and-command-line-interfaces
description: "Use when \"argparse and command line interfaces\" is the work. assuming type=int gives friendly errors for non-numeric input without testing."
---

# argparse and Command-Line Interfaces

assuming type=int gives friendly errors for non-numeric input without testing.

1. Do not: assuming type=int gives friendly errors for non-numeric input without testing.
2. Do not: forgetting required=True on subparsers and getting None silently.

Example:
```bash
python3 -c "import importlib.metadata as m; print(m.version('pip'))"
```

Check: Do not: assuming type=int gives friendly errors for non-numeric input without testing.
