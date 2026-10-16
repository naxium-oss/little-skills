# Node.js Runtime Fundamentals

## Node Version and LTS Grounding
Node's runtime behavior (V8 version, built-in modules, permission model) is tied to its exact release; always verify the running version and whether it's an LTS ("Active"/"Maintenance") or Current release before depending on a feature like `fetch`, `test runner`, or `--watch`.
```bash
node --version                        # v22.11.0
node -p "process.release.lts"         # 'Iron' or undefined if Current
node -p "process.versions"
```
Check the official Node.js release schedule page for the exact EOL date of the version in production, since running an EOL version silently loses security patches.
**Pitfalls:** assuming a feature landed in a version because it exists in the *latest* Node docs, without checking when it was introduced relative to the pinned version.

## Event Loop Phases and Non-Blocking I/O
Node's event loop has distinct phases (timers, pending callbacks, poll, check, close callbacks) plus microtasks (Promises) and `process.nextTick` running between phases. Blocking the loop with synchronous CPU work stalls all concurrent requests.
```javascript
const fs = require("node:fs");
fs.readFile("big.json", "utf8", (err, data) => {   // non-blocking
  if (err) throw err;
  console.log(JSON.parse(data).length);
});
// fs.readFileSync would block the entire event loop until done
```
Profile with `node --prof` or `clinic.js` to confirm suspected event-loop blocking rather than assuming from code review alone; use `perf_hooks.monitorEventLoopDelay()` for production lag detection.
**Pitfalls:** using synchronous filesystem/crypto calls (`readFileSync`, `execSync`) in a request handler; scheduling recursive `process.nextTick` calls that starve I/O.

## Built-in Test Runner and Module System
Node ships a built-in test runner (`node:test`) and assertion module (`node:assert`) since v18+, removing the need for external frameworks in simple projects; verify feature parity (mocking, coverage flags) against the installed version before relying on it for CI.
```javascript
import { test } from "node:test";
import assert from "node:assert/strict";

test("adds numbers", () => {
  assert.equal(1 + 1, 2);
});
```
```bash
node --test --experimental-test-coverage
```
Confirm whether `--experimental-test-coverage` or watch-mode flags are stable or experimental in the exact version pinned, since experimental flags can change behavior between minors.
**Pitfalls:** assuming built-in test runner mocking (`t.mock`) matches Jest/Sinon APIs; running `--test` against files that don't match the default `*.test.js` glob and getting zero tests silently.

## Streams and Backpressure
Node Streams (Readable, Writable, Duplex, Transform) model data as chunks flowing over time; ignoring backpressure signals (`write()` returning `false`) can exhaust memory when producers outpace consumers.
```javascript
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream("input.log"),
  createGzip(),
  createWriteStream("input.log.gz")
);
```
Prefer `pipeline`/`stream/promises` over manual `.pipe()` chains so errors and backpressure propagate correctly; verify large-file behavior under real load rather than small test fixtures alone.
**Pitfalls:** chaining `.pipe()` without error handling on each stream, causing unhandled 'error' events to crash the process; buffering an entire stream into memory with `on('data')` collection instead of processing chunk-by-chunk.

## Environment Configuration and Secrets
Node reads configuration from `process.env`, `.env` files (native support since v20.6 via `--env-file`, or via `dotenv`), and CLI flags; verify precedence order and which mechanism is actually active in production versus local dev.
```bash
node --env-file=.env.production server.js
```
```javascript
const port = Number(process.env.PORT ?? 3000);
if (!process.env.DATABASE_URL) {
  throw new Error("DATABASE_URL is required");
}
```
Confirm secrets are never logged or committed by checking `.gitignore` coverage and grepping recent commits for accidental `.env` inclusion.
**Pitfalls:** assuming `dotenv` auto-loads without explicit `import "dotenv/config"`; hardcoding fallback secrets that silently work in dev and mask missing production config.

## Package Scripts and Process Management
`package.json` scripts define the project's canonical entry points (`start`, `build`, `test`); verify what a script actually runs by reading it, not assuming from its name, since teams override defaults.
```json
{
  "scripts": {
    "dev": "node --watch src/server.js",
    "start": "NODE_ENV=production node dist/server.js"
  }
}
```
In production, use a process manager (`pm2`, systemd, or a container orchestrator) for restart-on-crash behavior instead of relying on `node` alone, and verify graceful shutdown handling (`SIGTERM`) closes DB connections before exit.
**Pitfalls:** relying on `npm start` restarting automatically on crash with no supervisor configured; ignoring `SIGTERM` and having the orchestrator hard-kill (`SIGKILL`) mid-request.

## Node's Module Resolution Algorithm
Node resolves `require`/`import` specifiers through a documented algorithm, relative paths resolve to the filesystem directly, bare specifiers walk up `node_modules` directories, and a package's `"exports"` field (if present) restricts which subpaths are importable, overriding the historical "import anything in the package" behavior. Verify actual resolution with `node --experimental-specifier-resolution` diagnostics or by reading the target package's `package.json` `"exports"` map rather than assuming any file in the package tree is reachable.
```javascript
import { helper } from "some-package/internal/helper.js";  // fails if "exports" doesn't expose this subpath
```
```bash
node -e "console.log(require.resolve('some-package'))"
```
**Pitfalls:** assuming a deep-import path that worked in an older version of a dependency still resolves after it adopted an `"exports"` map that hides internal paths; mixing relative and bare-specifier assumptions when moving code between packages.

## Node Cluster and Worker Threads for Scaling
Node's single-threaded event loop bottlenecks on CPU-bound work and cannot use multiple cores within one process; `cluster` forks multiple processes sharing a listening socket for I/O-bound scaling, while `worker_threads` runs actual parallel JS threads (with `SharedArrayBuffer` for shared memory) suited to CPU-bound tasks. Verify which one matches the actual bottleneck before adding either, since both add operational complexity (inter-process/thread communication, graceful shutdown coordination).
```javascript
import { Worker, isMainThread, parentPort } from "node:worker_threads";
if (isMainThread) {
  const worker = new Worker(new URL(import.meta.url));
  worker.once("message", (result) => console.log("computed:", result));
} else {
  parentPort.postMessage(heavyComputation());
}
```
**Pitfalls:** reaching for `cluster` to solve a CPU-bound bottleneck when `worker_threads` is the correct tool, since cluster only multiplies I/O-handling capacity, not per-request CPU parallelism; forgetting worker threads have separate memory by default, requiring explicit message passing or `SharedArrayBuffer` for shared state.

# Bun Runtime Fundamentals

## Bun Version and Compatibility Grounding
Bun reimplements the JS runtime, package manager, bundler, and test runner in one binary; Node API compatibility is high but not complete, and behavior differs by exact Bun version. Always verify against the installed build.
```bash
bun --version                 # 1.1.34
bun -e "console.log(process.versions.bun)"
```
Check Bun's official "Node.js compatibility" page for the exact release before assuming a Node built-in module (e.g., `node:cluster`, `worker_threads` edge cases) is fully supported.
**Pitfalls:** assuming full Node API parity for less common modules; shipping to production without testing under the exact Bun version pinned in CI.

## Bun as Package Manager: Install and Lockfile
`bun install` resolves and installs dependencies significantly faster than npm/yarn by using a binary lockfile (`bun.lock` or the older `bun.lockb`) and a global cache. Verify the lockfile format matches what your CI expects.
```bash
bun install
bun install --frozen-lockfile     # CI: fail if lockfile would change
bun pm ls                          # list resolved deps like `npm ls`
```
Confirm `bun.lock`/`bun.lockb` is committed and that teammates aren't mixing `npm install` and `bun install` in the same repo, which produces conflicting lockfiles and version drift.
**Pitfalls:** running `npm install` in a Bun project and overwriting `bun.lockb` implicitly via a stray `package-lock.json`; assuming `bunfig.toml` registry overrides apply retroactively to an existing lockfile without reinstalling.

## Bun's Built-in APIs: Bun.serve, Bun.file, Bun.$
Bun exposes fast native APIs beyond Node compatibility: `Bun.serve` for HTTP servers, `Bun.file` for zero-copy file reads, and `Bun.$` for shell scripting without spawning subprocess boilerplate.
```javascript
const server = Bun.serve({
  port: 3000,
  fetch(req) {
    return new Response("hello from bun");
  },
});

const text = await Bun.file("config.json").text();

import { $ } from "bun";
const branch = (await $`git rev-parse --abbrev-ref HEAD`.text()).trim();
```
Verify `Bun.serve` routing/middleware conventions against the installed version's docs, since the API has evolved across releases (e.g., native routing objects added later).
**Pitfalls:** porting Express middleware directly assuming identical request/response objects; using `Bun.$` shell templating with unsanitized user input, risking injection just like any shell call.

## Native TypeScript and JSX Execution
Bun executes `.ts`/`.tsx` files directly without a separate build step for development, using its own fast transpiler; it does not perform type-checking (only syntax transformation), so `tsc --noEmit` is still required for type safety.
```bash
bun run src/index.tsx
bunx tsc --noEmit         # separate type-check pass
```
Confirm project `tsconfig.json` target/JSX settings align with what Bun's transpiler expects, and don't assume Bun enforces `strict` mode errors, it will happily run type-invalid code.
**Pitfalls:** treating a successful `bun run` as proof of type safety; relying on decorators or TS features Bun's transpiler doesn't yet support without checking the changelog.

## Bun Test Runner and Jest-Compatible API
`bun test` provides a fast, built-in test runner with a Jest-like API (`describe`, `it`, `expect`), snapshot testing, and mocking; verify which Jest matchers are actually implemented before porting an existing Jest suite wholesale.
```javascript
import { describe, it, expect, mock } from "bun:test";

describe("sum", () => {
  it("adds two numbers", () => {
    expect(1 + 1).toBe(2);
  });
});

const fn = mock(() => 42);
```
Run the full existing Jest suite under `bun test` in CI before switching permanently, checking for matcher gaps or differing snapshot formats.
**Pitfalls:** assuming full Jest plugin/reporter ecosystem compatibility; snapshot files generated by Jest and Bun may not be interchangeable.

## Bundling and Building Standalone Executables
`bun build` bundles JS/TS for the browser or Node, and `bun build --compile` produces a single standalone executable embedding the runtime, useful for CLI distribution without requiring Node/Bun installed on target machines.
```bash
bun build ./src/index.ts --outdir ./dist --target browser --minify
bun build ./cli.ts --compile --outfile mycli
```
Verify the target platform/architecture of a compiled executable (`--target=bun-linux-x64`, etc.) matches the deployment environment, since cross-compiled binaries must be tested on the actual target OS.
**Pitfalls:** assuming a `--compile` binary built on macOS runs on a Linux container without cross-target flags; missing native addons that don't bundle correctly into a single binary.

## Workspaces and Monorepo Support
Bun supports npm-style workspaces natively for monorepos, resolving internal package references without publishing, and can run scripts across workspaces with filtering.
```json
{ "name": "root", "workspaces": ["packages/*"] }
```
```bash
bun install
bun --filter "./packages/api" run build
```
Verify workspace protocol resolution (`workspace:*`) behavior matches expectations by inspecting `node_modules` symlinks after install, especially when mixing Bun with tools that expect npm/pnpm-style hoisting.
**Pitfalls:** assuming pnpm-specific workspace features (like strict dependency isolation) apply identically under Bun; forgetting to re-run install after adding a new workspace package.

## Environment Variables and .env Handling
Bun automatically loads `.env`, `.env.local`, and mode-specific files (`.env.production`) without extra packages, exposing values via `process.env` and also `Bun.env`. Verify load order and precedence against the official docs for the installed version.
```javascript
console.log(Bun.env.API_KEY, process.env.API_KEY); // both populated
```
```bash
bun run --env-file=.env.staging src/index.ts
```
Confirm no conflicting `dotenv` package is also loading and silently overriding values, which can cause confusing precedence bugs when migrating an existing Node project to Bun.
**Pitfalls:** keeping a `dotenv` import from a ported Node codebase that double-loads env vars with different precedence than Bun's native loader.
