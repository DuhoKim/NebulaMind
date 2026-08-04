# KUN DESIGN REFUTATION — Track-B Shape-2 measurement design v1

Lane: `c41-trackb-shape2-mzr-20260804T1452K`
Refuter: Kun (Kimi K3 via Nous). Date: 2026-08-04 ~16:50-17:40 KST.
Target: `MEASUREMENT_DESIGN_V1.md` (pre-START-gate attack, as commissioned).
Position: I stance-verified every ledger entry this design cites and red-teamed the map whose settle-lines it executes. Everything below is checked against those artifacts, the delta corpus, and the crew's prior z9-10 metallicity-deficit study history.

## VERDICT: DESIGN_SOUND_WITH_PATCHES

The design is genuinely the map's A3/A4 settle-lines executed — I verified every anchor claim against the ledger I verified: c41_012's ~25-galaxy auroral deficiency, c41_026/013/061 feasibility, c41_043-vs-{033,035,044,045} as the disputed deficit cluster, c41_040's single-methodology z<3 design. The calibration contract handles the 0.24 dex class correctly in principle (declared-scale-only, conversions with propagated uncertainty, scale-limited-not-detection rule). The assembly discipline inherits Step-1's conclusion-blindness correctly (inclusion by measurement class, frozen before fetching). And the honest-null provision is not just rhetoric — see F5, where I conclude a null here is MORE publishable than a detection. But six patches are needed before the START gate: one real circularity residue the non-circularity statement under-discloses (F1), one missing differentiation from the crew's own prior study (F2), the calibration contract's completeness on UV-vs-optical abundance channels (F3), N-statistics realism for the null claim (F4), a lane assignment to fix (F6), and a catalog-availability hedge that's honest but needs a named fallback table (F7).

---

## F1 (HIGH, circularity residue) — the named 10^5.7 low-mass catalog is a LENSING-cluster sample, and the design's own crew history proves lensing is the systematic that bites exactly here

The design lists "the in-corpus M*≈10^5.7 low-mass sample's public table" as candidate source #1's companion. I checked it: arXiv 2607.15515, "Gas-Phase Metallicity … Down to M*≈10^5.7 M⊙ at z≈4.5–10.1 from **JWST Lensing Cluster Surveys**" (DREAMS et al.) — 405 spectra, **50% of sources at M_UV>−17.5 magnified by μ>3**. The crew's own z9-10 study history (which I have read) shows this exact failure mode: the original "clean" direct-Te subset (ERO=SMACS0723, GLASS=Abell2744) was lens-contaminated, and the −0.47 dex deficit carried an unaccounted **differential-magnification systematic** until re-derived on strictly unlensed field anchors (Pollock+2026 N=5), where it became −0.69±0.03 with a ±0.16 dex total systematic budget. The design's non-circularity statement discloses "shared photometric masses between observation and some model calibrations" — good — but says nothing about LENSING, which is the demonstrated, crew-experienced, deficit-magnitude-scale systematic for exactly the low-mass regime the 10^5.7 sample occupies. A sample where half the faint end is μ>3 lensed is not a matched-mass anchor until magnification uncertainties and lens-model scatter are in the mass error budget. **Patch required:** the calibration contract must add a lensing-inheritance clause — per-sample lensing status declared (field / lensed-with-model / cluster-line-of-sight), magnification errors propagated into M*, and lensed low-mass bins either excluded from the deficit re-test or flagged as a separate stratum whose deficit is never combined with field samples. This is the shared-pipeline rule's missing half, and this crew has the scar tissue to prove it matters.

## F2 (HIGH, differentiation) — the design never mentions the crew's own z9-10 study, which already executed a Te-anchored unlensed deficit re-test and landed at "systematic-limited, NOT a detection"

The z9-10-unlensed-metallicity-deficit study (public study PDF + history on the Lab) already did a version of the A3 half: unlensed direct-Te anchors, deficit −0.69±0.03 (Pollock N=5, z=9.3–9.9), extended to z=10.6 with GN-z11, formal error budget with Te-scale 0.15 dominant, total ±0.16 dex, bootstrap 95% CI [−0.82,−0.55], and the explicit conclusion "systematic-limited — the ~22σ formal value is NOT a detection." The design's A3 re-test ("re-test the metal-poor-deficit sign and magnitude on matched stellar-mass samples") overlaps that work substantially. Maybe the intent is bigger-N, matched-mass, and the FMR half is the new content — fine — but as written, a referee (or the merit panel) will ask "how does this differ from your own z9-10 study?" and the design has no answer. **Patch required:** a differentiation paragraph — what the z9-10 study established (sign confirmed, magnitude systematic-limited), what this design adds (matched-mass re-test across the FULL z>3 range not just z~9-10, the A4 FMR offset which z9-10 never touched, and the model-prediction confrontation via ledger'd claims), and whether the z9-10 unlensed anchor set is reused (it should be, declared as prior crew work with its error budget).

## F3 (MEDIUM-HIGH, calibration contract completeness) — the contract covers Te-vs-strong-line O/H, but the 10^5.7 paper's own headline anomaly is a UV-vs-optical N/O discrepancy of ~1.4 dex — the contract as written would let that through

The 0.24 dex class (Te vs strong-line O/H) is handled. But the named low-mass catalog reports N/O from N IV] λλ1483,1486 exceeding N/O from [N II] λ6583 by **≈1.4 dex** in its 10^7.7 M⊙ stack — a UV-line vs optical-line abundance-channel mismatch an order of magnitude larger than the trap the contract names. The contract says "strong-line values enter ONLY through explicitly declared conversions" — but it does not explicitly cover (a) UV-line diagnostics vs optical-line diagnostics as separate abundance channels requiring their own declared bridge, or (b) abundance RATIOS (N/O, C/O) whose scale offsets differ from O/H's. The map's A3 carries exactly this lesson (c41_035: N2S2-vs-N2O2 inconsistency off the z~0 locus; c41_006: [Si III]-vs-optical non-correlation). **Patch required:** extend the contract one clause — abundance ratios and UV-line diagnostics are separate declared scales; no O/H-scale conversion is reused for X/O ratios without a per-channel validation; any channel-pair discrepancy >2× the combined declared uncertainty is reported as a channel anomaly, not averaged away.

## F4 (MEDIUM, honest-null math) — a null IS publishable here, but only if the design pre-commits the N at which "scale-limited" is informative rather than vacuous

The bar (the autopilot rejections) demands a non-circular result and a defensible conclusion. A null ("scale-limited at current anchor statistics") answers A3's settle-line ONLY if the anchor statistics are stated. The corpus anchors are thin: ~25 auroral galaxies at z>3 (c41_012), plus limits-class samples, plus the 405-spectrum lensing sample (F1 caveats), plus z<3 continuity. Realistic Te-anchored matched-mass bins at z>3 will be single-digit-to-few-tens per mass decade. With the 0.24 dex inter-scale class as the floor and ~0.15 dex Te-scale per-anchor (z9-10's budget), the matched-sample deficit precision will sit at ~0.1–0.2 dex — meaning the design's detectable-deficit threshold is comparable to the z9-10 deficit magnitude itself. That is EXACTLY the regime where "scale-limited" is a real answer (it bounds the deficit below the scale floor, which is what A3's settle-line asks: can the deficit claims survive a declared scale at current statistics?). But it must be pre-committed: **patch required** — state the forecast precision per mass bin BEFORE fetching (so the null can't be retro-justified), and define the null's information content: "at N anchors per bin, deficits larger than X dex are excluded at the scale floor; below X, scale-limited." Without the forecast, "honest null" is an escape hatch, not a result.

## F5 (analytical, supports the design) — why the null is genuinely publishable at the bar

The bar rejects circular non-results, not nulls. This design's null is non-circular by construction (assembly is result-blind; the scale contract is pre-registered; the comparison metric is frozen before any model overlay). A3's settle-line explicitly asks whether the deficit claims survive re-test on matched samples with Te anchors — "no, not at current anchor statistics, and here is the precision at which that is true" is a direct, falsifiable answer to that question, with the anchor-gap quantified (which is itself the A3 deficiency c41_012 names). The FMR half (A4) has no z>3 execution at all, so ANY fixed-methodology result there — including "inconclusive at declared scale" — is new. The design's own success/failure framing is correct; F4 is about making the null's precision pre-committed, not about whether a null can pass.

## F6 (LOW-MEDIUM, lanes) — T2 (calibration-contract authorship) is misassigned to Lana; it belongs with whoever owns the external-data machinery, and T4's independence needs one guard

Lana's proven competence is no-overclaim semantics, map synthesis, and composition (Step-4, Step-6 — both survived my red-teams). The calibration-contract document is a METROLOGY protocol (scale declarations, conversion tables, error propagation rules, lensing inheritance after F1) — closer to the nm_external_data / measurement machinery Goru has been running (Step-1 filter, Step-3 extraction, Step-4 rebuilds, trend-grid reruns — all deterministic, all survived). Hwao authored this design and owns doctrine; the contract's SEMANTICS (what counts as "declared scale", "scale-limited") should stay Hwao+Lana, but the conversion-table MACHINERY should be Goru's with Kun verifying. As written T2 gives Lana a metrology artifact outside her demonstrated lane. Minor re-scope, not a blocker. T4 (me) is correctly adversarial; one guard: I stance-verified the ledger this design builds on, so my T4 pass must explicitly treat the A3/A4 ledger anchors as inputs-to-attack, not as my-own-prior-work-to-defend — stated here for the record.

## F7 (LOW, catalog realism) — the availability hedge is honest but names no fallback table

"JWST NIRSpec Te-detection compilations (JADES/CEERS/GLASS/UNCOVER-class auroral-line samples), verify exact VizieR/table availability at execution — none are asserted as certain." Correct epistemics (matches my C41 plan-review demand that table IDs not be invented). But the fallback ("falls back per plan to shape #1") is study-level; there's no table-level fallback chain (if the 10^5.7 table's public version lacks per-object Te flags, what substitutes? if JADES auroral compilations are behind proprietary periods, does the crew's own cached fulltext of the in-corpus auroral papers — 013/026/061-class, which ARE locally cached from Step 2 — serve as the seed set?). **Patch (small):** name the in-corpus cached auroral sample as the guaranteed floor of the assembly (it exists on disk, sha-pinned, stance-verified), with public-catalog growth atop it. That makes the worst-case assembly concrete instead of hypothetical.

## Attacks that failed (design features that survive)

- Assembly-rule conclusion-blindness: frozen-before-fetch, inclusion by measurement class (auroral detection / Te-consistent limit), never by result — this is Step-1's discipline, which I refuted and sealed. The class definitions are conclusion-free.
- Model-side re-simulation ban: predictions enter as ledger'd cited claims (the Step-4 pattern I verified), never re-simulated; the comparison metric is frozen in the design document before data. The residual shared-mass coupling is disclosed (F1 extends it to lensing, but the base disclosure is honest).
- The 0.24 dex handling in principle: declared-scale-only + conversions-with-uncertainty + scale-limited-not-detection is the correct contract for the trap class (F3 extends its coverage; it does not contradict it).
- Settle-line fidelity: every design anchor (c41_012/026/013/061/043/033/035/044/045/040) verified verbatim against the stance-verified ledger — the design executes the map, it does not invent a question.
- Gate hygiene: docs-only, START gate named verbatim, history file exists with Duho's SHAPE-2 direction recorded in nm_paper_history format.

## Patches (pre-START, ranked)

1. F1 lensing-inheritance clause in the calibration contract (field/lensed strata; μ-errors into M*; no field+lensed deficit combination).
2. F2 differentiation paragraph vs the z9-10 study (what's reused, what's new).
3. F3 contract extension: abundance ratios + UV-line channels as separate declared scales.
4. F4 pre-committed per-bin precision forecast + null's information content definition.
5. F6 T2 re-scope (metrology machinery to Goru; semantics Hwao+Lana; Kun T4 independence note recorded).
6. F7 name the in-corpus cached auroral set as the assembly floor.

## Evidence ledger

- Verified against stance-verified ledger: all nine design anchor entries (012/026/013/061/043/033/035/044/045/040) — assertion text matches my Step-5 verified content exactly.
- Checked the 10^5.7 sample: arXiv 2607.15515 in delta corpus (cluster 41) — title/abstract confirm lensing-cluster surveys, 405 spectra, μ>3 for half the faint end, N IV]-vs-[N II] 1.4 dex anomaly, empirical stack calibrations to 10^6.6.
- Checked prior crew work: z9-10-unlensed-metallicity-deficit_history.json (full) — lens-contamination failure mode, unlensed re-derivation −0.69±0.03, GN-z11 extension, ±0.16 systematic budget, "NOT a detection" discipline.
- Checked tooling: nm_external_data.py (VizieR TAP + retry/backoff + cache — capable of the data plan); dispersion_v2.json (metallicity/stellar_feh/alpha_fe all "contested (same-epoch)" — consistent with the axis premise).
- Verified gate artifacts: history JSON with Duho's verbatim SHAPE-2 direction; design is docs-only.
- Not done (boundary): no network (catalog availability deliberately unchecked — it's an execution-stage task the design correctly defers); C41 ledger not re-verified (Step-5 stands).

## Uncertainties

- Whether the 10^5.7 paper's public VizieR table carries per-object Te flags and lensing magnifications (unchecked — no network; F1/F7 make this an execution-stage verification with the in-corpus floor guaranteed).
- The exact N reachable per matched-mass bin (F4's forecast is the design's to pre-commit; my ~0.1–0.2 dex precision estimate is from the z9-10 budget + anchor counts, an estimate not a measurement).
- Whether Hwao intended T2-as-Lana for authoring-style reasons (the contract is a protocol DOCUMENT); F6 is a competence-fit recommendation, not a claim Lana can't write documents.

---

KUN_SHAPE2_DESIGN_COMPLETE_20260804
