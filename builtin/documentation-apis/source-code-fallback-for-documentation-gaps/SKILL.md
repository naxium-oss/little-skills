---
name: source-code-fallback-for-documentation-gaps
description: "Use when \"source code fallback for documentation gaps\" is the work. Inspect the matching source tag and tests; label implementation behavior separately from public API guarantees."
---

# Source-Code Fallback for Documentation Gaps

Inspect the matching source tag and tests; label implementation behavior separately from public API guarantees.

1. Resolve the installed package revision.
2. Locate its matching official documentation or source tag.
3. Run the smallest executable example and compare actual output with the documented contract.

Example:
```text
Resolve the installed package revision.
```

Check: Record the documentation version, quoted section, retrieval date, executed example, exit code, and any contradictions.
