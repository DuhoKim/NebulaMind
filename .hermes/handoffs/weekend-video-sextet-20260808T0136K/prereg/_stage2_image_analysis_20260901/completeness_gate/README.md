# Catalogue-only completeness gate

This draft implements the pre-signature catalogue gates allowed by
`MINI_PREREG_GZ_TIERC_DRAFT_V9_20260902.md` §1.5. The live backend is
deliberately a refusing stub; Hwao must approve the data-source plan and a
separately reviewed artifact-backed implementation before any live catalogue
run.

## Clause map

| Preregistration clause | Implementation |
|---|---|
| §§3.1--3.4 | Strict sexagesimal GZ1 parsing, printed declination sign, binary64 DR10 coordinates, finite/range checks, duplicate-GZ1 refusal |
| §§3.5--3.7 | Binary64 great-circle distance, inclusive 1.0 arcsec, `CandidateSource` contract requires all candidates |
| §§3.8--3.12 | Zero/one/multiple dispositions, duplicate identity refusal, shared-DR10 collision exclusion, coordinate exclusions completed before labels |
| §§4.1--4.6 | Inclusive positional priority A, then protected-parent B, then C; excluded objects never become pairs |
| §§4.7--4.12 | Inclusive 0.8 labels, below-threshold exclusion, contradictory-label refusal, no magnitude/vote-count cut |
| §§4.13--4.14 | Unique four-part pair identity and integer canonical sort |
| §§5.1--5.3 | Backend provenance refuses magnitude predicates, truncation, or anything short of complete all-candidate enumeration |
| §§5.4--5.7 | Receipt binds inputs/source/artifacts/software/radius, row-once coverage, funnel counts, candidate proof, and every prior-unresolved terminal disposition; gaps refuse |

`InMemoryCandidateSource` exists only for deterministic fixtures.
`AstroDataLabCandidateSource` performs no network operation and always refuses.
The approved production adapter must consume already-downloaded, hashed complete
query artifacts (or equivalently proven local Tractor partitions) and expose
their provenance through the same interface.

Run the tests from this directory:

```sh
python3 -m unittest -v test_completeness_gate.py
```

## Explicit non-actions

This tool does not open image pixels, FITS coadds, or `bricks_tier_c/`. It does
not render cutouts, invoke the image instrument, form image labels, or execute
the live catalogue query. The module writes only when `write_outputs()` is
explicitly called, and that function writes only `tier_c_pairs.csv` and
`completeness_receipt.json` beneath its caller-supplied output directory. It
does not modify acquisition state, journals, pins, seals, preregistrations,
referee reports, Git state, or any file outside that output directory.

## Test log (2026-09-03 KST)

Command: `python3 -m unittest -v test_completeness_gate.py`

```text
test_backend_duplicate_candidate_refused (test_completeness_gate.MatchTests) ... ok
test_equality_at_one_arcsecond_is_inclusive (test_completeness_gate.MatchTests) ... ok
test_gz_collision_excludes_all_owners (test_completeness_gate.MatchTests) ... ok
test_ra_wrap_great_circle (test_completeness_gate.MatchTests) ... ok
test_zero_one_two_candidates (test_completeness_gate.MatchTests) ... ok
test_csv_duplicate_is_checked_by_gate (test_completeness_gate.ParserTests) ... ok
test_declination_sign_applies_to_whole_quantity (test_completeness_gate.ParserTests) ... ok
test_official_gzip_csv_is_parsed (test_completeness_gate.ParserTests) ... ok
test_parser_requires_printed_dec_sign (test_completeness_gate.ParserTests) ... ok
test_ra_wrap_and_invalid_24_hours (test_completeness_gate.ParserTests) ... ok
test_missing_prior_unresolved_position_refused_exactly (test_completeness_gate.ReceiptTests) ... ok
test_required_receipt_fields_present (test_completeness_gate.ReceiptTests) ... ok
test_row_once_gap_refused_exactly (test_completeness_gate.ReceiptTests) ... ok
test_canonical_pair_sort_uses_integer_keys (test_completeness_gate.TierAndLabelTests) ... ok
test_contradictory_labels_refused_exactly (test_completeness_gate.TierAndLabelTests) ... ok
test_equality_at_point_eight_is_inclusive (test_completeness_gate.TierAndLabelTests) ... ok
test_tier_priority_a_then_b_then_c (test_completeness_gate.TierAndLabelTests) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.013s

OK
```
