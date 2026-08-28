# MERIT PANEL SCORES — MERGED f_esc z-sweep draft (fesc-zsweep-merged-paper-20260804T1040K)

Target: `MERGED_FESC_ZSWEEP.tex` (post R1–R4, per `LANA_MINOR_FIXES.md`) with
`fesc_zsweep_trend.pdf/png`, `TREND_RESULTS.json`, `MERGE_CHANGELOG.md`, and Kun's
referee report `KUN_MERGED_REFEREE.md` (verdict **MINOR**, all four required revisions
since applied and receipts verified — figure y-label inspected directly by this panel,
now unambiguously `req`).

Rubric: the shipped 5-member panel structure from `frontend/src/app/lab/paperScores.ts`
— five seats (DR = literature precedent, Hwao = synthesis & field impact, Tori =
framing & motivation, Kun = adversarial, Goru = rigor & result-solidity), each scoring
**originality × significance** on 1–10 with a grounded note. Advisory, not a validated
peer-review judgment; the grounded reasons matter more than the numbers.

**DR seat: ABSTAINS for this packet** (same grounds as the pre-merge packet; abstention
note at the end). Scores, medians, and means below are over the FOUR remaining seats —
directly comparable to the pre-merge 4-seat numbers in
`papers-overnight-20260803T2328K/LC-fesc-decision-packets/MERIT_PANEL_SCORES.md`.

## What the panel is scoring (one paragraph of context)

The three overnight single-redshift drafts (z=7/8/9; 4-seat merit means 3.1/2.8/3.6)
were superseded by one merged z=6.0–10.0 sweep (Δz=0.5, nine runs, 40k-draw systematic
MC each, fixed seed). The new content — computed in this lane, present in none of the
source drafts — is the trend analysis itself: the closure-crossing redshift
z_c=8.05 (bootstrap 16–84%: 8.03–8.06) where the 16–84% interval of the deficit
detaches from zero, the median crossing z_m=6.33, and a `boost=none` corner sweep
showing the shortfall *strengthens* (z_c→7.62) when the JWST-motivated, most
crisis-correlated prior is removed. All six pre-merge panel defects (E1–E6) are
repaired or disclosed: lane-computed z-specific figure (E1), JWST-provenance
contradiction retracted in §2.4 (E2), the z-independent inferred side stated in
abstract/figure/table rather than hidden (E3), an explicit closure criterion with the
z=8 boundary asymmetry stated (E4), framing narrowed to the one question the shipped
landscape paper does not answer (E5, partially — overlap remains structural), and the
"dex-frac" unit retired (E6). Kun's referee pass independently re-executed the model
and reproduced every headline number.

## Persona scores

| persona (lens) | originality | significance | note |
|---|---|---|---|
| DR (literature precedent) | — | — | **ABSTAINED** (see abstention note) |
| Hwao (synthesis & field impact) | 5 | 6 | The merge converts three redundant grid slices into the one thing the sweep actually contains: a falsifiable number, z_c=8.05, on the live Muñoz-vs-Davies budget dispute — and the none-corner direction argument (removing the JWST-coupled prior *strengthens* the shortfall) is the kind of self-test that makes a synthesis quotable. Field impact is real but bounded: it is still per-z arithmetic over the same maintenance equation as the shipped landscape paper, no new datum enters, and its sharpest output is a statement about frozen anchors — its stated endpoint ("proxy transport is the only remaining escape route") points at the measurement someone else must make. |
| Tori (framing & motivation) | 7 | 6 | The framing problem that sank the drafts is genuinely solved: one deliberately narrow question ("at which z does the mismatch stop being attributable to the stated systematics?"), a title whose one imprecise word was fixed at referee demand ("above z≈8"), modality declared in the abstract's last two sentences, and the z=8 boundary case told with the asymmetry (closure survives only at the 1σ edge, 83% of mass in deficit) instead of the old "CLOSES" spin. The conclusion's closing sentence — on these anchors, proxy non-transport is now the only escape route by which the z≳8 budget closes — is the sharpest sentence any version of this work has produced. Docked on motivation: the crisis stakes are still inherited wholesale from Muñoz/Davies, and the honest answer to "why these anchors?" remains "they are the pipeline's constants." |
| Kun (adversarial) | 4 | 5 | I refereed this merge (MINOR, R1–R4 since applied) and could not break its numbers — my own re-execution reproduced z_c, z_m, the corner, and all nine rows. But merit is not correctness. Originality capped at 4: the sweep is the shipped landscape calculation given a z-axis, and z_c is arithmetic guaranteed at spec time — the inferred side is a z≈0.3 constant, so *some* crossing had to exist; the original content is locating it, bounding it (bootstrap ±0.02), and the none-corner direction proof. Significance capped at 5 by the paper's own honesty: the 93%/97% shortfall fractions are conditional probabilities given frozen anchors, not the probability a real shortfall exists, and the dominant systematic (proxy transport) lies entirely outside the MC. A well-measured number about a model of the literature, not about the sky. |
| Goru (rigor & result-solidity) | 4 | 6 | The most solid artifact this pipeline has produced: nine run JSONs reproduced to 2.2e-16, headline crossings independently re-derived by the referee from a fresh MC stream, sign-robustness tabulated per-z with the one non-robust point (z=6.5) explained correctly as adjacent to the median crossing, the conservative-direction corner actually run rather than argued, and figure/caption/table mutually consistent on direct inspection. Originality of method is modest (percentile crossing plus bootstrap on a standard budget model). Significance held at 6, not higher, for the same structural reason as ever: "robust to the *stated* systematics" is load-bearing — the calculation cannot be wrong about the anchors, and cannot be right about the universe, and it now says so in the correct places. |

## Medians, means, deltas vs pre-merge

4-seat medians (this packet): **originality 4.5, significance 6.0.**
4-seat merit mean (all 8 scores): **(5+7+4+4+6+6+5+6)/8 = 5.4.**

| packet | orig median | sig median | 4-seat merit mean |
|---|---|---|---|
| pre-merge ovl6221700 (z=7) | 2.5 | 4.0 | 3.1 |
| pre-merge ovl6221701 (z=8) | 2.5 | 3.0 | 2.8 |
| pre-merge ovl6221702 (z=9, best) | 3.0 | 4.5 | 3.6 |
| **MERGED (this packet)** | **4.5** | **6.0** | **5.4** |
| Δ vs best pre-merge candidate | **+1.5** | **+1.5** | **+1.8** |

Yes — the merge+fixes moved the medians, and every seat moved every axis upward vs its
own best pre-merge score. For calibration against the shipped Lab portfolio: 5.4 sits
just below the reionization landscape paper (5-seat mean 5.6) and well below the
flagship tier (~6.5–7.3), which the panel considers the correct ordering — this paper
is more rigorous and more honest than the landscape paper but derivative of the same
machinery, and its ceiling is set by having no measurement in it.

## Panel summary for Duho

The panel's verdict: the merge did exactly what the pre-merge panel said a merge could
do, and the numbers reflect it — 4-seat merit mean 5.4 versus 2.8–3.6 for the three
superseded slices, with medians up +1.5 on both axes against the best of them. What
changed is not the calculation (bit-identical where it overlaps) but that the paper now
contains its own actual result: the closure-crossing z_c=8.05±0.02, a bounded, referee-
reproduced number on a top-tier live dispute, wrapped in the most honest uncertainty
framing this pipeline has yet produced (conditional-probability language, the
JWST-prior circularity bounded by an executed corner that strengthens the claim, and
proxy transportability named as the dominant untested systematic and the sole remaining
escape route). All four seats agree it clears the publishable bar that rejected the
nine autopilot papers — grounded motivation, non-circular result with the residual
circularity risk bounded in the conservative direction, defensible conclusion — and
all four agree on the ceiling: it is a rigorous propagation of frozen literature
anchors, not a measurement, so it earns "solid bounded note," not "flagship." Panel
recommendation: advance it as the sweep note it is; the natural follow-on with real
upside is the one the paper itself points at — any empirical constraint on O32/β
proxy transport at z>6 would convert this from a conditional statement into an
adjudication.

## Abstention note — DR seat

**The DR (literature-precedent) seat formally ABSTAINS on the merged draft; no DR
scores are recorded and all medians/means in this packet are computed over the four
remaining seats (Hwao, Tori, Kun, Goru).** Per standing project policy, Deep Research
output is a filed reference artifact feeding existing workflows, not a lane
replacement, and no fresh DR literature-grounding run was commissioned for this packet
— scoring the "literature precedent" lens without one would fabricate the very
grounding that lens exists to provide. The abstention is recorded explicitly, exactly
as in the pre-merge packet, so the 4-seat numbers here remain directly comparable to
those and are not mistaken for the shipped 5-seat merit structure.

MERIT_PANEL_MERGED_COMPLETE_20260804
