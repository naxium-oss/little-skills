# Vue.js Fundamentals

## Version and API Style Grounding
Vue 2 (Options API only, deprecated end-of-life) and Vue 3 (Options API + Composition API) differ fundamentally in reactivity implementation (`Object.defineProperty` vs `Proxy`) and lifecycle hook names. Verify the installed major version before applying guidance.
```bash
npm ls vue                        # vue@3.5.13
```
```vue
<script setup>
import { ref } from "vue";
const count = ref(0);
</script>
```
**Pitfalls:** applying Vue 2 lifecycle names (`beforeDestroy`) in a Vue 3 project where they were renamed (`beforeUnmount`); mixing Options API `data()` mental model with Composition API `ref`/`reactive` without understanding unwrapping rules.

## Reactivity System: ref, reactive, and Unwrapping
Vue 3's reactivity wraps primitives in `ref` (accessed via `.value` in script, auto-unwrapped in templates) and objects in `reactive` (a Proxy, no `.value`); destructuring a `reactive` object loses reactivity unless using `toRefs`.
```javascript
import { reactive, toRefs } from "vue";
const state = reactive({ count: 0, name: "app" });
const { count, name } = toRefs(state);  // preserves reactivity as individual refs
```
Verify actual reactivity is preserved after refactors by checking whether the UI updates on mutation, plain destructuring (`const { count } = state`) silently breaks reactivity without a runtime error.
**Pitfalls:** destructuring a `reactive()` object directly and losing reactive tracking; reassigning a whole `reactive` object (`state = {...}`) instead of mutating its properties, which breaks the original Proxy reference held by templates.

## Component Communication: Props, Emits, and Provide/Inject
Data flows down via `props` and up via `emit`-ed events by convention; `provide`/`inject` bypasses prop drilling for deeply nested trees but sacrifices explicit data-flow traceability. Verify prop types and emitted event names are declared for tooling/runtime validation.
```vue
<script setup>
const props = defineProps({ modelValue: { type: String, required: true } });
const emit = defineEmits(["update:modelValue"]);
</script>
<template>
  <input :value="modelValue" @input="emit('update:modelValue', $event.target.value)" />
</template>
```
Confirm `v-model` custom component bindings match the exact prop/event pair name (`modelValue`/`update:modelValue`) expected by the Vue version in use, since naming conventions shifted between Vue 2 and 3.
**Pitfalls:** mutating a prop directly inside a child component, violating one-way data flow and producing a runtime warning; overusing `provide`/`inject` for data that would be clearer as explicit props.

## Computed Properties versus Watchers
`computed` derives cached, reactive values from other reactive state and should be preferred for pure derivations; `watch`/`watchEffect` run side effects in response to changes and should be reserved for things computed properties can't do (API calls, DOM manipulation, logging).
```javascript
const fullName = computed(() => `${first.value} ${last.value}`);
watch(userId, async (newId, oldId) => {
  if (newId !== oldId) user.value = await fetchUser(newId);
}, { immediate: true });
```
Verify a `watch` isn't being used to derive a value that `computed` would handle more efficiently (with automatic caching and dependency tracking), a common anti-pattern.
**Pitfalls:** using `watch` to manually recompute a derived value instead of `computed`, causing redundant renders/logic; forgetting `{ deep: true }` when watching a nested object mutation that isn't reassigned wholesale.

# Angular Fundamentals

## Version, CLI, and Standalone Components Grounding
Angular ships major versions roughly every 6 months with real breaking changes (NgModules-first vs. standalone-components-first defaults since v14+/v17+); verify the exact version and whether the project uses NgModules or standalone bootstrapping before applying tutorials.
```bash
ng version                          # Angular CLI: 19.0.4, Angular: 19.0.5
```
```typescript
bootstrapApplication(AppComponent, {
  providers: [provideRouter(routes), provideHttpClient()],
});
```
**Pitfalls:** following older NgModule-centric tutorials (`declarations`, `NgModule` bootstrap) against a modern standalone-only project scaffold; assuming CLI schematics generate the same file structure across major versions.

## Dependency Injection and Providers
Angular's DI resolves providers hierarchically (root, module, component); `providedIn: 'root'` creates an app-wide singleton, while providing a service at the component level creates a new instance scoped to that component subtree. Verify the intended scope matches actual behavior with a shared-counter test.
```typescript
@Injectable({ providedIn: "root" })
export class CartService {
  private items = signal<Item[]>([]);
  readonly total = computed(() => this.items().reduce((s, i) => s + i.price, 0));
}
```
Confirm whether a service is unexpectedly re-instantiated per component (common when accidentally re-declaring it in a component's `providers` array) by adding a constructor log and checking instance counts.
**Pitfalls:** re-providing a service meant to be a singleton at the component level, creating unintended separate instances with disconnected state; injecting via constructor parameter without the `@Injectable` decorator on the target class, causing a runtime DI error.

## Change Detection and Signals
Angular's default (Zone.js-based) change detection checks the whole component tree on any async event; `OnPush` change detection and the newer Signals API (stable since v17+) provide fine-grained, explicit reactivity, reducing unnecessary checks. Verify which model a component uses before debugging "why didn't the UI update."
```typescript
@Component({ changeDetection: ChangeDetectionStrategy.OnPush })
export class UserCard {
  user = input.required<User>();
  displayName = computed(() => `${this.user().first} ${this.user().last}`);
}
```
Confirm `OnPush` components only fail to update when an `@Input()` reference doesn't change (mutating an object in place won't trigger it), verify with `ChangeDetectorRef.markForCheck()` debugging if a suspected update is missed.
**Pitfalls:** mutating an `@Input()` object in place under `OnPush`, expecting a re-render since the object "changed", reference equality is what matters; mixing signals and Zone.js-triggered detection without understanding which schedules the actual re-render.

## Routing, Guards, and Lazy Loading
The Angular Router matches URL paths to components, supports functional route guards (`CanActivateFn`) for authorization checks, and lazy-loads feature routes via `loadComponent`/`loadChildren` to reduce initial bundle size. Verify actual network tab chunk-loading behavior matches the configured lazy boundaries.
```typescript
export const routes: Routes = [
  {
    path: "admin",
    canActivate: [authGuard],
    loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES),
  },
];
```
Confirm guards return `false`/`UrlTree` correctly for redirect-on-deny behavior by testing an unauthenticated navigation attempt directly, not just via UI links.
**Pitfalls:** forgetting a guard also needs to protect child routes explicitly (guards don't automatically cascade in all configurations); bundling a "lazy" route inside a shared chunk accidentally by importing it eagerly elsewhere, defeating code-splitting.

# Vue.js Fundamentals

## Template Directives and List Rendering Keys
Vue's template directives (`v-if`, `v-for`, `v-bind`, `v-on`) compile to render functions; `v-for` requires a `:key` bound to a stable unique identifier (never the array index for reorderable lists) so Vue's virtual DOM diffing patches the correct DOM node instead of reusing one with stale local state. Verify actual patch behavior by giving a list item local state (an open/closed toggle) and reordering the list.
```vue
<template>
  <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</template>
```
Confirm `v-if` and `v-for` are never combined on the same element (Vue evaluates `v-for` with higher priority in Vue 2, but this is explicitly disallowed/warned in Vue 3), using a wrapping `<template>` instead when both are needed.
**Pitfalls:** using the loop index as `:key` on a filterable/sortable list, causing input state to attach to the wrong row after reordering; combining `v-if` and `v-for` directly on one element, producing confusing conditional-per-iteration behavior.

## Single-File Component Structure and Scoped Styles
A `.vue` Single-File Component bundles template, script, and style in one file; `<style scoped>` automatically scopes CSS to the component via generated data attributes, preventing global leakage, while `<style module>` provides CSS Modules-style class mapping. Verify scoping actually applies by inspecting generated class/attribute names in DevTools rather than assuming visual isolation.
```vue
<template><button class="btn">Save</button></template>
<style scoped>
.btn { padding: 0.5rem 1rem; border-radius: 0.375rem; }
</style>
```
Confirm deep selectors (`:deep()`) are used deliberately when a scoped style must reach into a child component's markup, since scoped styles do not cross component boundaries by default.
**Pitfalls:** expecting a scoped style to affect a child component's internal markup without `:deep()`, silently having no effect; relying on global `<style>` blocks for component-specific styling, reintroducing the leakage scoped styles were meant to prevent.

## Composables for Reusable Logic
Composables (functions using Composition API primitives like `ref`/`computed`/lifecycle hooks, conventionally prefixed `use*`) extract and share stateful logic across components, replacing Vue 2's mixins which suffered from naming collisions and unclear data sources. Verify a composable actually returns fresh, independent state per call (not a shared singleton) unless a singleton is explicitly intended.
```javascript
export function useMousePosition() {
  const x = ref(0), y = ref(0);
  const update = (e) => { x.value = e.clientX; y.value = e.clientY; };
  onMounted(() => window.addEventListener("mousemove", update));
  onUnmounted(() => window.removeEventListener("mousemove", update));
  return { x, y };
}
```
Verify cleanup (`onUnmounted`) is present for any subscription/listener a composable sets up, since forgetting it leaks listeners across every component instance that used the composable.
**Pitfalls:** defining reactive state as a module-level singleton inside a composable when each component actually needs independent state, causing unintended cross-component data sharing; omitting `onUnmounted` cleanup, accumulating listeners across repeated mount/unmount cycles.

## Pinia State Management Patterns
Pinia (the officially recommended store, replacing Vuex) defines stores as composables with `state`, `getters`, and `actions`, fully typed and DevTools-integrated; verify store instances are accessed within a component's `setup()` scope or explicitly passed a Pinia instance, since calling a store outside an active Pinia context throws at runtime.
```javascript
export const useCartStore = defineStore("cart", {
  state: () => ({ items: [] }),
  getters: { total: (state) => state.items.reduce((s, i) => s + i.price, 0) },
  actions: { addItem(item) { this.items.push(item); } },
});
```
Verify store mutations happen only through actions (or direct state assignment within components, which Pinia allows but should be used consistently) so state changes remain traceable in DevTools.
**Pitfalls:** calling `useCartStore()` outside of a component setup or an active Pinia instance (e.g., in a plain module at import time), throwing "no active Pinia" errors; mutating nested store state deeply without going through a documented pattern, making changes hard to trace in DevTools.

# Angular Fundamentals

## RxJS Observables and Subscription Management
Angular integrates deeply with RxJS Observables for async data (HTTP, forms, router events); unmanaged subscriptions that never unsubscribe cause memory leaks and duplicate handler execution across component recreations. Verify every manual `.subscribe()` has a corresponding teardown (the `async` pipe in templates handles this automatically) rather than assuming garbage collection alone cleans up subscriptions.
```typescript
export class UserListComponent implements OnDestroy {
  private destroy$ = new Subject<void>();
  ngOnInit() {
    this.userService.getUsers().pipe(takeUntil(this.destroy$)).subscribe((users) => this.users = users);
  }
  ngOnDestroy() { this.destroy$.next(); this.destroy$.complete(); }
}
```
Prefer the template `async` pipe over manual subscriptions wherever possible, since it automatically subscribes on render and unsubscribes on destroy, eliminating a whole class of leak bugs.
**Pitfalls:** subscribing manually in `ngOnInit` without any teardown logic, leaking subscriptions on every component destroy/recreate cycle; nesting subscriptions (`subscribe` inside `subscribe`) instead of composing with operators like `switchMap`, causing race conditions on rapid repeated triggers.

## Reactive Forms and Validation
Angular's Reactive Forms model form state explicitly in the component class (`FormGroup`, `FormControl`) rather than the template-driven approach, giving typed, testable access to validity, value changes, and custom validators. Verify validators actually run on the expected trigger (`valueChanges`, blur, submit) and that async validators' pending state is handled in the UI.
```typescript
form = new FormGroup({
  email: new FormControl("", [Validators.required, Validators.email]),
  age: new FormControl(0, [Validators.min(18)]),
});
```
Verify custom validators return `null` for valid and an error object for invalid (not `false`/`true`), since Angular's validator contract specifically expects this shape and a mismatched return silently breaks validation state.
**Pitfalls:** writing a custom validator that returns a boolean instead of `null`/error-object, causing Angular to treat the field as permanently invalid or always valid; forgetting to handle `PENDING` status during async validation, showing a stale valid/invalid state to the user.

## Pipes and Template Transformation
Pipes transform values directly in templates (`date`, `currency`, custom pipes) without cluttering component logic; verify a custom pipe is marked `pure: true` (default) unless it genuinely needs to react to mutations of the same object reference, since impure pipes re-run on every change-detection cycle regardless of whether their input actually changed, hurting performance.
```typescript
@Pipe({ name: "truncate" })
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 50): string {
    return value.length > limit ? `${value.slice(0, limit)}…` : value;
  }
}
```
Verify pure pipes are only re-evaluated when their input reference changes by testing with a mutated-in-place object versus a newly created one, confirming Angular's default change-detection semantics for pipe inputs.
**Pitfalls:** marking a pipe `pure: false` for convenience, causing it to run on every change-detection cycle across the whole component tree and degrading performance; mutating an array/object in place and expecting a pure pipe watching it to re-render, when pure pipes only react to reference changes.

## Angular Universal Server-Side Rendering
Angular Universal renders the app to static HTML on the server for faster first paint and SEO, then "hydrates" it client-side; verify code doesn't directly access browser-only globals (`window`, `document`, `localStorage`) without guarding for the server environment, since such calls throw during server rendering unless wrapped in a platform check.
```typescript
import { isPlatformBrowser } from "@angular/common";
constructor(@Inject(PLATFORM_ID) private platformId: object) {
  if (isPlatformBrowser(this.platformId)) {
    localStorage.getItem("theme");
  }
}
```
Verify hydration doesn't produce mismatches (flicker, duplicated content) by testing an actual server-rendered page load rather than only client-side-rendered dev mode, since SSR-specific bugs often only appear in a true server-rendered build.
**Pitfalls:** calling `window`/`document`/`localStorage` unconditionally in a service or component constructor, crashing server-side rendering entirely; never testing the actual SSR build output, missing hydration mismatches that only manifest outside of pure client-side dev mode.
