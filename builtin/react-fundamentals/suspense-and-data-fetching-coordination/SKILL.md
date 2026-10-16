---
name: suspense-and-data-fetching-coordination
description: "Use when \"suspense and data fetching coordination\" is the work. assuming any async useEffect-based data fetch automatically integrates with a wrapping Suspense boundary without the library explicitly supporting."
---

# Suspense and Data-Fetching Coordination

assuming any async useEffect-based data.

1. Do not: assuming any async useEffect-based data fetch automatically integrates with a wrapping Suspense boundary without.
2. Do not: not testing fallback UI on fast networks, shipping a jarring flash-of-loading-state on every navigation.

Example:
```jsx
const ProfilePage = React.lazy(() => import("./ProfilePage"));
```

Check: Do not: assuming any async useEffect-based data fetch automatically.
