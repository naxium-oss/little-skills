---
name: node-s-module-resolution-algorithm
description: "Use when \"node s module resolution algorithm\" is the work. assuming a deep-import path that worked in an older version of a dependency still resolves after it adopted."
---

# Node's Module Resolution Algorithm

assuming a deep-import path that.

1. Do not: assuming a deep-import path that worked in an older version of a dependency still.
2. Do not: mixing relative and bare-specifier assumptions when moving code between packages.

Example:
```javascript
import { helper } from "some-package/internal/helper.js";  // fails if "exports" doesn't expose this subpath
```

Check: Do not: assuming a.
