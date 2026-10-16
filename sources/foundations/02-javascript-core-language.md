# JavaScript Core Language

## Engine and Specification Version Grounding
JavaScript behavior depends on the ECMAScript edition and the specific engine (V8, JavaScriptCore, SpiderMonkey) executing it. Before relying on a feature like `Array.prototype.toSorted`, `Object.groupBy`, or top-level `await`, confirm the runtime's engine version.
```bash
node --version                     # v22.11.0
node -e "console.log(process.versions.v8)"
node -e "console.log(Object.groupBy ? 'supported' : 'missing')"
```
In browsers, check `navigator.userAgent` and, better, run a feature-detection snippet rather than trusting a User-Agent string, since it can be spoofed or frozen.
**Pitfalls:** assuming a Baseline "widely available" feature works in all target browsers without checking the actual support table date; testing only in one engine and shipping to others.

## Equality, Coercion, and Type Semantics
`==` performs type coercion with surprising rules (`[] == false` is `true`); `===` compares without coercion and should be the default. `Object.is` differs from `===` for `NaN` and `-0`.
```javascript
console.log(NaN === NaN);        // false
console.log(Object.is(NaN, NaN)); // true
console.log(0 === -0);            // true
console.log(Object.is(0, -0));    // false
```
Verify numeric edge cases (`NaN`, `-0`, `Infinity`) explicitly in tests rather than assuming intuitive behavior, especially in financial or scientific code.
**Pitfalls:** using `==` for null checks broadly (`x == null` is idiomatic for null-or-undefined, but confirm the codebase's lint rules allow it); comparing floats for exact equality without an epsilon.

## Closures, Scope, and the Event Loop
`var` is function-scoped and hoisted with `undefined` initialization; `let`/`const` are block-scoped with a temporal dead zone. The event loop processes microtasks (Promises) before macrotasks (`setTimeout`), which affects ordering.
```javascript
console.log("start");
setTimeout(() => console.log("timeout"), 0);
Promise.resolve().then(() => console.log("promise"));
console.log("end");
// Output: start, end, promise, timeout
```
Verify ordering assumptions with an actual run rather than intuition, and check whether `queueMicrotask` or `process.nextTick` (Node-specific, runs before other microtasks) is involved.
**Pitfalls:** assuming `setTimeout(fn, 0)` runs immediately; forgetting `process.nextTick` starves the event loop if recursively scheduled.

## Prototypes, Classes, and `this` Binding
JavaScript classes are syntactic sugar over prototypal inheritance; `this` is determined by call-site, not definition-site, unless bound via arrow functions, `.bind()`, or class fields.
```javascript
class Counter {
  count = 0;
  incrementRegular() { this.count++; }
  incrementArrow = () => { this.count++; };
}
const c = new Counter();
const detachedRegular = c.incrementRegular;
const detachedArrow = c.incrementArrow;
detachedArrow();       // works, `this` bound lexically
// detachedRegular();  // throws or increments undefined.count depending on strict mode
```
Verify `this` behavior with an actual invocation test when passing methods as callbacks (event handlers, `array.map(obj.method)`), a very common source of bugs.
**Pitfalls:** passing `obj.method` directly as a callback without binding; assuming class fields and prototype methods behave identically for memory (class fields allocate per-instance).

## Promises, async/await, and Error Propagation
`async` functions always return a Promise; unhandled rejections can crash Node processes (since v15) or fail silently in browsers. Always attach `.catch()` or wrap in `try/catch`.
```javascript
async function loadUser(id) {
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error("loadUser failed", err);
    throw err;
  }
}
```
Verify `Promise.all` versus `Promise.allSettled` semantics before choosing one: `all` rejects fast on the first failure, dropping other results, while `allSettled` waits for everything.
**Pitfalls:** using `Promise.all` when partial failures should be tolerated; forgetting `await` inside a `.map()` callback, producing an array of pending Promises instead of resolved values.

## Modules: CommonJS vs ESM Interop
Node supports both CommonJS (`require`/`module.exports`) and ECMAScript Modules (`import`/`export`); the `"type"` field in `package.json` and file extensions (`.mjs`/`.cjs`) determine which is used. Interop has real gaps (`require()` of a pure ESM package fails).
```json
{ "type": "module" }
```
```javascript
// works only if the target package ships a CJS build or Node's experimental require(esm)
import pkg from "some-cjs-package";
const { namedExport } = await import("some-esm-only-package");
```
Verify a package's actual exports map (`"exports"` field in its `package.json`) rather than guessing, since dual-package hazards cause duplicate module instances.
**Pitfalls:** mixing `require` and `import` in the same file without a bundler; assuming `import` default interop always matches CJS `module.exports`.

## Array and Object Immutability Patterns
Native methods split into mutating (`push`, `splice`, `sort`) and non-mutating (`concat`, `slice`, `toSorted` in ES2023+), verify which category a method falls into before use, especially with shared references (React state, Redux).
```javascript
const original = [3, 1, 2];
const sorted = [...original].sort();   // pre-ES2023 safe copy
const sortedModern = original.toSorted(); // ES2023+, no copy needed
console.log(original); // [3, 1, 2] unchanged in both cases
```
Confirm `toSorted`/`toReversed`/`toSpliced`/`with` availability in the target runtime before relying on them instead of spread-based copies.
**Pitfalls:** calling `.sort()` directly on state arrays in React/Vue, mutating them in place and breaking change detection; assuming `Object.freeze` is deep (it is shallow).

## Error Objects and Custom Error Hierarchies
Always throw `Error` instances (or subclasses), never plain strings or objects, to preserve stack traces. Custom error classes should call `super(message)` and set `this.name`.
```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
    Error.captureStackTrace?.(this, ValidationError);
  }
}
```
Verify `instanceof` checks work across module boundaries/bundler builds, duplicate copies of a class (from mismatched dependency versions) break `instanceof` even though the error looks identical.
**Pitfalls:** throwing strings (`throw "failed"`) which lose stack traces; catching errors broadly and re-throwing a new error without preserving `cause` (`new Error("wrap", { cause: err })`).

# TypeScript Fundamentals

## Compiler Version and tsconfig Strictness Grounding
TypeScript's checked behavior depends entirely on the installed compiler version and the `tsconfig.json` flags in effect (`strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`). Verify both before asserting whether code "type-checks."
```bash
npx tsc --version              # Version 5.7.2
npx tsc --showConfig           # resolved effective config
```
```json
{ "compilerOptions": { "strict": true, "noUncheckedIndexedAccess": true } }
```
**Pitfalls:** assuming `strict: true` implies every strictness flag is on in older TS versions where a newer flag was added later; trusting editor type-checking (which may use a different TS version) over the CI compiler.

## Structural Typing and Type Narrowing
TypeScript uses structural (duck) typing, two types are compatible if their shapes match, regardless of declared names. Narrowing via `typeof`, `in`, discriminated unions, and type guards refines a union to a specific member within a branch.
```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rect"; width: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle": return Math.PI * shape.radius ** 2;
    case "rect": return shape.width * shape.height;
  }
}
```
Verify exhaustiveness with a `never`-typed default branch so the compiler flags unhandled cases when the union grows.
**Pitfalls:** using `as` casts to silence narrowing instead of fixing the discriminant; forgetting an exhaustiveness check, so new union members compile silently unhandled.

## Generics and Constraint Design
Generics let functions and types operate over a family of types while preserving relationships between inputs and outputs; constraints (`extends`) restrict what a generic can be to enable safe operations.
```typescript
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] {
  return items.map((item) => item[key]);
}
const ids = pluck([{ id: 1, name: "a" }], "id"); // number[]
```
Verify inference results with hover-over in an editor or `tsc --noEmit` on a scratch file, generic inference can silently widen to `unknown` or `any` when constraints are missing.
**Pitfalls:** overusing generics where a union or simple overload would be clearer; forgetting constraints, causing `T` to infer as `unknown` and requiring casts downstream.

## Utility Types and Type Transformations
Built-in utility types (`Partial`, `Pick`, `Omit`, `Record`, `ReturnType`, template literal types) transform existing types without redeclaration, keeping types in sync with source-of-truth definitions.
```typescript
interface User { id: number; name: string; email: string; }
type UserPatch = Partial<Pick<User, "name" | "email">>;
type UserId = User["id"];
type EventName = `on${Capitalize<"click" | "hover">}`; // "onClick" | "onHover"
```
Confirm which TS version introduced a given utility or template-literal feature (e.g., `Uppercase`/`Lowercase` template literal types require 4.1+) before using it in code targeting older compilers.
**Pitfalls:** manually duplicating a shape derived from another type instead of using `Pick`/`Omit`, causing drift when the source type changes.

## Declaration Files and Third-Party Type Verification
Types for a package may come bundled, from `@types/*`, or be entirely missing; verify with the package's actual shipped `.d.ts` files rather than assuming an API's TS types match its JS runtime behavior.
```bash
npm view express types
cat node_modules/express/package.json | grep types
npm ls @types/express
```
When types are wrong or absent, use a local `declare module` augmentation rather than casting everywhere, and file/check upstream issues for known type gaps tied to the exact package version installed.
**Pitfalls:** trusting `@types/*` version compatibility with a much newer or older runtime package version without checking their version ranges align.

## Type-Level Safety at Runtime Boundaries
TypeScript types are erased at compile time and provide zero runtime protection; data crossing a boundary (API responses, `JSON.parse`, form input) must be validated with a runtime library like `zod` or manual checks.
```typescript
import { z } from "zod";

const UserSchema = z.object({ id: z.number(), email: z.string().email() });
type User = z.infer<typeof UserSchema>;

const result = UserSchema.safeParse(await response.json());
if (!result.success) throw new Error(result.error.message);
```
Verify the schema library's version-specific API (`safeParse` vs `parse`, error shape) against the installed version's documentation before writing error-handling code.
**Pitfalls:** casting `fetch` responses with `as User` and trusting it without runtime validation; assuming TypeScript "catches" malformed external data.

## Module Resolution and Build Target Configuration
`moduleResolution`, `module`, and `target` in `tsconfig.json` determine how imports resolve and what JS syntax is emitted; mismatches between these and the actual bundler/runtime cause resolution errors that look like type errors.
```json
{
  "compilerOptions": {
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "target": "ES2022"
  }
}
```
Verify the runtime's actual module support (Node ESM vs CJS, bundler-specific resolution like Vite/webpack) matches the configured `moduleResolution` before debugging phantom "cannot find module" errors.
**Pitfalls:** using `moduleResolution: "node"` (classic) with modern package `exports` maps that require `NodeNext`/`Bundler` resolution; targeting `ESNext` output for a runtime that doesn't support the emitted syntax.

## Declaration Merging and Ambient Type Augmentation
Interfaces with the same name in the same scope merge; this enables augmenting third-party or global types (like `Express.Request` or `Window`) without modifying source packages.
```typescript
declare global {
  interface Window {
    __APP_CONFIG__: { apiUrl: string };
  }
}
export {};

// express augmentation
declare module "express-serve-static-core" {
  interface Request {
    user?: { id: string };
  }
}
```
Verify the exact module name to augment by inspecting the package's own type declarations, augmenting the wrong module path silently creates a disconnected type with no effect.
**Pitfalls:** augmenting `"express"` when the types actually live in `"express-serve-static-core"`; forgetting `export {}` in a global augmentation file, turning it into a script instead of a module.
