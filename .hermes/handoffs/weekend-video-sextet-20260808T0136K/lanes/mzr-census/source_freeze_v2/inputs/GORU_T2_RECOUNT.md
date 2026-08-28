# GORU T2 Recount

**1. Quoted spans in §3, §3b and §4**
- The contract claims 49 quoted spans across §3, §3b, and §4 (T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md).
- Extracted and counted: D1 (3), D2 (3), D3 (2), D4 (3), D5 (3), D6 (3), D7 (3), D8 (3), D9 (3), D10 (4), D11 (3), D12 (4), P1 (3), P2 (3), P3 table (2), P3 text (4). Total = 49.
- Result: PASS

**2. Control counts (Decoys and Anchors)**
- Decoy tables in §3 and §3b contain 3 and 9 rows respectively (12 total decoys).
- Anchor table in §4 contains 3 rows.
- Sentences in §5 and §6 referring to counts (12 decoys, 3 anchors, 15 controls, 157 candidates, 142 other candidates) all correctly reflect these numbers (T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md).
- Result: PASS

**3. Manifest counts**
- The contract claims 157 candidates, 178 pre-filter, and 21 dropped.
- In `T1_MZR_MANIFEST.json`, `"n_candidates_pre_filter": 178` and `"n_candidates": 157` are explicitly present.
- The `dropped_candidates` array contains exactly 21 items.
- Arithmetic: 157 + 21 = 178.
- Result: PASS

**4. Gas-phase count**
- The contract claims 62 for the gas-phase evidence count.
- Re-derived by running the specified regex pattern (`12\s*\+\s*log|log\(?O/H|oxygen abundance|gas.?phase|nebular|emission.?line`) across the concatenated description fields of the three axes for all 157 candidates in `T1_MZR_MANIFEST.json`.
- The script reproduced exactly 62 matches.
- Result: PASS

**5. descriptions_clipped counts**
- The contract claims 24 entries, spanning 13 distinct tables, with zero overlap with the 15 control tables.
- In `T1_MZR_MANIFEST.json`, `descriptions_clipped` contains exactly 24 entries.
- These belong to 13 distinct `table_id`s.
- None of the 13 distinct tables are in the set of 15 control tables (D1–D12, P1–P3).
- Result: PASS

**6. Other self-referential numbers**
- **Status and Error Counts**: The contract claims `status DONE`, `0 channels failed`, `7/7 members returned`, `0/3 controls appeared` (Lines 14-15, 19). Reconciled with `T1_MZR_MANIFEST.json`, which reports `"status": "DONE"`, `"channels_failed": []`, 7 members returned `true`, and 3 controls appeared `false`.
- **Three substantive elisions**: The contract claims "Three elisions were substantive rather than boilerplate and are quoted in full" (Line 73) and itemizes them: D3's `vGR1`, P1's `A(O)`, and D6's `logZ`. This explicitly names exactly 3 instances.
- **Eight P3 ...fmol columns**: The contract claims "the `…fmol` glob denotes eight columns" (Line 119) and lists 6 survey-prefixed and 2 consolidated (8 total). The manifest candidate for P3 contains exactly 8 primary mass columns containing `fmol` (`ACABeamfmol`, `ACAGlobfmol`, `APEXBeamfmol`, `APEXGlobfmol`, `CARMABeamfmol`, `CARMAGlobfmol`, `FinalBeamfmol`, `FinalGlobfmol`), perfectly matching the claim.
- Result: PASS

GORU_RECOUNT_COMPLETE
