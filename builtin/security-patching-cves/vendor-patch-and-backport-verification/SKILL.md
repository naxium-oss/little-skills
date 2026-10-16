---
name: vendor-patch-and-backport-verification
description: "Use when \"vendor patch and backport verification\" is the work. Verify signed vendor packages, backport patch identifiers, and changelog evidence for the exact build."
---

# Vendor Patch and Backport Verification

Verify signed vendor packages, backport patch identifiers, and changelog evidence for the exact build.

1. Cross-check vendor advisories and independent databases with retrieval dates.
2. Map affected ranges to the deployed artifact including backports.
3. Assess configuration and reachability before applying the smallest supported remediation.

Example:
```text
Cross-check vendor advisories and independent databases with retrieval dates.
```

Check: Reproduce only in an authorized isolated environment; validate patch effectiveness and compatibility; track exceptions with owners and expiry.
