---
name: uri-components-percent-encoding
description: "Use when \"uri components percent encoding\" is the work. Percent-encode individual components, not a fully assembled URI."
---

# URI Components & Percent Encoding

Percent-encode individual components, not a fully assembled URI.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
from urllib.parse import quote, urlencode, urlsplit
path = "/items/" + quote("a/b", safe="")
query = urlencode({"q": "hello world", "page": 1})
```

Check: Do not edit the assert to match a surprising result.
