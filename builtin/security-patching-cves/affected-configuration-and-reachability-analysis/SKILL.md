---
name: affected-configuration-and-reachability-analysis
description: "Use when \"affected configuration and reachability analysis\" is the work. Trace untrusted input to the vulnerable code under the deployed configuration and mitigations."
---

# Affected Configuration and Reachability Analysis

Trace untrusted input to the vulnerable code under the deployed configuration and mitigations.

1. Cross-check vendor advisories and independent databases with retrieval dates.
2. Map affected ranges to the deployed artifact including backports.
3. Assess configuration and reachability before applying the smallest supported remediation.

Example:
```text
Cross-check vendor advisories and independent databases with retrieval dates.
```

Check: Reproduce only in an authorized isolated environment; validate patch effectiveness and compatibility; track exceptions with owners and expiry.
