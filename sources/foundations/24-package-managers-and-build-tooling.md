# Package Managers & Build Tooling

## Lockfile Semantics Across Package Managers
npm, Yarn (classic/Berry), pnpm, and language-specific managers (pip, cargo, bundler) each produce lockfiles with different resolution algorithms and guarantees; verify which manager and lockfile format a project actually uses, and never mix managers on the same project, since their lockfiles and `node_modules` layouts (flat vs. symlinked/strict) are incompatible.
```bash
ls package-lock.json yarn.lock pnpm-lock.yaml 2>/dev/null   # confirm exactly one is present and current
npm ci     # installs strictly from lockfile, fails if package.json and lockfile disagree
```
Verify CI uses the reproducible install command (`npm ci`, `pnpm install --frozen-lockfile`, `yarn install --immutable`) rather than a mutable `install` command that can silently update the lockfile.
**Pitfalls:** committing both `package-lock.json` and `yarn.lock` after switching tools, causing confusion about which is authoritative; using `npm install` in CI instead of `npm ci`, allowing dependency drift between local dev and CI builds.

## Semantic Versioning and Range Resolution
Semantic Versioning (`MAJOR.MINOR.PATCH`) signals compatibility intent, but range operators (`^`, `~`, `>=`) resolve differently and a dependency author can still ship a breaking change under a minor/patch bump by mistake; verify the actual resolved version installed (not just the declared range) before assuming compatibility.
```json
{ "dependencies": { "left-pad": "^1.3.0" } }
```
```bash
npm ls left-pad          # shows actually-resolved version, which may differ from the range's minimum
```
Pin exact versions for critical infrastructure dependencies where an unexpected transitive update could cause outages, and verify changelogs for the actual delta between the previously installed and newly resolved version during upgrades.
**Pitfalls:** assuming `^1.3.0` guarantees safety from breaking changes, when the maintainer violates semver (common in practice) with a minor/patch release; never checking `npm outdated`/`npm ls`, missing that a wide-open range has silently pulled in a much newer major-adjacent version transitively.

## Monorepo Workspaces and Dependency Hoisting
Workspace tools (npm/Yarn/pnpm workspaces, Turborepo, Nx) hoist shared dependencies to a root `node_modules` to avoid duplication, but hoisting behavior differs (pnpm uses strict symlinked isolation by default, npm/Yarn classic hoist more permissively), verify actual module resolution with a deliberate import test rather than assuming a package is available just because it's hoisted somewhere in the tree.
```bash
pnpm why some-package         # trace exactly which workspace package depends on it and why it resolved where it did
npm ls some-package --workspaces
```
Confirm a package doesn't accidentally work locally only because of permissive hoisting (a "phantom dependency" not actually declared in its own `package.json`), which would break once hoisting order changes or the project switches to strict pnpm-style isolation.
**Pitfalls:** importing a package that resolves successfully only due to hoisting from a sibling workspace's dependency, without declaring it directly, a "phantom dependency" that breaks unpredictably; running build scripts without configuring task-graph caching (Turborepo/Nx), rebuilding unaffected packages on every change.

## Build Tool Transformation Pipelines (Vite/webpack/esbuild)
Modern build tools (Vite, webpack, esbuild, Rollup) transform, bundle, and optimize source code through configurable pipelines (plugins, loaders); verify the actual applied transformation chain and its order, since plugin ordering changes output (e.g., a CSS preprocessor plugin must run before a minifier plugin sees the CSS).
```javascript
// vite.config.ts
export default defineConfig({
  plugins: [react(), svgr()],
  build: { target: "es2020", sourcemap: true },
});
```
Verify production build output (`dist/`) actually reflects intended optimizations (minification, tree-shaking, code-splitting) by inspecting the built bundle directly, not just trusting the dev-server behavior, since dev and production pipelines often diverge significantly.
**Pitfalls:** assuming dev-server behavior (unminified, unbundled, HMR-enabled) predicts production build output correctness, missing production-only bugs (tree-shaking removing a side-effectful import); misordering plugins so a transform runs on already-transformed (or not-yet-transformed) code, causing subtle build artifacts.

# Regular Expressions Mastery

## Regex Engine and Flavor Compatibility
Regex syntax varies meaningfully across engines (POSIX BRE/ERE, PCRE, JavaScript's engine, Python's `re`/`regex`, RE2), features like lookbehind, named groups, and possessive quantifiers aren't universally supported (notably RE2 and older JS engines lack backreferences/lookbehind for performance/security reasons). Verify the actual regex engine and its supported feature set before assuming portability.
```python
import re
match = re.search(r"(?<=\$)\d+(\.\d{2})?", "Price: $42.50")   # lookbehind: supported in Python re, not in RE2
```
```javascript
/(?<year>\d{4})-(?<month>\d{2})/.exec("2025-06")   // named groups: ES2018+, verify target runtime support
```
**Pitfalls:** writing a lookbehind-based regex intended for a Go service using RE2 (which doesn't support lookbehind at all), causing a compile-time error; assuming a regex tested in one language's REPL behaves identically when ported to another language's regex engine.

## Catastrophic Backtracking and ReDoS Prevention
Certain regex patterns (nested quantifiers over overlapping character classes, like `(a+)+b`) exhibit exponential worst-case backtracking on crafted input, causing a Regular Expression Denial of Service (ReDoS) when applied to untrusted input; verify a regex's worst-case behavior with a deliberately adversarial test input and a timeout, not just typical inputs.
```python
import re, time

pattern = re.compile(r"^(a+)+$")   # classic ReDoS-vulnerable pattern
malicious = "a" * 30 + "!"
start = time.perf_counter()
# pattern.match(malicious)  # would hang for an extremely long time on a vulnerable engine
```
Test any regex applied to user-supplied input (URLs, emails, form fields) against known ReDoS attack patterns, and prefer atomic groups/possessive quantifiers or a non-backtracking engine (RE2) for untrusted input paths.
**Pitfalls:** validating user input (email, URL) with a regex copied from an untrusted source without testing its worst-case backtracking behavior; using an unbounded nested quantifier pattern on any endpoint reachable by unauthenticated users.

## Greedy versus Lazy Quantifiers
`*`/`+`/`{n,m}` are greedy by default (match as much as possible, then backtrack), while appending `?` makes them lazy (match as little as possible); verify actual match boundaries with a test string containing multiple potential match points, since greedy vs. lazy produces different results on ambiguous input, not just different performance.
```python
import re
text = "<b>bold</b> and <i>italic</i>"
print(re.findall(r"<.+>", text))    # greedy: matches from first < to LAST >, spanning both tags
print(re.findall(r"<.+?>", text))   # lazy: matches each tag individually
```
Verify with the exact target string containing repeated delimiters, since greedy/lazy behavior only diverges visibly when there's more than one potential match boundary in the input.
**Pitfalls:** using a greedy `.+`/`.*` to match "up to the next delimiter" and unintentionally matching across multiple delimiters to the last occurrence instead of the nearest; assuming lazy quantifiers are always "more correct," when greedy is actually intended for some patterns (e.g., matching the longest valid token).

## Capture Groups, Non-Capturing Groups, and Replacement
Capturing groups `(...)` extract sub-matches and are numbered by order of opening parenthesis (nesting affects numbering); non-capturing groups `(?:...)` group for alternation/quantification without creating a numbered capture, keeping group indices predictable in complex patterns. Verify actual group numbering with a test against the target regex library, since group-counting mistakes silently reference the wrong captured text.
```python
import re
m = re.match(r"(?:https?://)?(?P<host>[\w.-]+)(?::(?P<port>\d+))?", "https://example.com:8080")
print(m.group("host"), m.group("port"))   # named groups avoid fragile positional numbering
```
Prefer named groups (`(?P<name>...)` in Python, `(?<name>...)` in JS/PCRE) over positional numbering in any pattern with more than two or three groups, since refactoring a pattern's group order silently breaks positional references.
**Pitfalls:** adding a new capturing group to an existing pattern and breaking every downstream `\1`/`group(2)` reference due to renumbering; forgetting `(?:...)` for a purely structural group, cluttering match results with unwanted captured substrings.

# Package Managers & Build Tooling

## Python Packaging Ecosystem: pip, Poetry, and uv
Python's packaging tooling has fragmented into multiple tools with different resolution algorithms and lockfile formats (`pip` + `requirements.txt`, Poetry's `poetry.lock`, the newer high-performance `uv`); verify which tool a project actually uses and its exact version before running installation commands, since mixing tools on the same project (installing with `pip` into a Poetry-managed virtualenv) causes dependency-tracking drift invisible to either tool.
```bash
uv --version
uv sync --frozen             # install exactly from uv.lock, fail if it would change
poetry check                  # verify pyproject.toml and poetry.lock are consistent
```
Verify a project's lockfile is actually committed and that CI installs from it in a frozen/locked mode rather than a mode that permits silent re-resolution, which would allow dependency drift between local development and CI.
**Pitfalls:** running a bare `pip install package` inside a Poetry- or uv-managed virtualenv, bypassing the lockfile and causing the environment to silently diverge from what's declared; committing `pyproject.toml` changes without regenerating and committing the corresponding lockfile, leaving them out of sync.

## Native Extension and Binary Dependency Builds
Some packages (numpy, cryptography, native Node addons) require compiling native code during installation unless a prebuilt wheel/binary matching the exact platform and architecture is available; verify build toolchain prerequisites (a C compiler, Python headers, Rust toolchain) are actually present before assuming an installation failure is a packaging bug rather than a missing system dependency.
```bash
pip install cryptography --verbose 2>&1 | grep -i "building wheel\|error"
node-gyp rebuild --verbose
```
Verify prebuilt wheel availability for the exact target platform (`manylinux` tags, macOS universal2, Windows) with `pip download --no-deps` before deploying to a new platform, since a package with excellent prebuilt wheel coverage on Linux x86_64 might force a slow/fragile source build on a less common architecture.
**Pitfalls:** deploying to a new CPU architecture (ARM-based cloud instances, Apple Silicon) without verifying prebuilt wheels exist, causing unexpectedly slow or failing builds during deployment; assuming a "successful" local build on a developer machine with build tools installed will also succeed in a minimal production container lacking the same toolchain.

## Vendoring and Dependency Bundling Tradeoffs
Vendoring copies a dependency's source directly into a project's repository rather than fetching it via a package manager, trading automatic update convenience for full control and resilience against upstream package removal/compromise; verify a vendoring decision is deliberate and documented (with a clear update process) rather than an accidental result of copy-pasting code without attribution or a plan to receive security patches.
```bash
go mod vendor                     # Go's built-in, well-supported vendoring workflow
git subtree add --prefix=vendor/some-lib https://github.com/org/some-lib.git v2.3.1 --squash
```
Verify vendored code's license compliance is tracked (vendoring doesn't remove licensing obligations) and that a process exists for periodically checking upstream for security patches, since vendored code doesn't automatically receive them like a package-manager-tracked dependency would.
**Pitfalls:** vendoring a dependency once and never revisiting it for security updates, silently running an increasingly outdated and vulnerable copy indefinitely; vendoring code without preserving license/attribution information, creating compliance risk.

## Build Reproducibility and Hermetic Builds
A hermetic build produces identical output given identical inputs, independent of the host machine's installed tools/environment beyond what's explicitly declared; verify a build is actually hermetic by attempting it in a clean container with only declared dependencies present, since a build that "just works" on a developer's machine may implicitly depend on a globally installed tool version never declared anywhere.
```dockerfile
FROM node:22.11.0-bookworm-slim
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci                     # hermetic: only lockfile-declared dependencies, no implicit global tools
COPY . .
RUN npm run build
```
Verify build output byte-for-byte (or at least functionally) matches across repeated builds on different machines/times by comparing checksums of build artifacts, catching hidden non-determinism (embedded timestamps, unordered file globbing) that undermines reproducibility claims.
**Pitfalls:** relying on a globally installed tool version (a system Python, a global npm package) that isn't declared anywhere in the project, causing builds to succeed on one machine and mysteriously fail on another; embedding build timestamps or unordered directory listings in build output, breaking bit-for-bit reproducibility verification.

# Regular Expressions Mastery

## Anchors, Boundaries, and Multiline Matching
Anchors (`^`, `$`) and word boundaries (`\b`) constrain where a match can occur, but their behavior changes with multiline (`m`) and dotall (`s`) flags, verify the exact flag combination in use, since `^`/`$` match start/end of the whole string by default in most engines but start/end of each line when the multiline flag is set, a frequent source of unexpected partial matches.
```python
import re
text = "line one\nline two"
print(re.findall(r"^line", text))              # ['line'], matches only at string start by default
print(re.findall(r"^line", text, re.MULTILINE)) # ['line', 'line'], matches at start of each line
```
Verify `\b` word-boundary behavior with actual target strings containing Unicode word characters, since boundary detection can behave unexpectedly with non-ASCII text depending on the engine's Unicode-awareness configuration.
**Pitfalls:** assuming `^`/`$` always match line boundaries without checking whether the multiline flag is actually set for the specific engine call; using `\b` on Unicode text without verifying the engine's Unicode word-character definition matches the target language's actual word boundaries.

## Character Classes, Unicode Properties, and Escaping
Character classes (`[...]`) and Unicode property escapes (`\p{L}` for any letter, `\p{N}` for any number) let patterns match categories of characters portably across scripts/languages, but verify actual engine support for Unicode properties (not universally available, some engines require a specific flag or don't support them at all) before relying on them for internationalized text validation.
```javascript
const namePattern = /^[\p{L}\p{M}'\- ]+$/u;   // requires the 'u' flag in JavaScript for Unicode property escapes
console.log(namePattern.test("François"));     // true
```
Verify special characters intended literally (`.`, `*`, `(`, `)`) are properly escaped when building a pattern from dynamic/user-supplied text, using the language's built-in escaping utility rather than manual, error-prone escaping.
**Pitfalls:** forgetting the Unicode flag (`u` in JavaScript) required for `\p{...}` property escapes to work at all, causing a silent pattern compilation error or unexpected literal interpretation; building a regex dynamically by string-concatenating unescaped user input, both breaking the intended pattern and creating a potential ReDoS/injection vector.

## Multiline Parsing and the Limits of Regex for Structured Data
Regex is well-suited to matching well-defined, non-recursive lexical patterns (emails, dates, log line prefixes) but poorly suited to parsing recursively nested or context-sensitive structures (balanced parentheses, full JSON/HTML/XML), verify a problem doesn't actually require a real parser before forcing an increasingly complex, brittle regex to handle nested structure it fundamentally cannot express correctly in the general case.
```python
# Fragile: regex cannot correctly handle arbitrarily nested parentheses in the general case
import re
naive_pattern = re.compile(r"\(([^()]*)\)")  # only handles one level of nesting correctly

# Correct approach for genuinely nested/recursive structure: use a real parser
import json
data = json.loads(json_text)
```
Verify a chosen regex-based "parser" is only ever applied to genuinely flat, bounded-complexity text, and switch to an actual grammar-based parser (or an existing format's official parser library) the moment nesting or context-sensitivity is discovered in real input samples.
**Pitfalls:** attempting to parse HTML, JSON, or another recursively nested format with an increasingly complicated regex instead of using an actual parser, producing subtly incorrect results on real-world edge cases; not recognizing when a "one more special case" regex fix is actually evidence the problem needs a fundamentally different parsing approach.

## Regex Performance Profiling and Precompilation
Regex compilation has real cost, verify patterns used repeatedly (in a loop, per-request in a server) are precompiled once and reused rather than recompiled from a string literal on every invocation, since most engines cache a small number of compiled patterns internally but this caching behavior shouldn't be relied upon for hot-path performance.
```python
import re

EMAIL_PATTERN = re.compile(r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$")   # compiled once, at module load time

def is_valid_email(s: str) -> bool:
    return bool(EMAIL_PATTERN.match(s))   # reuses the precompiled pattern on every call
```
Profile actual regex performance in a hot path with realistic input volume and length distributions before assuming a pattern is fast enough, since worst-case backtracking behavior only appears with specific adversarial or unusually long inputs that typical test cases may not include.
**Pitfalls:** recompiling the same regex pattern from a string literal inside a hot loop or per-request handler instead of precompiling it once at module scope; testing regex performance only with short, typical inputs and missing catastrophic backtracking behavior that only manifests on longer or adversarial input.
