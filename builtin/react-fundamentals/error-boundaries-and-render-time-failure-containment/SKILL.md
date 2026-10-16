---
name: error-boundaries-and-render-time-failure-containment
description: "Use when \"error boundaries and render time failure containment\" is the work. assuming an error boundary catches all errors anywhere in the app, including those thrown inside onClick handlers or."
---

# Error Boundaries and Render-Time Failure Containment

assuming an error boundary catches.

1. Do not: assuming an error boundary catches all errors anywhere in the app, including those thrown.
2. Do not: placing only one boundary at the very root, causing any single component's render error.

Example:
```jsx
class ErrorBoundary extends React.Component {
```

Check: Do not: assuming an error boundary catches all errors anywhere in the app, including those thrown inside onClick.
