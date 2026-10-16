# Java Programming Fundamentals

## JDK Version, LTS Status, and Bytecode Target Grounding
Java's language features (records, sealed classes, pattern matching, virtual threads) are tied to specific JDK versions, and only certain releases (8, 11, 17, 21, 25) are LTS; verify the exact JDK version, vendor (OpenJDK, Temurin, Oracle), and target bytecode level before assuming a feature or its finalized (non-preview) status.
```bash
java -version
javac -version
mvn -version   # or: gradle -version
```
```xml
<properties><maven.compiler.release>21</maven.compiler.release></properties>
```
**Pitfalls:** using a preview feature (`--enable-preview` required) in production code without noting it's not yet stable/final in that release; assuming a feature available in the latest LTS is available in an older LTS still running in production.

## Object Equality, hashCode Contracts, and Collections
Overriding `equals()` without also overriding `hashCode()` (and keeping them consistent) breaks hash-based collections (`HashMap`, `HashSet`) silently, objects that are "equal" can end up in different buckets, causing lookups to fail unexpectedly. Verify the equals/hashCode contract holds with an explicit test rather than assuming IDE-generated code is automatically correct after further field changes.
```java
public final class Point {
    private final int x, y;
    @Override public boolean equals(Object o) {
        if (!(o instanceof Point p)) return false;
        return x == p.x && y == p.y;
    }
    @Override public int hashCode() { return Objects.hash(x, y); }
}
```
Confirm mutable fields used in `hashCode()` aren't mutated after an object is placed in a `HashSet`/`HashMap` key position, since that silently corrupts the collection's internal bucket structure.
**Pitfalls:** overriding `equals()` and forgetting `hashCode()`, breaking `HashMap`/`HashSet` membership checks; using a mutable object with a mutable-field-based `hashCode()` as a map key, then mutating it after insertion.

## Checked Exceptions and Exception Hierarchy Design
Java distinguishes checked exceptions (must be declared or caught, `IOException`) from unchecked (`RuntimeException` and subclasses, not enforced by the compiler); verify whether a new custom exception should be checked (recoverable, caller should handle) or unchecked (programming error, shouldn't normally be caught broadly) based on actual recoverability, not habit.
```java
public class InsufficientFundsException extends Exception {   // checked: caller must decide how to handle
    public InsufficientFundsException(String message) { super(message); }
}

public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance) throw new InsufficientFundsException("balance too low");
}
```
Verify a `catch (Exception e)` block isn't silently swallowing unrelated unchecked exceptions (like `NullPointerException`) meant to surface as bugs, by scoping catches to the narrowest applicable exception type.
**Pitfalls:** catching `Exception` broadly to satisfy the compiler's checked-exception requirement, accidentally swallowing unrelated runtime bugs; overusing checked exceptions for conditions that are really unrecoverable programming errors, forcing boilerplate `try/catch` everywhere.

## Concurrency: Threads, Executors, and Virtual Threads
Java's concurrency utilities (`ExecutorService`, `CompletableFuture`, and virtual threads finalized in JDK 21) each fit different workloads; verify the actual JDK version supports virtual threads before assuming lightweight-thread-per-task scaling, and confirm thread-pool sizing is based on measured workload (CPU-bound vs I/O-bound), not a copied default.
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    List<Future<String>> futures = urls.stream()
        .map(url -> executor.submit(() -> fetch(url)))
        .toList();
    for (var f : futures) System.out.println(f.get());
}
```
Verify no code pinning virtual threads to platform threads occurs (e.g., via `synchronized` blocks around blocking I/O in older JDK 21 releases), which defeats the scalability benefit, check current JDK release notes for pinning caveats.
**Pitfalls:** sizing a fixed thread pool by copying a number from a tutorial instead of measuring actual CPU core count and workload type; using `synchronized` around blocking calls inside virtual threads on JDK versions where this caused thread pinning.

# C++ Programming Fundamentals

## Standard Version and Compiler Flag Grounding
C++ behavior changes significantly across standards (C++11 through C++23) and compiler (`gcc`, `clang`, `msvc`); verify both the language standard flag actually passed to the compiler and its version support before assuming a feature like concepts, ranges, or coroutines is available.
```bash
g++ --version
g++ -std=c++20 -Wall -Wextra -c file.cpp
echo '#include <version>
#ifdef __cpp_concepts
#endif' | g++ -std=c++20 -E -
```
Verify actual feature-test macros (`__cpp_lib_ranges`, etc.) at compile time rather than assuming a standard version implies full library support, since standard library implementations lag behind language standard adoption.
**Pitfalls:** assuming `-std=c++20` alone guarantees a specific library feature is implemented by the actual standard library shipped with the compiler; mixing object files compiled with different standard versions or ABI-incompatible compiler flags.

## RAII and Resource Ownership
Resource Acquisition Is Initialization ties resource lifetime to object scope via constructors/destructors, making `std::unique_ptr`, `std::vector`, and lock guards automatically release resources on scope exit, even during exception unwinding, eliminating most manual cleanup bugs. Verify no raw `new`/`delete` or manual resource management exists where an RAII wrapper would be safer.
```cpp
void process(const std::string& path) {
    std::ifstream file(path);              // RAII: closed automatically on scope exit
    std::lock_guard<std::mutex> lock(mtx); // RAII: unlocked automatically, even on exception
    if (!file) throw std::runtime_error("cannot open file");
    // ... use file ...
}   // destructors run here regardless of how the function exits
```
Verify with a deliberate exception-throwing test path that resources still release correctly, since manual `try/finally`-style cleanup is easy to get wrong compared to RAII's automatic guarantee.
**Pitfalls:** using raw `new`/`delete` instead of smart pointers, leaking memory on an exception path that skips the `delete`; forgetting a mutex lock's scope, holding it far longer than needed and creating contention.

## Undefined Behavior and Sanitizer-Verified Correctness
C++ has a large surface of undefined behavior (out-of-bounds access, use-after-free, signed integer overflow, strict aliasing violations) where the compiler is permitted to do anything, including seemingly "working" code that breaks under a different optimization level. Verify suspect code with sanitizers rather than trusting that a lack of a crash means correctness.
```bash
g++ -std=c++20 -fsanitize=address,undefined -g -O1 file.cpp -o file_sanitized
./file_sanitized
```
```cpp
int arr[5];
arr[5] = 1;   // UB: out-of-bounds write, may silently "work" in an unoptimized build and corrupt memory in an optimized one
```
Run the full test suite under AddressSanitizer/UndefinedBehaviorSanitizer in CI, not just locally, since UB manifestation is highly sensitive to compiler, optimization level, and memory layout.
**Pitfalls:** treating "it ran without crashing" as proof of correctness for pointer/array code, when UB can silently corrupt memory without immediate symptoms; relying on signed integer overflow wrapping behavior, which is undefined (not guaranteed to wrap) in standard C++.

## Move Semantics and Copy Elision
Move semantics (`std::move`, move constructors) let resources be transferred instead of deep-copied when a source object is about to be destroyed anyway; verify a type actually implements efficient move operations (or relies on the compiler-generated ones being correct) before assuming a `std::vector<LargeObject>` push is cheap.
```cpp
class Buffer {
    std::unique_ptr<char[]> data;
    size_t size;
public:
    Buffer(Buffer&& other) noexcept : data(std::move(other.data)), size(other.size) { other.size = 0; }
};
```
Verify with `-fsanitize=address` or an instrumented build whether an object is being needlessly copied instead of moved (e.g., missing `std::move` on an rvalue-eligible local, or a move constructor lacking `noexcept`, which prevents `std::vector` from using it during reallocation).
**Pitfalls:** forgetting `noexcept` on a move constructor, causing `std::vector` to fall back to copying during reallocation for exception-safety guarantees; using `std::move` on an object still needed afterward, leaving it in a valid-but-unspecified emptied state that's then accidentally read.

# Java Programming Fundamentals

## Generics, Type Erasure, and Wildcards
Java generics are implemented via type erasure, generic type information is removed at compile time, meaning `List<String>` and `List<Integer>` share one runtime class (`List`), which explains why you can't create a generic array directly or check `instanceof List<String>`. Verify wildcard usage (`? extends T` for read-only producer, `? super T` for write-only consumer, the PECS mnemonic) matches the actual variance needed rather than guessing.
```java
public static double sumOfList(List<? extends Number> list) {   // producer: read-only, covariant
    double sum = 0;
    for (Number n : list) sum += n.doubleValue();
    return sum;
}
```
Verify a generic method's bound actually permits the intended call sites by testing with both a `List<Integer>` and `List<Double>` argument, confirming the wildcard variance is neither too restrictive nor accidentally too permissive.
**Pitfalls:** attempting `new T[10]` inside a generic class, hitting a compile error due to type erasure preventing generic array creation; using an unbounded wildcard or the wrong PECS direction, either over-restricting valid callers or under-restricting to allow unsafe writes.

## Immutability and the Builder Pattern for Complex Objects
Immutable objects (all fields `final`, no setters, defensive copies of mutable fields in constructors) are inherently thread-safe and easier to reason about; the Builder pattern (or Java 16+ `record` for simpler cases) provides readable construction for objects with many fields without a telescoping constructor or error-prone setter-based partial construction.
```java
public final class HttpRequestConfig {
    private final int timeoutMs;
    private final Map<String, String> headers;
    private HttpRequestConfig(Builder b) {
        this.timeoutMs = b.timeoutMs;
        this.headers = Map.copyOf(b.headers);   // defensive copy, prevents external mutation
    }
    public static class Builder {
        private int timeoutMs = 5000;
        private Map<String, String> headers = new HashMap<>();
        public Builder timeout(int ms) { this.timeoutMs = ms; return this; }
        public HttpRequestConfig build() { return new HttpRequestConfig(this); }
    }
}
```
Verify defensive copies are actually made for mutable field types (collections, arrays, `Date`) in both the constructor and any getter, since returning the internal mutable reference directly breaks the immutability guarantee even if the constructor copied correctly.
**Pitfalls:** accepting a mutable collection/array in a constructor without copying it, allowing external code to mutate the "immutable" object's internal state after construction; returning an internal mutable field directly from a getter, letting callers mutate it and break the immutability contract from the outside.

## Streams API and Functional-Style Collection Processing
The Streams API (`stream()`, `map`, `filter`, `collect`) enables declarative collection processing, but verify streams are used for genuinely beneficial cases, a stream pipeline over a small collection with a simple transformation can be less readable and slightly slower than an equivalent enhanced `for` loop due to lambda/pipeline overhead, and parallel streams (`parallelStream()`) require careful verification that the underlying operation is actually stateless and thread-safe.
```java
List<String> activeUserEmails = users.stream()
    .filter(User::isActive)
    .map(User::getEmail)
    .sorted()
    .collect(Collectors.toList());
```
Verify `parallelStream()` actually improves performance with a real benchmark before adopting it, since the common ForkJoinPool it uses by default is shared application-wide, and a non-trivial parallel stream operation can starve unrelated parallel work elsewhere in the same JVM.
**Pitfalls:** reaching for `parallelStream()` on a small collection or I/O-bound operation, adding overhead without benefit and potentially introducing thread-safety bugs in a supposedly "stateless" lambda that actually mutates shared state; chaining an excessively long stream pipeline that sacrifices readability for a marginal functional-style preference over a clear imperative loop.

## Java Memory Model and Volatile/Synchronized Visibility
The Java Memory Model defines when writes by one thread become visible to reads by another; without proper synchronization (`synchronized`, `volatile`, `java.util.concurrent` atomics), a thread may never observe another thread's write due to compiler/CPU reordering and per-core caching, verify visibility guarantees explicitly rather than assuming a plain field read always sees the latest write from another thread.
```java
public class FlagHolder {
    private volatile boolean shutdownRequested = false;   // volatile ensures visibility across threads
    public void requestShutdown() { shutdownRequested = true; }
    public boolean isShutdownRequested() { return shutdownRequested; }
}
```
Verify a suspected visibility bug (a worker thread "never sees" a flag change) with a controlled multi-threaded test rather than assuming the field access was already thread-safe because it "usually works" in ad hoc manual testing, since visibility bugs are highly timing- and JIT-optimization-dependent.
**Pitfalls:** reading/writing a shared field without `volatile` or synchronization and assuming the JVM guarantees prompt cross-thread visibility, when the compiler/CPU are free to cache or reorder in the absence of explicit memory barriers; using `volatile` for compound operations (`counter++`) that aren't actually atomic despite the field itself being visibility-safe, still requiring `AtomicInteger` or synchronization for correctness.

# C++ Programming Fundamentals

## Templates and Compile-Time Polymorphism
C++ templates generate specialized code per instantiated type at compile time (similar in spirit to Rust generics' monomorphization), enabling zero-overhead generic programming; verify template error messages (often long and cryptic, especially pre-C++20) actually point to the real constraint violation, and prefer C++20 concepts to constrain template parameters with readable, enforceable requirements instead of relying on SFINAE tricks.
```cpp
template <typename T>
concept Numeric = std::is_arithmetic_v<T>;

template <Numeric T>
T clamp(T value, T lo, T hi) {
    return value < lo ? lo : (value > hi ? hi : value);
}
```
Verify a concept-constrained template actually produces a clear compile-time error (naming the failed concept) when instantiated with an invalid type, confirming the constraint is doing real work rather than being silently bypassed by an unconstrained overload.
**Pitfalls:** relying on old-style SFINAE (`std::enable_if`) for constraints in a C++20-capable codebase, producing far less readable errors than concepts would; forgetting that each template instantiation for a distinct type generates separate compiled code, causing unexpectedly large binaries for heavily templated, multi-type-instantiated code.

## The Rule of Three/Five/Zero for Resource-Managing Classes
A class managing a raw resource (owning a pointer, file handle) must carefully define (or explicitly delete) its copy constructor, copy assignment, destructor (Rule of Three), and move constructor/move assignment (Rule of Five) to avoid double-frees or resource leaks from compiler-generated defaults that perform shallow copies; the Rule of Zero recommends instead composing only RAII-wrapping members (`std::unique_ptr`, `std::vector`) so the compiler-generated special members are already correct.
```cpp
class Buffer {   // Rule of Zero: no manual resource management needed
    std::unique_ptr<char[]> data;
    size_t size;
public:
    Buffer(size_t n) : data(std::make_unique<char[]>(n)), size(n) {}
    // compiler-generated move ctor/assignment are correct; copy is implicitly deleted via unique_ptr
};
```
Verify a class holding a raw owning pointer explicitly defines or `= delete`s all five special member functions rather than leaving the compiler-generated (shallow-copying) defaults in place, which is the single most common source of double-free/use-after-free bugs in C++ codebases.
**Pitfalls:** leaving a class with a raw owning pointer member to use compiler-generated copy semantics, causing a double-free when two copies both try to delete the same pointer in their destructors; following the Rule of Three/Five when the Rule of Zero (composing RAII members) would eliminate the need for any manual special member definitions at all.

## Const-Correctness and Compile-Time Guarantees
`const` correctness lets the compiler enforce that a function/method doesn't (and can't accidentally) mutate data it shouldn't, catching a class of bugs at compile time; verify member functions that don't modify object state are actually marked `const`, and that pointers/references distinguish `const T*` (pointer to const data) from `T* const` (const pointer to mutable data) correctly for the intended guarantee.
```cpp
class Matrix {
    std::vector<double> data;
public:
    double at(size_t i) const { return data[i]; }        // read-only: correctly marked const
    void set(size_t i, double v) { data[i] = v; }         // mutates: correctly non-const
};
```
Verify a `const`-qualified method genuinely cannot mutate observable state (watch for `mutable` members used to bypass this for caching, which should be verified not to leak actual logical state changes) by reviewing every `mutable`-marked field's usage.
**Pitfalls:** omitting `const` on methods that don't modify state, preventing them from being called on `const` object references/parameters elsewhere in the codebase; overusing `mutable` to silence const-correctness errors instead of properly separating logical constness (observable behavior) from physical constness (bit-level object state).

## Exception Safety Guarantees
C++ exception safety is categorized into levels, no-throw guarantee (never throws), strong guarantee (operation either fully succeeds or leaves state unchanged, "commit or rollback"), and basic guarantee (no leaks, but partial state changes possible on exception); verify which guarantee a given function actually provides and documents, since assuming a stronger guarantee than what's implemented can lead to corrupted state after an exception during a supposedly atomic operation.
```cpp
void Container::push_back_strong(T value) {
    if (size == capacity) {
        auto new_data = std::make_unique<T[]>(capacity * 2);  // allocation can throw here safely
        std::move(data.get(), data.get() + size, new_data.get());
        data = std::move(new_data);   // no-throw: swap only happens after allocation succeeds
        capacity *= 2;
    }
    data[size++] = std::move(value);
}
```
Verify exception-safety claims with a deliberate fault-injection test (a type whose constructor/move throws partway through a container operation) to confirm the container is left in a valid, documented state rather than a corrupted one.
**Pitfalls:** assuming the strong exception-safety guarantee applies to a function that was never actually designed or tested for it, leading to corrupted object state after a caught exception; performing a resizing/reallocation operation that mutates existing state before a potentially-throwing step completes, violating the strong guarantee if that step fails.
