---
name: scroll-sites
description: "Use when \"scroll site\", \"scrollytelling\", or \"scroll narrative\". Not when the page is a normal document."
---

# Scroll sites

One scene per viewport, driven by native scroll.

1. Pin each scene to a viewport. Do not fake the scrollbar.
2. Drive motion from scroll position, not from a timer.
3. Provide pause, reduced motion, and captions.

Example:
```text
Scene 2 starts when scroll reaches 100vh. Autoplay stays off.
```

Check: A scroll site that ignores reduced motion is not done.
