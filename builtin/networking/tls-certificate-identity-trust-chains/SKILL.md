---
name: tls-certificate-identity-trust-chains
description: "Use when \"tls certificate identity trust chains\" is the work. Certificate-chain validation and hostname checking serve different purposes."
---

# TLS Certificate Identity & Trust Chains

Certificate-chain validation and hostname checking serve different purposes.

1. Write what the fixture should show before you run it.
2. Run it on the installed runtime and compare the output.
3. Keep the boundary case in its own run.

Example:
```python
import ssl
context = ssl.create_default_context()
assert context.check_hostname is True
```

Check: Do not edit the assert to match a surprising result.
