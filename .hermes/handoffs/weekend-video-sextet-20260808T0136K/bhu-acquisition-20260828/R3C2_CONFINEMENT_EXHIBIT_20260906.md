# R3C2 — seat confinement, settled and exhibited (2026-09-06 09:52:37 KST; Duho 09:46 KST: "fix the confinement … then exhibit it")

**Before:** the codex seat ran through a shim with `--dangerously-bypass-approvals-and-sandbox`; confinement was a sentence in a brief
("open nothing outside this directory") and a printed path list. The record has said for days that codex escapes its root. Abort A3
this morning was the mirror image: the sources were outside the directory the brief allowed, so the seat could not reach them.

**Now:** each seat runs inside a macOS sandbox profile, `r3c2_seat_sandbox.sb` (sha256 2e3d43c0e5818643…), with
`(deny default)`; reads allowed only under the seat's working directory (parameter WORKDIR), the system and binary paths the process
needs (/usr, /bin, /System, /Library, /Users/duhokim/.local, ~/.codex, ~/.hermes, /opt/homebrew, temp dirs); writes only under WORKDIR,
temp and the two tool state dirs; network open for the model. The lane, the frozen master, the original sources directory and the
rest of the home directory are unreadable. The dispatch shim `r3c2_seat_dispatch_sandboxed.sh` (sha256 87e22d6d6531178f…) wraps codex in it,
pins `-m gpt-6-astra`, closes stdin.

## Exhibition (live, this morning)
Test tree `/Users/duhokim/HermesOps/r3c2_confine_test/lane` holding one pinned source and `inside.txt`; `/Users/duhokim/HermesOps/r3c2_confine_test/outside.txt` one level up; the lane's frozen master as the far target.

**codex-cli 0.153.4, gpt-6-astra, under the profile** (`/Users/duhokim/HermesOps/r3c2_confine_test/probe.out`, exit 0):
```
82f0d604d5b43c86ad893af052cf03dfaafda73e681b80e8123f51ec2789a2ab  …/lane/2203.13295_clean.txt   ← equals the manifest row
INSIDE_OK
cat: /Users/duhokim/HermesOps/r3c2_confine_test/outside.txt: Operation not permitted
head: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md: Operation not permitted
ls: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828: Operation not permitted
CONFINE_PROBE_DONE
```
**hermes/kimi-k3 under the same profile** (`/Users/duhokim/HermesOps/r3c2_confine_test/probe_kimi.out`): see the run log line of 2026-09-06 09:52:37 KST for its printed lines.

**Plain cat probes under the profile:** inside file read; outside file "Operation not permitted"; lane master "Operation not permitted";
/usr/bin/python3 runs.

**What this does and does not settle.** The seat can read exactly the working directory it is given and nothing else on this disk;
that is enforced by the kernel, not by the brief. It does not confine the network (the model must be reachable) and it does not
prove the model did not remember something from another session — the frozen design's C4 already says the record bounds the record,
not the mind. The printed path list stays as the seat's own account; the sandbox is what makes it true.

R3C2_CONFINEMENT_EXHIBIT_COMPLETE
