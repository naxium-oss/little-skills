# Linux & Command Line Fundamentals

## Distribution, Kernel, and Shell Grounding
Command behavior and available flags differ across distributions (Debian/Ubuntu vs. Alpine vs. RHEL), kernel versions, and default shells (`bash` vs `dash` vs `zsh`). Verify all three before trusting a command snippet from unknown provenance.
```bash
cat /etc/os-release
uname -srm                 # kernel name, release, machine arch
echo $SHELL; readlink -f /bin/sh
```
Alpine's `sh` (BusyBox) lacks many GNU coreutils flags that Ubuntu's `bash`/`coreutils` support, a script tested on one silently breaks on the other.
**Pitfalls:** assuming GNU `sed`/`date`/`grep` flags work identically on BSD/macOS or BusyBox variants; copying commands from a container base image tutorial without checking the actual base image in use.

## Filesystem Hierarchy and Permissions Model
Linux organizes files under a standard hierarchy (`/etc`, `/var`, `/usr`, `/home`) and enforces access via owner/group/other permission bits plus optional ACLs. Verify actual permissions with `ls -l`/`stat` rather than assuming from context.
```bash
ls -l file.sh                      # -rwxr-xr-- 1 user group ...
stat -c "%a %U %G" file.sh         # octal mode, owner, group
chmod 750 file.sh
getfacl file.sh                    # check for extra ACL entries beyond basic bits
```
Confirm whether a "permission denied" error is due to file mode, directory execute bit (needed to traverse), SELinux/AppArmor context, or ownership before applying a fix.
**Pitfalls:** using `chmod 777` as a quick fix instead of diagnosing the real ownership/group issue; forgetting a directory needs execute (`x`) permission to be traversed even if files inside are readable.

## Process Management and Job Control
Every running program is a process with a PID, parent PID, and signal-handling behavior; job control (`&`, `fg`, `bg`, `jobs`) manages foreground/background execution within a shell session.
```bash
long_running_task.sh &        # background
jobs -l
kill -SIGTERM %1              # signal the first job
ps aux | grep long_running
pstree -p $$                  # process tree from current shell
```
Verify a process actually terminated after sending a signal (`kill -0 PID` checks existence) rather than assuming `kill` always succeeds immediately, since `SIGTERM` can be ignored or delayed.
**Pitfalls:** using `kill -9` (`SIGKILL`) as a first resort, preventing graceful cleanup (open file handles, DB transactions); forgetting background jobs die when the parent shell exits unless `disown`/`nohup` is used.

## Pipes, Redirection, and Exit Status
Commands communicate via stdin/stdout/stderr streams; pipes (`|`) connect stdout of one command to stdin of the next, while `>`, `>>`, `2>`, `&>` redirect streams to files. Every command returns an exit status (`$?`), with `0` meaning success by convention.
```bash
grep -c "ERROR" app.log > error_count.txt 2> grep_errors.log
command1 | command2 || echo "pipeline failed"
echo $?                       # exit status of the last command
set -o pipefail                # make pipeline fail if ANY stage fails, not just the last
```
Verify exit codes explicitly in scripts rather than assuming success, especially in pipelines where only the last command's exit code is checked by default.
**Pitfalls:** forgetting `set -o pipefail` in scripts, masking a failing `grep`/`curl` upstream of a successful `wc -l`; redirecting `2>&1` in the wrong order, which merges streams incorrectly if placed before the file redirect.

## Text Processing: grep, sed, awk
`grep` filters lines by pattern, `sed` performs stream editing (substitution), and `awk` processes structured/columnar text with a full scripting language. Verify regex flavor (BRE/ERE/PCRE) since syntax for `+`, `?`, `|` differs.
```bash
grep -E "ERROR|WARN" app.log | awk -F'|' '{print $1, $3}'
sed -i.bak 's/old_host/new_host/g' config.yaml     # -i.bak keeps a backup
awk '$3 > 100 {sum += $3} END {print sum}' data.tsv
```
Test destructive `sed -i` edits on a copy first, or always use the backup-suffix form, since in-place edits are irreversible without one.
**Pitfalls:** using basic regex `grep` syntax and expecting `+`/`?` to work without `-E`; assuming `sed -i` behaves identically on macOS (BSD sed requires an explicit backup suffix argument) and Linux (GNU sed allows empty suffix).

## Environment Variables and Shell Configuration Files
Shell startup files (`.bashrc`, `.bash_profile`, `.profile`, `.zshrc`) load in different orders depending on login vs. non-login and interactive vs. non-interactive shell type, a common source of "works in my terminal but not in cron/CI" bugs.
```bash
echo $PATH
env | sort
type -a python3            # shows all resolvable locations, revealing PATH precedence
bash -lic 'echo $PATH'     # simulate login+interactive shell explicitly
```
Verify which startup file actually ran using `bash -x -c 'exit'` tracing or by adding a temporary echo, rather than assuming based on shell documentation alone.
**Pitfalls:** setting `PATH`/env vars only in `.bashrc`, then wondering why a cron job or systemd service (non-interactive, non-login) can't find them; assuming `.bash_profile` sources on every new terminal tab (it often doesn't for non-login shells).

## Disk, Memory, and System Resource Inspection
Diagnosing performance or capacity issues requires actual measurement, not assumption: `df` for disk space, `du` for directory usage, `free`/`vmstat` for memory, `top`/`htop` for live process resource use.
```bash
df -h                          # human-readable disk free per filesystem
du -sh /var/log/* | sort -rh | head -10
free -h
top -o %MEM
```
Verify whether a reported "disk full" is actually inode exhaustion (`df -i`) rather than space, a common confusing edge case with many small files.
**Pitfalls:** trusting `du` totals without `-x` when directories span multiple filesystems/mounts, causing double-counting; ignoring inode exhaustion as a separate failure mode from byte capacity.

## Package Management Across Distributions
Package managers (`apt`, `dnf`/`yum`, `apk`, `pacman`) differ in commands, repository formats, and caching; verify which is present and its cached index freshness before installing.
```bash
apt-cache policy nginx          # Debian/Ubuntu: shows installed vs. candidate version
dnf info nginx                  # Fedora/RHEL
apk info -a nginx               # Alpine
apt-get update && apt-get install -y --no-install-recommends nginx=1.24.*
```
Pin exact versions in reproducible builds (containers, IaC) rather than installing "latest," and verify a stale local index isn't silently offering an outdated version.
**Pitfalls:** forgetting `apt-get update` before install in a fresh container layer, installing a stale cached version; leaving `apt` cache files in container images, bloating size unnecessarily.

# Bash Shell Scripting

## Shebang, Shell Dialect, and Strict Mode
The shebang line determines which interpreter runs a script; `#!/bin/sh` may resolve to `dash` (no arrays, limited features) while `#!/bin/bash` guarantees bash-specific syntax. Verify the actual interpreter with `readlink -f /bin/sh` before using bashisms in a `sh` script.
```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
```
`set -e` exits on error, `-u` errors on unset variables, `-o pipefail` propagates pipeline failures, together this is the standard "strict mode" that catches silent bugs early.
**Pitfalls:** using array syntax (`arr=(a b c)`) in a `#!/bin/sh` script that runs under `dash` in production, causing a syntax error only in that environment; relying on `set -e` to catch errors inside `if` conditions or `&&` chains, where it does not trigger by design.

## Argument Parsing and Input Validation
Positional parameters (`$1`, `$2`, `$@`, `$#`) and `getopts` provide argument handling; always validate argument count and content before using them, since unset positional args expand to empty strings (or error under `set -u`).
```bash
#!/usr/bin/env bash
set -euo pipefail

usage() { echo "Usage: $0 -e <env> [-d]" >&2; exit 1; }

dry_run=false
while getopts "e:d" opt; do
  case "$opt" in
    e) env="$OPTARG" ;;
    d) dry_run=true ;;
    *) usage ;;
  esac
done
[[ -z "${env:-}" ]] && usage
```
Verify `getopts` only handles single-dash short options; use a manual `while [[ $# -gt 0 ]]` loop or a library for long `--options`.
**Pitfalls:** assuming `getopts` supports `--long-options` natively; forgetting `shift` in manual arg-parsing loops, causing infinite loops or misread arguments.

## Quoting and Word Splitting
Unquoted variable expansions undergo word splitting and glob expansion, a leading cause of subtle bugs with filenames containing spaces. Always quote variable expansions unless intentional splitting is required.
```bash
files=("my file.txt" "other.txt")
for f in "${files[@]}"; do        # correct: preserves each element intact
  echo "Processing: $f"
done

rm $unquoted_var        # DANGEROUS: word-splits and globs
rm -- "$quoted_var"     # safe: treated as a single literal argument
```
Use `--` before variable arguments to prevent a value starting with `-` from being interpreted as a flag.
**Pitfalls:** iterating `for f in $(ls *.txt)` instead of a glob (`for f in *.txt`), breaking on filenames with spaces or globs expanding unexpectedly; omitting `--` and having a filename like `-rf` misinterpreted as an option.

## Functions, Return Values, and Error Propagation
Bash functions communicate success/failure via exit status (`return N`, 0-255) and output via stdout captured with `$(...)`; they cannot directly "return" arbitrary data types like other languages.
```bash
fetch_status() {
  local url="$1"
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url") || return 2
  echo "$code"
}

if status=$(fetch_status "https://example.com"); then
  echo "Got status: $status"
else
  echo "Request failed with code $?" >&2
fi
```
Always declare function-local variables with `local` to avoid leaking into global scope, and check the actual exit code of the invocation, not just whether output was produced.
**Pitfalls:** forgetting `local`, causing a function's temp variable to clobber a global one used elsewhere; assuming a non-empty stdout implies success without checking `$?`.

## Trap-Based Cleanup and Signal Handling
`trap` registers handlers for signals (`INT`, `TERM`) and pseudo-signals (`EXIT`, `ERR`), enabling guaranteed cleanup of temp files/locks even on failure or interruption.
```bash
tmpdir=$(mktemp -d)
cleanup() { rm -rf "$tmpdir"; }
trap cleanup EXIT
trap 'echo "Interrupted" >&2; exit 130' INT TERM
```
Verify the trap fires under all expected exit paths by deliberately testing `Ctrl-C` and a forced error path, not just the happy path.
**Pitfalls:** registering cleanup only for `EXIT` and assuming `Ctrl-C` triggers it identically without also trapping `INT`/`TERM` explicitly in some shell versions; overwriting a previously set trap by calling `trap` again without combining handlers.

## Arithmetic, Comparisons, and Test Constructs
Bash distinguishes string comparison (`[[ "$a" == "$b" ]]`) from numeric comparison (`(( a == b ))` or `[ "$a" -eq "$b" ]`); mixing them causes silent logic errors, since `"10" == "9"` as strings differs from `10 -gt 9` numerically... but string-lexicographic "10" < "9".
```bash
count=5
if (( count > 3 )); then echo "large"; fi
[[ -f "$path" && -r "$path" ]] && echo "file exists and is readable"
[[ "$name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] && echo "valid identifier"
```
Prefer `[[ ]]` over `[ ]` in bash-specific scripts for safer word-splitting behavior and regex support (`=~`), but verify `[[ ]]` isn't used in a `#!/bin/sh` script where it's unsupported.
**Pitfalls:** using `-eq` on non-numeric strings, causing a runtime error only when unexpected input appears; using `[[ ]]` in a script shebanged as `#!/bin/sh`, breaking under `dash`.

## Here-Documents and Multi-Line String Handling
Here-documents (`<<EOF`) and here-strings (`<<<`) feed multi-line text into commands without escaping quoting hell; quoting the delimiter (`<<'EOF'`) disables variable expansion when literal text is needed.
```bash
cat <<EOF > config.yaml
host: ${DB_HOST}
port: ${DB_PORT:-5432}
EOF

cat <<'EOF' > script_template.sh
echo "This \$VAR is NOT expanded because delimiter is quoted"
EOF
```
Verify indentation: `<<-EOF` strips leading tabs (not spaces) for readable indented heredocs, a frequently misremembered detail.
**Pitfalls:** expecting `<<-EOF` to strip leading spaces (it only strips tabs); forgetting to quote the delimiter when literal `$` or backticks must not be interpreted.

## Debugging with set -x and Shellcheck
`bash -x` (or `set -x` inline) traces every command with expanded variables before execution, the fastest way to see what a script actually does versus what you think it does. `shellcheck` statically catches quoting, portability, and logic bugs before runtime.
```bash
bash -x deploy.sh 2> trace.log
set -x   # enable mid-script
...
set +x   # disable
shellcheck deploy.sh
```
Run `shellcheck` in CI on every script change, and treat its warnings about quoting/word-splitting as high-priority since they correspond to real production incidents in practice.
**Pitfalls:** debugging by adding scattered `echo` statements instead of `set -x`, missing the actual expanded command and word-splitting behavior; ignoring shellcheck warnings as "style only" when many flag genuine correctness bugs.

