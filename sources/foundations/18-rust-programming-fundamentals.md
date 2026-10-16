# Rust Programming Fundamentals

## Toolchain, Edition, and Crate Version Grounding
Rust behavior depends on the installed `rustc`/`cargo` toolchain version and the crate's declared `edition` (2015/2018/2021/2024) in `Cargo.toml`, which changes defaults like closure capture and prelude contents. Verify both before assuming a syntax feature is available.
```bash
rustc --version --verbose
cargo --version
grep edition Cargo.toml
```
Check `Cargo.lock` for exact resolved dependency versions rather than the version ranges in `Cargo.toml`, since ranges permit drift across builds without a committed lockfile.
**Pitfalls:** assuming a nightly-only feature (behind a `#![feature(...)]` flag) is available on stable Rust; using edition-2021 idioms in a crate still declared as edition 2018 without updating `Cargo.toml`.

## Ownership, Borrowing, and Lifetime Fundamentals
Every value has one owner; moving transfers ownership and invalidates the previous binding, while borrowing (`&T`, `&mut T`) grants temporary access under the compiler-enforced rule of either one mutable or many immutable borrows at a time. Verify borrow-checker errors by reading the actual compiler diagnostic, which usually names the exact conflicting borrow and its span.
```rust
fn main() {
    let mut data = vec![1, 2, 3];
    let first = &data[0];        // immutable borrow starts
    // data.push(4);             // ERROR: cannot borrow `data` as mutable while borrowed as immutable
    println!("{}", first);       // immutable borrow ends here (NLL)
    data.push(4);                 // now fine
}
```
Read lifetime elision rules before manually annotating lifetimes (`'a`), the compiler infers them in common patterns, and manual annotations are only needed when the relationship between input/output references is ambiguous.
**Pitfalls:** fighting the borrow checker by cloning excessively instead of restructuring ownership, hiding real design issues behind unnecessary allocations; assuming a lifetime error means the code is fundamentally wrong rather than needing restructured scope boundaries.

## Error Handling with Result and the ? Operator
Rust has no exceptions for recoverable errors; `Result<T, E>` and the `?` operator propagate errors explicitly and are checked by the compiler (a function returning `Result` that ignores an inner `Result` triggers an `unused_must_use` warning). Verify error types are properly converted across boundaries with `From`/`?` rather than unwrapping with `.unwrap()` in production paths.
```rust
use std::fs;

fn read_config(path: &str) -> Result<String, std::io::Error> {
    let contents = fs::read_to_string(path)?;   // propagates io::Error automatically
    Ok(contents)
}
```
Use `anyhow` for application-level error aggregation and `thiserror` for library-level typed errors, verifying which convention the crate/project actually follows before adding a third inconsistent style.
**Pitfalls:** using `.unwrap()`/`.expect()` widely in production code paths, causing panics on recoverable errors instead of graceful handling; mixing custom error enums with `Box<dyn Error>` inconsistently across a codebase, complicating callers' error matching.

## Traits, Generics, and Zero-Cost Abstraction
Traits define shared behavior (like interfaces) that types can implement, and generics with trait bounds enable code reuse without runtime dispatch overhead (monomorphization generates specialized code per concrete type) unless `dyn Trait` is explicitly used for dynamic dispatch. Verify which dispatch mechanism is intended based on actual performance/flexibility needs.
```rust
trait Shape {
    fn area(&self) -> f64;
}

fn total_area<T: Shape>(shapes: &[T]) -> f64 {   // static dispatch, monomorphized
    shapes.iter().map(Shape::area).sum()
}

fn total_area_dyn(shapes: &[Box<dyn Shape>]) -> f64 {  // dynamic dispatch via vtable
    shapes.iter().map(|s| s.area()).sum()
}
```
Verify binary size/compile time tradeoffs of heavy generic monomorphization with `cargo bloat` if compile times balloon unexpectedly, since each concrete type instantiation generates separate code.
**Pitfalls:** defaulting to `dyn Trait` everywhere out of unfamiliarity with generics, paying unnecessary vtable dispatch overhead in hot paths; over-using generics in ways that cause combinatorial monomorphization bloat and slow compile times.

# Go Programming Fundamentals

## Go Version, Modules, and Toolchain Grounding
Go's module system (`go.mod`) pins a minimum Go version and dependency versions; behavior around generics (1.18+), workspaces (1.18+), and the `go` directive's toolchain-selection semantics (1.21+) varies by version. Verify the installed toolchain and module Go version before assuming a language feature is available.
```bash
go version                       # go version go1.23.3 linux/amd64
cat go.mod | head -5
go env GOFLAGS GOPROXY
```
Confirm `go.sum` is committed and verified (`go mod verify`) for supply-chain integrity, since it pins cryptographic hashes of every dependency version.
**Pitfalls:** assuming generics syntax works on a `go.mod` declaring `go 1.16`; ignoring `go mod tidy` drift, where `go.mod` lists dependencies no longer imported or missing ones actually used.

## Goroutines, Channels, and the sync Package
Goroutines are cheap, runtime-scheduled concurrent functions; channels provide synchronized communication between them ("share memory by communicating"), while the `sync` package (Mutex, WaitGroup) protects shared state directly when channels are less natural. Verify goroutine lifecycle termination explicitly, leaked goroutines blocked forever on a channel are a common invisible resource leak.
```go
func fetchAll(urls []string) []string {
    results := make(chan string, len(urls))
    var wg sync.WaitGroup
    for _, u := range urls {
        wg.Add(1)
        go func(url string) {
            defer wg.Done()
            results <- fetch(url)
        }(u)
    }
    wg.Wait()
    close(results)
    out := make([]string, 0, len(urls))
    for r := range results {
        out = append(out, r)
    }
    return out
}
```
Run `go test -race` regularly to catch data races the type system doesn't prevent, and use `pprof`'s goroutine profile to detect leaked/blocked goroutines in long-running services.
**Pitfalls:** capturing a loop variable incorrectly in a goroutine closure (fixed by-value per iteration since Go 1.22, but still a bug on older versions without an explicit parameter capture); forgetting to close channels or `wg.Wait()`, leaking goroutines that block forever.

## Error Handling Conventions and Wrapping
Go treats errors as ordinary return values (no exceptions for expected failures); the `error` interface plus `fmt.Errorf("...: %w", err)` wrapping and `errors.Is`/`errors.As` enable structured error inspection without losing the original cause. Verify wrapped errors are actually inspectable at the point they're handled, not just stringified.
```go
func loadUser(id string) (*User, error) {
    row, err := db.QueryRow("SELECT ...", id)
    if err != nil {
        return nil, fmt.Errorf("loadUser %s: %w", id, err)
    }
    return row, nil
}

if errors.Is(err, sql.ErrNoRows) {
    // handle not-found specifically, even though it was wrapped upstream
}
```
Confirm every returned error from a called function is actually checked (`if err != nil`): Go's compiler does not enforce this, unlike some other languages' checked exceptions, making silent error-ignoring a real risk caught only by linters like `errcheck`.
**Pitfalls:** discarding an error with `_` out of convenience, silently swallowing failures; comparing wrapped errors with `==` instead of `errors.Is`, missing matches because wrapping changes the concrete error value.

## Interfaces and Implicit Satisfaction
Go interfaces are satisfied implicitly (no `implements` keyword), any type with matching methods satisfies an interface automatically, encouraging small, focused interfaces defined at the point of use (consumer-defined) rather than large upfront hierarchies. Verify an interface is actually the minimal contract needed by its consumers, per Go's "accept interfaces, return structs" idiom.
```go
type Reader interface {
    Read(p []byte) (n int, err error)
}

func CountBytes(r Reader) (int, error) {   // works with any type satisfying Read, no explicit declaration needed
    buf := make([]byte, 4096)
    total := 0
    for {
        n, err := r.Read(buf)
        total += n
        if err == io.EOF { return total, nil }
        if err != nil { return total, err }
    }
}
```
Verify a struct's method set actually satisfies an interface with a compile-time assertion (`var _ Reader = (*MyType)(nil)`) to catch accidental signature mismatches early rather than discovering them only at a distant call site.
**Pitfalls:** defining large, "kitchen sink" interfaces upfront instead of small consumer-defined ones, increasing coupling; forgetting a pointer receiver method set differs from a value receiver's, causing a type to unexpectedly not satisfy an interface it was assumed to implement.

# Rust Programming Fundamentals

## Smart Pointers: Box, Rc, Arc, and RefCell
Rust's smart pointers extend ownership rules for specific needs: `Box<T>` for heap allocation with single ownership, `Rc<T>` for shared ownership within a single thread (reference-counted, not thread-safe), `Arc<T>` for shared ownership across threads (atomic reference counting), and `RefCell<T>` for interior mutability with runtime-checked borrow rules. Verify the actual concurrency requirement before choosing `Rc` versus `Arc`, since using `Rc` across threads fails to compile (it doesn't implement `Send`), while `Arc` has real atomic-operation overhead unnecessary in single-threaded code.
```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];
for _ in 0..10 {
    let counter = Arc::clone(&counter);
    handles.push(thread::spawn(move || { *counter.lock().unwrap() += 1; }));
}
for h in handles { h.join().unwrap(); }
```
Verify `RefCell`'s runtime borrow checks don't panic in production by testing all code paths that could cause overlapping mutable borrows, since `RefCell` moves the borrow-checker's guarantees from compile-time to a runtime panic.
**Pitfalls:** using `Rc<RefCell<T>>` reflexively for shared mutable state without considering whether ownership could instead be restructured to avoid it entirely; forgetting `RefCell::borrow_mut()` panics (not compile-errors) on an already-active borrow, turning a class of bugs invisible until a specific runtime code path executes.

## Cargo Workspaces and Feature Flags
Cargo workspaces let multiple related crates share a single `Cargo.lock` and build directory, while feature flags allow conditional compilation of optional functionality (and optional dependencies) without maintaining separate crate variants; verify feature unification behavior across a workspace: Cargo unifies enabled features for a dependency across all workspace members by default, which can unexpectedly enable a feature in one crate because a sibling crate needs it.
```toml
[workspace]
members = ["core", "cli", "server"]

[features]
default = ["std"]
std = []
async = ["dep:tokio"]
```
Verify a crate intended to be `no_std`-compatible or minimal-dependency doesn't accidentally get a heavier feature enabled due to workspace-wide feature unification from an unrelated sibling crate.
**Pitfalls:** assuming a crate's feature set is isolated within a workspace, then discovering an unrelated sibling crate's dependency requirement unified an unwanted feature into a supposedly minimal build; not testing a crate with `--no-default-features` explicitly, missing that its code implicitly depends on a "default" feature being enabled.

## Async Rust and Runtime Selection
Rust's `async`/`await` syntax is runtime-agnostic, the standard library provides only the building blocks (`Future` trait), while an actual executor (Tokio, async-std, smol) must be chosen and added as a dependency; verify a project doesn't accidentally mix incompatible async runtimes (a Tokio-specific type used inside an async-std context), since `Future`s from different ecosystems' I/O types are generally not interoperable without explicit compatibility shims.
```rust
#[tokio::main]
async fn main() {
    let response = reqwest::get("https://example.com").await.unwrap();
    println!("{}", response.status());
}
```
Verify library crates intended for broad reuse are runtime-agnostic in their public API (accepting generic `Future`s rather than hardcoding a specific runtime's types) unless deliberately scoping the crate to one runtime ecosystem.
**Pitfalls:** mixing Tokio-specific async I/O primitives with an async-std-based executor in the same binary, hitting confusing runtime panics about "no reactor running"; publishing a library that hardcodes a specific async runtime, forcing every downstream consumer onto that same runtime choice.

## Pattern Matching and Exhaustiveness in Rust
Rust's `match` expression requires exhaustive handling of all enum variants (or an explicit wildcard `_`), enforced at compile time, making it a strong tool for safely handling state machines and error variants; verify a match doesn't rely on a catch-all `_` arm where explicit handling of each case would be safer against future enum variant additions silently falling into the wrong branch.
```rust
enum ConnectionState { Connecting, Connected { session_id: String }, Disconnected { reason: String } }

fn handle(state: &ConnectionState) {
    match state {
        ConnectionState::Connecting => println!("connecting..."),
        ConnectionState::Connected { session_id } => println!("connected: {session_id}"),
        ConnectionState::Disconnected { reason } => println!("disconnected: {reason}"),
        // no wildcard: adding a new variant forces a compile error here until handled
    }
}
```
Verify a deliberately removed wildcard arm actually causes new variants to trigger compile errors (confirming exhaustiveness is truly enforced for the specific enum) rather than assuming it based on habit from other languages' `switch` statements.
**Pitfalls:** adding a catch-all `_` arm purely to satisfy the compiler without considering whether a new future variant should actually be handled explicitly, silently routing new cases into unintended default behavior; matching on borrowed data without considering whether the pattern needs `ref`/deref adjustments, causing ownership-related compile errors that are fixed incorrectly by cloning unnecessarily.

# Go Programming Fundamentals

## Slices, Arrays, and Underlying Array Sharing
Go slices are a view (pointer, length, capacity) over an underlying array; slicing an existing slice shares the same backing array, so mutating one slice can unexpectedly affect another that shares the same underlying memory, and `append` may or may not reallocate depending on remaining capacity, verify actual sharing/reallocation behavior with a small test rather than assuming independence.
```go
original := make([]int, 3, 5)
copy(original, []int{1, 2, 3})
alias := original[:2]
alias = append(alias, 99)   // capacity allows this to write into original's backing array
fmt.Println(original)        // [1 2 99], original was mutated through alias
```
Verify whether a function receiving a slice parameter is expected to mutate the caller's underlying array or not, and use `copy()` explicitly to create an independent slice when isolation is required.
**Pitfalls:** assuming slicing always creates an independent copy, then being surprised when appending to a sub-slice corrupts data in the original slice due to shared backing-array capacity; passing a slice into a goroutine without considering that concurrent appends from multiple goroutines can race on the same backing array.

## Defer, Panic, and Recover Semantics
`defer` schedules a function call to run when the surrounding function returns (LIFO order for multiple defers), commonly used for cleanup; `panic` unwinds the stack running deferred calls along the way, and `recover` (only effective when called directly inside a deferred function) can stop a panic from propagating further. Verify recover is placed correctly, since calling it outside a deferred function has no effect and the panic continues unimpeded.
```go
func safeDivide(a, b int) (result int, err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("recovered from panic: %v", r)
        }
    }()
    return a / b, nil   // panics on b == 0, caught by the deferred recover above
}
```
Verify `recover` is used sparingly and deliberately at clear boundary points (like an HTTP server's top-level request handler) rather than scattered throughout business logic to paper over unexpected errors that should instead be handled as ordinary returned `error` values.
**Pitfalls:** calling `recover()` outside of a directly deferred function, having no effect and letting the panic crash the program anyway; overusing `panic`/`recover` as a general error-handling mechanism instead of Go's idiomatic explicit `error` return values, fighting the language's conventions.

## Struct Embedding and Composition
Go achieves composition-based code reuse through struct embedding (an anonymous field), which promotes the embedded type's methods and fields to the outer struct, resembling but distinct from inheritance, verify method resolution/shadowing behaves as expected when both the embedding and embedded types define a method with the same name, since Go's rule (outer type's method wins) can be surprising if not verified explicitly.
```go
type Base struct{ Name string }
func (b Base) Describe() string { return "Base: " + b.Name }

type Derived struct {
    Base          // embedded: Describe() and Name are promoted
    Extra string
}
```
Verify embedding doesn't silently create ambiguous method promotion when embedding multiple types with overlapping method names, which produces a compile error only when the ambiguous method is actually called, not at the embedding declaration itself.
**Pitfalls:** assuming struct embedding provides polymorphic method overriding like class inheritance in other languages, when Go's embedding is really field/method promotion with no dynamic dispatch involved; embedding multiple types with colliding method names and only discovering the resulting ambiguity error when the method is actually invoked, not at compile time of the struct definition.

## Context Propagation for Cancellation and Deadlines
Go's `context.Context` propagates cancellation signals, deadlines, and request-scoped values through a call chain, and is the idiomatic way to bound the lifetime of any operation that could otherwise run indefinitely (an HTTP request, a database query); verify context is actually threaded through every downstream call that supports it, since a context cancellation is a no-op if the function ignores its context parameter entirely.
```go
func fetchWithTimeout(ctx context.Context, url string) ([]byte, error) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()
    req, _ := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
    resp, err := http.DefaultClient.Do(req)
    if err != nil { return nil, err }
    defer resp.Body.Close()
    return io.ReadAll(resp.Body)
}
```
Verify `defer cancel()` is always called even on the success path (a very common oversight) to release resources associated with the context's timer, since forgetting it leaks timers until the parent context itself is cancelled or expires.
**Pitfalls:** creating a derived context with `WithTimeout`/`WithCancel` and forgetting to call the returned `cancel` function, leaking the associated timer/goroutine; passing `context.Background()` deep into a call chain instead of the actual request-scoped context, silently losing cancellation/deadline propagation.
