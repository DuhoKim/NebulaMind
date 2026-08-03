# XM-1 pass1 — STOP + immutable defect receipt

Status: **STOP** (ladder halted at XM-1 pass1). Recorded by Hwao; executed/verified by Tori as bounded executor. No patch, no rerun under the current approval — per user direction only Duho may authorize a repaired pass1 retry.

## What happened
XM-1 pass1 (`xm1_cross_host.py … 5591 1`) exited 1 with `node_exit=null` — it failed during the **remote passdir preflight**, before the Pro browser controller was copied or launched. The fail-closed harness aborted and cleaned up.

## Exact defect (root cause)
The remote passdir preflight invoked:
`ssh <pro> python3 -c "import os,sys;d='…';sys.exit(2 if os.path.isdir(d) and os.listdir(d) else 0)"`.
OpenSSH joins the remote-command argv into a **single string handed to the Pro's login shell (zsh)**, which re-parses it. The `-c` body was therefore interpreted by zsh, not delivered intact to `python3 -c`: zsh mangled the quoting/`;`/glob and Python saw a `SyntaxError` at `import` (with a zsh "no matches found" class error), so the preflight exited rc=1. This is a **harness remote-invocation defect**, not a viability finding and not a remote-host problem.

## Safety posture — fail-closed worked; no side effects (Tori-verified)
- No remote Chrome launched; remote pass1 Chrome processes = 0.
- No account, sign-in, default Chrome profile, or user Flow window touched on either host.
- Studio writerA: `term-clean`; no local open handles/listener left; `/tmp` nmbrk dirs = 0.
- The failure occurred at a preflight guard, upstream of scp/controller/`ssh -L`/CDP — the fail-closed ordering held.
- Main run ledger intact; SM-1 passes 1–3 (PASS, identical normalized sha256 `91d32b39…7f7c16`) and the broker probe (PASS) remain valid on record. XM-1 (cross-host parallelism) is **UNPROVEN**.

## Preservation
Failed `receipts/archeval/xm1/pass1/` is preserved as-is (immutable). No retry attempted; no code modified under this approval.

## Advisory remediation (NOT applied — requires Duho authorization + a repaired pass1 retry)
For a future gated fix, make every remote invocation shell-safe rather than relying on `ssh host python3 -c "…"`:
1. Feed the preflight script to the remote interpreter over **stdin** (`ssh <pro> python3 - <<'PY' … PY`) so no shell re-parsing of a `-c` body occurs; or use a plain POSIX remote test with correct quoting (e.g. `ssh <pro> test -d <d> && …`), single-quoted.
2. Audit the sibling remote calls for the same argv-joining hazard: the `mkdir -p`, the copied-controller sha256 check (also `python3 -c "…"`), and the controller launch/`ssh -L` arguments — convert the `python3 -c` ones to stdin-fed scripts.
3. Re-run only pass1 first under a fresh Duho authorization; if green, resume passes 2–3 on distinct free loopback ports.

HWAO_XM1_PASS1_STOP_DEFECT_20260714T034720Z
