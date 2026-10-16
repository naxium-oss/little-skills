---
name: computed-properties-versus-watchers
description: "Use when \"computed properties versus watchers\" is the work. using watch to manually recompute a derived value instead of computed, causing redundant renders/logic."
---

# Computed Properties versus Watchers

using watch to manually recompute a derived.

1. Do not: using watch to manually recompute a derived value instead of computed, causing redundant renders/logic.
2. Do not: forgetting { deep: true } when watching a nested object mutation that isn't reassigned.

Example:
```javascript
const fullName = computed(() => `${first.value} ${last.value}`);
```

Check: Do not: using watch to manually recompute a derived value instead of computed, causing redundant renders/logic.
