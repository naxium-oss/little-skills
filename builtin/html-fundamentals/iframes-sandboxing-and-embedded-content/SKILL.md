---
name: iframes-sandboxing-and-embedded-content
description: "Use when \"iframes sandboxing and embedded content\" is the work. combining allow-scripts and allow-same-origin carelessly, which together can let sandboxed content escape the sandbox by rewriting its own."
---

# Iframes, Sandboxing, and Embedded Content

combining allow-scripts and allow-same-origin.

1. Do not: combining allow-scripts and allow-same-origin carelessly, which together can let sandboxed content escape the sandbox.
2. Do not: embedding third-party iframes without referrerpolicy, leaking referrer URLs.

Example:
```html
<iframe
```

Check: Do not: combining allow-scripts and allow-same-origin carelessly, which together.
