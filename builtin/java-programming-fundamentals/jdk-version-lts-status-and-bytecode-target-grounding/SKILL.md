---
name: jdk-version-lts-status-and-bytecode-target-grounding
description: "Use when \"jdk version lts status and bytecode target grounding\" is the work."
---

# JDK Version, LTS Status, and Bytecode

using a preview feature.

1. Do not: using a preview feature (--enable-preview required) in production code without noting it's not yet.
2. Do not: assuming a feature available in the latest LTS is available in an older LTS.

Example:
```xml
<properties><maven.compiler.release>21</maven.compiler.release></properties>
```

Check: Do not: using a.
