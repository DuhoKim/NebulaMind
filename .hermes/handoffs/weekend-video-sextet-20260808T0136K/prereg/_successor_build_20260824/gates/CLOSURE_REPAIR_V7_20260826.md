# The v7 repair — five of KIMI's findings closed, four left open

2026-08-26, Hwao. Written against `CLOSURE_V6_KIMI.md` (CLEAR with conditions). Duho's
instruction was to fix F1/F2/F3 and re-gate. F5 and F6 came with them because both were
one-liners that KIMI had already demonstrated, and shipping a known-false docstring into the
same re-gate would have been worse than the scope discipline it protects.

v6 is untouched: KIMI's report pins its digests and stays legible against them.

## Fixed

**F3 — BLOCKING in spirit even though KIMI ruled it non-blocking.**
`closure_receipt(manifest_bricknames, python_executable=None)` let the caller name the
interpreter that runs the worker. KIMI forged it: a three-line executable that ignores `-I` and
the worker and prints `{"outcome":"PASS"}`, handed to `closure_receipt`, and the forged result
came back with no closure having run. The parameter is gone; the call is
`[sys.executable, "-I", worker]`. Probe **B06** calls with the keyword and requires a TypeError
from the signature itself. Fixture `CLOSURE-NO-INTERPRETER-ARGUMENT` asserts the same on the
source — and asserts it against the *call*, not the comment, because my first version of that
assertion failed on its own explanatory prose.

I put that parameter there for testing convenience while building the boundary whose entire
purpose is to deny nomination. It survived my own review, both my repair records, and the brief.

**F1 — the verify hooks were registered and never invoked.** Zero references to `p["verify"]` in
the runner. The suite's conformance was PASS/REFUSE plus a message substring — exactly v5's
narrowness — while the v6 brief told two seats the hooks "assert on the structured result". They
now run on the live result (not the receipt's truncated copy) and their verdict is folded into
conformance. The receipt carries `verify_hooks_declared`, `verify_hooks_ran` and
`verify_hooks_all_ran` so the claim is computed rather than asserted.

**F2 — `stable_sha256` could not reproduce across processes.** F03/F04's refusal payloads carry
the per-process run directory, and `normalise()` was applied to `message` only. Three same-mode
runs produced three hashes over byte-identical evidence. `normalise_deep()` now rewrites the run
directory out of every string in the hashed structure. Verified before this went out: the same
probe subset in two separate processes printed `9b7c6560c4accfc2cf098c6cc826bc42fe27e99234efb34cb8277184f0155503` both times.

**F5 — the symlink refusal is now on the open.** `O_NOFOLLOW`, with the preceding `lstat`
removed. The old docstring claimed both checks were on the descriptor; only `S_ISREG` was.
Probe **F05** covers it.

**F6 — the worker validates the manifest's type.** A JSON object was iterated as its keys and
accepted, reporting 12,117 entries. It cannot under-cover a manifest, but an unvalidated type at
the trust boundary is what R06 and R07 exist to refuse. Probe **B07** covers it.

## Not fixed, and not claimed

- **F4's three blind spots.** A global resolving to a module folds as `<module>` — KIMI rebound
  `math.radians` and the digest did not move. A pure-Python helper reachable only through a class
  method is not recursed into — same result with `tangent_plane_offsets`. C callables contribute
  a type name only. The suite's `not_covered` list now names all three in KIMI's terms, including
  that the digest's cross-process stability and its blindness have the same root cause.
- **The residual is wider than v6 said.** Under `-I` the CommandLineTools system site-packages
  still precedes the single pinned add-back, and **astropy — which parses the sidecar — resolves
  from the same unpinned user directory as numpy**. The sidecar's bytes are pinned; its parser is
  not.
- **F8.** No frozen phase-aware refusal schema; `require_environment()` is still never called on
  the closure path.
- **CODEX-V5 F6.** The selection still has a code pin and no producer receipt.

## What a reader should take from three repair rounds

Each round closed the findings of the round before and introduced something new for the next one
to find: v5 fixed the caller-supplied artifacts and left a mutable-pin hole; v6 fixed the pins
and shipped a nomination parameter plus hooks that never ran; v7 fixes those. The suite has now
caught two of my defects that no referee saw (the unreachable during-plan branch, and this
round's assertion that failed on its own comment), and referees have caught defects the suite
could not, three rounds running. That is the arrangement working, and it is also the reason not
to read a CLEAR as "done".
