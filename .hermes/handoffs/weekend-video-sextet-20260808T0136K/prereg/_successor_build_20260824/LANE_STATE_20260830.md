**STATUS: HOLDING — V73 banked, round deliberately not dispatched (Blanc, 2026-08-30 01:46: prefer
banking over a post-02:30 referee pass). This file supersedes `LANE_STATE_20260829.md`.**

# DESI prereg lane — state at 2026-08-30 02:00 KST

## Where the document is

**Current draft: V73** = `d48c3000aa50d804841f3c170cd660791dc5f3355d7aa682ed33147f6aa3a8ae`
(`PREREG_SUCCESSOR_DRAFT_V73_20260830.md`), committed `12d087f8f` + brief `a28fd3142`.
**Last refereed: V72**, NOT CLEAR ×2 (GPT56 5, CODEX 8) — every finding repaired or dispositioned in
V73. **FROZEN: `ref/successor_ref_v9.py` = `6a9abbbd…`** — read all night, never written.
**BS-6 and the first image byte remain blocked. γ̂ unmeasured. Nothing unblocked anywhere tonight.**

## The morning's first command

    .hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/gates/_tmp_v73_round.sh

then arm `gates/_tmp_v73_wait.sh` in the background. Brief: `gates/BRIEF_V73_REVIEW.md` — **the
draw-discipline text is excluded from the attack surface** (⛔ banner, five-round freeze); the named
targets are the wired derivation checker, the registry generator, and the entry↔emission bijection.

## The battery (all green on V73, and two checks are new tonight)

counts 16/8 · trace 72 transitions/0 · **lint 0 — now includes `lifecycle_derivation_check` as
blocking** · refusal vocabulary 0 across 21 controls · derivation 0 · **string-field registry 37/37
classified, 0 forbidden-by-default** (`ref/gen_string_field_registry.py`).

## Standing rulings that shaped tonight (all applied)

catch-all taken, non-closure established (22:18) · χ-blind precommitted access schedule +
flag-discard-replace kept as a digest-bound finding (22:49) · Row F read-surface widened, strata to
be decided before freeze (23:02) · V54 residue: basis (i) dropped, clauses disjoint, planning not an
outcome, withdrawal-on-rule (22:00) · gain mapping option A, worst case over draws.

## AWAITING THE PRINCIPAL (nothing below moves without him)

1. **The VOID/numerical partition** — three constructions failed; options in `DECISIONS_FOR_DUHO.md` §1.
2. **The BS-3g sitting — seven parameters, one sitting**: `n_draws` · master seed · generator ·
   `Δγ` · `k_γ` · bound shape (measured vs a-priori) · **draw-variate semantics (what "same draw"
   means across γ)**. **The draw-discipline text is frozen UNSTABLE-PENDING-RULING on this sitting**
   after five consecutive rounds of findings against text built over unruled parameters.
3. **`REFUSED-INTEGRITY-MISMATCH`** — unadjudicable at emission; collides with phase-Any VOID.
4. **The four availability codes describe the logged object** (CODEX-V64 F2) — part of the ruled
   vocabulary, so his.
5. **The durable pre-verdict state** — needs a second event class; changing what the log records is
   not authorised.
6. **The strata + their producer, coupled** — `FINDING_ROW_F_STRATA.md` +
   `OPEN_QUESTION_STRATUM_PRODUCER.md`: both stratum axes are χ-derived, no covenant row produces
   the index, and BS-8p/BS-2f/BS-8f are blocked behind the pair.

## Mechanisms built tonight (each with self-test/controls)

`LIFECYCLE_GUARANTEE_SPEC.md` (G1–G6, N1–N3, window×reader table; draft carries digest-pinned
verbatim quotes) · `tools/lifecycle_derivation_check.py` (label-bound, deletion-detecting, wired
into lint) · `ref/STRING_FIELD_REGISTRY.md` + generator (enumerated string rule; forbidden by
default) · `tools/refusal_vocabulary_check.py` (21 controls; decoration-independent member parse;
negation-guarded retirement) · enumeration verifier spec (five gates, bijection, closed-vocabulary
explanations, testimony named as testimony) · atomic touch contract as BS-2k design obligation.

## Traps for whoever boots next

- **Sibling BHU lane sweeps DESI files via repo-wide `git add -A`** — date artifacts with
  `git log -- <path>`, not by commit message.
- **Blanc's relay-header times ran AHEAD of the clock during the evening** (his correction, 21:57);
  order is trustworthy, absolutes are not — file mtimes govern.
- **The unsent-input-box defect ate four continuation phrases today**; if the lane looks idle after
  a round closes, that is the likeliest cause. Standing continuation on a NOT-CLEAR round: repair
  and re-round, mine to execute without a fresh prompt.
- **hermes runner logs are 0 bytes until process exit** — an empty log is not a dead seat; count
  `hermes -z` processes.
- **Digest quoted for a file the same revision edits: compute it LAST** (went stale twice in one
  night inside the repair that was fixing it).
