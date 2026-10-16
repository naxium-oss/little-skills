---
name: net-runtime-version-and-sdk-grounding
description: "Use when \"net runtime version and sdk grounding\" is the work. using a C# 12 language feature in a project whose .csproj doesnt set LangVersion high enough despite a."
---

# .NET Runtime Version and SDK Grounding

using a C# 12 language feature in a project whose .csproj.

1. Do not: using a C# 12 language feature in a project whose .csproj doesn't set LangVersion.
2. Do not: assuming a package supports a TFM without checking its actual nuspec target frameworks.

Example:
```bash
dotnet --info
```

Check: Do not: using a C# 12 language feature in a project whose .csproj doesn't set LangVersion high enough.
