# COMPLETENESS GATE — FULL RUN RECEIPT (PASS), 2026-09-03 21:27 KST

Receipt: completeness_gate/artifacts_full/completeness_receipt_20260903T122712Z.json
  sha256 bd4433064a5d830194bdefff9f910efed8e9adda561d92c0a00f94bb45fbc3a2
Pair list: completeness_gate/artifacts_full/tier_c_pairs_20260903T122712Z.csv (12,217 rows + header)
  sha256 0e21269a0512ebdc255aa1286afe889bf17b7b9c8bb69f6bef8e6085e35c9a82  (receipt field tier_c_pair_file_sha256 matches)
Checkpoint sha256 da812d6e2934dbda57f90f3132994b165cc46522a58c02c02a97a2922ac0315f (8,933/8,933 admitted); chunk manifest b40e58ea…36f77.
Backend: NOIRLab Astro Data Lab sync TAP q3c, ls_dr10.tractor_s, complete-all-candidates, QUERY_STATUS=OK on every chunk (MAXREC=10000, no cap hit); 688,924 client rows.
Software: completeness_gate.py d403c8cc… (COMPLETENESS_GATE_PIN_INDEXED), tap_source.py 74e82503… (COMPLETENESS_GATE_PIN_ONCE); wall 110 s on the pinned once-verified path.

Funnel (893,212 unique valid GZ1 rows, each considered exactly once):
  below_threshold 446,845 | no_dr10 307,540 | multiple_dr10 101,500 | collision 44 | one_dr10 459,106
  tier_a 16,600 | tier_b 8,466 | tier_c_eligible 12,217  (6,437 ANTICLOCKWISE, 5,780 CLOCKWISE)
  sum of terminal dispositions = 893,212 ✓
Prior unresolved 13,725: all terminal, all unique — NO-DR10 8,935 / ONE-DR10 4,658 / MULTIPLE-DR10 132.

History: full TAP run 09-02 16:51Z → 09-03 10:01Z (8,933 chunks, 1→2 workers at 08:48Z per Duho's override); finalisation stalled twice on quadratic loops (exclusion scan; per-chunk checkpoint re-verification), both fixed, refereed PINNABLE, pinned; stops announced in switchover_2w.log. Validation only (ruling "a"): nothing here feeds the flagship.
