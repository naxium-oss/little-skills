# Deno Runtime Fundamentals

## Deno Version and Permission Model Grounding
Deno is secure-by-default: scripts have no filesystem, network, or environment access unless explicitly granted via flags. Verify the exact Deno version and required permission flags before running unfamiliar scripts.
```bash
deno --version                     # deno 2.1.4 (release, x86_64-unknown-linux-gnu)
deno run --allow-net=api.example.com --allow-env=API_KEY server.ts
```
Deno 2.x changed npm compatibility and workspace behavior substantially versus Deno 1.x; confirm major version before trusting older tutorials or Stack Overflow answers.
**Pitfalls:** running with `--allow-all`/`-A` out of convenience in production, defeating the sandboxing model; assuming Deno 1.x npm/node compatibility docs apply unchanged to Deno 2.x.

## Native TypeScript, Web APIs, and JSR/npm Imports
Deno runs TypeScript natively without a build step and prioritizes Web Platform APIs (`fetch`, `WebSocket`, `URL`) over Node-specific globals. Dependencies are imported by URL or specifier (`npm:`, `jsr:`) rather than requiring a `node_modules`-centric `package.json`.
```typescript
import { serve } from "jsr:@std/http/file-server";
import express from "npm:express@4.21.1";

Deno.serve({ port: 8000 }, (req) => new Response("hello deno"));
```
Verify pinned versions in import specifiers (`npm:express@4.21.1` vs unpinned `npm:express`) since unpinned imports can silently drift on cache invalidation.
**Pitfalls:** mixing unpinned URL imports across a team, causing "works on my machine" drift; assuming every npm package works flawlessly under Deno's Node compatibility layer without testing.

## deno.json Configuration and Import Maps
`deno.json`/`deno.jsonc` centralizes formatting, linting, tasks, compiler options, and import aliases (replacing scattered config files from the Node ecosystem). Verify the resolved config with `deno info` before debugging import errors.
```json
{
  "tasks": { "dev": "deno run --watch --allow-net main.ts" },
  "imports": { "@std/assert": "jsr:@std/assert@^1.0.0" },
  "compilerOptions": { "strict": true }
}
```
```bash
deno task dev
deno info main.ts     # shows resolved dependency graph
```
**Pitfalls:** assuming an import alias defined in `deno.json` is available without re-running with `--config` pointing at the right file in monorepos; forgetting `deno.lock` needs committing for reproducible resolution.

## Built-in Tooling: Test, Lint, Format, Bench
Deno bundles a test runner, linter, formatter, and benchmarking tool with zero external dependencies, all invoked as subcommands with consistent flags across projects.
```bash
deno test --allow-net --coverage=cov_profile
deno lint
deno fmt --check
deno bench
```
```typescript
Deno.test("adds numbers", () => {
  if (1 + 1 !== 2) throw new Error("math is broken");
});
```
Verify `deno test` permission flags match what the code under test actually needs, tests fail closed (permission denied) rather than silently succeeding with missing access.
**Pitfalls:** assuming `deno fmt`/`deno lint` rules match Prettier/ESLint defaults exactly; omitting `--allow-*` flags on CI test runs and getting permission-denied failures unrelated to actual test logic.

## Deno Deploy and Edge Runtime Constraints
Deno Deploy (and similar edge runtimes) run V8 isolates rather than full OS processes, imposing restrictions (no arbitrary filesystem access, limited subset of Node compatibility, execution time/memory caps) that differ from a local `deno run` environment. Verify actual constraints against the specific deployment target's current documented limits before assuming local behavior transfers unchanged.
```typescript
Deno.serve((req) => new Response("hello from the edge"));
```
Test with the platform's actual local emulator/CLI before deploying, since some Node built-ins available locally under Deno's compatibility layer may be unavailable or behave differently in the isolate-based production environment.
**Pitfalls:** assuming full filesystem/network access identical to local development once deployed to an edge isolate runtime; not checking the platform's specific cold-start and execution-time limits before deploying a long-running task.

## Permissions Auditing for Third-Party Modules
Because Deno requires explicit permission grants, auditing exactly which permissions a script (and its imported third-party modules) actually needs is a meaningful security practice, run with no permissions first and add only what's demonstrably required, verified by the specific `PermissionDenied` errors encountered.
```bash
deno run main.ts                     # start with zero permissions
# error: Requires net access to "api.example.com", add narrowly, not with -A
deno run --allow-net=api.example.com main.ts
```
Verify third-party dependencies aren't requesting broader permissions than their stated purpose (a data-formatting library asking for `--allow-net` is a red flag) by reading their source before granting blanket trust.
**Pitfalls:** defaulting to `--allow-all` to make errors go away without investigating which specific permission was actually needed; trusting a third-party module's permission requirements without spot-checking its source for unexpected network/filesystem access.

## Deno's Standard Library Version Pinning
Deno's `@std` library ships as independently versioned JSR packages rather than a single bundled runtime version, meaning different `@std` modules can be at different maturity/version levels; verify each imported `@std` module's specific version and stability status (some are still pre-1.0 and change behavior between releases) rather than assuming the whole standard library moves in lockstep.
```json
{ "imports": { "@std/path": "jsr:@std/path@^1.0.0", "@std/testing": "jsr:@std/testing@^1.0.5" } }
```
Check each module's own changelog on JSR before upgrading, since a `@std/path@2.x` bump can carry breaking changes independent of the Deno runtime version itself.
**Pitfalls:** assuming all `@std` modules share one version number and upgrading them as a monolith; relying on a pre-1.0 `@std` module's API shape without pinning an exact version, then having a routine update silently change function signatures.

## Node Compatibility Layer Verification
Deno's `node:` specifier compatibility layer lets many existing npm packages run unmodified, but coverage of Node-specific APIs (native addons, some `fs` edge cases, certain `process` behaviors) is incomplete and evolves per release; verify a specific package actually works under Deno with a real smoke test rather than assuming compatibility from the package's popularity alone.
```typescript
import { readFileSync } from "node:fs";
import process from "node:process";
console.log(process.platform, readFileSync("./data.txt", "utf8").length);
```
Run the target package's own test suite under Deno (`deno test --allow-all` against a vendored copy) before depending on it in production, since silent partial-compatibility bugs are more common than hard failures.
**Pitfalls:** assuming a popular npm package "just works" under Deno without running its actual test suite in the target environment; hitting a native Node addon dependency that has no Deno-compatible equivalent, blocking migration entirely.

# Git Fundamentals

## Repository State and Version Grounding
Before making any Git decision, verify the actual repository state rather than assuming it, branch, HEAD position, staged/unstaged changes, and remote tracking status all affect correctness.
```bash
git --version
git status
git log --oneline -5 --decorate
git branch -vv                 # shows tracking + ahead/behind counts
```
Confirm `git status` is clean (or that changes are intentional) before running destructive commands like `checkout`, `reset --hard`, or `clean -fd`.
**Pitfalls:** running `git reset --hard` without checking `git status` first, silently discarding uncommitted work; assuming the checked-out branch matches expectations without `git branch --show-current`.

## Staging, Committing, and the Three Trees
Git tracks three trees, working directory, staging area (index), and HEAD (last commit), and understanding the flow between them explains `add`, `commit`, `restore`, and `diff` behavior.
```bash
git diff                 # working dir vs. staging area
git diff --staged        # staging area vs. HEAD
git add -p               # interactively stage hunks
git restore --staged file.txt   # unstage without discarding edits
```
Verify exactly what will be committed with `git diff --staged` immediately before `git commit`, rather than trusting memory of what was edited.
**Pitfalls:** using `git add .` blindly and committing unintended files (build artifacts, secrets); confusing `git restore` (working tree) with `git restore --staged` (index) targets.

## Branching Model and Fast-Forward vs. Merge Commits
Branches are lightweight movable pointers to commits; merges either fast-forward (if no divergence) or create a merge commit (if histories diverged). Verify which will happen before merging in shared repositories.
```bash
git log --graph --oneline --all
git merge --no-ff feature/login   # force a merge commit even if fast-forward possible
```
Check team convention (merge commits vs. squash vs. rebase) in `CONTRIBUTING.md` before choosing a merge strategy, since mixed strategies produce confusing history.
**Pitfalls:** assuming `git merge` always creates a merge commit (it fast-forwards silently by default when possible); merging `main` into a long-lived feature branch repeatedly without ever rebasing, creating tangled history.

## Remote Tracking and Fetch vs. Pull
`git fetch` downloads remote history without touching the working tree or local branches; `git pull` is `fetch` + `merge` (or `rebase` with `--rebase`) in one step, hiding what actually happened.
```bash
git fetch origin
git log origin/main --oneline -5     # inspect before merging
git pull --rebase origin main        # explicit, avoids surprise merge commits
```
Verify `pull.rebase` and `pull.ff` config settings (`git config --get pull.rebase`) since defaults vary by Git version and global config, causing inconsistent behavior across a team.
**Pitfalls:** running `git pull` on a branch with local unpushed commits without knowing whether it will merge or rebase, based on unexamined config; force-pushing after an unexpected merge commit muddies shared history.

## Ignoring Files and Repository Hygiene
`.gitignore` patterns prevent untracked files from being accidentally staged, but do not un-track files already committed. Verify patterns against actual `git status` output rather than assuming syntax correctness.
```bash
git check-ignore -v path/to/file    # shows which rule matches
git rm -r --cached node_modules     # untrack already-committed files
echo "node_modules/" >> .gitignore
```
Confirm sensitive files (`.env`, credentials, key files) were never committed historically with `git log --all --full-history -- .env`, since adding to `.gitignore` afterward doesn't remove history.
**Pitfalls:** adding a pattern to `.gitignore` and assuming already-tracked files are retroactively ignored; committing secrets and only fixing `.gitignore` without purging history or rotating the leaked credential.

## Tags and Release Points
Tags mark specific commits as immutable reference points (releases); annotated tags carry metadata (author, date, message) while lightweight tags are just pointers. Verify which type a project uses before scripting around them.
```bash
git tag -a v1.4.0 -m "Release 1.4.0"
git push origin v1.4.0
git describe --tags --abbrev=0      # nearest tag from HEAD
```
Confirm tag immutability conventions with the team before moving/deleting a pushed tag, since consumers may have already built against it.
**Pitfalls:** force-moving a tag that's already been pulled by others, causing divergent builds referencing "the same" tag; using lightweight tags where CI expects annotated tag metadata.

## Stashing Work in Progress
`git stash` shelves uncommitted changes (staged and unstaged) to a stack, letting you switch context cleanly; verify stash contents before applying, since stashes can silently pile up and get forgotten.
```bash
git stash push -m "wip: refactor auth" --include-untracked
git stash list
git stash show -p stash@{0}
git stash pop           # apply and remove from stack
```
Confirm no conflicting changes exist on the target branch before `stash pop`, and prefer `stash apply` + manual `stash drop` when conflict resolution might be needed.
**Pitfalls:** forgetting `--include-untracked` and losing new files from a stash; letting stashes accumulate indefinitely, becoming an untracked second history nobody reviews.

## Blame, Log Filtering, and History Archaeology
`git blame` and filtered `git log` reconstruct why a line of code exists, essential before "fixing" code whose rationale isn't obvious. Verify authorship and context before assuming a line is dead code or a mistake.
```bash
git log -L 20,35:src/parser.py           # line-range history
git blame -w -C src/parser.py            # ignore whitespace, detect moved code
git log --follow --oneline -- src/parser.py   # history across renames
```
Cross-reference the commit message and linked issue/PR (if any) rather than trusting the diff alone, since commit messages can be misleading or incomplete.
**Pitfalls:** blaming a line to a large "reformat everything" commit and giving up instead of using `-w`/`-C` to skip past it; assuming a file's history is complete without `--follow` across renames.
