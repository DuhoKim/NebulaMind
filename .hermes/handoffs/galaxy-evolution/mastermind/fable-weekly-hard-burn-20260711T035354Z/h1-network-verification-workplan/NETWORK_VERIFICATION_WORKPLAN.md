FABLE_HARD_BURN_H1_NETWORK_WORKPLAN_20260711T035354Z

# Unified gated network-verification workplan (rollup follow-up item 1)

Burn `fable-weekly-hard-burn-20260711T035354Z`, lane H1. Generated 2026-07-11T04:15:06Z by Fable. **PLAN ONLY - zero network calls performed.** Execution of every item below is gated on separate Duho approval; the sidecar channel additionally sits under `DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`. Machine-readable mirror: `network_verification_queue.json` (same 47 items, same field content).

## 0. Input custody (pinned vs recomputed sha256)

All seven inputs recomputed at run start; **all seven MATCH their pins** - every input usable.

| Input (prior burn root) | pinned = recomputed sha256 | result |
|---|---|---|
| `p2-cycle7-source-ledger/SOURCE_LEAD_LEDGER.json` | `faadcc22f20e0037...` | MATCH |
| `p2-cycle7-source-ledger/AGN_SFR_STATUS_DEBATE_MAP.md` | `8f3d33429bd70b37...` | MATCH |
| `p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md` | `874794a1ea1202ce...` | MATCH |
| `p3-m3-rt-baseline/M3_ACCEPTANCE_BASELINE.md` | `d028f3c716cc123b...` | MATCH |
| `p3-m3-rt-baseline/RT_CARDS_DEEPENING.md` | `21564dd6d78c7248...` | MATCH |
| `p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md` | `1c8d9a7d28566a19...` | MATCH |
| `p1-rp1-invariants/INVARIANT_MANIFEST.json` | `f4eb857e8cc20022...` | MATCH |

Full hashes: receipt and JSON mirror. Prior burn root: `.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z`.

## 1. What this plan merges

One deduplicated, priority-ordered queue of **47 items** covering:

- **P2**: all **39** `NEEDS_NETWORK_VERIFICATION` leads (N01-N13, U01-U26) from `SOURCE_LEAD_LEDGER.json`, folded into **19 dedup clusters** (same paper/survey -> one fetch covering every label instance).
- **P1**: the four gated literature slots **EXT-1...EXT-4** from `INTRODUCTION_LITERATURE_REFERENCE.md` section 3 (EXT-4 collides with P2 N08 - one fetch, two consumers).
- **P3**: **all 17** per-card `GATED - needs sidecar/network pass` items from `RT_CARDS_DEEPENING.md` Cards 1-6 (e)-sections, with acceptance wired to `M3_ACCEPTANCE_BASELINE.md` gates/CHKs.
- **P4**: **all 13** claim/evidence candidates from `CLAIM_EVIDENCE_CANDIDATES.md` as external-value enrichment targets, grouped into 8 offline adoption items that consume upstream outputs.

Coverage tally - P2: 39/39; P1: 4/4; P3: 17/17; P4: 13/13 (asserted programmatically at generation time).

## 2. Ordering rules

- Rule 1 (brief): the five retained P2 leads run first, in debate-map section-6 relative order: N01, N09, N07, N05, N11 -> NVQ-01..NVQ-05.
- Rule 2: remaining section-6-named items follow in section-6 order: U19 (section-6 rank 2, displaced below the retained five by Rule 1 - displacement is deliberate and documented), then N08 -> NVQ-06, NVQ-07.
- Rule 3: P1 EXT slots rank next (manuscript-audit blocker: 'missing explicit quantitative comparison to prior work'); EXT-4 is satisfied inside NVQ-07 (dedup).
- Rule 4: remaining P2 linked leads (N03/N04, N10, N12, N13), then P2 uncited clusters (U-family dedup groups) - all after the section-6-named seven, satisfying section-6 item 8.
- Rule 5: P3 per-card items rank after P2/P1 because they are literature sweeps routed primarily to the gated M3 sidecar (one batched run adjudicated against M3_ACCEPTANCE_BASELINE), not single-claim fetches.
- Rule 6: P4 enrichment items are offline adoption steps that consume upstream outputs - they close the pass but perform no fetches.

## 3. Execution channels, verdicts, fail-closed defaults

- **DIRECT_FETCH** - Supervised fetch pass (approval required): snapshot every fetched page/PDF, record bytes+sha256 (cycle-7 capture-set custody pattern), transcribe claims character-exact with anchors, write one verification note per item, propose ledger/manifest deltas. No DB/API/wiki writes.
- **M3_SIDECAR_PRIMARY** - Gated Gemini Deep Research run over REQ_M3_RT_20260711T091128Z, adjudicated per M3_ACCEPTANCE_BASELINE.md (G1-G8, F1-F5, per-card CHKs). Sidecar answers are advisory leads; per-item closure happens only after local adjudication. Direct fetch is the fallback channel for any card item the sidecar misses (NOT_ADDRESSED).
- **OFFLINE_AFTER_UPSTREAM** - No network. Drafts enrichment deltas from CONFIRMED upstream items; integrator-gated adoption into candidates/ or wiki staging.
- **EITHER** - Open literature search; route to whichever approved channel runs first.

Verdict vocabulary: `VERIFIED_NETWORK` = claim confirmed against pinned snapshot(s), character-exact, with anchors; `REFUTED_NETWORK` = source contradicts the claim - lead dies; record the true span; `PARTIAL` = some sub-claims confirmed; itemized; `NOT_FOUND` = claim absent from the source - stays unusable; `UNREACHABLE` = fetch failed (paywall/dead link) - stays NEEDS_NETWORK_VERIFICATION; note the block.

Fail-closed defaults (bind every item):
- Any transcription mismatch -> the mismatching sub-claim stays unusable; no nearest-rounding, no paraphrase-to-number.
- Every fetched ID (DOI/arXiv/bibcode) is QUARANTINED_PENDING_LOCAL_CHECK until it resolves (G5).
- No adopted external numeral without a same-change external_references manifest entry (P1 section 3 rule b).
- Wording contract binds all outputs: no establishes/proves/settles/confirms-that register; non-commensurable absolute quantities labeled at every mention (G2/G4).
- New bibitems are declared changes (RCA section 5.5); prefer cycle-5 bib keys.

**Manifest-registration mechanics.** INVARIANT_MANIFEST.json currently has 105 entries and NO external_references block (verified: 0 occurrences). Adoption therefore requires ADDING the block itself - a declared manifest change to stage with the first registration.

Proposed `external_references` entry schema:

```json
{
 "id": "EXT-REF-<SLUG>",
 "exact_string": "<verbatim adopted numeral/string>",
 "kind": "external_reference",
 "source_citation": "<author year, venue, DOI/arXiv/bibcode>",
 "source_snapshot_sha256": "<sha256 of pinned fetch snapshot>",
 "verified_utc": "<UTC>",
 "verification_note": "verification-notes/<item>.md",
 "allowed_context": "<mandatory labels incl. non-commensurability where applicable>",
 "match_mode": "substring",
 "occurrences_expected": "<n per candidate file>",
 "labels_required": [
  "as applicable"
 ]
}
```

## 4. The queue (priority order)

### Tier A - retained five (debate-map section-6 order)

#### 1. NVQ-01 - Ellison et al. (2016) global matched-control SFR offset

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 N01, N02
- **Claim/value at stake:** Headline: median global DeltaSFR = -0.06 dex for optically selected AGN vs matched controls (mass, redshift, local density; ANN-derived L_IR SFR; global aperture). Full-text details (N02): matching tolerances 0.1 dex in stellar mass, 0.005 in z, 0.1 dex in local density delta_5; median composite of >=5 star-forming controls; IR-selected AGN median SFR enhancement ~1.5x. Also documents (no reuse) whether the retracted -0.12 dex / 25 percent figure (R01) appears anywhere in the full text.
- **Query/URL strategy:** URL pinned in ledger: https://academic.oup.com/mnrasl/article/458/1/L34/2589536 . Alternates: ADS title search 'Star formation in AGN hosts Ellison 2016 MNRAS Letters'; arXiv mirror search 'Ellison 2016 AGN star formation matched controls artificial neural network'. Snapshot abstract page AND full text (PDF if reachable); sha256 both.
- **Acceptance criterion (upgrade condition):** N01 -> VERIFIED_NETWORK when abstract+full text state the -0.06 dex median DeltaSFR for optically selected AGN vs matched controls AND the three matching variables AND the ANN L_IR SFR methodology, transcribed character-exact with section anchors. N02 details each individually CONFIRMED/REFUTED/NOT_FOUND with anchors; any mismatch -> that detail stays unusable (fail closed). URL identity must resolve to Ellison et al. 2016, MNRAS Letters 458(1) L34.
- **Expected output artifact:** verification-notes/NVQ-01_ellison2016.md + snapshots/ellison2016.{html,pdf} with sha256; proposed ledger delta for N01/N02.
- **Manifest-registration stub:** On adoption into prose: NEW manifest external_references entry EXT-REF-ELLISON2016-DSFR {exact_string: '-0.06', allowed_context: 'global median DeltaSFR, optically selected AGN vs matched controls (Ellison et al. 2016); GLOBAL aperture - non-commensurable with RP-1 fiber-centered matched-control Delta log sSFR', labels_required: [non-commensurable]}. Registered in the same change as first prose use (P1 ref block section 3 rule b). Tolerance/enhancement numerals get separate EXT-REF-ELLISON2016-* entries only if used.
- **Risk notes:** Paywall (academic.oup.com) may block full text - abstract-level pass then covers N01 only, N02 stays open. Prior misquote history (R01) demands character-exact transcription. Non-commensurability label mandatory at every mention (wording contract rule 2 / baseline G4). Retained lead 1 of 5.
- **Depends on / feeds:** Feeds NVQ-40 (P4-C01/C03 enrichment) and debate D1. ANTI-CONFLATION: Ellison 2011 (NVQ-08, EXT-1) is a different paper by the same author - never merge citations or values.
- **Dedup:** N01+N02 merged (same paper, one fetch). R01 documentation-only sub-check attached (R01 itself is REJECTED, not a queue member).

#### 2. NVQ-02 - Simard (2011) / Mendel (2014) bulge-disk decomposition catalog

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 N09
- **Claim/value at stake:** VizieR J/ApJS/196/11 provides PSF-convolved bulge+disk decompositions for 1,123,718 SDSS DR7 galaxies (report rounded to '1.12 million'), with ugriz structural measurements, bulge-to-total (B/T) light ratios, Sersic indices - the concrete path to the morphology control RP-1 lacks (tex: R90/R50, fracDeV, petroR50/90 not retained in cache).
- **Query/URL strategy:** URL pinned in ledger: https://cdsarc.cds.unistra.fr/viz-bin/cat/J/ApJS/196/11 . Alternates: VizieR query 'Simard 2011 bulge disk decomposition SDSS'; ADS 'Simard 2011 ApJS 196 11'; separately locate Mendel et al. (2014) catalog (likely a DIFFERENT VizieR entry, e.g. masses) to untangle the bundled attribution.
- **Acceptance criterion (upgrade condition):** N09 -> VERIFIED_NETWORK when the VizieR entry resolves, the exact row count (1,123,718) is confirmed, the structural fields (B/T, Sersic index, component sizes, ugriz) are enumerated from the catalog ReadMe, AND the Simard-vs-Mendel attribution is resolved (which names belong to J/ApJS/196/11 vs a separate catalog). Fail closed on row-count mismatch.
- **Expected output artifact:** verification-notes/NVQ-02_simard_mendel.md + snapshots/vizier_J_ApJS_196_11_readme.txt sha256; column inventory table; attribution note.
- **Manifest-registration stub:** No prose numeral expected initially -> stub NONE_NUMERAL (catalog lead). If the row count enters prose: EXT-REF-SIMARD2011-NROWS {exact_string: '1,123,718'}. A future morphology-controlled rerun would register its own new invariants - out of scope here.
- **Risk notes:** Report bundles two papers under one URL - attribution error risk. CDS mirrors may differ. Row count from Tori's check (1,123,718) vs report's rounded 1.12 million: adopt only the catalog's own number. Retained lead 4 of 5.
- **Depends on / feeds:** Blocks the D2 morphology-control rerun design; feeds NVQ-23 (C1 matched-control design), NVQ-47; related NVQ-11 (Gatto used morphology-matched controls).

#### 3. NVQ-03 - Cid Fernandes WHAN diagram and W_Halpha boundary

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 N07
- **Claim/value at stake:** WHAN diagram separates weakly accreting AGN from 'retired galaxies' ionized by hot evolved low-mass stars (HOLMES); exact boundary wording at stake: 'W_Halpha = 3 A' vs '> 3 A' (raw report used 'requiring W Halpha >3 A for true weak AGN'). Which of the 2010 vs 2011 papers arXiv:1012.4426 resolves to, and whether both are needed.
- **Query/URL strategy:** URL pinned in ledger: https://arxiv.org/abs/1012.4426 . Alternates: ADS 'Cid Fernandes WHAN diagram comprehensive classification'; search both 2010 (MNRAS 403) and 2011 (MNRAS 413) papers; fetch full text (arXiv PDF - no paywall expected).
- **Acceptance criterion (upgrade condition):** N07 -> VERIFIED_NETWORK when the boundary wording is captured verbatim from the full text (operator included), the retired-galaxy/HOLMES interpretation is confirmed, and the paper identity of the arXiv id is resolved; if the boundary lives in the other paper, both are pinned and the ledger note is corrected. Fail closed if operator wording is ambiguous in-source: record both spans.
- **Expected output artifact:** verification-notes/NVQ-03_cidfernandes_whan.md + snapshots/arxiv_1012.4426.pdf sha256 (+ second paper if needed).
- **Manifest-registration stub:** On adoption: EXT-REF-WHAN-BOUNDARY {exact_string: '3 A' with verified operator and unit as printed, allowed_context: 'WHAN weak-AGN boundary (Cid Fernandes et al.), used for retired-galaxy contamination framing only'}. RP-1 already cites cidfernandes2011 (cycle-5 bib key exists - no new bibitem needed).
- **Risk notes:** Two-paper ambiguity (2010 vs 2011). Boundary-operator misquote is exactly the small-wording error class the contract targets. arXiv version vs journal version wording may differ - pin both if they diverge. Retained lead 2 of 5.
- **Depends on / feeds:** Feeds D4 (denominator contamination), NVQ-44 (P4-C08/C11 enrichment); context for RP-1 tex line 22 citation.

#### 4. NVQ-04 - Gawade (2025) TNG/EAGLE green-valley medians (preprint)

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 N05, N06, U18
- **Claim/value at stake:** Green-valley median log10 sSFR = -14.85 dex (IllustrisTNG, pile-up at imposed SFR floor) vs -11.71 dex (EAGLE, broad continuous distribution). Raw-report extras (N06): TNG pile-up 'approximately 3.5 dex below observed SDSS AGN hosts'; subgrid contrast 'stochastic thermal feedback in EAGLE versus kinetic momentum modes in TNG'. U18: enumerate exactly which floor/median values the preprint itself supports and in what context.
- **Query/URL strategy:** URL pinned in ledger: https://arxiv.org/abs/2512.22268 (24-Dec-2025 preprint). Alternates: arXiv listing search 'Gawade green valley EAGLE IllustrisTNG sSFR'; ADS arXiv:2512.22268. Pin the version string (v1/v2 + date) at check time; record refereed status.
- **Acceptance criterion (upgrade condition):** N05 -> VERIFIED_NETWORK when the -14.85 and -11.71 medians are confirmed in the pinned version with section anchors AND version+peer-review status are recorded. N06 items CONFIRMED/REFUTED/NOT_FOUND individually. U18 closes by producing the definitive list of preprint-supported values (anything outside it stays UNCITED_NOT_USABLE). Absolute simulation medians: non-commensurable label mandatory at every mention.
- **Expected output artifact:** verification-notes/NVQ-04_gawade2025.md + snapshots/arxiv_2512.22268_vN.pdf sha256; version pin block; supported-values list (closes U18).
- **Manifest-registration stub:** On adoption: EXT-REF-GAWADE2025-TNG-MEDIAN {exact_string: '-14.85'} and EXT-REF-GAWADE2025-EAGLE-MEDIAN {exact_string: '-11.71'}, each with labels_required: [non-commensurable, unrefereed-preprint, version-pinned]. The ~3.5 dex mixed sim-vs-observed gap gets NO manifest entry unless the preprint states it verbatim AND it carries the mixed-estimand label.
- **Risk notes:** Preprint may be revised or withdrawn - version drift is the top risk; unrefereed status must travel with every use. Gawade-class estimand conflation (VER blocking fact 4) is the historical failure mode here. Retained lead 3 of 5.
- **Depends on / feeds:** Feeds D5, NVQ-46 (P4-C13); scopes NVQ-22 (U26 TNG/EAGLE carve-out: 'except where directly supported by the Gawade link'); related NVQ-36 (C5 data products).
- **Dedup:** N05+N06+U18 merged (same preprint, one fetch; U18 is a usage-scope label on the same values).

#### 5. NVQ-05 - SDSS-V SPIDERS x RP-1 denominator overlap feasibility

- **Class/channel:** FEASIBILITY / DIRECT_FETCH
- **Sources:** P2 N11
- **Claim/value at stake:** Program description (supported in supervised check): optical spectroscopic follow-up of eROSITA X-ray sources, bypassing optical dust obscuration and S/N line-ratio limits. THE UNVERIFIED PART (the actual item): footprint / redshift / flux-limit overlap between SPIDERS/eROSITA source lists and RP-1's SDSS DR17 0.02<z<0.12, 60,000-galaxy denominator - the 'BPT denominator cleaning and selection-bias boundary feasibility' claim.
- **Query/URL strategy:** URL pinned in ledger: https://www.sdss.org/dr18/bhm/programs/spiders/ . Alternates: SDSS DR18/DR19 BHM documentation; eROSITA eRASS1 data-release pages; SPIDERS value-added catalog documentation; ADS 'SPIDERS SDSS-V eROSITA AGN catalog'. Two-step: (1) re-pin program description; (2) gather footprint maps, z distributions, flux limits from citable release docs.
- **Acceptance criterion (upgrade condition):** Split verdict required. (a) Description re-confirmed -> stays supported. (b) Overlap: VERIFIED only if citable release documentation yields a quantitative or map-level overlap statement with RP-1's window (sky area intersection, z coverage 0.02-0.12, flux limit implications); otherwise the feasibility claim REMAINS UNSUPPORTED and is recorded as requiring an actual catalog cross-match run (a data task, separately gated - NOT part of this network pass).
- **Expected output artifact:** verification-notes/NVQ-05_spiders_overlap.md + snapshots of program page and release docs with sha256; explicit split-verdict block; if unresolved, a scoped follow-up data-run proposal (gated).
- **Manifest-registration stub:** NONE_NUMERAL until an overlap number exists; then EXT-REF-SPIDERS-OVERLAP {exact_string: value as published, allowed_context: 'SPIDERS/eROSITA x SDSS DR17 window overlap, feasibility context only'}.
- **Risk notes:** Program pages are living documents (DR-dependent) - snapshot+hash mandatory. High risk the doc-only pass cannot settle overlap: plan already fails closed to 'unsupported + data-run proposal'. Any use must keep description vs overlap separated (INTEG retention condition). Retained lead 5 of 5.
- **Depends on / feeds:** Feeds D4, NVQ-24 (C1 AGN-power proxies), NVQ-28 (C2 parent surveys); related NVQ-32 (eROSITA cooling samples).

### Tier B - section-6 remainder

#### 6. NVQ-06 - MPA-JHU pipeline AGN-host sSFR methodology (Brinchmann/Salim)

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U19, U02, U03
- **Claim/value at stake:** The raw report's central methodological critique: MPA-JHU catalog aperture corrections (models fit to photometry strictly outside the fiber footprint, 'originally developed by Brinchmann et al. (2004) and Salim et al. (2007)') and the claim that for AGN hosts the pipeline substitutes Dn(4000)-based fits for emission-line SFRs in specsfr_tot_p50, with a claimed systematic LOW bias for old bulge-dominated hosts. Directly bears on RP-1's own proxy (V03: specsfr_tot_p50).
- **Query/URL strategy:** ADS 'Brinchmann 2004 physical properties star-forming galaxies SDSS' (MNRAS 351); 'Salim 2007 UV star formation GALEX SDSS' (ApJS 173); MPA-JHU DR7 documentation page (wwwmpa.mpa-garching.mpg.de/SDSS/DR7/); SDSS DR17 galSpecExtra table documentation. Alternates: 'MPA-JHU SFR AGN D4000 substitution', 'galSpecExtra specsfr_tot_p50 derivation'. Fetch all four; the DR17 implementation doc is decisive for RP-1.
- **Acceptance criterion (upgrade condition):** U19 closes when the pipeline's actual AGN-class treatment is transcribed from primary documentation: CONFIRMED (Dn4000 substitution + documented bias direction), REFUTED, or PARTIAL (substitution confirmed, bias undocumented). U02/U03 close when each paper's actual role in the methodology is verified. DR7-paper-vs-DR17-implementation differences must be recorded explicitly; RP-1-facing statements bind to the DR17/galSpecExtra doc.
- **Expected output artifact:** verification-notes/NVQ-06_mpajhu_methodology.md + snapshots (2 papers + 2 doc pages) sha256; role-attribution table; DR7-vs-DR17 delta note.
- **Manifest-registration stub:** NONE_NUMERAL likely (methodology, not a value); cycle-5 bib already has brinchmann2004 (salim2007 presence must be checked in the cycle-5 bibliography before use - new bibitem would be a declared change). If a bias magnitude is found and adopted: EXT-REF-MPAJHU-AGN-BIAS.
- **Risk notes:** HIGHEST-VALUE U-item (debate-map section-6 rank 2 overall; placed after the retained five per the H1 brief's 'retained leads first' rule - displacement documented in the ordering-rules section). If confirmed it reframes interpretation of RP-1's offset; if refuted the raw report's central critique loses force. Conflating DR7 methodology with DR17 implementation is the main trap.
- **Depends on / feeds:** Feeds D2, NVQ-41 (P4-C04/C05), NVQ-15 (aperture family). Anti-conflation: U19's pipeline claim vs V03 (estimator identity - already locally verified).
- **Dedup:** U19+U02+U03 merged (one methodology family; single pass covers all label instances).

#### 7. NVQ-07 - Piotrowska et al. (2022) quenching predictor + P1 slot EXT-4

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2+P1 N08, EXT-4
- **Claim/value at stake:** N08: machine-learning classification result - central-galaxy quenching predicted by integrated SMBH mass (proxy for integrated feedback history) rather than instantaneous AGN accretion output; uses global quenching threshold sSFR < 10^-11 yr^-1 (= -11.0 dex, ABSOLUTE global quantity). EXT-4 (P1 L-2 slot): a specific citable quantitative value for 'velocity-dispersion vs BPT-class quenching predictors' suitable for the gated literature-comparison sentence.
- **Query/URL strategy:** URL pinned in ledger: https://academic.oup.com/mnras/article/512/1/1052/6482843 . Alternates: ADS 'Piotrowska 2022 quenching supermassive black hole mass machine learning' (MNRAS 512, 1052); arXiv mirror. One fetch serves both consumers.
- **Acceptance criterion (upgrade condition):** N08 -> VERIFIED_NETWORK when the predictor-dominance result and the sSFR<10^-11 yr^-1 threshold usage are confirmed with anchors and URL identity. EXT-4 closes when a specific value (e.g. classifier performance or importance ordering for sigma/M_BH vs BPT class) is selected, transcribed exactly, and staged for manifest registration + the P1 L-2 sentence form. Threshold usable only with absolute/non-commensurable label.
- **Expected output artifact:** verification-notes/NVQ-07_piotrowska2022.md + snapshots sha256; EXT-4 value-selection block with candidate sentence (wording-contract-compliant).
- **Manifest-registration stub:** On adoption: EXT-REF-PIOTROWSKA2022-QTY4 {exact_string: value captured at fetch, allowed_context: per L-2 sentence} and, only if the threshold is quoted in prose, EXT-REF-PIOTROWSKA2022-SSFR-THRESHOLD {exact_string: '-11.0', labels_required: [non-commensurable, absolute-global-threshold]}. Same-change registration rule applies. Cycle-5 bib key piotrowska2022 exists.
- **Risk notes:** Paywall risk. RP-1 tex already cites piotrowska2022 (TEX:25/75) - citation evidence is NOT number verification (ledger note). R03 rejected any raw comparison of -11.0 dex against RP-1's -1.309 matched-control difference - the label must make that impossible.
- **Depends on / feeds:** DEDUP COLLISION (cross-lane): P2 N08 and P1 EXT-4 are the same paper - ONE fetch, two acceptance criteria, two consumers (ledger upgrade + manuscript slot). Feeds D3, NVQ-23, NVQ-10 (same predictor-family literature).
- **Dedup:** N08 = EXT-4 (explicit cross-lane collision, merged here).

### Tier C - P1 EXT manuscript slots

#### 8. NVQ-08 - EXT-1 Ellison et al. (2011) SDSS pair/control sSFR offsets

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P1 EXT-1
- **Claim/value at stake:** P1 L-2 slot [EXT-1]: a verified quantitative sSFR offset from Ellison et al. (2011) (SDSS pairs vs matched controls) to fill 'This offset is [larger/smaller/consistent with] the <QTY-1> dex offset reported by <AUTHOR/YEAR, sample, matching variables>'. Value currently unknown by design - P1 forbids typing it from memory.
- **Query/URL strategy:** ADS 'Ellison 2011 galaxy pairs SDSS star formation' (MNRAS family); arXiv mirror; confirm which Ellison 2011 paper the cycle-5 bib key ellison2011 actually points to BEFORE fetching (read the cycle-5 .bib entry first - offline step).
- **Acceptance criterion (upgrade condition):** EXT-1 closes when: (a) the bib-key identity is confirmed against the cycle-5 bibliography; (b) a specific offset value + sample + matching variables are transcribed exactly with anchors; (c) a candidate L-2 sentence is drafted with the mandatory aperture/selection caveat (P1 L-3); (d) the manifest registration stub is staged. Until all four: slot stays empty (fail closed).
- **Expected output artifact:** verification-notes/NVQ-08_ellison2011_ext1.md + snapshots sha256; candidate sentence + registration stub.
- **Manifest-registration stub:** EXT-REF-ELLISON2011-QTY1 {exact_string: value captured at fetch, kind: external_reference, allowed_context: L-2 comparison sentence with commensurability statement}. Registered in the SAME change that first uses it in prose (P1 section 3 rule b).
- **Risk notes:** ANTI-CONFLATION with Ellison 2016 (NVQ-01) - different paper, different aperture logic. The bib-key-identity check is mandatory because the P1 slot binds to the existing cite key, not to whichever paper a search happens to find first.
- **Depends on / feeds:** Feeds P1 literature phase and NVQ-40. Depends on offline bib-key identity check (cycle-5 package - read-only).

#### 9. NVQ-09 - EXT-2 Schawinski et al. (2010) early/late-type AGN host star formation

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P1 EXT-2
- **Claim/value at stake:** P1 L-2 slot [EXT-2]: verified quantitative value from Schawinski et al. (2010) on early/late-type AGN host star-formation comparison, for the gated literature-comparison paragraph. Cycle-5 bib key schawinski2010 exists (also cited in RP-1 tex for the degeneracy point).
- **Query/URL strategy:** ADS 'Schawinski 2010 galaxy zoo AGN host morphology star formation'; confirm bib-key identity against cycle-5 .bib first. arXiv mirror preferred for full text.
- **Acceptance criterion (upgrade condition):** Same four-part closure as NVQ-08: bib-key identity; exact value + sample + morphology-split definition; candidate sentence with caveat; staged registration. Fail closed otherwise.
- **Expected output artifact:** verification-notes/NVQ-09_schawinski2010_ext2.md + snapshots sha256.
- **Manifest-registration stub:** EXT-REF-SCHAWINSKI2010-QTY2 {exact_string: value captured at fetch}. Same-change registration rule.
- **Risk notes:** ANTI-CONFLATION: Schawinski 2014 (NVQ-17, green valley) and Schawinski 2015 (NVQ-16, flickering) are different papers - three Schawinski entries in this queue, never merged.
- **Depends on / feeds:** Feeds P1 literature phase, NVQ-14 (structural-claims sourcing overlap), NVQ-23.

#### 10. NVQ-10 - EXT-3 Bluck et al. (2014) central-structure quenched-fraction dependence

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P1 EXT-3
- **Claim/value at stake:** P1 L-2 slot [EXT-3]: verified quantitative value from Bluck et al. (2014) on central-structure (bulge mass / central density) quenched-fraction dependence. Cycle-5 bib key bluck2014 exists (RP-1 tex cites it in the degeneracy list).
- **Query/URL strategy:** ADS 'Bluck 2014 bulge mass quenching SDSS' (MNRAS 441); confirm bib-key identity against cycle-5 .bib first; arXiv mirror.
- **Acceptance criterion (upgrade condition):** Same four-part closure as NVQ-08. Value candidates include a quenched-fraction dependence statement - transcribe exactly whichever value the paper states in a form usable by the L-2 sentence; no paraphrased-to-number conversion.
- **Expected output artifact:** verification-notes/NVQ-10_bluck2014_ext3.md + snapshots sha256.
- **Manifest-registration stub:** EXT-REF-BLUCK2014-QTY3 {exact_string: value captured at fetch}. Same-change registration rule.
- **Risk notes:** Predictor-family overlap with NVQ-07 (Piotrowska) - keep the two papers' claims distinct (different methods/eras).
- **Depends on / feeds:** Feeds P1 literature phase, NVQ-23, NVQ-14; related NVQ-07.

### Tier D - remaining P2 linked leads

#### 11. NVQ-11 - Gatto et al. (2025) nuclear values and sample details

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 N03, N04
- **Claim/value at stake:** Nuclear (2.5-arcsec, ~2.62 kpc mean width) values: -1.34+/-0.03 dex (AGN) vs -1.55+/-0.02 dex (controls), difference +0.21 dex / '60 percent higher' - INCLUDING what quantity these describe (surface density vs rate; the raw report is inconsistent). N04 raw-only details: 293 AGN hosts; controls 0.015<=z<=0.14, 10^8.5<M*<10^11 Msun, 30 percent tolerance, 2 controls per AGN matched on morphology+axial ratio; SFR from stars <20 Myr; global SFMS offsets -0.35 (AGN) vs -0.60 (controls); AGN global SFR ~70 percent higher; 44 percent of controls totally quenched; sAGN-et +0.62 / wAGN-lt +0.15 dex.
- **Query/URL strategy:** URL pinned in ledger: https://academic.oup.com/mnras/article/539/4/3229/8120227 . Alternates: ADS 'Gatto 2025 MaNGA AGN nuclear star formation control'; arXiv mirror.
- **Acceptance criterion (upgrade condition):** N03 -> VERIFIED_NETWORK when the nuclear values, their quantity definition (resolve the surface-density-vs-rate ambiguity explicitly), aperture definition, and the +0.21 dex sign/derivation are confirmed with anchors. N04 details individually CONFIRMED/REFUTED/NOT_FOUND. HARD RULE regardless of findings: no raw comparison to RP-1's -1.309 (R02 is rejected by construction).
- **Expected output artifact:** verification-notes/NVQ-11_gatto2025.md + snapshots sha256; quantity-definition resolution block.
- **Manifest-registration stub:** Only for values actually adopted into prose: EXT-REF-GATTO2025-NUC-AGN {'-1.34'}, EXT-REF-GATTO2025-NUC-CTRL {'-1.55'}, EXT-REF-GATTO2025-NUC-DIFF {'+0.21'}, each labels_required: [non-commensurable, absolute-nuclear-quantity]. Sample-detail numerals: register only what prose uses.
- **Risk notes:** Paywall risk. R02 history (asserted commensurability) makes this the single most label-sensitive item. Quantity-identity ambiguity is itself a finding to record. MaNGA-based - see NVQ-21 for survey-parameter sourcing.
- **Depends on / feeds:** Feeds D1 (nuclear-excess side), NVQ-40 (optional labeled context for P4-C01), NVQ-21.
- **Dedup:** N03+N04 merged (same paper).

#### 12. NVQ-12 - Tempel et al. (2014) SDSS filament catalog

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 N10
- **Claim/value at stake:** Public catalog of distances to cosmic-web filaments within the SDSS footprint (Bisous model); assigns distances to filament axes; structures up to 60 h^-1 Mpc in length. Environmental-control lead (RP-1 lists environment labels among missing observables).
- **Query/URL strategy:** URL pinned in ledger: https://academic.oup.com/mnras/article/438/4/3465/1107139 . Alternates: ADS 'Tempel 2014 filaments Bisous SDSS'; CDS/VizieR search for the released catalog itself (catalog access path is part of the claim).
- **Acceptance criterion (upgrade condition):** N10 -> VERIFIED_NETWORK when the paper + released catalog confirm: public availability, filament-axis distance fields, Bisous methodology, and the 60 h^-1 Mpc figure, each with anchors. Catalog access path recorded (URL + retrieval mechanics).
- **Expected output artifact:** verification-notes/NVQ-12_tempel2014.md + snapshots sha256; catalog access-path note.
- **Manifest-registration stub:** NONE_NUMERAL until used; then EXT-REF-TEMPEL2014-* per adopted value.
- **Risk notes:** Paywall for paper; catalog mirrors may have moved since 2014 - the access-path check is the real deliverable. DR7-era footprint vs RP-1 DR17 denominator overlap is a separate feasibility note, do not assert it.
- **Depends on / feeds:** Feeds NVQ-42 (P4-C06/C09), C1 environment control; related NVQ-18 (Yang groups - complementary environment metric).

#### 13. NVQ-13 - Citable source for four-line S/N-cut practice claim

- **Class/channel:** FETCH_SURVEY / EITHER
- **Sources:** P2 N12
- **Claim/value at stake:** Unattributed raw-report claim: 'Stringent S/N cuts - typically requiring S/N>3 or even S/N>5 for all four diagnostic lines - are routinely applied', excluding obscured populations, emission-weak nuclei, and massive galaxies transitioning to quiescence. RP-1's OWN S/N>=3 cut and bias statement are verified locally (V04) - only the field-wide practice generalization needs a source.
- **Query/URL strategy:** Open literature search (no pinned URL): ADS full-text 'BPT signal-to-noise 3 four lines classification SDSS'; classic candidates to CHECK (not assert): the BPT-practice methodology sections of major SDSS emission-line classification papers already in the cycle-5 bib (kauffmann2003bpt family). Sidecar routing acceptable (M3 question-1 style sweep).
- **Acceptance criterion (upgrade condition):** N12 closes when >=1 citable source states the practice range (S/N>3, and >5 if claimed) for four-line BPT work AND the exclusion-bias characterization is either sourced or explicitly reworded as RP-1-local-only (V04 already covers RP-1 itself). NONE_FOUND is an acceptable recorded outcome -> claim stays local-only.
- **Expected output artifact:** verification-notes/NVQ-13_sn_practice.md + snapshots of whichever sources qualify.
- **Manifest-registration stub:** NONE_NUMERAL (prose citation only; S/N digits already manifest-covered for RP-1's own text via FLG-SNCUT/SUP-SNCUT-*).
- **Risk notes:** Do not import practice claims from memory - the search must find and pin them; suggested candidates above are search hints, not attributions. Overlaps CORR's open-question framing ('What remains unknown').
- **Depends on / feeds:** Feeds D4, NVQ-47 (P4-C10 selection-bias context).

#### 14. NVQ-14 - Citable sources for morphological quenching and M_BH-M_bulge scaling

- **Class/channel:** FETCH_SURVEY / EITHER
- **Sources:** P2 N13
- **Claim/value at stake:** Unattributed raw-report structural claims: (a) massive dense bulges restrict central SF via morphological quenching (gas stabilized against fragmentation) and secular exhaustion; (b) AGN preferentially reside in larger-bulge galaxies because black hole mass scales with bulge mass. Standard-textbook-flavored but fail-closed: uncited is uncited.
- **Query/URL strategy:** Open literature search: ADS 'morphological quenching' (original theory paper) and 'black hole mass bulge mass scaling relation' (canonical measurement/review). NOTE: RP-1's tex already makes the related degeneracy point citing schawinski2010, bluck2014, piotrowska2022 - check whether those in-bib keys suffice before adding any new source (new bibitem = declared change).
- **Acceptance criterion (upgrade condition):** N13 closes when each claim has either a pinned citable source (verbatim supporting span) or a documented decision to rely on existing cycle-5 bib keys, or NONE_FOUND (claim stays unusable). Two sub-verdicts (a) and (b), independent.
- **Expected output artifact:** verification-notes/NVQ-14_structural_claims.md + snapshots.
- **Manifest-registration stub:** NONE_NUMERAL expected; if a scaling-relation numeral is adopted: EXT-REF-MBH-MBULGE-* with non-commensurability/absolute labels as applicable.
- **Risk notes:** Bibliography rule pressure: prefer in-bib keys (schawinski2010/bluck2014/piotrowska2022) over new bibitems. Keep (a) and (b) separate - different literatures.
- **Depends on / feeds:** Overlaps NVQ-09/NVQ-10 fetches (same papers may serve). Feeds NVQ-47 (P4-C10), D2 context.
- **Dedup:** Partial overlap with NVQ-09/NVQ-10 (in-bib candidate sources) - marked, not merged: different claims at stake.

### Tier E - P2 uncited-source clusters

#### 15. NVQ-15 - Kewley et al. (2005) fiber covering fraction

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U04, U11, U20
- **Claim/value at stake:** The ~20 percent minimum fiber covering fraction required for nuclear spectra to approximate global values; and whether the 'z~0.04 for the SDSS 3-arcsec fiber' mapping is stated by Kewley et al. (2005) or is the report's own derivation. U11 is the corrected report's unattributed restatement of the same content; U20 the do-not-use label instance.
- **Query/URL strategy:** ADS 'Kewley 2005 aperture effects star formation rate' (AJ 129 or PASP - resolve exact venue at fetch); arXiv mirror; fetch full text.
- **Acceptance criterion (upgrade condition):** Single verification covers all three label instances (ledger note). Closes when the covering-fraction result is transcribed verbatim AND the z~0.04 mapping is attributed (in-paper vs report-derived). Fail closed: if the mapping is report-derived, it stays unusable; only the in-paper statement may be adopted.
- **Expected output artifact:** verification-notes/NVQ-15_kewley2005.md + snapshots sha256.
- **Manifest-registration stub:** On adoption: EXT-REF-KEWLEY2005-COVFRAC {exact_string: '20' as printed with percent form, allowed_context: 'minimum fiber covering fraction (Kewley et al. 2005), aperture-systematics context'}. kewley2005 cite key is named in P1 L-1 - confirm presence in cycle-5 bib before use.
- **Risk notes:** RP-1's own aperture wording (1.2-6.5 kpc, tex-governed; R07) must NOT be altered by anything found here - context only. Venue ambiguity (Kewley/Jansen/Geller 2005) - pin exact paper.
- **Depends on / feeds:** Feeds D2, NVQ-41 (P4-C04/C05), NVQ-06 (aperture family).
- **Dedup:** U04+U11+U20 merged (same content, three label instances).

#### 16. NVQ-16 - AGN duty-cycle timescale family (Hickox 2014 / Schawinski 2015)

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U05, U06, U12, U21
- **Claim/value at stake:** Timescale attributions: AGN accretion broken into bursts ~0.1-10 Myr (attributed to Hickox et al. 2014); stochastic 'flickering' picture (Schawinski et al. 2015); optical stellar tracers integrate 100 Myr-1 Gyr; H-alpha traces ~10 Myr. U12 is the corrected report's unattributed restatement; U21 the do-not-use label.
- **Query/URL strategy:** ADS 'Hickox 2014 black hole variability star formation connection' (ApJ 782); 'Schawinski 2015 AGN flickering phases' (MNRAS 451); arXiv mirrors; one pass covers the family.
- **Acceptance criterion (upgrade condition):** Closes when each timescale range is attributed to its actual source with verbatim spans (which paper states 0.1-10 Myr; which states the tracer-integration baselines; where H-alpha ~10 Myr comes from). Misattributed pieces stay unusable individually.
- **Expected output artifact:** verification-notes/NVQ-16_dutycycle_family.md + snapshots sha256; attribution table (claim -> paper -> span).
- **Manifest-registration stub:** On adoption: EXT-REF-DUTYCYCLE-BURST {'0.1 to 10 Myr' as printed}, EXT-REF-TRACER-BASELINE {'100 Myr to 1 Gyr'} etc., each only if prose uses it.
- **Risk notes:** Family attribution risk: the two papers are routinely cross-cited - the table must say which claim lives where. Timescale numerals are ranges: transcribe punctuation exactly.
- **Depends on / feeds:** Feeds D3, NVQ-33 (population duty-cycle statistics - different aspect: attribution here, statistics there), NVQ-43 (P4-C07).
- **Dedup:** U05+U06+U12+U21 merged (one claim family).

#### 17. NVQ-17 - Schawinski et al. (2014) green-valley pathways

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U01, U17
- **Claim/value at stake:** Two-pathway green-valley characterization attributed to Schawinski et al. (2014): late-type slow gradual gas exhaustion vs early-type rapid quenching (likely merger-driven); morphological quenching speeds.
- **Query/URL strategy:** ADS 'Schawinski 2014 green valley two pathways quenching' (MNRAS 440); arXiv mirror.
- **Acceptance criterion (upgrade condition):** Single verification covers both label instances (U01/U17). Closes when the two-pathway characterization and the speed contrast are confirmed with verbatim spans, or refuted.
- **Expected output artifact:** verification-notes/NVQ-17_schawinski2014.md + snapshots sha256.
- **Manifest-registration stub:** NONE_NUMERAL expected (qualitative pathway claim); prose citation would need a NEW bibitem (schawinski2014 not in the P1 named keys) - declared change, flag to integrator.
- **Risk notes:** ANTI-CONFLATION with schawinski2010 (NVQ-09) and 2015 (NVQ-16). New-bibitem cost may make this low-adoption-value despite easy verification - priority reflects that.
- **Depends on / feeds:** Feeds D5 context (green-valley definition used by Gawade comparisons), NVQ-04.
- **Dedup:** U01+U17 merged (same paper, two label instances).

#### 18. NVQ-18 - Yang et al. (2007) halo-based group catalog

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U07, U13, U22
- **Claim/value at stake:** Halo-based group catalog categorizing over 600,000 SDSS galaxies into dark-matter halos, delineating centrals from satellites; access path and fitness for group/halo-membership control in the RP-1 window.
- **Query/URL strategy:** ADS 'Yang 2007 galaxy group catalogue halo-based SDSS' (ApJ 671); locate the released catalog (group finder products; check for DR7-updated versions); record access path.
- **Acceptance criterion (upgrade condition):** Single verification covers three label instances. Closes when: catalog description (>600,000 galaxies, central/satellite flags) confirmed; public access path pinned; RP-1-window fitness stated as feasibility note (DR4/DR7-era z coverage vs 0.02-0.12) without asserting overlap numbers.
- **Expected output artifact:** verification-notes/NVQ-18_yang2007.md + snapshots sha256; access-path note.
- **Manifest-registration stub:** NONE_NUMERAL until used; then EXT-REF-YANG2007-NGAL {'600,000' form as printed}.
- **Risk notes:** Catalog superseded by later versions - pin which release the claims describe. Same fail-closed overlap posture as NVQ-05/NVQ-12.
- **Depends on / feeds:** Feeds NVQ-42 (P4-C06/C09), C1 halo-mass control, D2 environment axis; complementary to NVQ-12 (filaments).
- **Dedup:** U07+U13+U22 merged (same catalog, three label instances).

#### 19. NVQ-19 - xCOLD GASS / Saintonge et al. (2017) CO survey

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U08, U14, U23
- **Claim/value at stake:** Survey design claims: mass-selected sample to z=0.05; IRAM 30-m CO(1-0); molecular gas fractions and depletion timescales; Saintonge 2017 attribution. Feasibility angle (U14): CO gas masses for 'physical gas depletion vs sSFR artifact' tests against the RP-1 denominator.
- **Query/URL strategy:** ADS 'Saintonge 2017 xCOLD GASS survey' (ApJS 233); xCOLD GASS public data page; arXiv mirror.
- **Acceptance criterion (upgrade condition):** Single verification covers three label instances. Closes when survey parameters (z limit, mass selection, instrument, line) and data-access path are confirmed. Feasibility note MUST state the z-window mismatch explicitly: xCOLD GASS z<0.05 vs RP-1 0.02<z<0.12 - overlap is partial by construction (0.02-0.05).
- **Expected output artifact:** verification-notes/NVQ-19_xcoldgass.md + snapshots sha256; z-overlap feasibility note.
- **Manifest-registration stub:** NONE_NUMERAL until used; survey parameters would enter as EXT-REF-XCOLDGASS-* if quoted. Cycle-5 bib key xcoldgass2017 exists (TEX:75).
- **Risk notes:** The partial z overlap is the headline feasibility fact - an answer that hides it fails the item. Sample sizes (~500 galaxies) mean matched-control designs will be statistics-limited; record honestly.
- **Depends on / feeds:** Feeds NVQ-45 (P4-C12), NVQ-29/NVQ-30 (C3 CO items), D2/D3 gas context.
- **Dedup:** U08+U14+U23 merged (same survey, three label instances).

#### 20. NVQ-20 - ALFALFA HI survey coverage

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U09, U15, U24
- **Claim/value at stake:** Claims: extensive neutral-hydrogen (HI) mass maps covering the SDSS footprint; usability for HI masses in the RP-1 window (large-scale gas-reservoir control feasibility).
- **Query/URL strategy:** ADS 'Haynes 2018 ALFALFA extragalactic HI source catalog alpha.100' (survey definition + final catalog paper); ALFALFA public data pages.
- **Acceptance criterion (upgrade condition):** Single verification covers three label instances. Closes when footprint (sky area, z<~0.06 sensitivity envelope), catalog contents, and access path are confirmed; 'covering the SDSS footprint' claim gets a precise restatement (partial overlap, which strips). Same explicit z-window caveat as NVQ-19.
- **Expected output artifact:** verification-notes/NVQ-20_alfalfa.md + snapshots sha256.
- **Manifest-registration stub:** NONE_NUMERAL until used. No cycle-5 bib key known - adoption would need a new bibitem (declared change).
- **Risk notes:** 'Covering the SDSS footprint' is loose - the verification must replace it with the survey's own coverage statement. HI z ceiling (~0.06) again truncates overlap with RP-1's window.
- **Depends on / feeds:** Feeds NVQ-45 (P4-C12), C3 gas-reservoir controls.
- **Dedup:** U09+U15+U24 merged (same survey, three label instances).

#### 21. NVQ-21 - SDSS-IV MaNGA survey parameters

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U10, U16, U25
- **Claim/value at stake:** Claims: integral-field spectroscopy for ~10,000 galaxies at z<0.15; cross-match feasibility with RP-1's denominator (fiber-collision/aperture questions); U25 additionally requires delimiting exactly which MaNGA statements the Gatto link itself supports.
- **Query/URL strategy:** ADS 'Bundy 2015 MaNGA overview' (ApJ 798) + MaNGA DR17 documentation (sdss.org/dr17/manga/); one fetch set covers program parameters and data access.
- **Acceptance criterion (upgrade condition):** Single verification covers three label instances. Closes when the ~10,000 / z<0.15 parameters are confirmed from a citable MaNGA source; cross-match feasibility stated as a note (sample-intersection expectations, not asserted numbers); and the Gatto-supported subset is delimited after NVQ-11 lands.
- **Expected output artifact:** verification-notes/NVQ-21_manga.md + snapshots sha256; Gatto-scope delimitation block.
- **Manifest-registration stub:** NONE_NUMERAL until used; then EXT-REF-MANGA-N {'10,000' as printed} etc. New bibitem likely needed for a MaNGA overview citation (declared change).
- **Risk notes:** The Gatto-scope sub-item depends on NVQ-11 - partial closure allowed (parameters first, delimitation after).
- **Depends on / feeds:** Feeds NVQ-28 (C2 parent surveys), NVQ-44 (P4-C08/C11), D2 (IFU follow-up). Depends on NVQ-11 for the U25 sub-item.
- **Dedup:** U10+U16+U25 merged (same survey, three label instances).

#### 22. NVQ-22 - IllustrisTNG / EAGLE project data-access claims

- **Class/channel:** FETCH_VERIFY / DIRECT_FETCH
- **Sources:** P2 U26
- **Claim/value at stake:** Claims: 'exhaustive, publicly accessible mock catalogs containing millions of simulated galaxies' (both projects); plus the carve-out: which statements the Gawade preprint itself supports (everything else about TNG/EAGLE is UNCITED_NOT_USABLE).
- **Query/URL strategy:** TNG public data release documentation (tng-project.org/data) + Nelson et al. data-release paper; EAGLE public database (icc.dur.ac.uk/Eagle) + McAlpine et al. release paper; ADS for both release papers.
- **Acceptance criterion (upgrade condition):** U26 closes when: public-access claims are confirmed against the projects' own release documentation (what is actually released: snapshots, group catalogs, mocks - 'mock catalogs' wording checked specifically); release papers pinned; and the Gawade-supported subset is delimited after NVQ-04. Cycle-5 bib keys tng2019/eagle2015 exist (TEX:75).
- **Expected output artifact:** verification-notes/NVQ-22_tng_eagle_access.md + snapshots sha256.
- **Manifest-registration stub:** NONE_NUMERAL expected ('millions' is loose prose - replace with release papers' own counts only if adopted, as EXT-REF-TNG-*/EXT-REF-EAGLE-*).
- **Risk notes:** 'Mock catalogs' is the report's wording - the releases may expose raw catalogs, not survey-realistic mocks; that distinction is exactly what C5 items need (NVQ-36).
- **Depends on / feeds:** Depends on NVQ-04 (Gawade scope). Feeds NVQ-36 (C5 data products), NVQ-46 (P4-C13), D5.
- **Dedup:** Distinct from NVQ-04 (paper values) - marked as related, not merged: different claims (project access vs preprint values).

### Tier F - P3 per-card items (sidecar-primary)

#### 23. NVQ-23 - C1: 2020+ matched-control / causal-inference quenching studies

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C1-e1
- **Claim/value at stake:** Which 2020+ matched-control or causal-inference quenching studies exist, and what host vector each controlled (mass, sigma, morphology, environment, halo mass). Card 1's design requires per-study covariate lists - an uncontrolled correlation study adds nothing (baseline CHK-1.3).
- **Query/URL strategy:** M3 sidecar REQ question 1 (missing 2020+ reviews/high-impact studies) scoped to Card 1; direct-fetch fallback: ADS full-text 'matched control AGN quenching causal 2020-2026', citation chase from piotrowska2022/bluck2014.
- **Acceptance criterion (upgrade condition):** Item closes when the answer lists studies WITH links (G3/G5) and per-study controlled-covariate vectors, or NONE_FOUND. Scored under baseline CHK-1.3; leads land in the Tori verification queue.
- **Expected output artifact:** Card-1 lead ledger section in the adjudicated sidecar output + quarantined-ID list.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Consumes NVQ-02 (morphology catalog availability), NVQ-07/NVQ-09/NVQ-10 (predictor family anchors). Feeds Card 1 design and NVQ-47.

#### 24. NVQ-24 - C1: survey-scale X-ray/radio AGN-power proxy catalogs

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C1-e2
- **Claim/value at stake:** Existence/coverage of survey-scale X-ray and radio AGN-power proxy catalogs usable as time-averaged power proxies at SDSS scale (baseline CHK-1.4 names the per-role instrument families).
- **Query/URL strategy:** M3 sidecar Card-1 realism question; fallback: eROSITA eRASS1 catalog docs, LoTSS DR2 docs, VLASS; ADS survey-description papers.
- **Acceptance criterion (upgrade condition):** Closes when candidate catalogs are named with links + coverage/depth statements, or NONE_FOUND. CHK-1.4: each named survey/instrument must carry a citation or UNCITED_NOT_USABLE.
- **Expected output artifact:** Card-1 realism block in adjudicated output.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Related NVQ-05 (SPIDERS), NVQ-32/NVQ-33 (C4 instruments). Feeds Card 1 CHK-1.4 verdict.

#### 25. NVQ-25 - C1: DESI-era denominator availability

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C1-e3
- **Claim/value at stake:** Whether DESI-era spectroscopic denominators are public at the depth needed for matched-control quenching work (Card 1 (e): 'whether DESI-era denominators are public at the needed depth').
- **Query/URL strategy:** M3 sidecar; fallback: DESI DR1 documentation, ADS 'DESI data release galaxy survey 2024-2026'.
- **Acceptance criterion (upgrade condition):** Closes with a cited availability statement (which release, which samples, depth) or NONE_FOUND.
- **Expected output artifact:** Card-1 realism block entry.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Data-release status is time-sensitive - pin release versions and dates. Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Feeds Card 1 design options; no upstream dependency.

#### 26. NVQ-26 - C2: existing 2020+ common-denominator multiphase outflow census

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C2-e1
- **Claim/value at stake:** Does a 2020+ common-denominator multiphase outflow census already exist? (Card 2's decisive-test design assumes it does not; an existing one would reshape P1/CUR.)
- **Query/URL strategy:** M3 sidecar REQ question 1 scoped to Card 2; fallback: ADS 'multiphase AGN outflow census common parent sample 2020-2026', review-article sweep.
- **Acceptance criterion (upgrade condition):** Closes with linked candidates + how each fails/meets the common-denominator requirement, or NONE_FOUND. Scored under CHK-2.5 (denominator discipline) and CHK-2.2 (four qualifiers per number: tracer, selection, denominator, z-range).
- **Expected output artifact:** Card-2 lead ledger section.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Feeds Card 2 verdict; consumes NVQ-28 (parent-sample candidates). The 17 percent / 46 percent local anchors must never be merged (floor-1).

#### 27. NVQ-27 - C2: JWST NIRSpec-IFU and ALMA CO sensitivity/exposure realism

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C2-e2
- **Claim/value at stake:** Instrument realism at the card's z grid: NIRSpec IFU outflow detectability and ALMA CO census depth - sample-size/exposure feasibility for a phase-resolved census.
- **Query/URL strategy:** M3 sidecar REQ question 2 scoped to Card 2; fallback: JWST/NIRSpec official documentation (JDox), ALMA sensitivity calculator documentation, published survey papers with stated depths.
- **Acceptance criterion (upgrade condition):** Closes when detectability claims carry instrument/survey documentation citations (CHK-2.4) with per-tracer sensitivity limits at matched depth, or NONE_FOUND/UNCITED_NOT_USABLE per claim.
- **Expected output artifact:** Card-2 realism block.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Exposure-calculator outputs are versioned tools, not literature - cite tool version + date. Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Feeds Card 2 CHK-2.4; pairs with NVQ-26/NVQ-28.

#### 28. NVQ-28 - C2: candidate parent surveys with published selection functions

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C2-e3
- **Claim/value at stake:** Candidate parent samples (with published selection functions) on which a common-denominator census could run - the survey's selection function must be citable, not assumed.
- **Query/URL strategy:** M3 sidecar; fallback: MaNGA/SAMI/Hector docs, SDSS spectroscopic selection papers, eROSITA-selected AGN parent samples.
- **Acceptance criterion (upgrade condition):** Closes with named candidates + selection-function citations, or NONE_FOUND. Each candidate must state which phases it can host at matched sensitivity.
- **Expected output artifact:** Card-2 parent-sample table (quarantined leads).
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Consumes NVQ-21 (MaNGA), NVQ-05 (SPIDERS). Feeds NVQ-26 design.

#### 29. NVQ-29 - C3: 2020+ resolved CO/dust surveys of quenched/transition galaxies

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C3-e1
- **Claim/value at stake:** Existence and sample sizes of 2020+ resolved-CO/dust surveys of quenched and transition galaxies (Card 3 needs both gas-fraction and depletion-time terms at fixed mass/z/environment).
- **Query/URL strategy:** M3 sidecar REQ question 1 scoped to Card 3; fallback: ADS 'resolved CO survey quenched galaxies 2020-2026', ALMA archive large-program listings.
- **Acceptance criterion (upgrade condition):** Closes with linked surveys + sample sizes + whether they separate f_gas vs t_dep terms, or NONE_FOUND. Simulation medians offered by the answer must carry non-commensurability labels (CHK-3.3).
- **Expected output artifact:** Card-3 lead ledger section.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Consumes NVQ-19 (xCOLD GASS baseline anchor). Feeds NVQ-45 (P4-C12) and Card 3 verdict.

#### 30. NVQ-30 - C3: ALMA central-kpc CO feasibility at card mass/z range

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C3-e2
- **Claim/value at stake:** ALMA feasibility for central-kpc CO mapping at the card's mass and z range (resolution + sensitivity for the central-vs-global depletion split).
- **Query/URL strategy:** M3 sidecar REQ question 2 scoped to Card 3; fallback: ALMA technical handbook, published central-kpc CO studies with stated beam/depth.
- **Acceptance criterion (upgrade condition):** Closes when feasibility statements engage CO-to-H2 conversion, aperture mismatch, and SFR-timescale systematics (CHK-3.2 - a realism verdict ignoring these is incomplete), with citations or NONE_FOUND.
- **Expected output artifact:** Card-3 realism block.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Pairs with NVQ-29; feeds Card 3 decomposition design (central-vs-global labels, CHK-3.4).

#### 31. NVQ-31 - C3: published matched-control decomposition precedents

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C3-e3
- **Claim/value at stake:** Published precedents for the matched-control decomposition Delta log sSFR = Delta log f_gas - Delta log t_dep at fixed mass/z/environment.
- **Query/URL strategy:** M3 sidecar; fallback: ADS 'gas fraction depletion time decomposition quenching matched'.
- **Acceptance criterion (upgrade condition):** Closes with linked precedents + which systematic budget each propagated, or NONE_FOUND (which would make Card 3's design novel - itself a useful recorded outcome).
- **Expected output artifact:** Card-3 precedent list.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Feeds Card 3 tightened criterion; related NVQ-23 (matched-control design family).

#### 32. NVQ-32 - C4: eROSITA-era group/poor-cluster cooling-luminosity samples

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C4-e1
- **Claim/value at stake:** eROSITA-era cooling-luminosity samples at group/poor-cluster scale (the halo-mass range where maintenance heating is least constrained).
- **Query/URL strategy:** M3 sidecar REQ question 1 scoped to Card 4; fallback: eROSITA eRASS1 cluster/group catalog papers, ADS 'eROSITA groups cooling luminosity 2024-2026'.
- **Acceptance criterion (upgrade condition):** Closes with linked samples + halo-mass ranges + cooling-luminosity availability, or NONE_FOUND. Balance/deficit numbers require sample definition, halo-mass range, duty-cycle treatment, and a link (CHK-4.2).
- **Expected output artifact:** Card-4 lead ledger section.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Related NVQ-05 (eROSITA family). Feeds NVQ-43 (P4-C07) and Card 4 verdict. JWST/ALMA are marginal for this card - saying so is the correct realism answer (baseline note).

#### 33. NVQ-33 - C4: LOFAR/MeerKAT radio duty-cycle population statistics 2020+

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C4-e2
- **Claim/value at stake:** Population-level radio AGN duty-cycle statistics from LOFAR/MeerKAT-era surveys (duty-cycle-averaged heating power needs a measured duty cycle, not an assumed one).
- **Query/URL strategy:** M3 sidecar; fallback: LoTSS DR2 AGN papers, MIGHTEE, ADS 'radio AGN duty cycle population 2020-2026'.
- **Acceptance criterion (upgrade condition):** Closes with linked population statistics + selection definitions, or NONE_FOUND. Instrument-realism claims need citations (CHK-4.4).
- **Expected output artifact:** Card-4 duty-cycle statistics block.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Consumes NVQ-16 (timescale attributions - different aspect). Feeds NVQ-43, Card 4 criterion (P_heat averaging).

#### 34. NVQ-34 - C4: low-halo-mass X-ray cavity detectability limits

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C4-e3
- **Claim/value at stake:** Detectability limits for X-ray cavities at low halo mass (SC: 'low-mass halos hardest' - the honest feasibility bound the card must state).
- **Query/URL strategy:** M3 sidecar; fallback: ADS 'X-ray cavity detectability groups simulations survey', Chandra/XMM deep group studies.
- **Acceptance criterion (upgrade condition):** Closes with cited detectability bounds vs halo mass, or NONE_FOUND. Cavity-power systematics must be acknowledged (CHK-4.2).
- **Expected output artifact:** Card-4 feasibility-bound note.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Feeds Card 4 verdict bands (deficit-as-upper-bound design).

#### 35. NVQ-35 - C5: 2020+ mock-observable / forward-modeling pipelines

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C5-e1
- **Claim/value at stake:** Which 2020+ mock-observable pipelines and forward-modeled sim-vs-survey comparisons exist (synthetic MaNGA/MUSE/ALMA/X-ray/radio observables).
- **Query/URL strategy:** M3 sidecar REQ question 1 scoped to Card 5; fallback: ADS 'forward model mock observations simulation galaxy survey 2020-2026'.
- **Acceptance criterion (upgrade condition):** Closes with linked pipelines/comparisons + which observables each forward-models, or NONE_FOUND. Unlinked 'TNG reproduces X' statements are UNCITED_NOT_USABLE (CHK-5.2).
- **Expected output artifact:** Card-5 pipeline inventory (quarantined leads).
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Feeds NVQ-46 (P4-C13), Card 5 design; pairs with NVQ-36/NVQ-37.

#### 36. NVQ-36 - C5: public simulation data products exposing needed fields

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C5-e2
- **Claim/value at stake:** Which public simulation data releases actually expose the fields the card's mocks need (gas, SFH, morphology, AGN power; light-cone or snapshot mocks).
- **Query/URL strategy:** M3 sidecar; fallback: TNG/EAGLE release docs (via NVQ-22 snapshots), FIRE/SIMBA release pages as comparators.
- **Acceptance criterion (upgrade condition):** Closes with a per-project field inventory (citable release docs), or NONE_FOUND per project. Distinguish raw catalogs from survey-realistic mocks (the NVQ-22 wording issue).
- **Expected output artifact:** Card-5 data-product matrix.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Depends on NVQ-22 (access claims). Feeds Card 5 realism verdict (CHK-5.4).

#### 37. NVQ-37 - C5: selection-function documentation per comparison survey

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C5-e3
- **Claim/value at stake:** Concrete selection-function documentation for each survey the forward-model comparison would target (CHK-5.4 requires naming at least one per compared survey or NONE_FOUND).
- **Query/URL strategy:** M3 sidecar; fallback: survey-definition papers for SDSS main sample, MaNGA, plus whichever surveys NVQ-35 pipelines target.
- **Acceptance criterion (upgrade condition):** Closes with per-survey selection-function citations, or NONE_FOUND. Matching observables through selection is the card's local warrant - undocumented selection = survey unusable for Card 5.
- **Expected output artifact:** Card-5 selection-function list.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Consumes NVQ-28 outputs where surveys overlap; feeds Card 5 design.

#### 38. NVQ-38 - C6: 2020+ per-channel reviews + cross-channel evidence-weight methodology

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C6-e1
- **Claim/value at stake:** Per-channel 2020+ reviews (metallicity compilations JADES/AURORA-class, size-mass/morphology evolution HST+JWST, halo regulation lensing/clustering+DESI-era, reionization budget) AND whether any source proposes a cross-channel evidence-weight methodology (the card's actual open methodology question).
- **Query/URL strategy:** M3 sidecar REQ question 1 scoped to Card 6; fallback: ADS review sweeps per channel, 2020-2026 window.
- **Acceptance criterion (upgrade condition):** Closes with linked reviews per channel (each tagged with its channel + z scope) or NONE_FOUND per channel; a cited weight-methodology proposal is the premium outcome (CHK-6.4: ranking methodologies with citations are the desired content; channel rankings in own voice are banned). FMR/MZR claims beyond z~2.3 enter only as linked leads explicitly marked beyond local scope (CHK-6.1); no SMBH-seeding attribution to our page (F4/CHK-6.3).
- **Expected output artifact:** Card-6 per-channel review ledger.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Feeds Card 6 metric design (verified-fraction metric uses local counts - offline); related NVQ-18/NVQ-12 (halo-regulation catalogs).

#### 39. NVQ-39 - C6: JWST spectroscopy realism for FMR beyond z~2.3

- **Class/channel:** FETCH_SURVEY / M3_SIDECAR_PRIMARY
- **Sources:** P3 P3-C6-e2
- **Claim/value at stake:** Realism of extending FMR/MZR constraints beyond z~2.3 with JWST spectroscopy (the local basis is scoped to z~0-2.3; beyond is out-of-scope by construction).
- **Query/URL strategy:** M3 sidecar REQ question 2 scoped to Card 6; fallback: JWST NIRSpec sensitivity docs, JADES/AURORA-class survey papers 2024-2026.
- **Acceptance criterion (upgrade condition):** Closes with cited feasibility statements (line sets, depths, sample sizes at z>2.3) or NONE_FOUND; every beyond-scope statement carries a link + beyond-local-scope marker (CHK-6.1).
- **Expected output artifact:** Card-6 realism block.
- **Manifest-registration stub:** NONE_NUMERAL (survey-sweep item: outputs are quarantined leads under G3/G5, never direct manifest entries; any later adopted value registers via its own EXT-REF entry).
- **Risk notes:** Sidecar outputs are advisory leads only (baseline G7); every ID quarantined (G5); NONE_FOUND is a first-class answer (G8).
- **Depends on / feeds:** Feeds Card 6 scope-extension planning only; no local claim changes.

### Tier G - P4 adoption/enrichment (offline)

#### 40. NVQ-40 - P4-C01/C03 flagship-result external context

- **Class/channel:** ADOPTION_ENRICH / OFFLINE_AFTER_UPSTREAM
- **Sources:** P4 P4-C01, P4-C03
- **Claim/value at stake:** Enrich the flagship headline claim (P4-C01) and matching-quality claim (P4-C03) with verified external anchors: Ellison 2016 -0.06 dex global offset (labeled cross-aperture context), Ellison 2011 EXT-1 value, optional Gatto nuclear values as labeled non-commensurable context; matching-tolerance comparison (N02 details) for C03.
- **Query/URL strategy:** NO independent fetch. Consumes upstream verification notes; drafts enrichment deltas offline; integrator-gated adoption.
- **Acceptance criterion (upgrade condition):** Delta drafted only from CONFIRMED upstream values; every external numeral carries its EXT-REF manifest entry in the same change; comparison sentences follow P1 L-2 form with L-3 boundedness paragraph; zero unmatched numerals in the numerals_check.
- **Expected output artifact:** enrichment-deltas/NVQ-40_delta.md (proposed claim_text additions + references), integrator-gated.
- **Manifest-registration stub:** New external_references entries per adopted value (EXT-REF-ELLISON2016-DSFR, EXT-REF-ELLISON2011-QTY1, optional EXT-REF-GATTO2025-*).
- **Risk notes:** All adoption obeys: wording contract (no settled/causal verbs), G4 non-commensurability labels, same-change manifest registration, cycle-5-bib-only citation rule (new bibitem = declared change), integrator approval before any candidates/ or wiki write.
- **Depends on / feeds:** Depends on NVQ-01, NVQ-08; optional NVQ-11. Feeds wiki claims on /wiki/active-galactic-nuclei.

#### 41. NVQ-41 - P4-C04/C05 selection/aperture external context

- **Class/channel:** ADOPTION_ENRICH / OFFLINE_AFTER_UPSTREAM
- **Sources:** P4 P4-C04, P4-C05
- **Claim/value at stake:** Enrich selection-context (P4-C04) and aperture-geometry (P4-C05) claims with: Kewley 2005 covering-fraction result, MPA-JHU aperture-correction/AGN-treatment methodology, and a citable S/N-practice source.
- **Query/URL strategy:** NO independent fetch. Consumes upstream verification notes; drafts enrichment deltas offline; integrator-gated adoption.
- **Acceptance criterion (upgrade condition):** Delta uses only CONFIRMED items; RP-1's own numerals (1.2--6.5 kpc, 249,917, 24.0 percent, S/N>=3) remain byte-identical (manifest FLG-KPC/FLG-PARENT/FLG-COVERAGE/FLG-SNCUT untouched); external additions labeled.
- **Expected output artifact:** enrichment-deltas/NVQ-41_delta.md (proposed claim_text additions + references), integrator-gated.
- **Manifest-registration stub:** EXT-REF-KEWLEY2005-COVFRAC if the 20 percent figure is adopted; otherwise citation-only (NONE_NUMERAL).
- **Risk notes:** R07 rule: the tex's 1.2-6.5 kpc governs; no external fiber-scale figure may replace it. All adoption obeys: wording contract (no settled/causal verbs), G4 non-commensurability labels, same-change manifest registration, cycle-5-bib-only citation rule (new bibitem = declared change), integrator approval before any candidates/ or wiki write.
- **Depends on / feeds:** Depends on NVQ-15, NVQ-06, NVQ-13.

#### 42. NVQ-42 - P4-C06/C09 environment external context

- **Class/channel:** ADOPTION_ENRICH / OFFLINE_AFTER_UPSTREAM
- **Sources:** P4 P4-C06, P4-C09
- **Claim/value at stake:** Enrich environment-baseline (P4-C06) and radio-jet-environment (P4-C09) claims with verified group/filament catalog context (Yang 2007 groups; Tempel 2014 filaments) as the named missing observables (atlas Table 3).
- **Query/URL strategy:** NO independent fetch. Consumes upstream verification notes; drafts enrichment deltas offline; integrator-gated adoption.
- **Acceptance criterion (upgrade condition):** Delta names catalogs with verified access paths; internal quartile numerals (0.230/0.181/[0.041,0.059]/0.032/3.2pp; 0.509/0.367/[0.112,0.170]) stay byte-identical (SUP-ENV-*/SUP-JET-* untouched); fiber-collision caveat (55-arcsec, SUP-FCOLL) retained.
- **Expected output artifact:** enrichment-deltas/NVQ-42_delta.md (proposed claim_text additions + references), integrator-gated.
- **Manifest-registration stub:** NONE_NUMERAL expected (catalog citations); new bibitems flagged as declared changes.
- **Risk notes:** All adoption obeys: wording contract (no settled/causal verbs), G4 non-commensurability labels, same-change manifest registration, cycle-5-bib-only citation rule (new bibitem = declared change), integrator approval before any candidates/ or wiki write.
- **Depends on / feeds:** Depends on NVQ-18, NVQ-12.

#### 43. NVQ-43 - P4-C07 maintenance-heating external context

- **Class/channel:** ADOPTION_ENRICH / OFFLINE_AFTER_UPSTREAM
- **Sources:** P4 P4-C07
- **Claim/value at stake:** Enrich the maintenance-heating denominator claim with verified X-ray/radio follow-up context: eROSITA cooling samples, LOFAR/MeerKAT duty-cycle statistics, burst/duty-cycle timescale attributions.
- **Query/URL strategy:** NO independent fetch. Consumes upstream verification notes; drafts enrichment deltas offline; integrator-gated adoption.
- **Acceptance criterion (upgrade condition):** Delta keeps the claim strictly a denominator statement (no heating-balance assertion - EB axis is contradicted_or_model_dependent, F1); internal numerals (10.8/9,298/5,695/0.430/0.607, SUP-MASS*) byte-identical; external context linked + labeled.
- **Expected output artifact:** enrichment-deltas/NVQ-43_delta.md (proposed claim_text additions + references), integrator-gated.
- **Manifest-registration stub:** NONE_NUMERAL expected; any adopted balance statistic needs EXT-REF + absolute-quantity labels.
- **Risk notes:** All adoption obeys: wording contract (no settled/causal verbs), G4 non-commensurability labels, same-change manifest registration, cycle-5-bib-only citation rule (new bibitem = declared change), integrator approval before any candidates/ or wiki write.
- **Depends on / feeds:** Depends on NVQ-32, NVQ-33, NVQ-34, NVQ-16.

#### 44. NVQ-44 - P4-C08/C11 outflow/tracer-census external context

- **Class/channel:** ADOPTION_ENRICH / OFFLINE_AFTER_UPSTREAM
- **Sources:** P4 P4-C08, P4-C11
- **Claim/value at stake:** Enrich high-excitation-subset (P4-C08) and tracer-threshold-census (P4-C11) claims with: WHAN boundary attribution, multiphase-census state of the art, MaNGA IFU follow-up parameters.
- **Query/URL strategy:** NO independent fetch. Consumes upstream verification notes; drafts enrichment deltas offline; integrator-gated adoption.
- **Acceptance criterion (upgrade condition):** Delta preserves internal numerals (4,440/0.074/-11.53/-10.14; 0.136/0.418/3.1 - SUP-HIEXC-*/SUP-TRACER-* untouched); per-tracer external fractions, if any, carry all four qualifiers (tracer, selection, denominator, z-range) + non-commensurability labels (CHK-2.2 discipline).
- **Expected output artifact:** enrichment-deltas/NVQ-44_delta.md (proposed claim_text additions + references), integrator-gated.
- **Manifest-registration stub:** EXT-REF-WHAN-BOUNDARY if the boundary is quoted; others NONE_NUMERAL/per-use.
- **Risk notes:** All adoption obeys: wording contract (no settled/causal verbs), G4 non-commensurability labels, same-change manifest registration, cycle-5-bib-only citation rule (new bibitem = declared change), integrator approval before any candidates/ or wiki write.
- **Depends on / feeds:** Depends on NVQ-03, NVQ-26, NVQ-27, NVQ-21.

#### 45. NVQ-45 - P4-C12 gas-depletion external context

- **Class/channel:** ADOPTION_ENRICH / OFFLINE_AFTER_UPSTREAM
- **Sources:** P4 P4-C12
- **Claim/value at stake:** Enrich the gas-depletion denominator claim with verified CO/HI survey context (xCOLD GASS design + partial z overlap; ALFALFA coverage; 2020+ resolved-CO surveys).
- **Query/URL strategy:** NO independent fetch. Consumes upstream verification notes; drafts enrichment deltas offline; integrator-gated adoption.
- **Acceptance criterion (upgrade condition):** Delta states the z-window overlaps honestly (0.02-0.05 for xCOLD GASS class); internal numerals (6,729/0.549/40.061/0.66, SUP-GAS-*) byte-identical; no CO-to-H2 conversion performed or implied.
- **Expected output artifact:** enrichment-deltas/NVQ-45_delta.md (proposed claim_text additions + references), integrator-gated.
- **Manifest-registration stub:** NONE_NUMERAL expected; survey parameters per-use.
- **Risk notes:** All adoption obeys: wording contract (no settled/causal verbs), G4 non-commensurability labels, same-change manifest registration, cycle-5-bib-only citation rule (new bibitem = declared change), integrator approval before any candidates/ or wiki write.
- **Depends on / feeds:** Depends on NVQ-19, NVQ-20, NVQ-29, NVQ-30.

#### 46. NVQ-46 - P4-C13 simulation-vector external context

- **Class/channel:** ADOPTION_ENRICH / OFFLINE_AFTER_UPSTREAM
- **Sources:** P4 P4-C13
- **Claim/value at stake:** Enrich the simulation-target-vector claim with verified simulation-side context: Gawade medians (labeled, version-pinned), TNG/EAGLE data-product reality, forward-modeling pipeline landscape.
- **Query/URL strategy:** NO independent fetch. Consumes upstream verification notes; drafts enrichment deltas offline; integrator-gated adoption.
- **Acceptance criterion (upgrade condition):** Delta keeps the vector observation-side (15 cells/n>=50/0.005-0.729/0.003-0.520 byte-identical, SUP-CELLS/SUP-CELL-MIN/SUP-SPAN-*); simulation medians appear only with non-commensurable + unrefereed labels; selection-function-first framing preserved (claim's own rule).
- **Expected output artifact:** enrichment-deltas/NVQ-46_delta.md (proposed claim_text additions + references), integrator-gated.
- **Manifest-registration stub:** EXT-REF-GAWADE2025-TNG-MEDIAN / EXT-REF-GAWADE2025-EAGLE-MEDIAN if quoted.
- **Risk notes:** All adoption obeys: wording contract (no settled/causal verbs), G4 non-commensurability labels, same-change manifest registration, cycle-5-bib-only citation rule (new bibitem = declared change), integrator approval before any candidates/ or wiki write.
- **Depends on / feeds:** Depends on NVQ-04, NVQ-22, NVQ-35, NVQ-36, NVQ-37.

#### 47. NVQ-47 - P4-C02/C10 denominator/selection external context

- **Class/channel:** ADOPTION_ENRICH / OFFLINE_AFTER_UPSTREAM
- **Sources:** P4 P4-C02, P4-C10
- **Claim/value at stake:** Enrich the denominator-census (P4-C02) and mass-bin-diagnostic (P4-C10) claims with: citable S/N-practice source, morphological-quenching/M_BH-M_bulge sources for the selection-bias interpretation, morphology-catalog availability note.
- **Query/URL strategy:** NO independent fetch. Consumes upstream verification notes; drafts enrichment deltas offline; integrator-gated adoption.
- **Acceptance criterion (upgrade condition):** Delta keeps counts byte-identical (39,553/12,234/8,146/67; [11.0,12.5]/0.520/0.5 - FLG-SF/FLG-COMP/FLG-8146/FLG-UNCLASS/SUP-MASSBIN-*/SUP-BPT-PEAK/SUP-HALF untouched); selection-function reading stays a reading, not a settled cause (wording contract).
- **Expected output artifact:** enrichment-deltas/NVQ-47_delta.md (proposed claim_text additions + references), integrator-gated.
- **Manifest-registration stub:** NONE_NUMERAL expected.
- **Risk notes:** All adoption obeys: wording contract (no settled/causal verbs), G4 non-commensurability labels, same-change manifest registration, cycle-5-bib-only citation rule (new bibitem = declared change), integrator approval before any candidates/ or wiki write.
- **Depends on / feeds:** Depends on NVQ-13, NVQ-14, NVQ-02.

## 5. Dedup map: every P2 lead -> queue item

| Queue item | P2 leads covered | Cluster identity |
|---|---|---|
| NVQ-01 | N01, N02 | Ellison et al. 2016 (one paper) |
| NVQ-02 | N09 | Simard/Mendel catalog |
| NVQ-03 | N07 | Cid Fernandes WHAN |
| NVQ-04 | N05, N06, U18 | Gawade 2025 preprint (+usage-scope label) |
| NVQ-05 | N11 | SPIDERS overlap |
| NVQ-06 | U19, U02, U03 | MPA-JHU methodology family |
| NVQ-07 | N08 (+P1 EXT-4) | Piotrowska 2022 - CROSS-LANE COLLISION |
| NVQ-11 | N03, N04 | Gatto et al. 2025 (one paper) |
| NVQ-12 | N10 | Tempel 2014 |
| NVQ-13 | N12 | S/N practice (unattributed) |
| NVQ-14 | N13 | structural claims (unattributed) |
| NVQ-15 | U04, U11, U20 | Kewley 2005 (three label instances) |
| NVQ-16 | U05, U06, U12, U21 | duty-cycle family (Hickox14/Schawinski15) |
| NVQ-17 | U01, U17 | Schawinski 2014 (two label instances) |
| NVQ-18 | U07, U13, U22 | Yang 2007 (three label instances) |
| NVQ-19 | U08, U14, U23 | xCOLD GASS (three label instances) |
| NVQ-20 | U09, U15, U24 | ALFALFA (three label instances) |
| NVQ-21 | U10, U16, U25 | MaNGA (three label instances) |
| NVQ-22 | U26 | TNG/EAGLE access (Gawade carve-out) |

Anti-conflation warnings (same-author different-paper near-collisions): Ellison 2011 (NVQ-08) vs Ellison 2016 (NVQ-01); Schawinski 2010 (NVQ-09) vs 2014 (NVQ-17) vs 2015 (inside NVQ-16). Never merge their citations or values.

## 6. Cross-item dependency graph (adjacency)

Directed edges `upstream -> downstream (why)`; ADOPTION items (Tier G) are sinks by construction.

- NVQ-01 -> NVQ-40 (confirmed Ellison 2016 value feeds P4-C01/C03 enrichment)
- NVQ-08 -> NVQ-40 (EXT-1 value feeds same delta)
- NVQ-11 -> NVQ-40 (optional labeled Gatto context)
- NVQ-11 -> NVQ-21 (U25 Gatto-scope delimitation needs Gatto findings)
- NVQ-04 -> NVQ-22 (U26 carve-out scoped by Gawade-supported list)
- NVQ-04 -> NVQ-46 (Gawade medians (labeled) feed P4-C13 delta)
- NVQ-22 -> NVQ-36 (access claims scope the C5 data-product matrix)
- NVQ-36 -> NVQ-46 (data-product reality feeds P4-C13 delta)
- NVQ-35 -> NVQ-46 (pipeline inventory feeds P4-C13 delta)
- NVQ-37 -> NVQ-46 (selection-function docs feed P4-C13 delta)
- NVQ-02 -> NVQ-23 (morphology-catalog availability shapes C1 designs)
- NVQ-02 -> NVQ-47 (catalog availability note in P4-C02/C10 delta)
- NVQ-07 -> NVQ-23 (predictor-family anchor for C1 study sweep)
- NVQ-09 -> NVQ-23 (predictor-family anchor)
- NVQ-10 -> NVQ-23 (predictor-family anchor)
- NVQ-09 -> NVQ-14 (in-bib candidate source for N13 claims)
- NVQ-10 -> NVQ-14 (in-bib candidate source)
- NVQ-05 -> NVQ-24 (SPIDERS is a candidate X-ray power-proxy source)
- NVQ-05 -> NVQ-28 (candidate parent sample for C2)
- NVQ-05 -> NVQ-32 (eROSITA family link)
- NVQ-21 -> NVQ-28 (MaNGA is a candidate parent sample)
- NVQ-28 -> NVQ-26 (parent-sample candidates shape census-existence verdict)
- NVQ-26 -> NVQ-44 (census state of the art feeds P4-C08/C11 delta)
- NVQ-27 -> NVQ-44 (instrument realism feeds same delta)
- NVQ-21 -> NVQ-44 (MaNGA parameters feed same delta)
- NVQ-03 -> NVQ-44 (WHAN boundary feeds same delta)
- NVQ-19 -> NVQ-29 (xCOLD GASS is the baseline anchor for C3 CO sweep)
- NVQ-19 -> NVQ-45 (survey design + z-overlap feed P4-C12 delta)
- NVQ-20 -> NVQ-45 (ALFALFA coverage feeds same delta)
- NVQ-29 -> NVQ-45 (2020+ CO surveys feed same delta)
- NVQ-30 -> NVQ-45 (ALMA feasibility feeds same delta)
- NVQ-16 -> NVQ-33 (timescale attributions underpin duty-cycle statistics reading)
- NVQ-16 -> NVQ-43 (timescales feed P4-C07 delta)
- NVQ-32 -> NVQ-43 (eROSITA samples feed same delta)
- NVQ-33 -> NVQ-43 (duty-cycle statistics feed same delta)
- NVQ-34 -> NVQ-43 (cavity limits feed same delta)
- NVQ-15 -> NVQ-41 (covering fraction feeds P4-C04/C05 delta)
- NVQ-06 -> NVQ-41 (MPA-JHU methodology feeds same delta)
- NVQ-13 -> NVQ-41 (S/N practice source feeds same delta)
- NVQ-13 -> NVQ-47 (S/N practice source feeds P4-C02/C10 delta)
- NVQ-14 -> NVQ-47 (structural-claim sources feed same delta)
- NVQ-18 -> NVQ-42 (Yang groups feed P4-C06/C09 delta)
- NVQ-12 -> NVQ-42 (Tempel filaments feed same delta)
- NVQ-06 -> NVQ-15 (aperture-methodology family (read together))
- NVQ-17 -> NVQ-04 (green-valley definition context for Gawade medians)
- NVQ-24 -> NVQ-05 (survey-scale proxies contextualize SPIDERS overlap verdict)

Wave plan implied by the graph: **Wave 1** NVQ-01..07 (Tier A+B fetches); **Wave 2** NVQ-08..14 (EXT slots + linked leads); **Wave 3** NVQ-15..22 (uncited clusters); **Wave 4** NVQ-23..39 (single batched M3 sidecar run + fallback fetches); **Wave 5** NVQ-40..47 (offline adoption, integrator-gated). Waves 1-3 are independent of Wave 4 and can run in either order once approved; Wave 5 strictly last.

## 7. Standing obligations for the executing lane

1. Custody first: no adjudication on un-hashed text (baseline section 5.1); snapshot+sha256 every fetched body.
2. Poll the burn's STOP/HOLD files between items if executed inside a burn; otherwise inherit the approving brief's clock.
3. Ledger deltas are proposals: `SOURCE_LEAD_LEDGER.json` is not edited in place by the fetch lane; deltas go to the integrator.
4. Wiki/candidates writes remain out of scope for the verification pass entirely (adoption items are drafts for the integrator).
5. The five retained leads (N01, N07, N05, N09, N11) keep their INTEG retention conditions; verification can only upgrade or kill, never silently reword.

FABLE_HARD_BURN_H1_NETWORK_WORKPLAN_20260711T035354Z
