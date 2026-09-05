#!/usr/bin/env python3
"""r3c2_timeout.py — the committed timeout wrapper the R3-C2 stall guard names.

  /usr/bin/python3 r3c2_timeout.py <seconds> -- <command> [args...]

Launches <command> and enforces a wall-clock deadline of <seconds> measured on the monotonic clock. Prints, in order:
  WRAPPER_COMMAND=<the exact argv>
  ---stdout--- / ---stderr--- (the child's captured output, verbatim)
  WRAPPER_EXIT=<child's exit status>  or  SYMBOLIC_TIMEOUT  (child killed at the deadline; exit 124)
  WRAPPER_ELAPSED=<seconds, monotonic>
Exit status: the child's, or 124 on timeout, or 2 on usage error. The preregistration's cap is 120.0 s.
"""
import subprocess, sys, time, shlex
def main(a):
    if len(a)<3 or a[1]!="--":
        print(__doc__); return 2
    try: limit=float(a[0])
    except ValueError: print("usage: <seconds> must be a number"); return 2
    cmd=a[2:]; print("WRAPPER_COMMAND="+" ".join(shlex.quote(c) for c in cmd), flush=True)
    t0=time.monotonic()
    try:
        p=subprocess.run(cmd, capture_output=True, text=True, timeout=limit)
        el=time.monotonic()-t0
        print("---stdout---"); print(p.stdout, end=""); print("---stderr---"); print(p.stderr, end="")
        print(f"WRAPPER_EXIT={p.returncode}"); print(f"WRAPPER_ELAPSED={el:.3f}"); return p.returncode
    except subprocess.TimeoutExpired as e:
        el=time.monotonic()-t0
        print("---stdout---"); print((e.stdout or b"").decode() if isinstance(e.stdout,bytes) else (e.stdout or ""), end="")
        print("---stderr---"); print((e.stderr or b"").decode() if isinstance(e.stderr,bytes) else (e.stderr or ""), end="")
        print("SYMBOLIC_TIMEOUT"); print(f"WRAPPER_ELAPSED={el:.3f}"); return 124
if __name__=="__main__": sys.exit(main(sys.argv[1:]))
