# Python Core Language

## Interpreter Version and Build Grounding
Never assume Python semantics from memory alone, behavior changes across minor versions (e.g., `match` statements need 3.10+, exception groups need 3.11+, the GIL becomes optional in 3.13 free-threaded builds). Before writing or debugging code, run the interpreter that will actually execute it and capture its exact identity.
```bash
python3 --version          # Python 3.12.4
python3 -c "import sys; print(sys.version_info, sys.implementation.name)"
python3 -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
```
Record the output verbatim in your notes before claiming a feature "works" or "doesn't exist." CPython, PyPy, and GraalPy diverge on GC timing, C-extension support, and startup cost, so also confirm `sys.implementation.name` when performance or C-API behavior matters.
**Pitfalls:** assuming a walrus operator, `tomllib`, or `except*` is available without checking the minimum supported version; conflating `python` and `python3` on systems where they point to different installs.

## Data Model and Object Semantics
Every Python value is an object with identity, type, and value; assignment binds names to objects rather than copying them. This underlies aliasing bugs with mutable defaults, list copies, and `is` vs `==`.
```python
def append_item(item, bucket=[]):   # BUG: default list is created once
    bucket.append(item)
    return bucket

print(append_item(1))  # [1]
print(append_item(2))  # [1, 2]  <- surprising shared state
```
Fix by defaulting to `None` and creating the container inside the function. Verify identity assumptions with `id()` and `is`, and confirm small-int/string caching behavior (`a is b` for small ints) is a CPython implementation detail, not a language guarantee.
**Pitfalls:** relying on integer/string interning across versions or implementations; using `==` when identity is intended for singletons like `None`.

## Iterators, Generators, and Laziness
Generators (`yield`) and generator expressions produce values lazily and are exhausted after one full traversal. Confusing a generator with a list causes silent empty-result bugs when a generator is iterated twice.
```python
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

lines = read_large_file("data.txt")
first_pass = [l for l in lines if l]
second_pass = [l for l in lines if l]   # always [], generator is exhausted
```
Use `itertools.tee`, materialize to a list when reuse is needed, or restructure as a function that returns a fresh generator each call. Check `inspect.isgenerator`/`isgeneratorfunction` when debugging unexpected empty results.
**Pitfalls:** passing a generator to a function that iterates it more than once; assuming generator expressions support indexing or `len()`.

## Exception Handling and Control Flow
Python exceptions are the primary control-flow mechanism for error handling; overly broad `except:` clauses hide bugs (including `KeyboardInterrupt` and `SystemExit`). Use precise exception types, `finally` for cleanup, and 3.11+ `except*` for exception groups from concurrent tasks.
```python
try:
    value = int(user_input)
except ValueError as exc:
    raise ValueError(f"invalid integer: {user_input!r}") from exc
finally:
    log.debug("input processing attempted")
```
Verify custom exception hierarchies inherit from `Exception`, not `BaseException`, unless intentionally bypassing normal handling. Use `traceback.print_exc()` or `logging.exception()` to capture the real chain instead of re-raising with lost context.
**Pitfalls:** swallowing exceptions with bare `except: pass`; losing the original traceback by raising a new exception without `from exc`.

## Decorators, Closures, and Scope
Decorators are ordinary functions that wrap other functions; understanding closures (free variables captured by reference, not value) is essential to avoid late-binding bugs in loops.
```python
handlers = []
for i in range(3):
    def handler(i=i):        # default arg captures value at definition time
        return i
    handlers.append(handler)
print([h() for h in handlers])  # [0, 1, 2], not [2, 2, 2]
```
When writing decorators that take arguments, use `functools.wraps` to preserve `__name__`/`__doc__`, and confirm whether the wrapped callable is a function, method, or class before assuming `self` handling.
**Pitfalls:** capturing loop variables in closures without a default-argument or factory-function fix; forgetting `functools.wraps` and breaking introspection/tools like `pytest` fixtures.

## Typing and Static Analysis
Type hints are not enforced at runtime by default; `mypy`, `pyright`, or `pyrefly` must be run explicitly, and their behavior depends on the exact tool version and `strict` settings. Verify the installed checker version before trusting a "no errors" result.
```bash
pip show mypy | grep Version
mypy --strict src/
```
```python
from typing import TypedDict, NotRequired

class UserRecord(TypedDict):
    id: int
    email: str
    nickname: NotRequired[str]   # requires typing_extensions or Python 3.11+
```
Cross-check that `NotRequired`, `Self`, or `override` are available in the running Python/typing_extensions version before using them in production code.
**Pitfalls:** trusting hints as runtime guarantees; using new typing constructs unsupported by the pinned checker version, causing CI-only failures.

## Packaging, Virtual Environments, and Reproducibility
Use isolated environments (`venv`, `uv venv`, or `conda`) per project, and pin exact versions in a lockfile (`requirements.txt` with hashes, `poetry.lock`, or `uv.lock`). Verify which resolver produced the lock and its date.
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.lock.txt
python -c "import requests; print(requests.__version__)"
```
Prefer `uv pip compile` or `pip-tools` for reproducible resolution, and record the resolver tool + version alongside the lockfile since resolution algorithms differ.
**Pitfalls:** installing globally with `sudo pip install`; assuming `requirements.txt` without hashes is reproducible across machines with different available wheels.

## Context Managers and Resource Safety
`with` statements guarantee cleanup via `__enter__`/`__exit__` even on exceptions; prefer them over manual `try/finally` for files, locks, sockets, and DB connections. Custom context managers can be written with classes or `contextlib.contextmanager`.
```python
from contextlib import contextmanager
import time

@contextmanager
def timed(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.4f}s")

with timed("query"):
    run_query()
```
Verify that any custom `__exit__` correctly returns `False`/`None` to propagate exceptions unless suppression is intended, since swallowing exceptions silently is a common resource-management bug.
**Pitfalls:** forgetting that `__exit__` returning `True` silently suppresses exceptions; opening files without `with` and leaking file descriptors under error paths.

# Python Standard Library & Tooling

## Dataclasses and Structured Records
`dataclasses.dataclass` generates `__init__`, `__repr__`, and `__eq__` from field annotations, reducing boilerplate for plain data holders. Use `frozen=True` for immutability and `field(default_factory=...)` for mutable defaults.
```python
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float
    tags: tuple[str, ...] = field(default_factory=tuple)

p = Point(1.0, 2.0)
```
`slots=True` requires Python 3.10+; verify the running version before relying on it for memory savings. Confirm equality/ordering semantics by checking generated `__eq__`/`__lt__` match your intent, or set `order=True` explicitly.
**Pitfalls:** using a mutable default like `[]` directly in a field instead of `default_factory`; assuming dataclasses are as fast as `__slots__`-only classes without verifying with a profiler.

## pathlib for Filesystem Operations
`pathlib.Path` provides an object-oriented, cross-platform API superior to raw string manipulation with `os.path`. It composes with `/`, resolves symlinks, and integrates with `open()`.
```python
from pathlib import Path

root = Path(__file__).resolve().parent
config = root / "config" / "settings.toml"
if config.exists():
    text = config.read_text(encoding="utf-8")
for py_file in root.rglob("*.py"):
    print(py_file.relative_to(root))
```
Verify path separator and case-sensitivity assumptions on the target OS before shipping cross-platform code; `Path` normalizes separators but not case-sensitivity behavior.
**Pitfalls:** mixing `os.path.join` string outputs with `Path` objects inconsistently; assuming `Path.resolve()` behaves identically across OSes for symlink cycles.

## Concurrency Primitives: threading, multiprocessing, asyncio
Choose based on the actual bottleneck: `threading` helps I/O-bound work despite the GIL, `multiprocessing` bypasses the GIL for CPU-bound work at the cost of IPC overhead, and `asyncio` gives cooperative concurrency for I/O without OS thread overhead. Confirm with profiling which category the workload falls into before picking a model.
```python
import asyncio, httpx

async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(u) for u in urls]
        return await asyncio.gather(*tasks)
```
On 3.13+, check whether the interpreter is a free-threaded (`--disable-gil`) build, since threading performance characteristics for CPU-bound code change substantially.
**Pitfalls:** using `threading` for CPU-bound number crunching and being surprised the GIL serializes it; forgetting `await` and silently creating unawaited coroutine warnings.

## Logging Configuration
The `logging` module is the standard way to emit diagnostics; `print()` does not support levels, handlers, or structured output. Configure a root logger once, and use `logging.getLogger(__name__)` per module.
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)
logger.info("service started", extra={"port": 8080})
```
Verify handler propagation and duplicate-handler bugs by inspecting `logger.handlers` and `logger.propagate`, especially in libraries that call `basicConfig` more than once (a no-op after first call unless `force=True`).
**Pitfalls:** calling `logging.basicConfig` multiple times expecting reconfiguration; logging secrets or PII in `extra` fields that reach shared log sinks.

## argparse and Command-Line Interfaces
`argparse` builds self-documenting CLIs with type coercion, subcommands, and auto-generated `--help`. For larger CLIs, verify whether `click` or `typer` is already a project dependency before reinventing parsing.
```python
import argparse

parser = argparse.ArgumentParser(description="Process a dataset")
parser.add_argument("input", type=Path)
parser.add_argument("--limit", type=int, default=100)
sub = parser.add_subparsers(dest="command", required=True)
sub.add_parser("validate")
args = parser.parse_args()
```
Test the actual `--help` output and exit codes (`argparse` calls `sys.exit(2)` on bad input) rather than assuming behavior, since custom `type=` callables changed error message formatting across versions.
**Pitfalls:** assuming `type=int` gives friendly errors for non-numeric input without testing; forgetting `required=True` on subparsers and getting `None` silently.

## Testing with pytest: Fixtures and Parametrization
`pytest` fixtures manage setup/teardown with dependency injection via function parameters; `@pytest.mark.parametrize` runs the same test logic across many inputs. Confirm the installed `pytest` version supports features like fixture `scope="session"` caching as documented.
```python
import pytest

@pytest.fixture
def db_session():
    conn = create_test_db()
    yield conn
    conn.rollback()

@pytest.mark.parametrize("value,expected", [(0, False), (1, True), (-1, True)])
def test_is_nonzero(value, expected):
    assert bool(value) == expected
```
Run `pytest --collect-only` to verify tests are actually discovered before trusting a green run, and check `pytest -q --version` to align syntax with the installed release.
**Pitfalls:** naming test files without a `test_` prefix and having them silently skipped; fixture scope leaking state between tests when marked `session` incorrectly.

## Serialization: json, pickle, and Safety Boundaries
`json` is safe for cross-language interchange but only supports a limited type set; `pickle` supports arbitrary Python objects but executes arbitrary code on load and must never be used on untrusted input. Verify the data's trust boundary before choosing a format.
```python
import json

payload = json.dumps({"id": 1, "tags": ["a", "b"]}, ensure_ascii=False)
data = json.loads(payload)
```
For pickle, confirm protocol version compatibility across Python versions with `pickle.HIGHEST_PROTOCOL`, and never call `pickle.load()` on data from an untrusted network source or file upload.
**Pitfalls:** using `pickle` for API payloads or cache values that cross a trust boundary; assuming `json.dumps` handles `datetime` or `Decimal` without a custom encoder.

## Packaging a Distributable Project with pyproject.toml
Modern Python packaging centers on `pyproject.toml` with a build backend (`hatchling`, `setuptools`, `flit-core`); verify which backend and Python requirement is declared before adding dependencies.
```toml
[project]
name = "mypackage"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["httpx>=0.27,<0.28"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```
Build and verify the artifact before publishing: `python -m build` then `twine check dist/*`, and install the built wheel in a clean venv to confirm it actually imports.
**Pitfalls:** publishing a package that only works because of files present in the dev checkout but excluded from the sdist/wheel; mismatched `requires-python` versus features actually used in the code.
