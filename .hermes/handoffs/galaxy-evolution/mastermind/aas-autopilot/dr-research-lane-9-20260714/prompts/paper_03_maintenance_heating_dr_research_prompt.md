# Deep Research prompt - Paper 03: Optical-AGN denominator for maintenance-heating follow-up

You are the **research lane** for a NebulaMind Galaxy-Evolution manuscript. Operate **read-only**. Build a rigorous, fully source-grounded literature packet that strengthens this specific paper. Do NOT edit files, re-run analysis, or produce new measurements. Produce a literature/source packet only, in the exact output format at the end. This paper is one of a nine-paper SDSS suite; it is a **guarded optical denominator / proxy** draft, not a completed physical-feedback paper.

**Title:** Optical-AGN denominator for maintenance-heating follow-up (proposal: "Empirical duty-cycle constraints on AGN maintenance heating in massive halos").

**Operational question:** Among massive, low-sSFR SDSS emission-line galaxies, what optical BPT-AGN fraction is available as a denominator for X-ray / radio maintenance-heating follow-up? This provides an optical duty-cycle denominator, NOT a heating-to-cooling measurement.

## Hard numeric invariants (do NOT contradict or restate as your own findings)

- Massive subset (log M* >= 10.8) = 9,298 emission-line galaxies; of these 5,695 are low-sSFR by the pilot threshold.
- Optical BPT-AGN fraction = 0.430 in the massive subset and 0.607 among massive low-sSFR objects.

## Current citations in the paper

`best2005, mcnamara2007, mcnamara2012, heckmanbest2014, eckert2024` (radio/X-ray/hot-atmosphere) plus SDSS backbone `sdssdr17, brinchmann2004, york2000`. Add NEW sources.

## What to find

Prioritise 2023-2025. Focus on: (1) radio-mode / maintenance-heating duty cycles, X-ray cavity and cooling-luminosity calorimetry, jet-power estimates in massive halos and groups/clusters; (2) how an optical BPT-AGN fraction relates to (and differs from) radio/X-ray duty cycles; (3) halo-selected parent samples and non-detection modelling. All radio/X-ray calorimetric observables are future-data motivation.

**Shared data scope (all nine papers - do not contradict):** Public SDSS DR17 only (spectroscopy, photometry, emission-line measurements, MPA-JHU-style `galSpecExtra`; stellar mass and sSFR from catalog `lgm_tot_p50` / `specsfr_tot_p50`). Redshift 0.02 < z < 0.12; 3-arcsec fiber (~1.2-6.5 kpc) so measurements are fiber-centered, not global. BPT four-line classes from Halpha, Hbeta, [O III]lambda5007, [N II]lambda6584. The analysis table is a **non-random 60,000-row cap** ordered by `specObjID` = **24.0%** of the strict four-line S/N>=3 parent of **249,917** galaxies. The four-line cut is strongly sSFR-dependent (keeps 33.6% of the -12<log sSFR<-11 bin but 94.9% of the -10<log sSFR<-9.5 bin), so every fraction is conditional on optical emission-line selection and is NOT volume-complete.
## Discipline rules (mandatory)

- **Real-data-only.** Never introduce mock, synthetic, fake, placeholder, or toy data. Never invent numeric values, sample sizes, DOIs, arXiv IDs, ADS bibcodes, journal volumes/pages, or URLs.
- **Verifiable identifiers only.** Every source must carry at least one checkable public identifier (DOI, arXiv ID, ADS bibcode, journal vol/page, or stable URL). If you cannot verify a source or its identifier, **omit it** or mark it explicitly "unverified / do not integrate" - never fabricate to fill a slot.
- **Association-not-causal / denominator-not-mechanism.** This paper reports an optical association / optical denominator or target vector, NOT a causal physical-feedback result. Do not phrase any suggestion as if it established a physical mechanism, and do not contradict or restate the paper's numeric invariants as your own findings.
- **Literature = future-observable motivation, not a measured NebulaMind result.** Literature can motivate future work; it cannot create a measured NebulaMind quantity. Radio, X-ray, CO/HI, resolved-outflow, halo/group, and simulation sources are strictly future-data motivation unless those data are actually present here (they are not).
- **Prioritise 2023-2025 work**, adding foundational sources only where they carry the argument.
- **Role-tag every source** with exactly one of: `method-support`, `interpretation-caveat`, `future-data-motivation`, `not-usable`.
- Read-only: do not edit files, request credentials, publish/deploy/commit, or write DB/API/wiki/trust/cron/billing.

## Required output format (produce exactly these four sections)

**Section 1 - Source-Grounded Literature Packet.** For EACH source, a block:
- `Source N:` Authors (Year, Journal, Volume, Page)
- `Identifier:` DOI and/or arXiv ID and/or ADS bibcode (at least one checkable ID; give more when available)
- `Role:` one of {method-support | interpretation-caveat | future-data-motivation | not-usable}
- `Stance / Rationale:` 1-3 sentences tying it to THIS paper's claim boundary (the measured invariant above, a named selection caveat, or a named missing observable).

**Section 2 - Missing Real Observables Assessment.** Bulleted list of the specific observables this paper names as absent (see the paper's "full proposal requires" list) that would be needed to turn the optical denominator/association into a physical inference. State explicitly that these are **absent from the SDSS-only inventory** and must NOT be written as measured results.

**Section 3 - Wording Improvements and Citation Insertions.** For each suggestion: quote (or closely paraphrase) the paper's current sentence, then give an exact safe replacement inserting `\citep{...}` (use hedged forms like `\citep[e.g.,][]{key}` for motivation). Wording must preserve the conditional, denominator-only framing.

**Section 4 - No-Mock-Data Receipt and Safety Ledger.** Affirm: no mock/synthetic/fabricated data or citations; every identifier is verifiable; the paper's invariants were left unchanged; and the run was read-only (no file edits, DB, API, git, deploy, cron, billing, or credential access).
