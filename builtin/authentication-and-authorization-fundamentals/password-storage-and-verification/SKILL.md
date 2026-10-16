---
name: password-storage-and-verification
description: "Use when \"password storage and verification\" is the work. using fast general-purpose hashes (MD5, SHA-256 alone) for passwords, making brute-force trivial with GPUs."
---

# Password Storage and Verification

using fast general-purpose hashes (MD5, SHA-256 alone).

1. Do not: using fast general-purpose hashes (MD5, SHA-256 alone) for passwords, making brute-force trivial with GPUs.
2. Do not: hardcoding a cost factor once and never revisiting it as hardware gets faster.

Example:
```bash
identify the token format and expiry policy from config, not memory
```

Check: Do not: using fast.
