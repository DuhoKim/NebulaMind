# Referee Report on V10 and Seal Gate V3

I have reviewed `MINI_PREREG_GZ_TIERC_DRAFT_V10_20260902.md` and `seal_gate/` V3 as instructed. 

## V10 Review
1. **Minimality**: Confirmed by diffing V9 and V10. The hunks are exactly the banner (×2), §7.9, one §18 row, the §19 entry for 7.9, and the trailer. All other sections (§7.11, §16.7a/b/c, §17) are byte-identical.
2. **Truth**: Checked `miniprereg_pins/fetch_bricks_pinned.py` lines 136-153. The four verdicts (`OK`, `OK-NO-PUBLISHED-SHA`, `SHA-MISMATCH-QUARANTINED`, and `FETCH-FAILED`) and their corresponding key lengths (7 or 5 keys) are implemented exactly as stated in §7.9. `OK` requires `published_sha256` to be non-null and equal to `computed_sha256`, while `OK-NO-PUBLISHED-SHA` sets `published_sha256` to null. Running a check against the 17,948 lines of `tier_c_fetch_receipts.jsonl` confirmed 17,947 are `OK` with 7 keys and 1 is `FETCH-FAILED` with 5 keys. 
3. **Safety**: §7.9 unambiguously states that `OK-NO-PUBLISHED-SHA` does not count as `OK` for the §7.11 condition and properly cross-references the later-OK rule without duplication. The refusal conditions are strictly tightened rather than weakened.

## Seal Gate V3 Review
1. Diff against V2 confirmed changes are confined to the journal schema check, tests, and README.
2. The code enforces exactly the V10 §7.9 rules: validates the two key shapes, requires `OK` to have non-null matching checksums, properly excludes `OK-NO-PUBLISHED-SHA` from the `ok_bricks` set, and treats it as non-OK needing a later `OK` receipt. Any unknown verdict or invalid schema raises `malformed_journal_schema`.
3. Tests run perfectly (25/25).
4. A dry run against the real acquisition journal and manifest (without `--fetch` and `--append`) correctly passed the schema and completion checks, finally refusing with `published_checksum_refetch_not_requested` as expected. The receipt showed `acquisition_completion_set_condition: true` and `receipt_count: 17948`.

SEAT: AGY
VERSION: V10-SEALGATE-V3-REFEREE
V10_VERDICT: SIGNABLE
V10_MINIMALITY: PASS
SEALGATE_VERDICT: PINNABLE
DRYRUN_COMPLETION: true
DRYRUN_FAILURE: published_checksum_refetch_not_requested
COUNT: 0
