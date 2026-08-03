# P0 Citation and Review-Link Audit — Lana

Artifact: served 4-page PDF, SHA-256 `0866…62ef`. Public web/ADS/arXiv reads only; no login/CAPTCHA/payment prompt was encountered; no such flow was entered.

## Reference-list entries (6 total)

| Entry as printed | Identity check | Role check | Verdict |
|---|---|---|---|
| Brinchmann, J., et al. 2004, MNRAS, 351, 1151 | Matches "The physical properties of star-forming galaxies in the low-redshift Universe" (canonical MPA–JHU SFR paper) | z≈0 SFMS anchor — appropriate | **PASS** |
| Tremonti, C. A., et al. 2004, ApJ, 613, 898 | Matches "The Origin of the Mass-Metallicity Relation" | z≈0 MZR anchor + named source of the default abundance scale — appropriate | **PASS** |
| Pillepich, A., et al. 2018, MNRAS, 473, 4077 | Matches "Simulating galaxy formation with the IllustrisTNG model" | TNG model description — appropriate | **PASS** |
| Nelson, D., et al. 2019, Comput. Astrophys. Cosmol., 6, 2 | Matches the IllustrisTNG public data release paper | TNG data access — appropriate | **PASS** |
| Nakajima, K., et al. 2023, ApJS, 269, 33 | **Verified live via ADS** (2023ApJS..269...33N): "JWST Census for the Mass-Metallicity Star Formation Relations at z = 4–10 with Self-consistent Flux Calibration and Proper Metallicity Calibrators" | Primary z≳4 mass/SFR/metallicity sample — appropriate. Note the paper's headline range is z=4–10; the manuscript quotes its sample as z=3.8–8.9 (plausible actual sample bounds; acceptable) | **PASS** |
| Lisiecki, K., et al. 2025, A&A, 708, A235 | **FAIL.** A&A 708, A235 verified live (aanda.org, DOI 10.1051/0004-6361/202557118): Lisiecki, K., Donevski, D., Man, A. W. S., et al., "Impact of stochastic star formation histories and dust information on selecting quiescent galaxies with JWST photometry", **2026** (not 2025) | **FAIL.** The resolved paper is a *quiescent-galaxy* photometric-selection study; it contains no z=3–6 star-forming SFMS/MZR measurements and cannot supply the "supplemented at z=3–6 … median offsets from the local relations" role. A targeted search found **no** Lisiecki 2025 paper matching the claimed role — the citation is cross-wired or fabricated | **FAIL — identity and role** |

## Missing bibliography entries for in-text load-bearing citations

1. **PP04 (Pettini & Pagel 2004)** — the "PP04 O3N2 calibration" is the pivot of the abstract's entire matched-Te-scale MZR claim, yet has **no entry** in REFERENCES and no in-text expansion. A load-bearing calibration cited only by nickname, in support of a claim the body does not contain (see SECTION_CLAIM_LEDGER Z4).
2. **Kennicutt** — §2 uses "Kennicutt L(Hα) → SFR" for the selection forward model (a load-bearing ingredient of the de-biasing envelope) with **no entry** in REFERENCES and no year given.

## Consequence for load-bearing values

- The observed SFMS/MZR medians at z≈4.7/5.4 (+0.89/+0.96; −0.50 dex) are described as Nakajima+2023 **blended with** the Lisiecki supplement, "analysed identically in a companion paper". With the Lisiecki identity failed, the blended medians carry unresolved provenance. The companion paper is the board's **WITHDRAWN** high-z scaling-relations draft; this manuscript's handling (treating the observed elevation as an upper bound and de-biasing it) is the correct response to that withdrawal, so the *direction* and lower-bound logic of the SFMS result survive on Nakajima alone — but the exact medians must be re-provenanced in any correction.
- The "2.0×10⁵ galaxies" PP04 recompute inherits both the missing PP04 reference and the missing body analysis: blocked.

## Review-link audit (artifact-integrity defect)

- Configured review URL: `https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft_review_loop.md`
- Baseline fetch (2026-07-27T13:02:48Z): **HTTP 404**, content-type text/html (Next.js error page, 22,147 bytes).
- Live re-check from this lane (~22:15 KST 2026-07-27, WebFetch): **HTTP 404 confirmed**.
- The board card (`FrontierDrafts.tsx` FRONTIER[4]) still exposes `review:` pointing at this dead URL; the card correctly has **no** `verdict` field, and the component lede's "two now carry an automated-referee verdict" does not include this draft — so no false verdict is displayed, but the reader-facing "review" link is broken.
- `served-history.json` is a human-direction record (`model: "n/a (human-directed)"`, two `feedbackSource: "human"` entries). Per the brief, **no automated review verdict is inferred from it**. It documents intent ("showed the apparent metallicity discrepancy dissolves on a matched Te-anchored scale") that the artifact body does not substantiate — recorded here as evidence of a claimed-but-not-landed revision, not as a verdict.

**Classification:** validator/review-link-caused, artifact-integrity defect. The served paper is publicly linked to a non-existent review while carrying abstract-level claims its own body contradicts; there is no referee artifact that could have caught the Z4 contradiction.

## Stop-condition compliance

No login, CAPTCHA, payment, account, OAuth, or secret prompt was encountered during the ADS/aanda.org/nebulamind.net reads. One lane-permission denial (local `curl` HEAD) was handled by falling back to WebFetch + the pinned baseline receipt; no boundary was bypassed.
