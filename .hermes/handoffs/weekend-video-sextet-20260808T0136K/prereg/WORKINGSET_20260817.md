# Brick working set built and RETAINED — 60,308 bricks; harvest is ~20 hours, not ~75

Recorded: 2026-08-17T10:31:51Z (2026-08-17T19:31:51+09:00)
Authorization: Duho's second transient position pull, this task only; does not generalise.
Stops BEFORE the checksum harvest — §11 step 4a awaits Duho's separate authorization.

## 1. The two ordering fixes, applied

1. **Digests at creation.** Each position file was hashed and row-counted the moment it was
   written, before any computation touched it (clause 4 of the position rule, satisfied in the
   order Kun's gap note required):

   | file | data rows | SHA-256 (at creation) | created UTC |
   |---|---:|---|---|
   | `positions_part_a.csv` | 95,380 | `4583bd62832c1174a2470f46624bee47b7da4915a797cb03115160794a680199` | 10:22:35Z |
   | `positions_part_b.csv` | 79,272 | `78ef1e9a82f60b7eec8bb1e43ba81ac75305f1d5d86d335c63a09d2c828c1f11` | 10:29:08Z |
   | `positions_part_c.csv` | 33,755 | `49c8a3f6da7548814e36d094b8adcbf44f845aca50c4bd110fdb2ff2a74a9a18` | 10:31:15Z |

   Row counts reproduce R1's exactly: **95,380 + 79,272 + 33,755 = 208,407** — the frozen parent
   count, no difference, no stop condition fired. Queries were the retained `q_pos_a/b/c.adql`,
   verbatim.
2. **The working set is retained** (brick identifiers — not per-object data, not covered by the
   deletion rule): `_tori_r1_workingset_evidence/workingset_bricks.csv`, 60,308 rows + header,
   SHA-256 `78ee99d6824bf4f5126b9ffd9eb622ad8201df2c64c3f232d99c1791b5f36b74`, with per-brick
   coverage class. No third position pull will ever be needed for this purpose.

## 2. Results

- **Working-set size: 60,308 distinct bricks** (primaries ∪ margin bricks over all 208,407
  parents), computed with the gated adapter's own rule
  (`output_overlap_area_in_source_pixels` > 1e-8, prefilter 0.21°, adapter `267b2a93d2a61f65…`).
- **Contributing-brick distribution, reproduced bit-for-bit from a fresh pull** (independent
  re-derivation of the R1 aggregates): 1 brick 172,983 · 2 bricks 32,320 · 3 bricks 2,939 ·
  4 bricks 165.
- **R2 classification by the exact indicator** (`nexphist_r sum > 0` ≡ `cosky_r != 0`, per
  `R1_EXACT_INDICATOR_20260817.md`): **required = 60,308; absent-by-coverage = 0.** Consistent
  with R1's zero: every working-set brick is predicted to carry `image-r`, and the harvest will
  ground-truth every one of these classifications from the survey's own `.sha256sum` listings.

## 3. Position deletion — auditable this time

All three position files were deleted immediately after the working set was written, and the
deletion record binds each filename to its **creation-time** digest
(`workingset_summary.json`, `deletion_record`): three files, three creation digests, all
`deleted: true`, verified absent post-run. Positions existed only under
`prereg/_tmp_r1_margin_20260817/` (gitignored, verified previously at `.gitignore:53`).

## 4. The number Duho asked for — harvest wall-clock

The checksum harvest is **one `.sha256sum` GET per working-set brick = 60,308 requests**, far
below the binding's ~75-hour full-survey-shaped estimate:

| pacing | continuous wall-clock |
|---|---|
| 1.2 s/request (this brief's figure) | **20.1 hours** |
| 1.0 s/request (the frozen §5.4 tier-2 value) | 16.8 hours |

Within the frozen §5.4 retrieval windows (20:00–08:00 US/Pacific weekdays + weekends), this is
**roughly two calendar days**, not weeks. Bytes: ~60,308 × ~6 KB ≈ 0.36 GB of checksum text.
(The successor binding's wall-clock statement can be revised downward at the harvest-authorization
step; the pacing values themselves are frozen and unchanged.)

## 5. Boundary receipt

- TAP queries: 3 async position partitions (same method, same custody lineage as the frozen
  counts — contiguous BRICKID 1..121000). **No HEAD requests this task. Zero image bytes, zero
  FITS, zero checksum harvest.**
- Positions: pulled under authorization, digested at creation, consumed, deleted, recorded. No
  rows, positions, or object identifiers in this deliverable or any committed artifact.
- Frozen artifacts verified unmoved before and after: successor binding `1371b11094a27652…`
  (mode 444), prereg `b06901c8a0f3a057…`, adapter `267b2a93d2a61f65…`.
- No commit, no push, no publication, no accepted status. **The harvest is NOT started.** Kun
  gates; Duho authorizes the harvest separately with the number above.
