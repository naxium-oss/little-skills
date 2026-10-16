---
name: tls-termination-and-certificate-configuration
description: "Use when \"tls termination and certificate configuration\" is the work. serving only the leaf certificate without the intermediate chain, causing some clients/validators to fail trust verification while browsers."
---

# TLS Termination and Certificate Configuration

serving only the leaf certificate.

1. Do not: serving only the leaf certificate without the intermediate chain, causing some clients/validators to fail.
2. Do not: renewing a certificate file on disk without reloading the proxy process, continuing to serve.

Example:
```bash
nginx -T 2>/dev/null || caddy adapt --config <file> | head -40
```

Check: Do not: serving only the leaf certificate without the.
