# T2b AMENDMENT RULING — Shape-2 contract conflicts (C41 Track-B)

Lane: `c41-trackb-shape2-mzr-20260804T1452K`
Author: Lana (contract-semantics author, per F6 re-scope)
Ruling stamped: 2026-08-04 06:32 UTC (15:32 KST), via `date`
Inputs ruled on: `T3_RESULTS.json` (status ABORTED), `GORU_T3_REPORT.md`,
`T2B_CONTRACT_SEMANTICS.md` (the contract), `T2A_FORECAST_FROZEN.json` (forecast_id
F4_SHAPE2_PREFETCH), `MEASUREMENT_DESIGN_V1.md` (F1/F4 clauses).

## Pre-result declaration (governs the whole ruling)

This ruling is issued **PRE-RESULT**. Both conflicts arose from **column metadata** during
T3's catalog inspection: T3 stopped with `status: ABORTED` and produced **no metallicity
value, no Δ, no deficit, no FMR offset, and no figure** (`T3_FIGURE_ABORTED.png` is the
abort placeholder, not a result). Nothing in this ruling can be conditioned on a measured
number, because no measured number exists in this lane. Every clause below is therefore
conclusion-blind in the Step-1 sense, and the receipt trail (`T3_RESULTS.json` sha-pinned
in the T1/T4 manifest alongside this file) shows the ordering: conflict → ruling → resumed
fetch. This is stated up front so no reader can construe the amendment as retro-fitting.

---

## Ruling 1 — JADES-class sources: Class A′ ACCEPTED, defined below

**Conflict as reported.** JADES `gsgrat` publishes line fluxes (including auroral lines)
but no source-computed Te or O/H. T2b §3 Class A, as written, requires "Te derived and O/H
computed by the direct method in the cited source" — so JADES-class tables fall to Class X
despite carrying exactly the auroral information the anchor set exists to use. Goru's stop
was contractually correct; the contract, not the executor, is what needs judging.

**Arguments for amending (accepted).** The single-scale contract's purpose (§1, §3) is a
homogeneous Te-anchored scale. Source-computed Class A values are computed by *different*
teams with *different* Te relations, ionization corrections, atomic data, and dust laws —
that heterogeneity is a real contributor to the 0.15 dex per-anchor Te-scale class. ONE
lane-frozen, documented direct-method pipeline applied uniformly to source-published fluxes
is *more* homogeneous than the heterogeneous source computations Class A already admits.
Rejecting flux-publishing surveys while admitting heterogeneous source computations would
optimize for a formality (who ran the arithmetic) over the contract's actual objective
(scale homogeneity).

**Arguments against (found honestly, and answered or absorbed as conditions).**

1. *The §3 re-measurement bar.* §3 bars "a re-measurement performed inside this lane."
   Answer: that bar targets **flux re-extraction from spectra** and B→A promotion — acts
   that can make the anchor set result-contingent. Deriving Te by frozen, cited arithmetic
   from **published** fluxes is derivation, not measurement; eligibility is decided by
   column metadata (auroral flux present at the floor below), never by the value obtained.
   The re-measurement bar itself **stands unchanged**: no spectra are re-extracted, and no
   Class B member (auroral NOT detected) may be promoted via A′ — A′ applies only where the
   auroral flux IS published and passes the floor.
2. *Loss of source vetting.* A source that computed its own Te also handled slit losses,
   blending, and aperture corrections. A lane pipeline can silently misapply these.
   Absorbed: A′ consumes fluxes **as published, with the source's own published
   corrections**; any object whose flux table requires corrections the source did not
   publish is ineligible (falls to X, flagged `aprime_inputs_incomplete`).
3. *Expanded audit surface.* The lane becomes a producer, not just a consumer; Kun's T4
   must reproduce the pipeline. Absorbed: the pipeline is versioned, seeded, and sha-pinned
   before use (requirement 2 below) precisely so T4 reproduction is mechanical.
4. *Two sub-scales inside the anchor class.* Mixing source-computed A with lane-computed A′
   creates an A-vs-A′ seam. Absorbed: A′ is a **labelled sub-class**, and a mandatory
   overlap cross-check (requirement 4) tests the seam instead of assuming it away.
5. *Retro-fitting optics.* Amending a contract after execution stopped looks like moving a
   goalpost. Answered by the pre-result declaration above: the goalpost is being moved
   before any ball exists.

**RULING: ACCEPTED.** §3 is amended with **Class A′ — direct auroral detection,
lane-derived Te** on the following requirements, all of which are contract conditions
(violation ⇒ the member is Class X, T4-reportable):

- **A′-1 (eligibility, mechanical).** The source publishes the line fluxes needed for the
  direct method, including an auroral line ([O III] λ4363-class, O III] λ1666-class,
  [N II] λ5755-class) with published flux and uncertainty giving **S/N ≥ 5** on the auroral
  line as tabulated. Below 5: if the source publishes a usable quantitative flux limit, the
  object may enter Class B under B's existing rules (limit propagated by the same frozen
  pipeline); otherwise Class X. The floor is set at 5 — not the contract's usual
  defer-to-source rule — because the source, having computed no Te, published no detection
  criterion *for the Te use of that line*, and because low-S/N λ4363 is a documented
  blending/misidentification regime ([Fe II] λ4360). The floor is declared here, pre-fetch,
  and applies uniformly to every A′ candidate in every sample.
- **A′-2 (the frozen pipeline).** Exactly ONE direct-method pipeline for all A′ members in
  this lane, its components named, cited, and versioned BEFORE the first Te is computed,
  the whole recorded as a sha-pinned artifact (`APRIME_PIPELINE_FROZEN.*`): (a) the Te
  relation and atomic data (named code + version + atomic dataset identifiers); (b) the
  ionization-correction scheme, cited; (c) the dust law, named, with the Balmer-decrement
  (or source-published) reddening input identified per sample; (d) the electron-density
  treatment; (e) the uncertainty propagation method (Monte Carlo with fixed, recorded
  seed and draw count). No per-source tweaks; the only per-source variation permitted is
  source-published inputs (fluxes, corrections, reddening) with citations.
- **A′-3 (per-object provenance).** For every A′ member the T1 manifest records: source
  table and column ids for every input flux, the dereddening inputs used, the derived Te,
  O/H, and uncertainty, and the pipeline artifact sha. An auditor must be able to recompute
  the object from the manifest row alone.
- **A′-4 (sub-class label + seam test).** A′ is flagged distinctly from A everywhere. The
  0.15 dex per-anchor Te-scale class applies to A′ exactly as to A (§2). The machinery
  tables must carry an A-vs-A′ consistency entry: for any object (or matched subset) where
  both a source-computed and lane-computed direct value exist, the pair is compared; a
  discrepancy exceeding twice the combined declared uncertainty is reported as an anomaly
  in its own right (§4.4 discipline, applied to the seam) and never averaged away.
- **A′-5 (uniformity of standing).** A′ members are anchors with the same standing as A in
  every §2/§6 rule; no rule may weight A over A′ or vice versa post hoc.

## Ruling 2 — GLASS/MACS μ-absence: §5 OPERATES AS WRITTEN. Consequence, not conflict.

Confirmed. The GLASS/MACS catalog lacks per-object μ and its uncertainty; per §5, its
lensed members default to `cluster-line-of-sight` — "the absence of magnification data is a
declaration of exclusion, not an invitation to assume μ≈1." They are **excluded from the
main matched-mass MZR** and may appear only in the appendix/feasibility track, flagged,
never averaged with the field stratum. Losing the 10^5.7 low-mass sample from the anchor
set is exactly the outcome §5 was written to force (the z9-10 lens-contamination
precedent); it is a **consequence of the contract, not a conflict with it**. No amendment
is made or needed. One permitted (not required) path back in, already inside §5 as written:
if a published lens model provides per-object μ with uncertainty in a citable companion
source, T1 may ingest it with the full inheritance chain (survey → lens model → μ →
mass correction → mass-error term); that is a T1 data task under existing rules, not a
semantics change.

## Ruling 3 — Forecast re-freeze as v2: PERMITTED, pre-fetch, both versions receipted.

The frozen forecast (`T2A_FORECAST_FROZEN.json`, forecast_id F4_SHAPE2_PREFETCH) was
computed for an eligibility universe that this ruling changes twice over: JADES-class A′
anchors enter; the GLASS/MACS 10^5.7 members leave the anchor set. F4's purpose (design
v2 block; §6) is that **a null cannot be retro-justified** — the forecast must pre-commit
the null's information content before results exist. Since no result exists (pre-result
declaration above), re-freezing now cannot retro-justify anything; refusing to re-freeze
would instead force §6's null template to cite a forecast for a universe that no longer
exists, degrading the very information content F4 protects. Note also that the two
eligibility changes push N in opposite directions (A′ adds anchors, §5 removes them), so
the re-freeze direction was not even knowable ex ante — further evidence of blindness.

**RULING: v2 re-freeze PERMITTED**, under all of the following:

1. **Ordering.** v2 is computed and frozen BEFORE the resumed science fetch and before any
   metallicity value exists in the lane. If any Te/O-H has been computed when v2 is cut,
   the re-freeze is void and v1 governs.
2. **Blind inputs only.** v2 derives from T1 row counts, the A′-1 eligibility floor applied
   to *column metadata* (published auroral S/N), the §5 exclusions, and pre-existing
   published detection-rate priors — never from any lane-computed abundance.
3. **Both versions receipted.** v1 is retained and sha-pinned, never overwritten. The v2
   artifact cites v1's sha, states the delta per bin, and states the cause verbatim
   (eligibility change from column metadata, rulings 1–2, pre-result).
4. **No silent substitution.** Any §6 null instantiation cites v2 as "the frozen forecast"
   AND discloses, in the same statement, that v1 was superseded pre-fetch and why. §6
   requirement 1's both-numbers discipline applies to the v1→v2 pair.
5. **One re-freeze for this cause.** This ruling licenses exactly one re-freeze. Any
   further forecast change requires a new logged revision gated the same way the design
   was (§7 closing rule).

## Standing of this document

This file is a logged revision to `T2B_CONTRACT_SEMANTICS.md` under §7's closing rule
("may not alter a definition or decision rule here without a logged revision gated the
same way the design was"). §3 gains Class A′ per Ruling 1; §5 and §6 are unchanged in
text; §6's frozen-artifact pointer is updated to the v2 forecast once cut per Ruling 3.
All other semantics stand frozen. T3 may resume only after `APRIME_PIPELINE_FROZEN.*`
and the v2 forecast are both sha-pinned.

LANA_SHAPE2_RULING_COMPLETE_20260804
