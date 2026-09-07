# BOUNDED CODEX TASK — B3: does particle production enlarge the bounce set? (Tori, 2026-09-07)

This computes the question B1 named as decidable-but-uncomputed. It is INSIDE the existing pre-registration
`B1_PREREG_BIANCHI_I_BOUNCE_20260907.md`: the classes `B1_PRODUCTION_RESCUES` and `B1_PRODUCTION_INSUFFICIENT` were declared
there before any of this was computed. You do NOT file a class; you produce the map and the tokens. I file.

## Read first
`B1_RESULT_V2_20260907.md` INCLUDING Amendments A and B, `B2_CLOSURE_20260907.md`, `KIMI_B2_CHALLENGE_20260907.md`,
`B1_SCOPE_QUALIFICATION_20260907.md`.

## Boundaries
- Write ONLY under `bounce/`. No pinned census file, no kit, no census version, no Hwao data, no new framework.
- FLUID row only. Flat Bianchi I is the primary case; if you also run Kantowski-Sachs, keep it in a separate section and never
  let a statement about one pass as a statement about the other.
- Carry alpha as an INTERVAL parameter; never insert the free-gas closure value at the bounce as though controlled.
- Run BOTH determined closures from B2 and report them separately — do not choose between them:
  (b) drop the n-T relation: eps = h_star T^4, p = eps/3, with n sourced by its own balance;
  (c) eps = F(T) specified with F' != 0, p = eps/3.
  For (c) state the F you use and why it is a defensible representative, not a tuned one.
- The production prescription Psi = beta H^4 is the paper's; state it as such. Where a result depends on that prescription
  rather than on production per se, say so — Amendment B makes that dependence load-bearing.

## Do exactly this
1. **Well-posedness first, again.** Re-verify constraint propagation for the exact system you integrate, in each closure. Print
   the residual. If it is non-zero, STOP and report that; do not integrate.
2. **The scaling question, analytically before numerically.** With production, n no longer falls as a^-3, so the torsion term
   no longer shares the shear term's a^-6 scaling. Derive how the torsion term scales under each closure, and state whether
   production breaks the degeneracy in the direction that HELPS a bounce (torsion outrunning shear) or HURTS it. This is the
   heart of the question; get it analytically if you can.
3. **The map.** Integrate collapse from declared initial data and determine, over a stated grid, which data bounce and which
   reach a singularity. Vary: initial shear fraction, initial n, and beta, across a stated range, for at least three alpha
   values spanning the declared interval. Report the boundary of the bounce set and, crucially, whether the bounce set is
   an OPEN region of the parameter space or remains a codimension-one threshold as it was without production.
4. **Compare with the no-production result.** State plainly whether the bounce set is enlarged, unchanged, or shrunk, and by
   what measure you are comparing (if you use a measure, name it and justify it; if you cannot, report the geometry of the set
   instead and say so — the lane has explicitly disclaimed unjustified measure language).
5. Everything in `bounce/b3_rescue.py`, runnable as `/usr/bin/python3 b3_rescue.py`, printing per-closure tokens:
   CONSTRAINT_RESIDUAL_<closure>, TORSION_SCALING_<closure>, BOUNCE_SET_<closure>=OPEN|THRESHOLD|EMPTY, and the grid summary.
   Deterministic; no network; no writes outside `bounce/`.

## Output: `bounce/B3_RESCUE_20260907.md` and `bounce/b3_rescue.py`
State every added assumption. Print both sha256s and all tokens as your final answer.
