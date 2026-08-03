# P2 Kun Cross-Review

Marker: `P2_KUN_CROSSREVIEW_COMPLETE_20260727`

## Disposition

`ISSUES`

Goru's primary finding should be preserved: `fesc002` is labelled literature-grounded on 6 papers / 5 passages, but the captured citation-entailment gate checked 0 claims. That is zero positive passage-level entailment evidence, not a citation pass. The proxy-calibration sources named in the pipeline prose are not covered by `lit_refs` or by the citation gate.

I do not endorse Goru's `CANONICAL_PLUS_SUPPORTING` recommendation as proven from the immutable packet. The packet supports topical and human-directed continuity between `fesc002` and the frontier manuscript, but not a mechanically proven derivation chain. The relationship should be downgraded to `UNRESOLVED` unless an integration owner accepts the human-history narrative as sufficient lineage evidence.

## Inputs Audited

- Read `input/BRIEF.md` and every file listed in `input/INPUT_MANIFEST.json`.
- Recomputed byte counts and SHA-256 hashes for all 21 immutable inputs: no mismatches.
- Parsed all primary JSON, JSONL, and CSV outputs:
  - `BIBLIOGRAPHY_IDENTITY.csv`: 3 data rows.
  - `PASSAGE_SUPPORT_LEDGER.csv`: 7 data rows.
  - `CLAIM_STATUS_LEDGER.jsonl`: 7 JSON objects.
  - `CITATION_GATE_REPLAY.json`, `LINEAGE_MATRIX.json`, and `RECEIPT.json`: syntactically valid JSON with expected top-level keys.

## Confirmed Findings

1. Citation-gate denominator is exactly zero.
   - `input/source/pipeline-live.json` records `gates.citation_entailment.checked = 0`, `n_unsupported = 0`, `unsupported = []`, `all = []`.
   - The same run log records `lit-grounded on 6 papers, 5 passages` and later `gate/citations: 0 unsupported of 0 checked`.
   - Therefore the correct replay summary is 0 checked, 0 pass, 0 partial, 0 fail, 0 unsupported. Any statement implying passage-level citation validation is unsupported.

2. Bibliography presence and entailment are distinct.
   - `lit_refs` contains 6 bibcodes.
   - `lit_reflist` contains 5 rendered references and omits Lewis 2020 (`2020MNRAS.496.4342L`).
   - The pipeline PDF bibliography contains only 5 entries and omits Chisholm+22, Flury+22, Simmonds+24, and Lewis20.
   - The frontier PDF bibliography does include Chisholm+22, Flury+22, and Simmonds+24, but that does not validate the pipeline run's zero-claim citation gate.

3. Goru correctly quarantined Simmonds+24 as ambiguous for the pipeline context.
   - The pipeline novelty gate contains two distinct Simmonds 2024 JADES papers: `2024MNRAS.535.2998S` and `2024MNRAS.527.6139S`.
   - The frontier PDF bibliography cites Simmonds 2024 as MNRAS 527, 6139, while the pipeline provenance only says `Simmonds+24`.
   - Topic proximity is not identity; without a concrete bibcode/DOI in `fesc002`, this remains cross-wired or under-specified.

4. The claim-status separation is mostly sound.
   - The ledger properly separates established assumptions, debated inputs, measured proxies, unknown direct high-z escape fraction, and the `DO_NOT_USE` claim about JWST/SDSS/TNG catalog data.
   - The frontier PDF itself states that the maintenance criterion assumes ionization equilibrium rather than integrating the full reionization history, and that all escape fractions are inferred from indirect, low-redshift-calibrated proxies.

## Corrections To Goru

1. Chisholm+22 bibcode is wrong in Goru's `BIBLIOGRAPHY_IDENTITY.csv`.
   - Goru records `2022MNRAS.515.4265C`.
   - The frontier PDF bibliography cites Chisholm et al. 2022 as MNRAS 517, 5104.
   - Public identity checks confirm the far-UV continuum slope LyC escape estimator as Chisholm et al. 2022, MNRAS 517, 5104-5120, DOI `10.1093/mnras/stac2874`, ADS bibcode `2022MNRAS.517.5104C`.
   - This should be patched before any roll-up treats Goru's identity table as verified.

2. Flury+22 needs role-specific narrowing.
   - Goru marks `2022ApJS..260....1F` as verified and notes ApJ Part II.
   - The frontier PDF bibliography cites Flury et al. 2022 as ApJ 930, 126.
   - Public identity checks confirm ApJS 260, 1 is LzLCS I, while ApJ 930, 126 is LzLCS II: New Insights into LyC Diagnostics, DOI `10.3847/1538-4357/ac61e4`, ADS bibcode `2022ApJ...930..126F`.
   - For O32 / LyC diagnostics, the Part II paper is the more direct role match. The Part I survey paper is real but not sufficient by itself for the diagnostic-calibration role.

3. The `CANONICAL_PLUS_SUPPORTING` relationship is an overclaim from captured evidence.
   - `frontier-history.json` records human direction from one z~6 result to a 232-point systematic landscape and synthesis.
   - The frontier PDF describes a 232-point landscape over redshift and systematic corners; the pipeline PDF is a single z~6 calculation.
   - Those facts support continuity and reuse of method, but the packet does not contain code provenance, commit lineage, exact notebook/run derivation, or a deterministic artifact build chain proving that the frontier manuscript derives from `fesc002`.
   - The conservative relationship is `UNRESOLVED`, with narrative note: "likely supporting precursor, not mechanically proven canonical lineage."

## External Identity Checks

- Chisholm et al. 2022: public publisher / institutional metadata identifies "The far-ultraviolet continuum slope as a Lyman Continuum escape estimator at high redshift", MNRAS 517, 5104-5120, DOI `10.1093/mnras/stac2874`, ADS bibcode `2022MNRAS.517.5104C`.
- Flury et al. 2022 LzLCS I: public metadata identifies "The Low-redshift Lyman Continuum Survey. I. New, Diverse Local Lyman Continuum Emitters", ApJS 260, article 1, DOI `10.3847/1538-4365/ac5331`.
- Flury et al. 2022 LzLCS II: public metadata identifies "The Low-redshift Lyman Continuum Survey. II. New Insights into LyC Diagnostics", ApJ 930, article 126, DOI `10.3847/1538-4357/ac61e4`, ADS bibcode `2022ApJ...930..126F`.
- Simmonds et al. 2024 has two plausible JADES identities in the packet. The frontier bibliography selects MNRAS 527, 6139, DOI `10.1093/mnras/stad3605`; the novelty gate also lists MNRAS 535, 2998, DOI `10.1093/mnras/stae2537`. The pipeline's bare `Simmonds+24` is therefore under-specified.

## Scope And Mutation Check

- No manuscripts, public artifacts, Lab records, DB/wiki/service/cockpit state, or Git state were intentionally modified.
- Work was limited to this cross-review directory.
- Existing repository status is dirty outside this packet; I treated it as pre-existing context and did not change those files.
- No stop file was found under the packet tree during start/mid-run checks.

