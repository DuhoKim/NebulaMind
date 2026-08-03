# Overnight Run — "Make ongoing papers publishable quality"
Planned by Trio (Hwao/Tori/Goru). ~10h. Start ~22:00 KST 2026-07-20 → ~08:00 KST 2026-07-21.
Status: **PLANNED — awaiting human go/no-go. NOT launched.**

## Goal
Take 2–3 ongoing drafts to *human-review-ready* (publishable-quality candidate) — grounded
motivation, non-circular result, defensible conclusion. NOT "validated" (final gate = human;
0 cleared to date). Leverages all local models + Deep Research (DR, reference-only, paced).

## Targets (work 3, shelve the rest)
- **A · z>7 mass–metallicity (flagship, referee MINOR).** #1 frontier. Blocker = thin
  independence (2nd-survey/orthogonal checks trace to the same ~N=4 lensed galaxies).
  Move: DO NOT chase a detection. Reframe to a **selection-bounded upper-limit / consistency
  test**; leave-one-out over the N=4; confirm all O/H on one Te/O3N2 scale.
- **B · IllustrisTNG massive-galaxy SMF ("too massive too early").** Non-circular by
  construction (sim prediction vs independent JWST obs); NO O/H artifact. Move: like-for-like
  M* (aperture+IMF+SED-prior matched), compare cumulative n(>M*,z), show tension survives the
  systematic budget — or honestly conclude "consistent within systematics."
- **C · MZR/FMR aperture sensitivity (methods).** Reframe as the *precondition* for any
  MZR-evolution claim (feeds A). Deliver a ΔO/H(aperture) correction prescription measured
  across ≥2 calibrations; resolved/IFU data as independent ground truth.
- **Shelve:** z≈0 scaling-relation & standalone MZR anchors; the rejected-class 1-cycle
  pipeline runs. Do not resurrect.

## Timeline (KST)
| KST | Phase | Work | Lead model |
|---|---|---|---|
| 22:00–23:15 | P0 Motivation + PRE-REGISTER | wiki-mine motivation A/B/C; **DR#1** (batched); lock gates before any result | gpt-5.6-sol + DR |
| 23:15–01:15 | P1 Measurement + calibration | galSpecLine **O3N2 reconciliation** (kill +0.24 dex offset); build independence firewall | qwen3:30b, gpt-5.6-sol |
| 01:15–02:00 | P2 **DR#2** (spaced) | A independence evidence + B massive-end SMF systematics; cooldown after | DR + qwen3.6:27b (file notes) |
| 02:00–04:30 | P3 Referee–revise (≥3 cycles) | astrosage-70b multi-cycle: scale→circularity→motivation→defensibility; drafter revises | astrosage-70b / qwen3:30b |
| 04:30–05:15 | P4 **DR#3** (final) | novelty + citation-entailment evidence | DR |
| 05:15–07:00 | P5 Novelty + entailment gates | enforce G4/G5; final referee cycle | astrosage-70b, qwen3-embedding:4b |
| 07:00–08:00 | P6 Package | human-review-ready bundle; write provenance events | qwen3:30b |
| T-90min | FREEZE | no new paper enters gates; finish in-flight; write ACCEPT/SHELVE ledger | — |

## Pre-registered gates (ALL must pass, in order; fixed before results)
G1 Motivation-grounded — cites ≥2 specific wiki/lit IDs the paper actually addresses · FAIL→SHELVE
G2 **Non-circular** — evidence set disjoint from hypothesis-forming set (or orthogonal method
   whose systematics don't trace back). z>7 detection framing FAILS G2 (same N≈4) → capped at
   bounded-descriptive · FAIL→SHELVE
G3 Calibration-reconciled — one declared O/H scale, conversion applied+cited, signal survives
   the ~0.24 dex inter-scale offset · FAIL→SHELVE
G4 Novelty — not already stated in the 120k corpus (or cites+differentiates) · FAIL→SHELVE
G5 Citation-entailment — every load-bearing citation truly supports its sentence · FAIL→REVISE
   (2nd failure → SHELVE)
G6 Honest-label — tier matches evidence; nothing "detection"/"validated" · FAIL→REVISE
Terminal states: ACCEPT = human-review-ready (queued for Duho; NOT validated) · REVISE (once) · SHELVE.

## Bright lines (never)
- Never call the z>7 deficit a "detection."
- Never compare metallicities on mismatched O/H scales without an applied, cited conversion.
- DR never edits .tex, replaces a computed/validated result, or writes the DB — reference only.
- Never mark "validated" or auto-publish without human sign-off. astrosage verdict is advisory,
  never a gate pass.
- Never retro-edit these rules to fit a result.

## Stop / fail conditions
- Paper: any G1–G4 fail, or 2 REVISE cycles w/o ACCEPT, or only-claim-is-the-overclaim → SHELVE.
- Run: all candidates SHELVED before any ACCEPT → abort; bright-line violation in an output →
  halt + surface to human; provenance/event-log breaks → abort.
- DR guardrails: ≤6 trips, ≥8 min spacing, one in flight; soft-throttle → double next interval;
  hard block (google/sorry) → stop DR ≥30 min; DR never on the critical path to ACCEPT.

## Exit criteria (per paper → ACCEPT)
motivation-grounded ∧ non-circular ∧ calibration-reconciled ∧ pre-reg unchanged ∧ astrosage ≤MINOR
over ≥2 cycles ∧ novelty ∧ citation-entailment ∧ honest-label ∧ queued for human sign-off.

## Provenance (to the Draft board / history.json event log)
Every gate emits an event (pass OR fail): pre-registration snapshot, DR artifact IDs+timestamps,
O3N2 reconciliation record, per-cycle referee logs, novelty + entailment results, independence-
firewall description, final ACCEPT/SHELVE flag. Recorded via draft_provenance.append_event so the
revision log shows human/DR feedback, not just the referee.

## Biggest risk → de-risk
Risk: a clean-compiling, MINOR-rated z>7 paper whose "independent" checks quietly collapse to the
same N≈4 → reads as a detection → 10th rejected paper. De-risk: **pre-registered non-circularity
firewall (G2) enforced by astrosage (a different model than the drafter), before any polish** —
disjointness of the evidence set can't be faked the way motivation/formatting can.
