PASS_POSITIONS_EXPORT

# KUN POSITIONS GATE — 2026-08-20

Gate seat: kimi, fresh one-shot. Scope: `_positions_20260820/` position-provisioning export.
Method: local files + python3 recompute. ONE network call: re-polled the recorded
`datalab.noirlab.edu` TAP job `/phase` endpoints only. `portal.nersc.gov` never touched.
Findings-only. No DB writes, no deploy, no publish, no git.

## Check 1 — BS-6 ADQL predicates byte-for-byte (frozen hash verified first)

`LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` SHA-256 recomputed:
`5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361` — matches required `5ff7f454…`.

Each frozen BS-6 / frozen-chain predicate appears byte-for-byte (in the receipt's qualified
`t.`/`p.` spelling) in ALL THREE export ADQL blocks (Q4/Q5/Q6) and in the focused count (Q3):

  t.brick_primary = 1            OK in all
  t.maskbits = 0                 OK in all
  t.type <> 'PSF'                OK in all
  t.flux_r > 0                   OK in all
  p.z_phot_median >= 0           OK in all
  p.z_phot_median < 0.15         OK in all
  t.dered_mag_r < 17.7           OK in all   (BS-6 magnitude constant)
  t.shape_r > 1.5                OK in all   (BS-6 size constant)

Cut-6 inclination predicate `POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551`
is present in the full Cut-6 aggregate (Q1) and correctly ABSENT from the study-parent
exports — the study parent is the frozen Cut-5 dered level (208,407), not the Cut-6
inclination parent (832,393). No SB cut exists (BS-6 §3a documented absence) — consistent.
No predicate was harmonised or restated with a changed value. PASS.

## Check 2 — export row/ls_id/brickname counts + SHA-256 (independent recompute)

Recomputed from `positions_parent_20260820.csv` with python3:

  data rows           208,407   (expect 208,407)   OK
  distinct ls_id      208,407   (expect 208,407)   OK
  distinct brickname   58,009   (expect  58,009)   OK
  blank/malformed rows      0
  SHA-256  90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9
           (expect 90fa6c96…)                        OK — byte-identical, matches sidecar

File line count 208,408 = 208,407 data + 1 header. PASS.

## Check 3 — subset: every exported brickname ∈ workingset_bricks.csv

`workingset_bricks.csv` SHA-256 recomputed
`78ee99d6824bf4f5126b9ffd9eb622ad8201df2c64c3f232d99c1791b5f36b74` — matches receipt.

  working-set distinct bricknames                    60,308
  exported distinct bricknames                       58,009
  exported bricknames MISSING from working set            0   (expect 0)  OK
  exported_brickname_set ⊆ workingset_bricks.csv       TRUE
  working-set bricknames not primary in export        2,299   (allowed margin-only remainder)

Independently recomputed by set difference, not trusting export_verification.json. PASS.

## Check 4 — chain counts vs frozen sources (frozen hashes verified, counts quoted side-by-side)

Frozen source hashes recomputed — all match receipt §1:
  TORI_BS1_CLOSURE_PACKET.md          50bf06b0…01b8f5  OK
  TORI_PARENT_ROW_COUNT_20260812.md   df935708…534f3   OK
  R1 fixed-range reconstruction       31e1c4a4…24ab    OK
  full-keyspace reconstruction        beb89247…7154    OK

### Full-keyspace chain — receipt vs TORI_BS1_CLOSURE_PACKET.md §3 (verbatim)

  Stage                              Receipt        Frozen §3      Verdict
  Cut 1 primary + mask          2,584,542,900   2,584,542,900    MATCH
  Cut 2 extended + flux         1,317,374,704   1,317,374,704    MATCH
  photo-z join after Cut 2      1,317,374,704   1,317,374,704    MATCH
  Cut 3 photo-z window             11,762,815      11,762,815    MATCH
  Cut 4 dered magnitude             1,162,237       1,162,237    MATCH
  Cut 5 dered parent                1,015,881       1,015,881    MATCH
  Cut 6 dered inclination parent      832,393         832,393    MATCH

### R1 study-parent chain (BRICKID 1..121000) — receipt vs R1 evidence
(re-summed from the 13 landed partitions AND matching the JSON's own totals block)

  Stage                              Receipt        R1 frozen      Verdict
  Cut 1 primary + mask            674,896,997     674,896,997    MATCH
  Cut 2 extended + flux           338,508,894     338,508,894    MATCH
  photo-z join after Cut 2        338,508,894     338,508,894    MATCH
  Cut 3 photo-z window              2,618,678       2,618,678    MATCH
  Cut 4 dered magnitude               238,922         238,922    MATCH
  Cut 5 dered study parent            208,407         208,407    MATCH

The fresh focused async count (Q3, result.csv) independently returned 208407. The export
row count equals the frozen Cut-5 dered study-parent count exactly. PASS.

## Check 5 — columns and ra/dec sanity

Header is exactly `ls_id,ra,dec,brickname` — no other column exported.
  ra  range [0.0003501236, 359.9985511712]   all in [0,360)    0 invalid
  dec range [-89.5928315515, -39.3750943441] all in [-90,90]  0 invalid
  dec > 35: 0 rows. Entirely southern (max dec ≈ -39.4°) — sane for DR10 South.
PASS.

## Network verification (permitted, datalab.noirlab.edu only)

Re-polled the 4 recorded successful job `/phase` endpoints (HTTP 200):
  Q3  npohnmsr1kxwiurr   COMPLETED
  Q4  l0jbiuupt7d5beqk   COMPLETED
  Q5  i0oorac153iw9yft   COMPLETED
  Q6  lxkp3nilg4ps6u6a   COMPLETED
All four jobs existed and reached COMPLETED. (`/resulturl` returns 404 — results expired
post-retrieval, normal TAP behaviour; phase persistence confirms completion.) Local run
dirs each hold job.xml + receipt.json + poll_log.jsonl; partition SHA-256s and row counts
(95,380 + 79,272 + 33,755 = 208,407) verified locally. export_verification.json self-hash
matches receipt (8d254c33…24c). nersc never contacted.

## Verdict

All five checks PASS. The export is internally consistent, byte-faithful to the frozen
BS-6 predicates, count-consistent with the frozen R1 study-parent chain, a verified subset
of the working set, hash-pinned, and the underlying TAP jobs are confirmed COMPLETED at
datalab.noirlab.edu. PASS_POSITIONS_EXPORT.
