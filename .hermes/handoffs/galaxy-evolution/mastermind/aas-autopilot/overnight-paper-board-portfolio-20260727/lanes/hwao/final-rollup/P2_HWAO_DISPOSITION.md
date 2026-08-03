# P2 Hwao Disposition — fesc Lineage, Bibliography Identity, Citation-Gap Census

Adjudicator: Hwao / Fable, final-rollup lane. Written 2026-07-27 ~22:47 KST (13:47 UTC). Stop files checked before writing: absent.

## Disposition

**Lineage relationship: `UNRESOLVED`. Goru's `CANONICAL_PLUS_SUPPORTING` recommendation is REJECTED.** Citation-gap census confirmed mechanically real. No artifact revision tonight.

## Receipts relied upon

| Receipt | Lane / role | Marker | Verdict |
|---|---|---|---|
| `input/P2/goru/RECEIPT.json` + 6 artifacts (`GORU_MECHANICAL_VERDICT.md`, `BIBLIOGRAPHY_IDENTITY.csv`, `CITATION_GATE_REPLAY.json`, `CLAIM_STATUS_LEDGER.jsonl`, `LINEAGE_MATRIX.json`, `PASSAGE_SUPPORT_LEDGER.csv`) | Goru, primary | `P2_GORU_PRIMARY_COMPLETE_20260727` | Citation gaps mechanically real; recommended `CANONICAL_PLUS_SUPPORTING` |
| `input/P2/kun/RECEIPT.json`, `CROSSREVIEW.md`, `VALIDATION.json` | Kun, citation-entailment cross-review | `P2_KUN_CROSSREVIEW_COMPLETE_20260727` | `ISSUES` — zero-denominator gap preserved; Chisholm identity patch, Flury role narrowing, lineage downgrade to `UNRESOLVED` |
| `input/P2/lana/RECEIPT.json`, `CROSSREVIEW.md`, `VALIDATION.json` | Lana, overclaim/status cross-review | `P2_LANA_CROSSREVIEW_COMPLETE_20260727` | `ISSUES` — Kun's three corrections confirmed; Tori's Simmonds split adopted; four new findings |
| `input/TORI_BROWSER_SOURCE_CHECK.md` | Tori, independent source-identity check | `TORI_INDEPENDENT_SOURCE_IDENTITY_CHECK_20260727` | `P2_GORU_PRIMARY_REQUIRES_PATCHES` — ADS-verified identities; Goru's Chisholm bibcode 404s on ADS |
| `input/VALIDATION_T1.json` | Tori validator | — | All five P2 public artifacts 200 with exact SHA-256 identity match; structural counts confirm `lit_refs`=6, `lit_reflist`=5, passages enumerated=0, citation gate checked=0, both Simmonds bibcodes in novelty gate |

No self-review occurred. Goru's primary is reviewed by Kun, Lana, and Tori; Goru reviewed no P2 primary content of its own beyond authoring it.

## 1. Citation-entailment denominator: ZERO — preserved

`fesc002`'s `gates.citation_entailment.checked = 0`, `n_unsupported = 0`, `unsupported = []`, `all = []`; log line "gate/citations: 0 unsupported of 0 checked" is **vacuous**. "Lit-grounded on 6 papers, 5 passages" is a grounding *claim*: zero passages are enumerated anywhere in the packet (Lana finding 8.4; T1 `lit_passages_count: 0`). Positive passage-level entailment evidence in this packet is exactly zero. No phrasing implying a citation pass may be derived from this run. Preserved by all five independent looks.

## 2. Chisholm / Flury / Simmonds identities — adjudicated

| Shorthand | Adjudicated correct identity | Status |
|---|---|---|
| Chisholm+22 | **`2022MNRAS.517.5104C`**, MNRAS 517, 5104, DOI `10.1093/mnras/stac2874` (far-UV continuum slope LyC escape estimator) | Goru's `2022MNRAS.515.4265C` "VERIFIED" is **false** — that ADS path 404s (Tori) and the frontier PDF itself prints 517, 5104. Patch required to Goru's identity table before any reuse. |
| Flury+22 | For the printed frontier citation and the O32/β diagnostic-calibration role: **`2022ApJ...930..126F`** (LzLCS II, ApJ 930, 126, DOI `10.3847/1538-4357/ac61e4`). LzLCS I (`2022ApJS..260....1F`, DOI `10.3847/1538-4365/ac5331`) is real but is the survey paper, not the cited entry. | Role patch required — Goru verified a related paper, not the exact cited one. |
| Simmonds+24 | **Split status (Tori's adjudication, adopted by Lana and here):** frontier identity **RESOLVED** to `2024MNRAS.527.6139S` (MNRAS 527, 6139, DOI `10.1093/mnras/stad3605`, printed in the frontier bibliography); pipeline identity **QUARANTINED** — `fesc002`'s bare "Simmonds+24" is cross-wired because its novelty gate lists both `2024MNRAS.527.6139S` and `2024MNRAS.535.2998S` (DOI `10.1093/mnras/stae2537`) and the run supplies no bibcode/DOI. | Open item preserved as *unverified attribution, not error*: whether log ξ_ion = 25.5 ± 0.15 actually appears in `527.6139S` rather than `535.2998S` cannot be closed from packet evidence. |

## 3. Frontier bibliography vs pipeline shorthand — kept distinct

These are different defect classes and this disposition forbids merging them:

- **Frontier PDF (clean):** prints identity-complete references for all three calibration sources (517, 5104; 930, 126; 527, 6139). Its residual defect class is at most the unverified ξ_ion passage attribution above.
- **Pipeline `fesc002` (cross-wired):** cites `[Chisholm+22, Flury+22; Simmonds+24]` in prose; omits all three from its printed 5-entry reference list and its 6-bibcode `lit_refs`; carries Lewis20 (`2020MNRAS.496.4342L`) in `lit_refs` but not the rendered reflist; only machine trace of "Simmonds" is the two-paper novelty-gate ambiguity. Goru's census (9 distinct cited sources / 5 reflist entries / 6 inline anchors / 4 missing / 3 unresolved roles) re-verified correct by Lana and consistent with T1 structural counts.

## 4. Lineage: `CANONICAL_PLUS_SUPPORTING` rejected → `UNRESOLVED`

The brief's standard: reject unless **direct derivation lineage is proven**. It is not. Evidence *for* continuity is real and preserved as narrative — human-history direction ("One z~6 result → a 232-point systematic landscape"), matching fiducials (frontier z=6 value 0.048 = fesc002 median f_required; inferred ≈6% = 0.062), identical MD14/ξ_ion/C/LzLCS inputs. But the packet contains **no code provenance, commit lineage, run-derivation chain, or artifact-build receipt**, and the frontier history JSON never names `fesc002`. Shared method plus matching numbers is equally consistent with an independent re-run. Kun's downgrade, upheld by Lana and Tori, is adopted.

As integration owner for this roll-up, I explicitly **decline** to accept the human-history narrative as sufficient lineage evidence tonight. Annotation of record: *"likely supporting precursor; strong topical and numerical continuity; derivation chain mechanically unproven."* Promotion requires a derivation receipt or an explicit acceptance by Duho at a later gate.

## 5. "Public data (jwst)" vs no-catalog provenance contradiction — preserved, not normalized

The pipeline PDF abstract states "Generated autonomously from public data (jwst)" while the same run's provenance field states NO survey catalog data is used (and forbids implying JWST/SDSS/TNG data use) and the body says it relies on published literature values. Origin: `spec.data_sources = ["jwst"]` leaks into the served abstract. Adjudication (per Lana/Tori, endorsed): **the abstract sentence is the defect; the provenance field is the truth.** The `DO_NOT_USE` ledger row must survive every downstream summary. Repair is out of scope tonight; it belongs on the morning repair list. Noted coverage gap: Kun's otherwise thorough cross-review omitted this item (caught by Lana) — no impact on the verdict.

## 6. Additional preserved findings (Lana §8, endorsed)

1. **Novelty-gate premise contradiction:** `fesc002`'s NOVEL verdict was granted on a "using JWST data" premise the run's own provenance forbids; novelty against the true estimand (literature-anchored systematics reconciliation) was never adjudicated. `gate/novelty: NOVEL` must not be cited as clean evidence.
2. **Wording hazard:** `LINEAGE_MATRIX.json`'s "landscape mapping where the shortfall is real" is locational; out of context it asserts the opposite of the frontier's conclusion. Any reuse must rephrase to "mapping where (in parameter space) a shortfall would be real."
3. **Review-trajectory understatement:** the frontier's record is **MAJOR → ACCEPT** by an advisory automated referee (astrosage-70b), not "ACCEPT in 1 cycle"; carry the full trajectory.
4. **"5 passages" is a claim count, not verified passages** (see §1).

## Disagreement resolution

One genuine disagreement existed: Goru (`CANONICAL_PLUS_SUPPORTING`) vs Kun/Lana/Tori (`UNRESOLVED`/patches). Resolved **against** Goru per the brief's direct-derivation standard — three independent reviewers converge and the primary's own packet lacks derivation evidence. Goru's mechanical citation-gap census itself survives fully; the identity-table errors (Chisholm bibcode, Flury row) are patch obligations recorded here, not applied to Goru's immutable files.

## Remaining unsupported / blocked / partial / disputed rows

- QUARANTINED: pipeline Simmonds+24 identity.
- PATCH_REQUIRED (recorded, unapplied): Goru's Chisholm bibcode row; Goru's Flury main row (role narrowing).
- UNRESOLVED: fesc002↔frontier lineage; ξ_ion passage attribution between the two Simmonds papers.
- DEFECT (standing, public-facing): "public data (jwst)" abstract sentence; pipeline reflist/lit_refs omissions incl. Lewis20 mismatch; novelty-gate premise.
- DO_NOT_USE (must survive all roll-ups): any claim the study uses JWST/SDSS/TNG observational or catalog data.

Automated reviews and this adjudication are not human validation or peer review. No artifact, public route, or project state was modified by this disposition.
