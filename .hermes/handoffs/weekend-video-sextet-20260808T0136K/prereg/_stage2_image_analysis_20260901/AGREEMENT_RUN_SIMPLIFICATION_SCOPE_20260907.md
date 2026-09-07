# SCOPE FOR THE SIMPLIFIED AGREEMENT RUN — Hwao's analysis for the amendment author (2026-09-07 10:31 KST)
Source: Duho's recorded direction (`.hermes/CODEX_DUHO_SIMPLER_AGREEMENT_PRIORITY_20260907.md`) and the go-ahead (`.hermes/CODEX_DUHO_HWAO_SIMPLIFICATION_GO_20260907.md`). This is a SCOPE NOTE for a PROPOSAL. Nothing here is reviewed, adopted or approved.

**THE GOAL, in one sentence.** One number: how often the machine's chirality call agrees with the human GZ1 call, on images the machine has never seen — with an interval, against a pre-stated bar.

## ESSENTIAL TO THAT NUMBER — KEEP
1. **Explicit eligibility**: the pinned guarded pool + renderability + r-band coverage, stated before selection. Without it "agreement" is over an undefined population.
2. **One reproducible selection**: seed → order by `h' = SHA256(lowercase seed hex ‖ "||" ‖ ASCII decimal GZ1_OBJID) mod 2^32`, ties by objid → take n. Anyone can recompute it from the seed.
3. **A seed fixed BEFORE we look** — a FUTURE drand round, named before it exists. This is the one safeguard that cannot be dropped: a seed chosen after seeing candidates makes the number worthless, and it costs one line.
4. **Evaluation separate from tuning**: disjoint tuning / holdout sets; the estimator and its configuration frozen by digest BEFORE the holdout opens; **the holdout opens once**.
5. **Exclusion of the 2,644 already-seen dry-run identities** (pinned exclusion file `77b29eafe18e02d4dee621a6e748e8f698381c6e23098e7db2db190aee270c95`) and the failed set — they are burnt.
6. **Pre-stated bar and floors** (2,000 drawn / 1,900 floor; 0.70 Wilson lower bound) so the result can FAIL.
7. **Attempts register**: every draw, abort and re-draw recorded, so this cannot become best-of-many.

## NOT ESSENTIAL TO THIS COMPARISON — REMOVE OR DEFER (nothing deleted; out of scope for this run)
1. The provenance / witness stack: GitHub PushEvent witness, history continuation, per-entry publication, receipts, Option-A′/B receipt identity, composed provenance mode. It proves chronology to a hostile third party; a prospectively named public drand round plus a committed digest already does that for us.
2. The NSD / precedence / input-boundary refusal apparatus (provenance v3–v14, driver v14–v18, tracks 8–14). It hardens a loader against adversarial evidence — not needed to draw a sample.
3. The 132 differential controls, the table verification and the fail-first kit AS RUN-GATING MACHINERY. Keep roughly six real tests on the selection function itself: determinism from a fixed seed, tuning/holdout disjointness, exclusion actually applied, exact sizes, no reuse across draws, and refusal when eligibility inputs are missing.
4. `verify_split`, the `holdout_once` flag machinery, the seal-append helper and step 2 as designed.
5. Further amendment/review rounds: ONE narrow amendment, ONE independent review — not another eleven.

## THE WAITING TIME — identify the real constraint, do not invent one
Duho asked to start as soon as possible. **V15's 24-hour wait is NOT inherited**: it is the NIST-primary fallback window (`RETRY` until T_pulse + 24 h, then the fixed drand fallback). With NIST removed by the drand-only direction there is no fallback window to wait out. The only genuine constraint is that the seed round must be **strictly in the future at the moment the procedure and its inputs are fixed and committed**, with enough margin to record that commit first. State the margin explicitly and keep it minutes, not hours. If the author finds a real inherited constraint requiring longer, name it precisely in the proposal rather than defaulting.

## BOUNDARIES THAT DO NOT MOVE
Drand-only stands (the source is NOT re-asked). The unseen evaluation data stay UNOPENED. No draw, split or holdout until the amended procedure is adopted. The V15 run record, round 6440756, the fixture history, every attempt and the real chronology stay exactly as filed. This proposal is not a review and not an adoption.
