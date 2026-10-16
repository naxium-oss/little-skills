# Object-Oriented Programming Principles

## Encapsulation and Invariant Protection
Encapsulation hides internal state behind a controlled interface so an object can enforce its own invariants; verify that mutation only happens through methods that maintain validity, not by exposing raw mutable fields that let external code put the object into an inconsistent state.
```python
class BankAccount:
    def __init__(self, balance: float):
        if balance < 0:
            raise ValueError("balance cannot be negative")
        self._balance = balance

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    @property
    def balance(self) -> float:
        return self._balance
```
Verify no external code bypasses the accessor by directly mutating a "private" field (Python's underscore convention isn't enforced), search the codebase for direct attribute writes to confirm the invariant truly holds everywhere.
**Pitfalls:** exposing a mutable field directly (`account.balance = -50`) that bypasses validation logic entirely; assuming a leading underscore or `private` keyword provides real enforcement without verifying the language's actual access-control guarantees.

## Inheritance versus Composition Tradeoffs
Inheritance models "is-a" relationships and shares implementation via a class hierarchy, but deep hierarchies become fragile (the "fragile base class" problem) when a base class change breaks distant subclasses unexpectedly; composition ("has-a") assembles behavior from independent parts, which is often more flexible and testable. Verify which relationship actually holds before choosing.
```python
# Composition: flexible, swappable behavior
class Logger:
    def log(self, msg: str) -> None: print(msg)

class OrderProcessor:
    def __init__(self, logger: Logger):
        self.logger = logger   # depends on behavior, not a rigid hierarchy
```
Verify a proposed subclass genuinely satisfies "is-a" semantics (Liskov Substitutability) rather than reaching for inheritance purely for code reuse, which composition usually serves better.
**Pitfalls:** creating deep inheritance chains for code reuse alone (a `Square extends Rectangle` example that violates behavioral substitutability when width/height are independently settable); changing a base class method and breaking unrelated subclasses that depended on undocumented behavior.

## Polymorphism and Interface Design
Polymorphism lets code operate uniformly over different concrete types through a shared interface/contract; verify interfaces are defined by behavior needed by callers (small, focused) rather than by the union of everything a concrete class happens to implement.
```python
from typing import Protocol

class PaymentProcessor(Protocol):
    def charge(self, amount: float) -> str: ...

def checkout(processor: PaymentProcessor, amount: float) -> str:
    return processor.charge(amount)   # works with any conforming implementation
```
Verify each interface implementation actually honors the contract's semantics (not just its method signature), a `charge` method that silently does nothing still "satisfies" the type check but breaks the behavioral contract.
**Pitfalls:** designing "fat" interfaces requiring implementers to support methods irrelevant to them (Interface Segregation Principle violation), forcing empty or exception-throwing stub methods; relying on type-checking alone to verify polymorphic correctness without testing actual behavior per implementation.

## SOLID Principles in Practice
Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion guide maintainable object design; verify a claimed adherence against actual code structure rather than treating SOLID as a checklist applied superficially, since over-applying it (e.g., an interface for every single class) can add needless indirection.
```python
# Dependency Inversion: high-level module depends on abstraction, not concrete detail
class NotificationSender(Protocol):
    def send(self, message: str) -> None: ...

class OrderService:
    def __init__(self, sender: NotificationSender):
        self._sender = sender   # concrete email/SMS implementation injected, swappable
```
Verify a "Single Responsibility" refactor actually reduces coupling and improves testability by writing a test before and after the change, rather than assuming smaller classes are automatically better.
**Pitfalls:** over-abstracting a single-implementation concept behind an interface "for future flexibility" that never materializes, adding indirection with no real benefit; violating Liskov Substitution by having a subclass throw on a method the base class contract promises always succeeds.

# Functional Programming Fundamentals

## Pure Functions and Referential Transparency
A pure function's output depends only on its inputs and produces no observable side effects, making it referentially transparent (replaceable by its result without changing program behavior); verify purity explicitly by checking for hidden reads/writes of external state, I/O, or mutation of arguments.
```javascript
// Impure: depends on external mutable state and mutates input
let taxRate = 0.08;
function addTax(cart) { cart.total *= 1 + taxRate; return cart.total; }

// Pure: explicit inputs, no mutation, same output for same input always
function addTaxPure(total, taxRate) { return total * (1 + taxRate); }
```
Verify purity claims with a property-based test asserting the function returns identical output across repeated calls with identical input and produces no detectable side effects (mock I/O calls to confirm zero invocations).
**Pitfalls:** claiming a function is "pure" while it mutates an object passed by reference, silently affecting the caller's data; hiding a side effect (logging, caching) inside a function presented as a pure computation.

## Immutability and Persistent Data Structures
Immutable data cannot be changed after creation; operations return new values instead of mutating in place, eliminating a whole class of aliasing bugs at the cost of extra allocations unless the data structure is designed for structural sharing (persistent data structures). Verify a library's "immutable" claim actually prevents mutation rather than just discouraging it by convention.
```javascript
const original = Object.freeze({ count: 1, tags: ["a"] });
const updated = { ...original, count: original.count + 1 };  // new object, original untouched
console.log(original.count); // still 1
```
Confirm `Object.freeze` is shallow, nested objects/arrays remain mutable unless deep-frozen, before relying on it as a complete immutability guarantee.
**Pitfalls:** assuming a spread-copy (`{...obj}`) deep-clones nested structures, when it only shallow-copies one level; relying on convention-only "treat as immutable" objects that a different part of the codebase mutates directly, breaking the assumption silently.

## Higher-Order Functions and Function Composition
Higher-order functions accept or return other functions, enabling composition of small, reusable pieces (`map`, `filter`, `reduce`, and custom `pipe`/`compose` utilities) instead of manually written loops; verify composed pipelines produce identical results to an equivalent imperative implementation during a refactor.
```javascript
const pipe = (...fns) => (input) => fns.reduce((acc, fn) => fn(acc), input);

const processOrders = pipe(
  (orders) => orders.filter((o) => o.status === "completed"),
  (orders) => orders.map((o) => o.total),
  (totals) => totals.reduce((sum, t) => sum + t, 0)
);
```
Verify the performance characteristics of a long functional pipeline (multiple full-array passes via chained `map`/`filter`) against a single-pass imperative loop when processing very large collections, since composition can trade some raw throughput for clarity.
**Pitfalls:** chaining many `.map().filter().reduce()` calls over huge datasets without profiling, incurring multiple full traversals where one loop would suffice; composing functions with mismatched arity/argument order, silently passing wrong values downstream.

## Monadic Error Handling with Result/Option Types
Result/Either and Option/Maybe types make the possibility of failure or absence explicit in a function's type signature, forcing callers to handle both cases rather than relying on exceptions or nullable returns that can be silently ignored. Verify a chosen library's actual API (`.map`, `.flatMap`/`.andThen`, `.unwrapOr`) matches the version installed, since these utility libraries vary widely in naming.
```typescript
type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

function parseAge(input: string): Result<number, string> {
  const n = Number(input);
  return Number.isInteger(n) && n >= 0 ? { ok: true, value: n } : { ok: false, error: "invalid age" };
}

const result = parseAge(rawInput);
if (!result.ok) {
  console.error(result.error);
} else {
  console.log(result.value + 1);
}
```
Verify every call site actually handles both branches (compiler exhaustiveness checking helps) rather than unwrapping optimistically with a cast, which reintroduces the exact class of bug the pattern was meant to prevent.
**Pitfalls:** unwrapping a Result/Option with an unchecked cast or `.unwrap()` in production code paths, reintroducing crash-on-failure behavior; mixing exception-based and Result-based error handling inconsistently across the same codebase, confusing callers about which convention applies where.

# Object-Oriented Programming Principles

## Abstract Classes versus Interfaces
Abstract classes provide partial implementation plus a contract subclasses must complete, supporting single inheritance in most languages; interfaces (or protocols/traits) define pure contracts implementable by unrelated classes, supporting multiple implementation. Verify the actual relationship needed (shared implementation vs. pure contract) before choosing, since forcing shared implementation through an abstract class where multiple inheritance-like behavior is needed leads to awkward workarounds.
```typescript
abstract class Shape {
  abstract area(): number;
  describe(): string { return `Area: ${this.area()}`; }  // shared implementation
}
interface Drawable { draw(ctx: CanvasRenderingContext2D): void; }
class Circle extends Shape implements Drawable {
  constructor(private radius: number) { super(); }
  area(): number { return Math.PI * this.radius ** 2; }
  draw(ctx: CanvasRenderingContext2D): void { /* ... */ }
}
```
Verify a language's actual multiple-inheritance rules (most disallow multiple abstract class inheritance but allow multiple interface implementation) before designing a class hierarchy that assumes otherwise.
**Pitfalls:** reaching for an abstract class when only a shared contract (no shared code) is actually needed, unnecessarily restricting a class to single inheritance; duplicating implementation across multiple interface implementers because interfaces can't carry default method bodies in some older language versions.

## Composition Root and Dependency Injection Wiring
A composition root is the single location in an application where the full object graph is wired together (concrete implementations bound to abstractions), keeping dependency injection explicit and testable rather than scattered `new` calls or a global service locator; verify a codebase has one clear composition root rather than ad hoc instantiation scattered throughout business logic.
```typescript
// composition root, the only place concrete implementations are chosen
const logger = new ConsoleLogger();
const paymentGateway = new StripeGateway(config.stripeKey);
const orderService = new OrderService(logger, paymentGateway);
```
Verify business logic classes receive dependencies via constructor/parameter injection rather than instantiating their own collaborators directly, which is what actually enables swapping implementations in tests.
**Pitfalls:** scattering direct instantiation of concrete dependencies throughout business logic instead of injecting them, making unit testing require heavy mocking frameworks or monkey-patching; using a global service locator pattern that hides a class's real dependencies, making them undiscoverable from its interface.

## Value Objects and Domain Modeling
Value objects represent domain concepts by their value rather than identity (two `Money` instances with the same amount/currency are interchangeable, unlike two `Order` entities with the same total), enforcing invariants at construction time and eliminating whole classes of primitive-obsession bugs (passing a raw float where a validated, unit-aware type should be used).
```typescript
class Money {
  private constructor(private readonly cents: number, private readonly currency: string) {}
  static of(amount: number, currency: string): Money {
    if (amount < 0) throw new Error("amount cannot be negative");
    return new Money(Math.round(amount * 100), currency);
  }
  add(other: Money): Money {
    if (other.currency !== this.currency) throw new Error("currency mismatch");
    return new Money((this.cents + other.cents) / 100, this.currency);
  }
}
```
Verify equality is implemented by value (not reference) for value objects in languages requiring explicit `equals`/`==` overrides, since default reference equality silently breaks the value-object contract.
**Pitfalls:** using raw primitives (floats for money, strings for validated identifiers) throughout a codebase instead of value objects, allowing invalid values to propagate silently through business logic; forgetting to override equality for a value object, causing collection membership/deduplication checks to behave incorrectly.

## Law of Demeter and Coupling Reduction
The Law of Demeter ("only talk to your immediate friends") discourages chaining calls through multiple objects' internals (`a.getB().getC().doSomething()`), since this couples calling code to the entire object graph's structure rather than just its immediate collaborator's public contract; verify a proposed refactor actually reduces coupling by checking how many classes would need to change if an intermediate object's internal structure changed.
```typescript
// Violates Demeter: reaches through Order -> Customer -> Address internals
const city = order.getCustomer().getAddress().getCity();

// Respects Demeter: Order exposes what callers actually need
const city = order.getShippingCity();
```
Verify the refactored method (`getShippingCity`) doesn't just relocate the same chain internally without actually reducing the number of classes that must change together, which would be coupling in disguise rather than genuinely reduced.
**Pitfalls:** chaining deep property/method access across multiple object boundaries, causing a change deep in the object graph to ripple through unrelated calling code; over-applying the Law of Demeter to simple data-transfer objects where direct field access is actually appropriate and idiomatic.

# Functional Programming Fundamentals

## Recursion, Tail Calls, and Stack Safety
Functional style favors recursion over mutable loop counters, but verify whether the target language/runtime actually implements tail-call optimization (TCO) before relying on deep recursion for large inputs, many mainstream runtimes (V8/Node, CPython) do NOT guarantee TCO, so a naive recursive function can overflow the call stack on inputs a loop would handle trivially.
```javascript
// Not stack-safe in most JS engines despite being "tail recursive" in form
function sumTo(n, acc = 0) {
  if (n === 0) return acc;
  return sumTo(n - 1, acc + n);   // V8 does not guarantee TCO; large n can overflow the stack
}
```
Verify actual stack-depth limits empirically for the specific runtime with a deliberately large input before shipping recursive code on unbounded-size data, and prefer an explicit loop or trampoline pattern when TCO isn't guaranteed.
**Pitfalls:** assuming "tail-recursive-looking" code is automatically stack-safe in a language/runtime that doesn't guarantee TCO (JavaScript engines generally don't, despite it being in the ES6 spec as optional); recursing on user-controlled input size without a depth limit or iterative fallback, creating a stack-overflow denial-of-service vector.

## Currying and Partial Application
Currying transforms a multi-argument function into a sequence of single-argument functions, and partial application fixes some arguments ahead of time to produce a more specific function; verify a currying utility's actual argument-arity detection works correctly for the target function, since JavaScript's `Function.length` (often used by curry helpers) doesn't count default or rest parameters, silently breaking arity-based curry implementations.
```javascript
const curry = (fn) => (...args) =>
  args.length >= fn.length ? fn(...args) : (...more) => curry(fn)(...args, ...more);

const add3 = curry((a, b, c) => a + b + c);
const addFive = add3(5);
console.log(addFive(2, 3));   // 10
```
Verify a curried function's arity-based auto-invocation actually triggers at the intended argument count by testing with the exact target function signature, especially ones using default parameters.
**Pitfalls:** using a generic arity-based curry helper on a function with default or rest parameters, causing it to invoke prematurely or never trigger, since `fn.length` doesn't reflect the intended usable arity in those cases; over-currying trivial two-argument functions where the added indirection doesn't earn its complexity cost.

## Lazy Evaluation and Infinite Sequences
Lazy evaluation defers computation until a value is actually needed, enabling working with conceptually infinite sequences (natural numbers, Fibonacci) by only computing as many terms as consumed; verify a language's actual laziness guarantees (Python generators, JavaScript iterators, Haskell's built-in laziness) since accidentally forcing full evaluation (e.g., calling `list()` on an infinite generator) hangs or exhausts memory.
```python
def naturals():
    n = 0
    while True:
        yield n
        n += 1

import itertools
first_five_squares = list(itertools.islice((n**2 for n in naturals()), 5))
```
Verify any function consuming a potentially infinite lazy sequence uses a bounded operation (`islice`, `take`, explicit loop with a break condition) rather than an eager one (`list()`, `sum()` without bound) that would never terminate.
**Pitfalls:** calling an eager, fully-materializing operation on an infinite or very large lazy sequence, hanging the program or exhausting memory; assuming a language's iterators/generators are lazy by default when some standard library functions actually force full evaluation internally.

## Algebraic Data Types and Exhaustive Pattern Matching
Algebraic data types (sum types/tagged unions, product types) combined with exhaustive pattern matching let the compiler guarantee every case is handled, catching a whole category of "forgot to handle this case" bugs at compile time rather than runtime; verify the language/tooling actually enforces exhaustiveness (TypeScript's `never`-based check, Rust's `match`, Haskell's built-in warnings) rather than assuming a `switch`/`if-else` chain is automatically exhaustive.
```rust
enum PaymentMethod {
    Card { last_four: String },
    BankTransfer { iban: String },
    Cash,
}

fn describe(method: &PaymentMethod) -> String {
    match method {
        PaymentMethod::Card { last_four } => format!("Card ending in {last_four}"),
        PaymentMethod::BankTransfer { iban } => format!("Transfer from {iban}"),
        PaymentMethod::Cash => "Cash payment".to_string(),
    }   // compiler error if a variant is added later and not handled here
}
```
Verify adding a new variant to a sum type actually triggers compiler errors at every non-exhaustive match site, confirming the exhaustiveness guarantee is real for the specific language/tooling configuration in use, not just assumed.
**Pitfalls:** using a plain `switch` with a `default` case that swallows unhandled new variants silently instead of an exhaustiveness-checked match, hiding bugs introduced when the type is extended; modeling what should be a sum type (mutually exclusive states) as a struct with multiple optional/nullable fields, allowing invalid combinations the type system could have prevented.
