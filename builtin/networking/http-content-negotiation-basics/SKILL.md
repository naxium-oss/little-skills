---
name: http-content-negotiation-basics
description: "Use when \"http content negotiation basics\" is the work. Accept describes preferred response representations; Content-Type describes the actual representation."
---

# HTTP Content Negotiation Basics

Accept describes preferred response representations; Content-Type describes the actual representation.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
def choose(accept):
for value in accept.split(","):
if value.strip() in {"application/json", "text/plain"}:
```

Check: Do not edit the assert to match a surprising result.
