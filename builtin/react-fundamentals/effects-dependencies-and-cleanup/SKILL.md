---
name: effects-dependencies-and-cleanup
description: "Use when \"effects dependencies and cleanup\" is the work. omitting a dependency to stop it from re-running, which instead captures a stale closure over old props/state."
---

# Effects, Dependencies, and Cleanup

omitting a dependency to "stop it from re-running,".

1. Do not: omitting a dependency to "stop it from re-running," which instead captures a stale closure.
2. Do not: forgetting cleanup, causing duplicate subscriptions or state updates on unmounted components.

Example:
```javascript
useEffect(() => {
```

Check: Do not: omitting a dependency to "stop it from re-running," which instead captures a stale closure over old.
