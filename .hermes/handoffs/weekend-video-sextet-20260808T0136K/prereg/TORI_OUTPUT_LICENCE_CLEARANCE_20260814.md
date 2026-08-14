# Tori output-licence clearance — no-derived-catalogue redesign

Recorded: 2026-08-14

## Verdict

**CONDITIONALLY VIABLE — the published result can avoid the unresolved derived-catalogue licence dependency, but Lana's design requires two material corrections and four explicit release controls before Kun re-gates it.**

The approved direction is to publish no per-object derived catalogue and seek no permission. This receipt does not grant publication authority, amend the preregistration, or accept Lana's amendments. It determines the source-backed output boundary for the redesign lane. It is not legal advice.

The two material corrections are:

1. `k >= 50` and `<= 5,000 cells` are useful operational guardrails, **not legal safe harbors and not sufficient by themselves**. Package-wide non-reconstructability and non-substitutability must be separate mandatory conditions.
2. Running the classifier on twenty arbitrary public cutouts does **not** spot-check the unpublished labels. It checks code behavior on newly selected objects. Without a published expected per-object result, object-level spot-checking of NebulaMind's hidden output is genuinely lost except through a deterministic rebuild whose hash matches the published commitment.

With those corrections, Lana's P1-P10/S1-S5 output set is licence-clearance viable under the fail-closed rule below.

## Independent-before-Lana custody

Tori derived and sealed the publication boundary before opening Lana's content:

- independent note: `_tmp_TORI_INDEPENDENT_LICENCE_BOUNDARY_20260814.md`;
- independent-note SHA-256: `ee28b2639570cc00b21ef1e34840c7361a784c57bcaad844b44c872463d7c59c`;
- strict quote-backed citation verification: **PASS**;
- Lana content read before that seal: **NO**.

Only after that seal did Tori read:

- `LANA_OUTPUT_REDESIGN_20260814.md`;
- Lana-design SHA-256: `6ca365449d567ea423eb3842078787cb02bcd07a05c51d6a19afab43eb0f6f16`.

This sequencing prevents the legal boundary from being reverse-engineered to ratify Lana's proposed artifacts.

## 1. What the source terms do and do not cover

### Legacy Surveys

The official Legacy Surveys page says that **images** are licensed under CC BY 4.0 and may be reproduced without fee when the required credit is clear and visible. It separately says that papers using Legacy Surveys data should use the supplied scientific acknowledgment. [1]

It also warns that image layers may have different terms and that the user is responsible for complying with the terms for the relevant layer. [1]

That is not an express licence for publishing the DR10 Tractor/sweep catalogue or a per-object catalogue derived from it.

### CC BY 4.0

CC BY defines Licensed Material as the material to which the licensor applied the licence. Its grant permits reproduction and sharing of that Licensed Material and Adapted Material, but the Licensed Rights are limited to rights that apply and that the licensor has authority to license. [2]

The CC legal code therefore does not expand the Legacy page's image statement into an unmentioned catalogue licence.

### Facts, expression, and databases

The U.S. Supreme Court states that facts are not copyrightable, while original selection or arrangement in a factual compilation may receive limited protection. [11] The U.S. Copyright Office likewise distinguishes unprotected ideas, methods, systems, and discoveries from the author's original expression describing them. [4]

Those authorities support independently expressed scientific findings, methods, and measured facts. They do not authorize copying a protected selection or arrangement, and they do not answer separate database-right or contract questions.

The EU Database Directive, where applicable, treats transfer of all or a substantial part as extraction and public availability of all or a substantial part as re-utilization. It also bars repeated and systematic extraction or re-utilization of insubstantial parts when that conflicts with normal exploitation or unreasonably prejudices the maker. [3] Its lawful-user and scientific-research provisions are not a universal catalogue-publication licence. [3]

This receipt does not decide whether an EU sui-generis right attaches to this U.S.-made survey catalogue or which jurisdiction would govern a future publication. The redesign avoids that unresolved question by releasing no source-content substitute or reconstructable row product.

## 2. Exact publishable output classes

### A. Paper text and aggregate findings — YES

The paper may publish Lana's P1-P10 items, subject to the final gate:

- monopole, dipole, amplitude, attenuation, intervals, p-values, and frozen decision category;
- evaluated constants and uncertainty tables;
- fixed-axis and free-axis aggregate scan summaries;
- aggregate cut-funnel, abstention, mirror-exclusion, and final-population counts;
- nine fixed hand-check-stratum confusion aggregates and intervals;
- covariate-battery, coupling-bound, negative-control, split, and blocked-jackknife summaries;
- synthetic instrument receipts and power curves.

These are finite study-level results, not source-catalogue rows. The complete Legacy scientific acknowledgment must appear in the paper. [1]

### B. Figures — YES, by two distinct routes

1. **Original result figures:** plots generated only from release-safe aggregate statistics may be published as original study visualizations.
2. **Figures containing Legacy image pixels:** if later added, they must use the separate Legacy image route, carry the required clear and visible `Legacy Surveys / D. Lang (Perimeter Institute)` credit, identify CC BY 4.0, and indicate modification when applicable. [1][2]

Lana's present set conservatively does not rely on image pixels. An object atlas, coordinate-keyed cutout grid, or fine map enabling row recovery remains forbidden even with image credit.

### C. Code and environment — YES

Lana's S3 pipeline may be released when it contains:

- exact public product/version declarations;
- selection and query definitions;
- classifier and statistics code;
- frozen weights and seeds;
- environment lockfile;
- WCS/parity and synthetic-injection tests;
- deterministic run and verification instructions.

It must contain no credentials, cached source responses, object identifiers, coordinates, per-object labels, or embedded catalogue/result rows.

### D. Summary tables and maps — YES, conditionally

The following are acceptable only after they pass the package-wide release rule in section 3:

- S1 masked `Nside=32` maps of accepted count, abstention fraction, mean sign, and sensitivity;
- S2 one fixed 67-row partition-aggregate table;
- fixed covariate deciles, nine hand-check strata, and preregistered tertile/split summaries;
- the `Nside=16` whole-sample directional scan surface, because each value is a whole-sample statistic rather than an object-cell export.

The following remain forbidden:

- the 270,577-row brick table;
- any per-object table, identifier, coordinate, cutout URL, row hash, label, score, confidence, embedding, or source field;
- brick-by-brick, fine-pixel, or exhaustive key-range exports;
- arbitrary multidimensional cubes or user-selectable public query endpoints;
- overlapping/differenced table families that reconstruct membership or attributes;
- aggregated re-tabulations of survey magnitudes, sizes, redshifts, or other source fields.

### E. Commitments and gate documents — YES

Lana's S4 hashes and S5 preregistration/gate documents may be published:

- one SHA-256 commitment for the canonical private per-object file;
- one SHA-256 commitment for each of the 67 fixed slices;
- aggregate verification receipts;
- frozen preregistration and amendment/gate history.

The commitments expose no rows. They allow a reproducer to test byte equality after a full rebuild. They **bind** the private artifact; they do not prove its scientific correctness by themselves and are not “strictly stronger” than row inspection. Correctness still rests on the public code, fixed inputs, tests, aggregate receipts, and independent rebuild.

## 3. The mandatory aggregation/database-rights rule

A proposed public artifact is accepted by this redesign only if **all** of the following hold across the complete release, not merely within one file:

1. **Rowless:** no object key, row, coordinate, URL, source field, per-object derived quantity, or reversible row hash.
2. **Fixed and finite:** schema and cells were frozen before real-sky statistics; no post-result boundaries, dynamic query interface, or unlimited slicing.
3. **Study-result only:** cells contain this study's estimands, instrument summaries, uncertainties, or controls—not re-tabulated survey attributes.
4. **Non-reconstructable cumulatively:** no combination, overlap, differencing, version sequence, or auxiliary release can recover membership or object-level attributes.
5. **Non-substitutive cumulatively:** the package cannot function as the source catalogue, a derived catalogue, or a catalogue-scale lookup/re-analysis product.
6. **Separate image compliance:** any source image pixels follow their actual layer's licence and credit route; image compliance cannot cure a catalogue-like table.

Lana's numeric rules then apply as **additional conservative guardrails**:

- every ordinary aggregate cell has `k >= 50`, with sub-threshold cells masked under the frozen rule;
- no ordinary table/map exceeds 5,000 released cells;
- the 67 partitions, nine hand-check strata, covariate deciles, and HEALPix grid are frozen and object-independent at analysis time.

No statement should call `k >= 50`, 160x compression, or 5,000 cells a licence threshold. The Directive evaluates substantiality qualitatively as well as quantitatively and separately addresses repeated/systematic release. [3]

**The line:** aggregation stops protecting the redesign when the public package identifies/localizes an object, supports row or membership reconstruction, systematically exposes source content, or becomes a substitute catalogue—even if every cell contains at least 50 objects and every individual file has fewer than 5,000 cells.

## 4. Reproducibility without a catalogue

The public reproduction contract is viable if it contains:

1. exact public source-product names, versions, access routes, and documentation;
2. exact frozen predicates, joins, column semantics, constants, seeds, and serialization rules;
3. complete independently authored code, weights, environment, and tests;
4. hashes of every local code/configuration artifact and every public manuscript-facing aggregate output;
5. canonical private-file and 67-slice commitments;
6. deterministic instructions to rebuild from public products and compare commitments;
7. aggregate-only receipts for counts, invariants, partition coverage, and negative controls;
8. a machine-enforced release manifest and linter that rejects row-like schemas, identifiers, coordinates, URLs, per-object quantities, unapproved grids, excessive cells, and cumulative overlap/differencing hazards.

The package must not require a reader to obtain the private derived catalogue from the authors. Internal row-level working data may remain in non-public research custody, but no public data-availability statement should promise it “on reasonable request.” Reproducibility is by rebuild from the primary public products.

### What is honestly lost

- Immediate object-level reuse of NebulaMind labels: **lost**.
- Sub-degree reuse without rebuilding: **lost**.
- Cross-matching hidden labels to external catalogues: **lost**.
- Direct object-level auditing of the hand-check table: **lost**.
- Arbitrary re-cuts and re-weighting without rebuilding: **lost**.
- Cheap inspection of NebulaMind's exact per-object output: **lost**.

Aggregate re-analysis at the declared map/stratum scales survives. Full independent reproduction survives but costs approximately the public-source retrieval and compute stated by Lana; it is materially more expensive than downloading a catalogue.

### Correction to Lana's spot-check claim

A third party may fetch an arbitrary public cutout and run the released classifier in minutes. That tests classifier execution and a small amount of code behavior. It does **not** compare against NebulaMind's hidden expected label and therefore is not a spot-check of the private result file.

A verifier can check NebulaMind's exact hidden output only by rebuilding the relevant canonical slice or full file and matching its published commitment. The final design and loss table must say this plainly.

## 5. Worked precedents

### Qualifying closest precedent: Shamir 2022

Shamir's DESI Legacy spin-direction paper publicly reports aggregate hemisphere counts and binomial probabilities, direction-dependent aggregate figures, axis summaries, and methodology. Its data-availability statement says the annotated Legacy data will be provided upon reasonable request rather than attaching a public per-object Legacy catalogue. [14]

That is a worked precedent for a public Legacy handedness result without a public derived catalogue. NebulaMind adopts the aggregate-paper pattern but not the request-only catalogue: this redesign removes the private catalogue from the public reproducibility dependency.

### Non-qualifying contrasts

- Longo 2011 explicitly provides a supplementary file with spin assignments, coordinates, and magnitudes. [6]
- Galaxy Zoo's later public release lets users download classifications for nearly 900,000 galaxies. [8]
- Galaxy Zoo DESI explicitly releases two per-object morphology-catalogue versions. [9]

Those publications cannot support the claim that a public per-object catalogue is unnecessary as a matter of their own design.

### Comparable survey-policy contrast

Policies cannot be transferred between surveys:

- SDSS expressly says its public-release data are considered public domain. [5]
- DES describes public releases distributed as images, files, and catalogues. [10]
- Legacy's cited page gives an image licence and a data-use acknowledgment, but no corresponding catalogue statement. [1]

The SDSS/DES statements show why an explicit catalogue-release policy matters; they do not fill Legacy's missing catalogue scope.

## 6. Comparison with Lana's design

### Agreement

Tori agrees with Lana that:

- the scientific decision can be reported entirely through P1-P10 aggregates;
- the per-object table, hand-check rows/keys, and cutouts must remain unpublished;
- S1/S2 can preserve meaningful coarse re-analysis under hard release controls;
- S3 code plus public-input rebuild is the core replacement for catalogue download;
- S4 commitments are valuable integrity anchors after reproduction;
- community reuse is genuinely reduced and must be disclosed;
- the amendment is pre-statistic and must be re-gated before any run;
- the 270,577-row per-brick output is a catalogue-like artifact and is forbidden.

### Disagreement / required correction

Tori does not accept these claims as written:

1. **“Publishable iff” based only on Lana's five rules:** insufficient without cumulative non-reconstructability and non-substitutability.
2. **Numeric threshold as the line:** `k >= 50` and 5,000 cells are conservative engineering limits, not rights-derived thresholds.
3. **“Commitment hashes — strictly stronger”:** overclaim. A hash proves equality to committed bytes, not correctness of hidden rows.
4. **“Spot-checking individual labels: not lost”:** incorrect without published expected labels. It is lost except through canonical rebuild-and-hash comparison.

### Exact required changes before Kun re-gates

1. Amend Lana section 2/F-10(b) to add the six package-wide conditions in section 3 of this receipt and label the numeric limits “additional conservative guardrails, not legal safe harbors.”
2. Amend S1/S2 to state that cumulative overlaps, differencing releases, subsequent finer versions, and public slice/query APIs are prohibited.
3. Replace “strictly stronger than table inspection” with “cryptographically binds the hidden artifact and permits byte-equality testing after rebuild; it does not establish correctness by itself.”
4. Change the section 4 spot-check row to **Lost/partial**: arbitrary small-n reruns test code behavior; exact hidden-label verification requires slice/full rebuild plus commitment match.
5. Add the release-manifest/linter gate described in section 4, run over the complete package rather than individual files.
6. Add an explicit data-availability statement: no per-object NebulaMind catalogue is public or available on request; reproducibility is from cited public products, frozen code, and aggregate/commitment receipts.

With these changes, Tori's assessment is **VIABLE FOR KUN RE-GATE**. Without them, Lana's legal threshold and reproducibility claims are overstated, so the design is not ready to freeze.

## 7. Pins and boundary

- Controlling Tori brief SHA-256: `399650774dce3c8f286b6e9118bd018c7c4166df23b02c7fd7c829bd57841275`.
- Prior BS-1 receipt SHA-256: `34aad1f17804b235a26f07aa25bbd85d2614d0611b428d1ec31faad375d2684e`.
- Independent pre-comparison note SHA-256: `ee28b2639570cc00b21ef1e34840c7361a784c57bcaad844b44c872463d7c59c`.
- Lana redesign SHA-256: `6ca365449d567ea423eb3842078787cb02bcd07a05c51d6a19afab43eb0f6f16`.
- Legacy source copy SHA-256: `4905bae9b6b6f61f494360ea9f06e760effbe1de48a614217d4a9d7501f28fea`.
- CC BY source copy SHA-256: `d4e38b78e507a4177f31c6aa67a181fe7a11aa5a8e90c9b2058321caaab2ce07`.
- EU Directive source copy SHA-256: `31b1c9506fc0e4eef869d0477a64199d9b223f834dd029e57038b9438a19c529`.
- SDSS policy source copy SHA-256: `9dbcdbf799ebe850dfb1557d06be5cf08d9ca8c95eebda20a25c6dff31782642`.
- Feist source copy SHA-256: `d98a307653f2dbd9ac932b4ff7730ef3f8174c1789c1a7d5f388a67239fba5a7`.
- Shamir 2022 paper source copy SHA-256: `479f3a138d7365021d59e1d733ef05a78a2297df1cb3735c39858f49600cc8cf`.

Work performed: documentation, source retrieval, citation binding, and design comparison only. New survey rows, positions, images, chirality labels, sky statistics, database writes, publication, acceptance, cockpit update, commit, push, merge: **ZERO/NONE**.

Duho owns acceptance. Kun must re-gate any exact preregistration amendment before freeze or execution.

## Sources

[1] https://www.legacysurvey.org/acknowledgment — Legacy Surveys acknowledgments and image licence
[2] https://creativecommons.org/licenses/by/4.0/legalcode.en — CC BY 4.0 legal code
[3] https://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:31996L0009:en:HTML — Directive 96/9/EC on legal protection of databases
[4] https://www.copyright.gov/circs/circ33.pdf — US Copyright Office Circular 33
[5] https://www.sdss.org/collaboration/image-use-policy — SDSS image use and public data policy
[6] https://arxiv.org/pdf/1104.2815v1 — Longo 2011 handedness paper v1
[8] https://data.galaxyzoo.org — Galaxy Zoo data releases
[9] https://zenodo.org/records/8331338 — Galaxy Zoo DESI morphology catalogue release
[10] https://des.ncsa.illinois.edu/terms — Dark Energy Survey terms of use
[11] https://tile.loc.gov/storage-services/service/ll/usrep/usrep499/usrep499340/usrep499340.pdf — Feist Publications v Rural Telephone, 499 US 340
[14] https://arxiv.org/pdf/2208.13866 — Shamir 2022 DESI Legacy spin-directions paper
