---
name: exception-handling-and-control-flow
description: "Use when \"exception handling and control flow\" is the work. swallowing exceptions with bare except: pass."
---

# Exception Handling and Control Flow

swallowing exceptions with bare except: pass.

1. Do not: swallowing exceptions with bare except: pass.
2. Do not: losing the original traceback by raising a new exception without from exc.

Example:
```bash
python3 --version
python3 -c "import sys; print(sys.version_info, sys.implementation.name)"
```

Check: Do not: swallowing exceptions with bare except: pass.
