PASS_S0S2_FIXED

# Phase 5 S0–S2 second re-gate verdict

## Scope

Single-item re-gate only: the optics inference previously identified in `REGATE_S0S2_VERDICT.md`.

## Verification

The blocker is fixed in the current `s1_crossing_shift.py`:

- Lines 25–30 explicitly label the optics step `DERIVED` and `NOT pinned`.
- The text distinguishes the pinned premises (Lipschitz metric matching and Rankine–Hugoniot conservation) from the adapted inference.
- It expressly states that the step to continuous photon four-momentum and the conclusion that the shift comes from the fluid-velocity discontinuity is `OURS`.
- The prior unlabelled wording is absent; the new labelled block occurs exactly once.

I enforced those conditions with independent static assertions against the current file. They passed. `python3 -m py_compile s1_crossing_shift.py` also passed, and a fresh execution of the script completed with all 6/6 limiting-case checks passing.

`METHOD_FINDING_BLIND_DOUBLES.md` second finding accurately records the earlier silent-no-op failure mode and the required pre-/post-condition discipline: old pattern present before replacement; old text gone and new text present afterward. The current artifact satisfies the resulting postconditions, so the earlier blocking objection has no residue.

PASS_S0S2_FIXED
