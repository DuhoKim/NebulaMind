# THE GATE CAUGHT SOMETHING REAL: PINNED SOURCE ≠ WHAT THE INTERPRETER MAY EXECUTE (2026-09-07 18:51 KST)
The reconciliation stopped at `MISSING-CORE-ENTRY` on `~/Library/Caches/com.apple.python/…`. The worker refused to add the cache to CORE, exempt it, delete it or regenerate it, and reported instead. **That was the right call and this is not a nuisance refusal.**

## WHAT IT FOUND
The prescribed interpreter discovers a macOS bytecode cache for four of our modules. CORE registers our own `__pycache__` bytecode (`our_imported_bytecode: 8`) but not these. Read-only inspection, retained in `_optionA_dev/agreement_run/_v52_cache_observation.json`:
| module | cached bytecode equals compilation of the CURRENT source? |
|---|---|
| `medium_perturbation.py` | yes |
| `runtime_binding.py` | yes |
| `select_sample.py` | yes |
| **`run_path.py`** | **NO — stale after the A1-pin edit** |
**So a bytecode artefact exists on this machine that does not match the source we pin, for the very module that enforces the pins.** That is the gap the whole runtime representation exists to close: pinning source bytes means nothing if the interpreter can execute something else. It is adjacent to the TOCTOU limit the reviewer accepted — but this one is not a disclosed limit, it is a live inconsistency, and it was found by a gate refusing rather than by anyone reasoning about it.

## THE FIX, AND WHY IT IS NOT A WEAKENING
Registering these caches in CORE would be a weakening **if registration were all**. It is not: the requirement becomes **every bytecode artefact the interpreter may load must correspond to the pinned source**, checked by code equality, and registered with its digest. Under that rule the stale `run_path` cache REFUSES until it matches — which is the behaviour we want, and it converts "we pinned the source" into "the source is what runs".
Rejected alternatives, and why: deleting the cache hides the question rather than answering it; exempting the directory reopens exactly the hole; and suppressing writes (`PYTHONDONTWRITEBYTECODE`) does not prevent READING a stale cache, so it would leave the gap while appearing to close it.

## STATUS
A1's pin was updated to the final A1 (`32057983…`) and CORE was NOT written, because the refusal fired before `record()` — so CORE still binds the previous A1 and the packet correctly refuses. Nothing was silenced. The next bounded step implements the correspondence rule, refreshes the stale artefact under the prescribed interpreter, re-runs the consumer verification, and makes the assembler execute that verification rather than read a stored boolean.
