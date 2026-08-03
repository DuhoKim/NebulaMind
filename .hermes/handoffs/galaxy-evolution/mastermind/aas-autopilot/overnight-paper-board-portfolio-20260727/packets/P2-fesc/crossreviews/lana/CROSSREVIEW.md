# P2 Lana Cross-Review — Overclaim and Research-Status Adjudication

Marker: `P2_LANA_CROSSREVIEW_COMPLETE_20260727`

Reviewer: Lana (P2 overclaim/status cross-reviewer). Reviewed Goru's completed primary, Kun's independent cross-review, and Tori's source-identity check without editing any of them. All work confined to `packets/P2-fesc/crossreviews/lana/`.

## Disposition

`ISSUES`

Goru's mechanical citation-gap finding is correct and must be preserved. Kun's three corrections (Chisholm identity patch, Flury role narrowing, lineage downgrade) are all **CONFIRMED** from the immutable packet. Tori's frontier-versus-pipeline Simmonds split is the correct adjudication and refines Kun's blanket treatment. Goru's `CANONICAL_PLUS_SUPPORTING` recommendation is an overclaim from captured evidence and must become `UNRESOLVED`. In addition, this review surfaces four items no prior lane flagged (§8).

## 1. Inputs audited

- Read `input/BRIEF.md` and every file listed in `input/INPUT_MANIFEST.json` (26 manifest entries + the manifest itself).
- Independently recomputed SHA-256 and byte counts for all 27 files: **0 mismatches** (matches Kun's audit).
- Stop-file check at the overnight root: no `GLOBAL_STOP_OVERNIGHT_PB_20260727.md` or `CONTENT_FREEZE_OVERNIGHT_PB_20260727.md` present at start or before receipt.
- PDFs were read via Tori's text extractions (`P2_FRONTIER_PDF_TEXT.txt`, `P2_PIPELINE_PDF_TEXT.txt`), whose parent PDFs are hash-pinned in the manifest and match `PUBLIC_ARTIFACT_IDENTITY.json` byte-for-byte (frontier: 160,454 B / `3a2f84ed…`; pipeline: 86,033 B / `bf044999…`). No external fetches were required; no login/CAPTCHA/payment/OAuth/secret prompt was encountered.

## 2. Claim-status adjudication

Per the brief, each load-bearing claim is placed into exactly one bucket. Goru's `CLAIM_STATUS_LEDGER.jsonl` is directionally sound; refinements are marked ▲.

**Established assumptions (adopted, literature-anchored inputs)**
- Madau & Dickinson (2014) analytic SFRD fit.
- log ξion = 25.5 ± 0.15, adopted from Simmonds et al. 2024 (frontier bibliography prints MNRAS 527, 6139).
- Clumping factor C ∈ [2, 5]; κ_UV = 1.15 × 10⁻²⁸; case-B maintenance criterion at T = 2 × 10⁴ K (Robertson et al. 2015).
- ▲ Nuance Goru's ledger flattens: ξion and the SFRD normalization are *established as adopted values* but simultaneously the frontier manuscript's own **dominant debated levers** — its central thesis is that the crisis verdict "is, to first order, a disagreement in those two priors." Any roll-up that reads `established_assumption` as "settled physics" for ξion overclaims. Status should read: established-as-adopted, debated-in-normalization.

**Model outputs (conditional on the assumptions; not measurements)**
- fesc002: f_required = 0.048 (+0.048/−0.025) at z = 6; median Δ(required−inferred) = −0.012; 41% MC shortfall fraction; "budget CLOSES within the systematic."
- Frontier: the 232-point grid; crisis-onset redshift spanning z ≈ 5.0–8.75; fesc = 1 crossing at z ≈ 8.5 (crisis corner) to never (optimistic corner); fiducial closure to z ≈ 6.5 and unphysicality by z ≈ 10.75.

**Proxy-inferred quantities (measured proxies, indirect)**
- f_inferred = 0.062 (+0.108/−0.039) from LzLCS O32/β calibrations (Chisholm et al. 2022; Flury et al. 2022), median ≈ 6% with 0.4–0.45 dex scatter, held redshift-independent when transported to z > 6.

**Debated inputs**
- Photon-budget sufficiency vs crisis itself (Muñoz+24/Davies+21 vs Duncan+15/Madau17).
- ξion normalization; JWST high-z SFRD normalization (frontier caveats call it "itself contested"); transportability of low-z proxy calibrations to z > 6.

**Unknowns**
- Direct f_esc at z ≳ 6: the IGM is opaque to Lyman-continuum photons; the frontier caveats state "no direct z > 6 Lyman-continuum detection is used." Goru's `unknown` status is correct.
- The true fesc(z) evolution (a genuinely rising fesc(z) would move the crisis onset beyond every corner in the grid).

**DO_NOT_USE**
- Any statement that the study uses JWST, SDSS, or TNG observational/catalog data. The provenance field forbids it explicitly. Goru's `DO_NOT_USE` row is correct and must survive every roll-up.

## 3. Maintenance-criterion vs integrated-history scope

Preserved correctly by all lanes and re-verified here: the frontier PDF states in both Discussion and Caveats that the maintenance criterion "assumes ionization equilibrium rather than integrating the full reionization history," which sets the normalization of the required emissivity. The pipeline note is a single z = 6 equilibrium calculation and carries no integrated-history claim. No artifact claims an integrated reionization history; any downstream description that says otherwise would be an overclaim. Scope boundary: **intact**.

## 4. Indirect proxy vs direct fesc

Preserved correctly: both manuscripts state all escape fractions are inferred from indirect, low-redshift-calibrated proxies. The frontier's non-circularity check (O32-only vs β-only swap) tests calibration-choice sensitivity, not directness — it does not upgrade the proxy to a measurement, and no lane claimed it does. Boundary: **intact**.

## 5. "Public data (jwst)" vs no-catalog provenance contradiction

**Confirmed as a live, reader-facing contradiction — must be preserved, not normalized.**

- Pipeline PDF abstract (served bytes, via pinned extraction): "Generated autonomously from public data (jwst) via the NebulaMind Lab runner."
- Same run's provenance field: "NO survey catalog data is used… Do NOT state or imply that this study uses JWST, SDSS, or TNG observational/catalog data."
- Same manuscript's body: "relies on existing data and published results rather than new observations or surveys."
- `spec.data_sources` = `["jwst"]` in both the live and local run JSONs, so the contradiction originates in the run spec and leaks into the served abstract.

Tori flagged this; Goru's `DO_NOT_USE` ledger row captures the truth side but the primary verdict does not name the abstract sentence as a standing defect; **Kun's cross-review does not mention it at all** — a coverage gap in Kun's otherwise thorough review. Adjudication: the abstract sentence is the defect; the provenance field is the truth. Repairing it is out of scope tonight (no-mutation boundary); it belongs on the morning repair list.

## 6. Exact Chisholm / Flury / Simmonds identities

| Shorthand | Adjudicated identity | Goru | Kun | Lana verdict |
|---|---|---|---|---|
| Chisholm+22 | `2022MNRAS.517.5104C`, MNRAS 517, 5104, DOI `10.1093/mnras/stac2874` (far-UV slope LyC estimator) | `2022MNRAS.515.4265C` marked VERIFIED — **false**; Tori found that ADS path 404s | Patch to 517.5104C | **CONFIRMED — patch required.** The frontier PDF itself prints "Chisholm, J., et al. 2022, MNRAS, 517, 5104"; Goru's bibcode contradicts the very artifact under review. |
| Flury+22 | Frontier prints ApJ 930, 126 = LzLCS **II** (diagnostics), `2022ApJ...930..126F`, DOI `10.3847/1538-4357/ac61e4`; ApJS 260, 1 = LzLCS **I** (survey), DOI `10.3847/1538-4365/ac5331` | Verified Part I as the main row, Part II in a note | Role narrowing to Part II | **CONFIRMED — role patch required.** For the O32/β diagnostic-calibration role and the exact printed citation, Part II is the match; Part I alone is insufficient. Goru's row verified a real but non-cited-entry paper. |
| Simmonds+24 | Frontier prints MNRAS 527, 6139 = `2024MNRAS.527.6139S`, DOI `10.1093/mnras/stad3605` ("Low-mass bursty galaxies in JADES…") | Blanket QUARANTINED | Quarantine confirmed, "under-specified" | **Split status (Tori's adjudication adopted):** frontier identity **RESOLVED** to `2024MNRAS.527.6139S`; pipeline identity **QUARANTINED** — `fesc002`'s bare "Simmonds+24" is genuinely cross-wired because its novelty gate contains both `2024MNRAS.527.6139S` and `2024MNRAS.535.2998S` and the run supplies no bibcode/DOI. |

▲ Open passage-level item no lane can close from this packet: whether log ξion = 25.5 ± 0.15 actually appears in `2024MNRAS.527.6139S` (as opposed to the mass-complete `2024MNRAS.535.2998S`, whose title targets the photon-budget crisis directly) is **unverifiable from packet evidence** — no passage was captured. Record as unverified attribution, not as an error.

## 7. Frontier citation vs pipeline cross-wire

These are distinct defect classes and must not be merged in the roll-up:

- **Frontier citation (clean):** the frontier PDF prints identity-complete references for all three calibration sources (517, 5104; 930, 126; 527, 6139). Its defect class is at most the unverified-passage item above.
- **Pipeline cross-wire (real):** `fesc002` cites `[Chisholm+22, Flury+22; Simmonds+24]` in prose, omits all three from its printed 5-entry reference list and its 6-bibcode `lit_refs`, carries Lewis20 in `lit_refs` but not in the rendered reflist, and its only machine trace of "Simmonds" is the two-paper novelty-gate ambiguity. Goru's counts (9 distinct cited sources, 5 reflist entries, 6 inline anchors, 4 missing, 3 unresolved roles) re-verified correct against the pinned artifacts.

## 8. Findings not raised by any prior lane

1. **Novelty-gate premise contradiction (overclaim vector).** The NOVEL verdict for `fesc002` was granted on the explicit premise of "using JWST data to measure reionization-photon-budget" — the gate's reason text says no prior paper "report[s] the exact measurement proposed using JWST data." The run's own provenance disavows JWST data use. The novelty verdict therefore rests partly on a data-usage premise the run itself forbids stating; novelty against the true estimand (a literature-anchored systematics reconciliation) was never adjudicated. Downstream consumers must not cite `gate/novelty: NOVEL` as clean evidence.
2. **"Shortfall is real" wording hazard in `LINEAGE_MATRIX.json`.** Goru's frontier `claimed_result` copies the history phrase "232-point systematic landscape mapping where the shortfall is real." In the source history JSON, "where" is locational (mapping *where in parameter space* the shortfall is real). Out of context it reads as the assertion "the shortfall is real" — the *opposite* of the frontier's actual conclusion ("the apparent 'photon-budget crisis' is not a robust observational result"). Any roll-up quoting Goru's matrix must rephrase, e.g. "mapping where (in parameter space) a shortfall would be real."
3. **Frontier review-state understatement.** `LINEAGE_MATRIX.json` records "ACCEPT in 1 cycle." The pinned `frontier-review.md` shows the initial verdict was **MAJOR**, revised once to ACCEPT, by an advisory automated referee (astrosage-70b) explicitly "not validated by a human scientist or journal referee." "ACCEPT in 1 cycle" without the MAJOR is status-inflating; carry the full trajectory.
4. **"5 passages" is a claim, not evidence.** `PASSAGE_SUPPORT_LEDGER.csv` row `exact_support_passages,5` transcribes the run-log string "lit-grounded on 6 papers, 5 passages." Zero passages are enumerated anywhere in the packet, and the citation gate checked 0 claims. The ledger row must be read as a count of the *claim*, not of verified passages. Positive passage-level support in this packet is exactly zero.

## 9. Lineage adjudication

**`CANONICAL_PLUS_SUPPORTING` does not survive. Adjudicated relationship: `UNRESOLVED`.**

Evidence *for* continuity (all real): the frontier history JSON records human direction "One z~6 result -> a 232-point systematic landscape" and "Synthesize the grid into one review-ready paper"; the frontier's fiducial z = 6 value (0.048) equals fesc002's median f_required (0.04789…) to quoted precision; proxy-inferred ≈ 6% matches 0.062; both use identical MD14/ξion/C/LzLCS inputs.

Why it still fails the brief's standard: the brief requires lineage be treated as unproven absent **direct derivation evidence**. The packet contains no code provenance, commit lineage, run-derivation chain, or artifact-build receipt connecting the frontier manuscript to `fesc002`'s outputs — and the history JSON never names `fesc002`. Shared method plus matching numbers is equally consistent with an independent re-run of the same calculation. That is strong *supporting-precursor* narrative, not proven *canonical* lineage.

Kun's downgrade to `UNRESOLVED` is **upheld**, with the narrative annotation: "likely supporting precursor; strong topical and numerical continuity; derivation chain mechanically unproven." Promotion back to `CANONICAL_PLUS_SUPPORTING` requires either a derivation receipt or an integration owner explicitly accepting the human-history narrative as sufficient — a decision for Hwao/Duho, not a reviewer lane.

## 10. Citation-gate truth (zero-claim) — preserved

Re-verified from both pinned run JSONs: `gates.citation_entailment.checked = 0`, `n_unsupported = 0`, `unsupported = []`, `all = []`; log line "gate/citations: 0 unsupported of 0 checked." "0 unsupported" is vacuous — the denominator is zero. All four lanes (Goru, Kun, Tori, this review) preserve this truth; it must not be softened into any phrasing that implies a citation pass.

## 11. Lane-by-lane summary

- **Goru primary:** core mechanical findings correct (zero-claim gate, missing-reference census, Simmonds pipeline cross-wire). Requires patches: Chisholm bibcode false-VERIFIED, Flury row cites the wrong LzLCS part for the printed reference, relationship overclaimed, plus wording hazards §8.2–8.3. Not a clean pass; not invalidated.
- **Kun cross-review:** all three corrections confirmed; hash audit reproduced. One coverage gap: the "public data (jwst)" abstract contradiction is absent from Kun's review.
- **Tori source-identity check:** fully consistent with packet evidence; the frontier-resolved/pipeline-quarantined Simmonds split and the preserve-the-contradiction instruction are adopted here as the correct adjudications.

## 12. Scope and mutation statement

- All writes confined to `packets/P2-fesc/crossreviews/lana/` (this file, `VALIDATION.json`, `RECEIPT.json`).
- No paper, public artifact, project source, Lab record, DB, wiki, service, cockpit, or Git mutation. Immutable inputs untouched (hash-verified before and used read-only).
- No external network access was needed; identity conclusions rest on the pinned artifacts plus prior lanes' attested public checks.
- Pre-existing repository dirtiness outside this packet was treated as context only.

Marker: `P2_LANA_CROSSREVIEW_COMPLETE_20260727`
