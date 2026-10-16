---
name: trap-based-cleanup-and-signal-handling
description: "Use when \"trap based cleanup and signal handling\" is the work. registering cleanup only for EXIT and assuming Ctrl-C triggers it identically without also trapping INT/TERM explicitly in some."
---

# Trap-Based Cleanup and Signal Handling

registering cleanup only for EXIT.

1. Do not: registering cleanup only for EXIT and assuming Ctrl-C triggers it identically without also trapping.
2. Do not: overwriting a previously set trap by calling trap again without combining handlers.

Example:
```bash
tmpdir=$(mktemp -d)
```

Check: Do not: registering cleanup only for EXIT and assuming Ctrl-C triggers it identically without also trapping INT/TERM explicitly.
