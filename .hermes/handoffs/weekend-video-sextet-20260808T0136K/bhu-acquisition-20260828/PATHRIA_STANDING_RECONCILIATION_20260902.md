# Entry 1 (Pathria 1972) — standing adjudication, blind-double reconciliation

**Date:** 2026-09-02 15:44 KST · **Coordinator:** Tori (Fable 5.1, post-restart) · **Brief:** `_PATHRIA_STANDING_BRIEF.md`
**Seats:** codex (`PATHRIA_STANDING_codex.md`, 15:24) and agy (`PATHRIA_STANDING_agy.md`, 15:40, foreground, 5 min, exit 0, stderr empty).
Blind: agy was instructed not to open any codex-named file; the dispatch was issued before agy could see this note.
**My verification:** `pathria_standing_verify.py` → `_tmp_pathria_verify.out` (eval-what-you-print; every number below is in that output).

## Result: the two seats AGREE — `FIRED_CANDIDATE` / `FIRED_CANDIDATE`

Both seats stated the refutation condition before evaluating, both drew it from Pathria's own eq. (18)
("we must have K = +1 and Λ ≤ Λ_c", pinned text line 409–410) rather than from a bar we supply, and
both found the measured configuration outside it by a margin where the σ count is decorative.

## What I verified against the pinned sources (register §1ap — adverse findings checked as hard as favourable ones)

| item | codex | agy | my recomputation | source check |
|---|---|---|---|---|
| q₀ = Ω_m/2 − Ω_Λ | −0.5268 ± 0.011 | −0.527 ± 0.008 | −0.5268 ± 0.01095 (flat-fit propagation) | Planck lines 2169–2170, 1773 ✓ |
| ρ_matter (g cm⁻³) | 2.6915e−30 | 2.69e−30 | 2.6915e−30 ± 7.6e−32 | H₀ line 1768 ✓ |
| Λ_measured (cm⁻²) | 1.0892e−56 ± 0.029e−56 | 1.09e−56 | 1.0891e−56 (from Ω_Λ,H₀); 1.0892e−56 ± 2.9e−58 (from Ω_Λh² line 1775) | ✓ |
| Λ / Pathria's printed Λ_c (1.0e−57 at H₀=75, q₀=1) | 10.89 | — | 10.89 | eq. (20), line 447 ✓ |
| Pathria's own Λ_c reproduced from codex's closed form λ_c(q₀) | — | — | λ_c(1)=0.1547 → 1.017e−57 cm⁻² — **reproduces Pathria's printed 1.0e−57**, so the closed form is right and so is Pathria's 1972 arithmetic | ✓ |
| Λ_c at Planck's own Ω_m, Ω_K = −0.001 (agy's formula Λ_c = (4/9)(H₀²/c²)(Ω_m+Ω_Λ−1)³/Ω_m²) | — | 2.38e−65, ratio 4.6e8 | 2.363e−65, ratio 4.61e8 — formula derived independently (turnaround cubic Λ_c = 4/(9C²), C = Ω_m(c/H₀)(Ω_tot−1)^(−3/2)) | ✓ |
| quotes | 5 Pathria + 4 Planck | 3 Pathria + 4 Planck | all located verbatim (Pathria lines 394–410, 443–453; Planck 471, 1768, 1773, 1775, 2169) | ✓ |

**Cleanest single statement (mine, from the same algebra):** holding Planck's Ω_m and Ω_Λ, Pathria's
Λ ≤ Λ_c requires a closed universe with **Ω_K ≤ −0.77**. Planck+BAO: Ω_K = 0.001 ± 0.002. No fit of any
dataset puts Ω_K within two orders of magnitude of that.

## Two imprecisions found, neither changing the verdict

1. **codex:** "the upper and lower inequalities have a nonempty physical interval only for q₀ > 1/2".
   Incomplete — a second branch exists for **q₀ < −1** (little matter, huge Λ; the bouncing/critical
   family). My root check: exists for q₀ ∈ {−2, −1.2, 0.51, 1}; does not for {−0.9, −0.527, 0, 0.4, 0.49}.
   Correct firing condition: **fire if −1 < q₀ < 1/2 is established.** Planck's q₀ = −0.527 sits inside
   that gap by 43σ on the lower side and 94σ on the upper side. Verdict unchanged.
2. **agy:** "Λ ≤ Λ_c necessitates q₀ ≥ 1/3 (or q₀ ≤ −1)". The 1/3 is where the discriminant turns
   positive, but both roots stay negative until q₀ > 1/2; the existence boundary is 1/2, as codex had.
   agy's separate 65σ figure is against eq. (6)'s q₀ > 0 (a stated input assumption of the paper, OCR
   line 122 shows "> 0 (6)"), a weaker bar than (18). Verdict unchanged.

Both imprecisions are in the *stated* boundary, not in the evaluation; the measured point is far from
every candidate boundary, so no third seat is mandated (the split rule triggers on token disagreement,
which did not occur).

## Author-supplied or lane-supplied threshold?

**Author-supplied.** Pathria's eq. (18) is a conjunction he asserts as necessary ("we must have"), and
eqs. (20)–(22) are his own numerical consequences of it. We supply only the evaluation convention
(Gaussian σ from Planck's 68% errors; flat-fit error propagation for q₀). Nothing about the firing
depends on that convention — the ratio Λ/Λ_c is 10.9 against his printed bound and ~5×10⁸ against his
bound re-evaluated at today's densities.

## What the lane does NOT do here

- The standing is **not stamped**. FIRED/LIVE is Duho's word (precedent: entry 44). Packet filed to
  `OPEN_QUESTIONS_FOR_DUHO.md`.
- No bibliography edit. On a FIRED stamp: entry 1 gets a standing-table row in §0 (alongside 7/31/51/44)
  and the tally headline becomes 3 fired / 2 live calibrated falsifiers.
- The paper hold stands; nothing outward.
