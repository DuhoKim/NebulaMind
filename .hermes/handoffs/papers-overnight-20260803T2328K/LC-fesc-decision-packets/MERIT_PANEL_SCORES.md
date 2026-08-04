# MERIT PANEL SCORES — L-C f_esc sweep candidates (overnight-fesc-sweep-20260803T1330Z)

Rubric: the shipped 5-member panel structure from `frontend/src/app/lab/paperScores.ts` —
five seats (DR = literature precedent, Hwao = synthesis & field impact, Tori = framing &
motivation, Kun = adversarial, Goru = rigor & result-solidity), each scoring
**originality × significance** on 1–10 with a grounded note. Advisory, not a validated
peer-review judgment; the grounded reasons matter more than the numbers.

**DR seat: ABSTAINS for this packet** (see abstention note at the end). Scores below are
the FOUR remaining personas; medians and means are over 4 seats, not 5.

Candidates (all triaged REVIEW by the overnight loop; ovl6221703 z=10 was SHELVED and is
not scored here):

| run | study | headline numbers | stated conclusion |
|---|---|---|---|
| ovl6221700 | f_esc z=7 | required f_esc=0.105 (+0.106/−0.054) vs inferred 0.062 (+0.108/−0.039); Δmedian +0.035; 66% of MC shortfall | budget **CLOSES** within the systematic |
| ovl6221701 | f_esc z=8 | required f_esc=0.210 (+0.211/−0.107) vs inferred 0.062; Δmedian +0.130 (16–84%: −0.003 to +0.343); 83% shortfall | budget **CLOSES** within the systematic |
| ovl6221702 | f_esc z=9 | required f_esc=0.390 (+0.393/−0.200) vs inferred 0.062; Δmedian +0.302 (16–84%: +0.087 to +0.697); 93% shortfall | genuine **SHORTFALL** remains |

## Panel-level evidence (verified against the run artifacts, cited in the notes below)

- E1 — **Identical figure in all three drafts**: `result.png` is byte-identical across
  ovl6221700/01/02 (SHA-1 `c11ffb33eaa6eb24b9b7d37cfa9aaee78fc261ab` for all three), so no
  draft's figure can be showing that run's z-specific result.
- E2 — **JWST contradiction**: each abstract says "Generated autonomously from public data
  (jwst)" and `spec.data_sources=["jwst"]`, while each Data-and-method section states the
  work uses *no* survey catalog data from JWST/SDSS/TNG — only literature anchors (the
  "JWST-SFRD tail" enters as a literature systematic term).
- E3 — **z-independent inferred side**: `result.fesc.f_inferred` is numerically identical
  in all three runs (0.0234/0.0622/0.1703 at 16/50/84%), i.e. the LzLCS (z≈0.3) O32/β
  proxy value is extrapolated unchanged to z=7–9. The required side rises mechanically
  with z, so the Δ(z) trend — close at 7, marginal at 8, shortfall at 9 — is largely an
  arithmetic consequence of the assumptions, not an independent per-z measurement.
- E4 — **z=8 verdict tension**: ovl6221701 concludes "CLOSES" while its own MC gives 83%
  shortfall and a 16–84% band (−0.003 to +0.343) that barely grazes zero; the
  closes/shortfall criterion is never stated.
- E5 — **Overlap with a shipped paper**: the Lab already carries
  `/agent-reports/research-frontiers/reionization-fesc-budget-landscape.pdf`, which maps
  the same ξ_ion × SFRD × f_esc maintenance-equation degeneracy over a systematics grid;
  these three are per-redshift slices of that same calculation.
- E6 — Minor consistent defects: "dex-frac" units are ill-defined (the quoted Δ values
  match *linear* f_esc differences, not dex); figure captions duplicate the titles;
  reference keys are malformed ([Muoz2024]); the novelty gate passed all three at
  top-similarity 0.784 with reasoning that mischaracterizes the study as "using JWST data".

---

## Candidate 1 — ovl6221700 (f_esc, z=7)

| persona (lens) | originality | significance | note |
|---|---|---|---|
| DR (literature precedent) | — | — | **ABSTAINED** (see abstention note) |
| Hwao (synthesis & field impact) | 3 | 4 | A single-redshift slice of the maintenance-equation grind the shipped landscape paper (E5) already performed, delivering a bounded null — "the z~7 budget closes within the systematic envelope." The reionization/LyC frontier is live and two-sided, so an honest closes-at-7 anchor has some synthesis value for the sweep, but as a standalone it adds no new datum and moves no one. |
| Tori (framing & motivation) | 3 | 4 | The title ("shortfall is not robust to systematics at z~7") honestly matches the numbers (66% is a coin-flip-plus, band straddles zero), which is the best title/number agreement of the three. But the motivation is inherited wholesale from the crisis literature and from the landscape paper — no sharp wedge of its own, and the method section's "we use no survey data" undercuts the abstract's JWST claim (E2), muddying what the paper even wants to be. |
| Kun (adversarial) | 2 | 3 | Originality floored: this is one grid point of the already-shipped landscape calculation (E5) with zero new data, and the novelty gate waved it through on a false premise (it says the study "uses JWST data"; the method says it doesn't — E2). Significance capped at 3: the conclusion (closes at z=7) is defensible only because it's weak, the figure is a duplicate not specific to this run (E1), and the inferred side is a z≈0.3 proxy pasted at z=7 (E3). |
| Goru (rigor & result-solidity) | 2 | 4 | The MC systematic envelope is a competent bounded calculation, and here the stated conclusion actually matches its own numbers (66%, interval straddling zero → "closes" is fair). Docked hard on solidity: the shipped figure is not this run's figure (E1), the O32/β sign-robustness claim is asserted but never shown in the draft, and units ("dex-frac") don't parse (E6). No measurement is made; nothing here can be wrong in an interesting way. |

**Panel medians (4 seats): originality 2.5, significance 4.0.**
4-seat merit mean (all 8 scores): **3.1**.

## Candidate 2 — ovl6221701 (f_esc, z=8)

| persona (lens) | originality | significance | note |
|---|---|---|---|
| DR (literature precedent) | — | — | **ABSTAINED** (see abstention note) |
| Hwao (synthesis & field impact) | 3 | 4 | Same machinery, next grid point. z=8 is where the budget question actually pivots (required f_esc≈0.21 is at the edge of anything LyC surveys support), so the slice is potentially the most informative of the sweep — but the draft blunts its own pivot by declaring "CLOSES" over an 83%-shortfall MC (E4), leaving the field-impact story muddled. |
| Tori (framing & motivation) | 3 | 3 | Weakest framing of the three: the title says the shortfall is "not robust to systematics" and the abstract says the budget "CLOSES," while the paper's own numbers say 83% of the systematic MC shows a shortfall and the 16–84% band only grazes zero at −0.003 (E4). A reader cannot tell what the paper claims. The motivation paragraphs are recycled nearly verbatim from the z=7 draft. |
| Kun (adversarial) | 2 | 2 | Both axes floored. Originality: identical calculation to ovl6221700 with z0=8 in the spec — textbook salami slicing off the shipped landscape paper (E5). Significance: the headline verdict contradicts the paper's own Monte Carlo (83% shortfall labeled "CLOSES", E4) under a never-stated closure criterion; the figure is a duplicate (E1); the inferred f_esc is the same z≈0.3 constant (E3). A result whose sign flips depending on which sentence you read has no adjudicating power. |
| Goru (rigor & result-solidity) | 2 | 3 | The arithmetic is presumably the same validated pipeline as z=7, but the reported verdict fails its own numbers: calling a 16th-percentile of −0.003 with 83% shortfall mass "CLOSES" needs an explicit criterion and there is none (E4). Combined with the non-specific duplicate figure (E1), the z=8 result as written is not solid enough to quote. |

**Panel medians (4 seats): originality 2.5, significance 3.0.**
4-seat merit mean (all 8 scores): **2.8**.

## Candidate 3 — ovl6221702 (f_esc, z=9)

| persona (lens) | originality | significance | note |
|---|---|---|---|
| DR (literature precedent) | — | — | **ABSTAINED** (see abstention note) |
| Hwao (synthesis & field impact) | 3 | 5 | The one non-null slice: at z=9 the required f_esc (0.39) exceeds the proxy-inferred value with the full 16–84% systematic band above zero (93% shortfall), a falsifiable statement sitting directly on the live Muñoz-vs-Davies budget dispute. Still a literature-anchored re-derivation rather than a new line of attack, and its force depends entirely on the least defensible input (E3). |
| Tori (framing & motivation) | 4 | 5 | Best-framed of the three: the title ("a residual shortfall at z~9") says exactly what the numbers say, and "genuine SHORTFALL remains" is a claim with stakes. Docked because the framing hides that the shortfall's growth with redshift is baked in — the inferred side is a z≈0.3 constant (E3) — so the paper's sharpest sentence rests on its softest assumption, and that tension is never surfaced as the central caveat it is. |
| Kun (adversarial) | 2 | 3 | Originality floored: "the photon budget is short at z≥9 under standard anchors" is Muñoz et al. 2024's own crisis statement re-derived from the same public anchors — the paper cites it as motivation and then re-concludes it. The shortfall trend across the sweep is arithmetic, not discovery: f_inferred is byte-identical across runs (E3) while f_required scales with z, so z=9 "finding" a shortfall was guaranteed at spec time. Duplicate figure (E1), JWST contradiction (E2), and salami overlap with the landscape paper (E5) all apply. Significance held at 3 only because the band-excludes-zero statement is at least checkable. |
| Goru (rigor & result-solidity) | 3 | 4 | The most solid result of the sweep on its own terms: the 16–84% envelope (+0.087 to +0.697) genuinely excludes zero, so "shortfall survives the stated systematics" is a real, bounded conclusion, and the caveats section names the proxy-extrapolation risk. Docked because the sign-robustness under both O32 and β is claimed but not shown, the figure is not this run's figure (E1), and the z-independent inferred side (E3) means the dominant systematic — redshift evolution of the proxy calibration — is outside the MC entirely, so the quoted 93% overstates the confidence. |

**Panel medians (4 seats): originality 3.0, significance 4.5.**
4-seat merit mean (all 8 scores): **3.6**.

---

## Panel summary

| candidate | orig median | sig median | 4-seat merit mean | rank |
|---|---|---|---|---|
| ovl6221702 (z=9) | 3.0 | 4.5 | 3.6 | 1 |
| ovl6221700 (z=7) | 2.5 | 4.0 | 3.1 | 2 |
| ovl6221701 (z=8) | 2.5 | 3.0 | 2.8 | 3 |

For calibration: the strongest shipped Lab papers carry 5-seat merit means around 6.5–7.3,
and the weakest shipped item (the MZR methods synthesis) sits at ~3.0. All three sweep
candidates land at or barely above that floor. The panel's cross-candidate read: these are
one z-sweep of a single calculation (per-z slices of the shipped f_esc landscape paper),
and only the z=9 slice contains a sentence with adjudicating content — and that sentence
inherits the z≈0.3→z=9 proxy extrapolation as an unquantified dominant systematic. None
of the four scorers sees a standalone candidate that clears the publishable bar that
rejected the nine autopilot papers; if anything advances, the panel's scores point to a
single merged z-sweep note anchored on the z=9 envelope, with E1–E4 repaired first.

## Abstention note — DR seat

**The DR (literature-precedent) seat formally ABSTAINS on all three candidates; no DR
scores are recorded and all medians/means in this packet are computed over the four
remaining seats (Hwao, Tori, Kun, Goru).** Per standing project policy, Deep Research
output is a filed reference artifact feeding existing workflows, not a lane replacement,
and no DR literature-grounding run was commissioned for this packet — scoring the
"literature precedent" lens without a fresh DR sweep would fabricate the very grounding
that lens exists to provide. The abstention is recorded explicitly rather than backfilled
by another persona so the 4-seat medians are not mistaken for the shipped 5-seat merit
structure.

MERIT_PANEL_LC_COMPLETE_20260804
