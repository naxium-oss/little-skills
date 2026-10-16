---
name: concurrency-primitives-threading-multiprocessing-asyncio
description: "Use when \"concurrency primitives threading multiprocessing asyncio\" is the work. using threading for CPU-bound number crunching and being surprised the GIL serializes it."
---

# Concurrency Primitives: threading, multiprocessing, asyncio

using threading for CPU-bound number crunching and being surprised the GIL serializes it.

1. Do not: using threading for CPU-bound number crunching and being surprised the GIL serializes it.
2. Do not: forgetting await and silently creating unawaited coroutine warnings.

Example:
```bash
python3 -c "import importlib.metadata as m; print(m.version('pip'))"
```

Check: Do not: using threading for CPU-bound number crunching and being surprised the GIL serializes it.
