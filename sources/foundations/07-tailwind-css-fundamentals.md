# Tailwind CSS Fundamentals

## Version and Configuration Grounding
Tailwind v4 changed its architecture significantly from v3 (CSS-first config via `@theme` in a stylesheet instead of `tailwind.config.js`, native CSS engine, no PostCSS required by default). Verify the installed major version before applying config guidance.
```bash
npm ls tailwindcss                 # tailwindcss@4.1.17
```
```css
/* v4: config lives in CSS */
@import "tailwindcss";
@theme {
  --color-brand: oklch(0.7 0.15 250);
  --font-display: "Inter", sans-serif;
}
```
**Pitfalls:** applying v3 `tailwind.config.js` `theme.extend` guidance to a v4 project expecting CSS-first `@theme`; assuming PostCSS/`autoprefixer` are still required when using the v4 Vite plugin.

## Utility-First Composition and Class Ordering
Tailwind encourages composing small utility classes directly in markup rather than writing custom CSS; verify the actual rendered result matches intent since utilities apply in source-order-independent cascade layers, not left-to-right class order.
```html
<button class="inline-flex items-center gap-2 rounded-lg bg-slate-900 px-4 py-2 text-sm font-medium text-white hover:bg-slate-700 focus-visible:outline focus-visible:outline-2 disabled:opacity-50">
  Save changes
</button>
```
Use `prettier-plugin-tailwindcss` to auto-sort classes consistently, and verify conflicting utilities (e.g., two different `bg-*` classes), the one later in Tailwind's internal layer order wins, not necessarily the one written last in the string.
**Pitfalls:** assuming the last class in the `class` string always wins for conflicting utilities; hand-writing custom CSS for something a utility already covers, causing specificity fights with Tailwind's own layers.

## Responsive and State Variants
Variants (`sm:`, `md:`, `hover:`, `focus:`, `dark:`, `group-hover:`, `data-[state=open]:`) prefix utilities to apply conditionally; verify actual breakpoint pixel values from the active theme rather than assuming standard defaults if customized.
```html
<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
  <div class="group rounded border p-4 hover:shadow-lg dark:border-slate-700">
    <h3 class="text-slate-900 group-hover:text-brand dark:text-slate-100">Title</h3>
  </div>
</div>
```
Confirm `dark:` mode strategy (`media` vs `class`/`selector`) matches how the app actually toggles theme, since a misconfigured strategy silently makes `dark:` utilities inert.
**Pitfalls:** using `dark:` utilities while the project has no mechanism toggling the `dark` class/attribute, so styles never activate; nesting `group`/`peer` incorrectly, so `group-hover:` targets the wrong ancestor.

## Design Tokens and Arbitrary Values
Theme tokens (spacing, colors, font sizes) keep designs consistent; arbitrary value syntax (`w-[137px]`, `bg-[#1da1f2]`, `grid-cols-[1fr_2fr]`) escapes the scale for one-off needs but should be used sparingly and verified against design specs.
```html
<div class="mt-[calc(100vh-4rem)] bg-[image:var(--hero-bg)] text-[13px]">
  Custom-fit hero spacer
</div>
```
Verify whether a repeated arbitrary value should instead be promoted to a named `@theme` token to keep the design system consistent and avoid magic numbers scattered across markup.
**Pitfalls:** overusing arbitrary values instead of extending the theme, defeating the consistency benefit of a design system; forgetting underscores for spaces in arbitrary grid/value syntax (`grid-cols-[1fr_2fr]`, not `1fr 2fr`).

## Content Detection and Unused-Class Purging
Tailwind scans source files at build time to determine which utility classes are actually used and generates CSS only for those (no runtime purge step needed in v4's automatic content detection); verify dynamically constructed class strings (`` `text-${color}-500` ``) are detected, since Tailwind's static scanner cannot resolve runtime string interpolation and will omit those classes from the build entirely.
```javascript
// BROKEN: Tailwind's scanner can't see the full class name at build time
const cls = `bg-${color}-500`;

// CORRECT: use a complete, statically-scannable class map
const colorClasses = { red: "bg-red-500", blue: "bg-blue-500" };
const cls = colorClasses[color];
```
Verify the production build actually contains an expected utility by searching the generated CSS output, especially after refactoring dynamic class construction.
**Pitfalls:** building class names via string concatenation/interpolation, causing Tailwind's static scanner to silently omit the utility from the compiled CSS; excluding a source directory from the scanned content paths, causing all utilities used only in that directory to be missing in production.

## Dark Mode Strategy Configuration
Tailwind supports `media`-based dark mode (follows OS preference automatically) or `class`/`selector`-based dark mode (toggled manually via JS, giving user control); verify which strategy is configured, since a project expecting manual toggling but left on the `media` default will have `dark:` utilities that silently ignore any in-app toggle button.
```css
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```
```javascript
document.documentElement.classList.toggle("dark", userPrefersDark);
```
Verify persisted theme preference (localStorage) is applied before first paint to avoid a flash of the wrong theme, testing with actual page reloads rather than only in-session toggles.
**Pitfalls:** configuring `class`-based dark mode but never actually toggling the class anywhere in the app, leaving `dark:` utilities permanently inert; applying the dark class after first paint, causing a visible flash of incorrect theme on load.

## Custom Utilities and the @utility Directive
Beyond built-in utilities, Tailwind v4 supports defining first-class custom utilities via the `@utility` directive (replacing v3's `theme.extend` + plugin API for many simple cases), which participate in variant stacking (`hover:`, `md:`) automatically. Verify a genuinely reusable pattern justifies a custom utility versus just composing existing ones inline.
```css
@utility scrollbar-hidden {
  scrollbar-width: none;
  &::-webkit-scrollbar { display: none; }
}
```
```html
<div class="scrollbar-hidden overflow-y-auto hover:scrollbar-hidden">...</div>
```
Verify the custom utility actually participates correctly in variant prefixes by testing a `hover:`/`md:` prefixed usage, since improperly defined custom utilities can fail to stack with Tailwind's variant system.
**Pitfalls:** writing a plain global CSS class instead of an `@utility`, losing automatic variant-prefix support (`hover:my-class` won't work on a non-utility class); duplicating an existing utility combination as a "custom utility" that Tailwind's own composition already covers concisely.

## Component Extraction versus Utility Duplication
Repeating the same long utility string across many components suggests extracting a shared component (React/Vue component) rather than a CSS class, preserving Tailwind's co-location benefits while avoiding duplication; verify the extraction actually reduces duplication meaningfully rather than creating a rigid one-size-fits-all component that fights every future variation.
```jsx
function Button({ variant = "primary", children, ...props }) {
  const base = "inline-flex items-center rounded-lg px-4 py-2 text-sm font-medium";
  const variants = {
    primary: "bg-slate-900 text-white hover:bg-slate-700",
    secondary: "bg-slate-100 text-slate-900 hover:bg-slate-200",
  };
  return <button className={`${base} ${variants[variant]}`} {...props}>{children}</button>;
}
```
Verify the component API (props for variants) actually covers real usage variance observed in the codebase before finalizing, rather than guessing at variants that never get used.
**Pitfalls:** extracting a component too early with only one real use case, guessing at a variant API that doesn't match actual future needs; copy-pasting long utility strings across a dozen components instead of extracting a shared one, making global style updates error-prone.

# React Fundamentals

## Version and Rendering Model Grounding
React's behavior around Strict Mode double-invocation, automatic batching, and Server Components differs sharply between React 17, 18, and 19; verify the installed version and rendering entry point (`createRoot` vs legacy `render`) before diagnosing "why does this run twice" issues.
```bash
npm ls react react-dom              # react@19.2.6
```
```javascript
import { createRoot } from "react-dom/client";
createRoot(document.getElementById("root")).render(<App />);
```
**Pitfalls:** assuming React 18+ Strict Mode double-invoking effects/render in development indicates a bug, when it's intentional to surface impure code; using legacy `ReactDOM.render` patterns from pre-18 tutorials against a React 19 project.

## Component State and the Rules of Hooks
Hooks must be called unconditionally at the top level, in the same order, on every render; state updates are asynchronous and batched, and reading state immediately after calling its setter returns the stale value from the current render's closure.
```javascript
function Counter() {
  const [count, setCount] = useState(0);
  const increment = () => {
    setCount((prev) => prev + 1);   // functional update avoids stale-closure bugs
  };
  return <button onClick={increment}>{count}</button>;
}
```
Verify state-update logic uses the functional updater form when the new value depends on the previous one, especially inside loops, timers, or event handlers that batch multiple updates.
**Pitfalls:** calling hooks conditionally (`if (x) useState()`), which desyncs hook order between renders and throws or corrupts state silently; reading a state variable right after calling its setter and expecting the updated value synchronously.

## Effects, Dependencies, and Cleanup
`useEffect` synchronizes a component with an external system (subscriptions, timers, DOM APIs); the dependency array determines when it re-runs, and returning a cleanup function prevents leaks from stale subscriptions across re-renders/unmounts.
```javascript
useEffect(() => {
  const controller = new AbortController();
  fetch(`/api/users/${userId}`, { signal: controller.signal })
    .then((res) => res.json())
    .then(setUser)
    .catch((err) => { if (err.name !== "AbortError") setError(err); });
  return () => controller.abort();
}, [userId]);
```
Run the ESLint `react-hooks/exhaustive-deps` rule and treat its warnings as real bugs rather than suppressing them, since missing dependencies are the most common source of stale-closure effect bugs.
**Pitfalls:** omitting a dependency to "stop it from re-running," which instead captures a stale closure over old props/state; forgetting cleanup, causing duplicate subscriptions or state updates on unmounted components.

## Reconciliation, Keys, and List Rendering
React reconciles lists by `key`, matching elements across renders to decide whether to update, reorder, or remount; using array index as a key for a reorderable/filterable list causes state to attach to the wrong item.
```javascript
{items.map((item) => (
  <TodoItem key={item.id} item={item} />   // stable identity, not index
))}
```
Verify with React DevTools' "Highlight updates" or by adding local state inside a list item (e.g., an input) and reordering the list to confirm state follows the correct item, not the position.
**Pitfalls:** using `key={index}` on lists that can reorder, filter, or have items inserted/removed, causing input focus or local state to jump to the wrong row; regenerating keys (e.g., `Math.random()`) every render, forcing full remounts and losing state/focus.

## Context, Memoization, and Re-Render Control
`useContext` triggers a re-render of every consumer when the provided value changes identity, even if only one field changed; `useMemo`/`useCallback`/`React.memo` prevent unnecessary recomputation or child re-renders but only help when dependencies are stable and the cost of memoization is less than the cost avoided.
```javascript
const value = useMemo(() => ({ user, theme }), [user, theme]); // stable identity
const ExpensiveList = React.memo(function ExpensiveList({ items }) {
  return items.map((i) => <Row key={i.id} {...i} />);
});
```
Profile with React DevTools' Profiler before adding memoization reactively, premature memoization adds complexity and can even hurt performance if dependency arrays are unstable.
**Pitfalls:** wrapping every component in `React.memo` without profiling, adding comparison overhead with no measured benefit; passing a new inline object/function as a context value every render, defeating consumers' memoization downstream.

## Controlled versus Uncontrolled Form Inputs
A controlled input's value is driven entirely by React state (`value` + `onChange`), while an uncontrolled input manages its own DOM state internally, accessed via a `ref` when needed; verify a component consistently uses one pattern per input, since switching between controlled and uncontrolled on the same element (e.g., `value` starting `undefined` then becoming a string) triggers a distinct React warning and inconsistent behavior.
```jsx
function SearchBox() {
  const [query, setQuery] = useState("");   // always a string, never undefined, stays controlled
  return <input value={query} onChange={(e) => setQuery(e.target.value)} />;
}
```
Verify initial state is never `undefined` for a value intended to be controlled from the start, since React warns about a component "changing an uncontrolled input to be controlled" the first time a real value arrives.
**Pitfalls:** initializing state as `undefined` for a controlled input, causing a console warning and subtle focus/cursor bugs on the first keystroke; mixing a `defaultValue` (uncontrolled) with a `value` (controlled) on the same input.

## Error Boundaries and Render-Time Failure Containment
Error boundaries (class components implementing `static getDerivedStateFromError`/`componentDidCatch`, or libraries wrapping this pattern) catch render-time errors in their child tree and display a fallback UI instead of crashing the entire app; verify boundaries are placed at meaningful granularity (per-route or per-widget) rather than only once at the app root, since a single root boundary takes down the whole UI for one widget's bug.
```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  static getDerivedStateFromError() { return { hasError: true }; }
  componentDidCatch(error, info) { logErrorToService(error, info); }
  render() { return this.state.hasError ? this.props.fallback : this.props.children; }
}
```
Verify error boundaries do NOT catch errors in event handlers, async code, or server-side rendering, those require explicit `try/catch`, by testing an intentionally thrown error inside a click handler and confirming the boundary does not activate.
**Pitfalls:** assuming an error boundary catches all errors anywhere in the app, including those thrown inside `onClick` handlers or `fetch` callbacks, which it does not; placing only one boundary at the very root, causing any single component's render error to blank the entire application.

## Suspense and Data-Fetching Coordination
`Suspense` lets a component tree "wait" for asynchronous work (lazy-loaded components via `React.lazy`, or data sources integrated with Suspense) by showing a fallback until children resolve; verify the actual data-fetching library used (React Query, Relay, or framework-level fetching) actually integrates with Suspense, since a plain `useEffect`-based fetch does not automatically suspend and requires the older loading-state pattern instead.
```jsx
const ProfilePage = React.lazy(() => import("./ProfilePage"));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <ProfilePage />
    </Suspense>
  );
}
```
Verify fallback flashing behavior on fast connections (a fallback that flashes for 50ms is worse UX than no fallback) by testing on throttled and fast network conditions, adjusting with a minimum-display-time pattern if needed.
**Pitfalls:** assuming any async `useEffect`-based data fetch automatically integrates with a wrapping `Suspense` boundary without the library explicitly supporting the Suspense contract; not testing fallback UI on fast networks, shipping a jarring flash-of-loading-state on every navigation.
