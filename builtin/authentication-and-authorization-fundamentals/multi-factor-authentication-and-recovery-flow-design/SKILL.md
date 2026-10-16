---
name: multi-factor-authentication-and-recovery-flow-design
description: "Use when \"multi factor authentication and recovery flow design\" is the work."
---

# Multi-Factor Authentication and Recovery Flow Design

treating SMS-based MFA as equivalent in strength to.

1. Do not: treating SMS-based MFA as equivalent in strength to TOTP/WebAuthn when designing threat models for.
2. Do not: implementing a recovery flow that doesn't require re-verification of identity, effectively creating a backdoor.

Example:
```bash
identify the token format and expiry policy from config, not memory
```

Check: Do not: treating SMS-based.
