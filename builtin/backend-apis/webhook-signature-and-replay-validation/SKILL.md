---
name: webhook-signature-and-replay-validation
description: "Use when \"webhook signature and replay validation\" is the work. Verify signatures over raw bytes and enforce timestamp windows and deduplication before side effects."
---

# Webhook Signature and Replay Validation

Verify signatures over raw bytes and enforce timestamp windows and deduplication before side effects.

1. Define request, response, error, and authorization contracts.
2. Validate untrusted inputs at boundaries.
3. Test normal, malformed, unauthorized, duplicate, and concurrent requests against the actual service stack.

Example:
```text
Define request, response, error, and authorization contracts.
```

Check: Check object-level authorization, stable pagination, status semantics, replay windows, and backward compatibility with real contract fixtures.
