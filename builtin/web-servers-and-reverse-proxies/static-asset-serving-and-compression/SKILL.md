---
name: static-asset-serving-and-compression
description: "Use when \"static asset serving and compression\" is the work."
---

# Static Asset Serving and Compression

setting a long max-age on.

1. Do not: setting a long max-age on assets without content-hashed filenames, causing users to be stuck.
2. Do not: not verifying byte-range request support for video/audio files, breaking seeking functionality for media players.

Example:
```bash
nginx -T 2>/dev/null || caddy adapt --config <file> | head -40
```

Check: Do not: setting a.
