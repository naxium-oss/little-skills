---
name: html-templates-slots-and-custom-elements
description: "Use when \"html templates slots and custom elements\" is the work. assuming global CSS resets apply inside shadow roots."
---

# HTML Templates, Slots, and Custom Elements

assuming global CSS resets apply inside shadow roots.

1. Do not: assuming global CSS resets apply inside shadow roots.
2. Do not: forgetting customElements.define must run before the tag is parsed, or upgrading won't happen until.

Example:
```html
<template id="card-template">
<style>.card { border: 1px solid #ccc; padding: 1rem; }</style>
```

Check: Do not: assuming global CSS resets apply inside shadow roots.
