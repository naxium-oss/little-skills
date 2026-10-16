---
name: reactivity-system-ref-reactive-and-unwrapping
description: "Use when \"reactivity system ref reactive and unwrapping\" is the work. destructuring a reactive() object directly and losing reactive tracking."
---

# Reactivity System: ref, reactive, and Unwrapping

destructuring a reactive() object directly and losing reactive tracking.

1. Do not: destructuring a reactive() object directly and losing reactive tracking.
2. Do not: reassigning a whole reactive object (state = {...}) instead of mutating its properties, which.

Example:
```javascript
import { reactive, toRefs } from "vue";
const state = reactive({ count: 0, name: "app" });
```

Check: Do not: destructuring a reactive() object directly and losing reactive tracking.
