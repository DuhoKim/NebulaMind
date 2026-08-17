# R1 CLOSED at zero — every margin brick of the frozen parent set has r-band imaging on the portal

Recorded: 2026-08-17T06:18:56Z (2026-08-17T15:18:56+09:00)
Owner: Tori lane. Kun rules; Duho decides. This document reports counts; it authorizes nothing.

## Custody status — read this before the numbers

**Method: contiguous BRICKID partitions over the frozen range `1..121000`, matching
`TORI_PARENT_ROW_COUNT_20260812.md` exactly** (Duho's choice offered in the 2026-08-17 addendum;
route 1 taken deliberately). The counts below are therefore:

- **COMPLETE with respect to the frozen parent set** — the 208,407 dered-branch survivors whose
  definition IS that contiguous range; and
- **`STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND` with respect to the full
  catalogue** — BRICKID keyspace coverage 121,000/662,174 = 18.273%, the same wording and the same
  scope as the frozen counts, because they were produced the same way. Margin GEOMETRY, by contrast,
  used the full 366,912-brick real DR10 South table, so neighbour bricks outside the BRICKID range
  are fully accounted for.

A method-2 (full-table async) census was deliberately NOT used for the counts: its number would be
incommensurable with the frozen 208,407. One global count job mistakenly submitted before reading
the precedent was aborted at the UWS level (job `aopbb1f3uc5hk01f`, phase `ABORTED`, zero rows
retrieved).

## Frozen-cut reproduction — zero difference

`SELECT count(*)` under the frozen cuts, **verbatim** (`brick_primary=1 AND maskbits=0`;
`type<>'PSF' AND flux_r>0`; photo-z join on `(ls_id, release, brickid, objid)` with
`0<=z_phot_median<0.15`; `dered_mag_r<17.7`; `shape_r>1.5`; dered branch), over
`BRICKID BETWEEN 1 AND 121000`:

    n_parent = 208,407   — bit-equal to the frozen dered Cut-5 parent count. No difference to report.

The three position partitions (1..50000, 50001..100000, 100001..121000) sum to exactly 208,407
rows; 0 objects produced an empty margin set.

## STEP 1 — proxy validation: `nexp_r` errs only in the safe direction

80 paced HEAD requests (seeded stratified sample across declination; 1.2 s pacing; zero body bytes):

| stratum | sample | image-r on portal | verdict |
|---|---:|---:|---|
| `nexp_r > 0` | 40 | **40 present** | **0 dangerous disagreements** — the proxy never claims r-band that is absent |
| `nexp_r = 0` | 40 | 33 absent, **7 present** | 17.5% conservative disagreement — `nexp_r=0` over-states risk |

Direction ruling: **safe.** `nexp_r`-based counts can only OVER-count r-less exposure, never
under-count it. (Receipt: `proxy_validation.json`, `7e2669e629ac0210…`.)

## STEP 2 — margin sets by the gated adapter's own rule

Per-object margin sets were computed with the production adapter's **actual inclusion rule** —
`output_overlap_area_in_source_pixels` with threshold `1e-8` source px² and the 0.21° prefilter,
imported directly from `nm_brick_cutout_adapter.py` (`267b2a93d2a61f65…`, the seven-gate pinned
artifact) — against the real brick geometry. Not a re-derivation, not an approximation.

**Counts (frozen parent set, 208,407 objects):**

| contributing bricks | objects | proxy-flagged incomplete (`nexp_r=0`) | ground-truth incomplete (file absent) |
|---:|---:|---:|---:|
| 1 (interior) | 172,983 | 144 | **0** |
| 2 (edge) | 32,320 | 74 | **0** |
| 3 (T-junction) | 2,939 | 12 | **0** |
| 4 (corner) | 165 | 0 | **0** |
| **total** | **208,407** | **230 (0.110%)** | **0 (0.000%)** |

**Ground truth:** the 230 proxy-flagged objects implicate 138 distinct `nexp_r=0` margin bricks.
All 138 were HEAD-verified (paced, zero body bytes): **138/138 have `image-r.fits.fz` on the
portal (HTTP 200), 0 absent.** Every proxy flag was the conservative artifact validated in Step 1.

> **R1 answer: for the frozen parent set, zero objects have a margin brick lacking an r-band image
> file. The position-correlated-loss hazard R1 named does not obtain.** The `absent-by-coverage`
> class of the successor binding §11 step 4b is, for this parent set's margin working set, empty.

Incidental but load-bearing corroboration: 2,939 real three-brick T-junction objects and 165
four-brick corner objects exist in the frozen parent set — the exact geometry classes the round-5
and corner-repair gates were built for.

## What could not be determined, and residual caveats

1. **File existence ≠ photometric depth.** An `image-r` file in an `nexp_r=0` brick may be an
   edge/zero-weight coadd; some of its pixels may carry no valid data. That is handled downstream,
   per design, by the adapter's per-pixel coverage machinery (zero-coverage is terminal and
   receipted, never padded) — but the 230 objects / 138 bricks above are the population where such
   pixel-level effects would concentrate, and that number is now on the record. The mechanism by
   which `nexp_r=0` coexists with a published image file was not determined here.
2. **Scope.** These are counts for the frozen parent set (BRICKID 1..121000). Nothing here
   describes bricks or objects outside that range; any future widening of the parent set re-runs
   R1 under the same method.
3. **Proxy-artifact spatial spread (informational):** the 230 proxy flags spread across all 13
   10k-BRICKID blocks (range 2–51 per block; receipt `recount_ground_truth.json`). Since the
   ground-truth count is zero, no spatial assessment of real loss is required.

## Position handling — authorization, compliance, and one honestly recorded gap

Transient per-object positions were authorized by Duho for R1 under the four-clause deletion rule
(`_tmp_tori_R1_position_handling_rule_20260817.md`). Compliance, clause by clause:

1. **Location — satisfied.** Position files (`positions_part_a/b/c.csv`, columns ra/dec/brickid
   only, no `ls_id`) existed solely under `prereg/_tmp_r1_margin_20260817/`. Never in the
   scratchpad, TMPDIR, or any output directory.
2. **Never committed — satisfied and verified.** `.gitignore:53` (`.hermes/**/_tmp_*`) covers the
   directory; `git status` and `git log --all` show no position file ever tracked, staged, or in
   history.
3. **Deleted when the counts existed — satisfied.** All three position files and the
   implicated-brick list were deleted immediately after the aggregate counts were written.
   `bricks_geometry.csv` (public survey metadata, not per-object) remains, as the rule permits;
   its re-pull hashed byte-identical to the original (`a8c3b3af76b69832…`), anchoring continuity.
4. **Deletion recorded with evidence — PARTIAL, gap stated plainly.** The rule requires row counts
   **and** SHA-256 of each file before deletion. Row counts were captured exactly:
   `positions_part_a.csv` 95,380 · `positions_part_b.csv` 79,272 · `positions_part_c.csv` 33,755
   = **208,407** data rows, matching the frozen parent count bit-for-bit. **The SHA-256 digests
   were not captured**, because the rule reached this lane after the deletion had already been
   performed; a rule that post-dates the act it governs cannot be satisfied retroactively.
   **No attempt was made to reconstruct the digests.** A re-materialization of the 208,407
   positions was briefly started for that purpose and was stopped on Duho's instruction
   (`_tmp_tori_R1_do_not_rematerialize_20260817.md`): regenerating the data in order to hash what
   was deliberately destroyed re-creates the exact exposure the rule exists to bound, and a
   re-pull's hashes would in any case be hashes of new bytes (SQL result order is not guaranteed),
   not of the deleted files. The re-materialization's TAP job was aborted server-side
   (`rpc6li3gislasjv7`, phase `ABORTED`, zero rows retrieved), its script and copies deleted, and
   no position file was ever produced by it. What pins the extraction instead: the exact row
   counts above, the query texts verbatim (`q_pos_a/b/c.adql`, retained in the form that actually
   ran), the frozen cuts, and the pinned adapter rule — reproducibility by method, as this
   project has defined it since the aggregate-only redesign. The R1 answer itself does not rest
   on the position files: it rests on the 138/138 HEAD verifications of implicated bricks.
   **For future tasks the rule is unweakened**; the fix is ordering — capture digests at file
   creation, not at deletion.

## Deliverable boundary

No object rows, positions, identifiers, or margin-brick lists appear in this deliverable. The
authorization covers computation, not publication, and does not generalise to other tasks.

## Receipts and network accounting

- TAP queries (NOIRLab Data Lab, `ls_dr10`): schema probes ×2 (sync); bricks_s geometry pulls ×2
  (sync, 366,912 rows, both byte-identical at `a8c3b3af76b69832…`); frozen-range count ×1 (async,
  `019868cd71e2b243…`); position partitions ×3 (async); one malformed-query async job that errored
  in parse (zero rows). Two aborted async jobs, both receipted: the pre-addendum global count
  (`aopbb1f3uc5hk01f`) and the stopped re-materialization pull (`rpc6li3gislasjv7`), each phase
  `ABORTED` with zero rows retrieved. One sync count attempt timed out at the endpoint's limit
  before the method was corrected per the addendum.
- Portal HEAD requests: 80 (validation) + 138 (implicated bricks) = **218 total, all HEAD, all
  paced ≥1.2 s, zero image bytes transferred.**
- Evidence retained under `_tmp_r1_margin_20260817/`: `proxy_validation.json`
  (`7e2669e629ac0210…`), `margin_counts.json` (`0ab08a112ba8b9e0…`), `recount_ground_truth.json`
  (`9ae93d2e78334733…`), `count_frozen_range.csv` (`019868cd71e2b243…`), query texts.
- Forbidden operations at zero: image bytes fetched **0**; FITS downloaded **0**; checksum harvest
  **0** (belongs to the manifest gate); manifests built **0**; sky statistics **0**; chirality
  **0**; commit/push/publication/acceptance **0**. K-8 untripped.
- Frozen artifacts verified unmoved before and after:
  `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md` `1371b11094a27652…` (mode 444);
  `TORI_ROUTE_BINDING_20260815.md` `c7ed11c12ad7c26d…` (mode 444);
  `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` `b06901c8a0f3a057…` (mode 444);
  adapter `267b2a93d2a61f65…`.

Kun rules on whether R1's closure stands; Duho owns acceptance. The next gate step (checksum
harvest, manifest sealing) is NOT started by this document.

## Addendum 2026-08-17 — Kun's proxy hold, answered by an exact indicator

Kun held this receipt (`HOLD_PROXY_CONFIDENCE_OVERSTATED`): the HEAD pass covered only
`nexp_r=0` flags, so a dangerous false negative among `nexp_r>0` planned bricks could have made
the zero an artifact. The repair is `R1_EXACT_INDICATOR_20260817.md`: on a 388-brick adversarial
labelled sample, `nexphist_r sum > 0` (≡ `cosky_r != 0`, equivalent on all 366,912 bricks)
separates `image-r` presence with **zero disagreements in both directions**, and the table-wide
exact lemma `{hist=0} ⊆ {nexp_r=0}` entails — together with the exhaustive 138/138 implicated
HEAD pass already in this receipt — that **no planned margin brick lacks the file. The zero
stands, re-derived without positions and without relying on `nexp_r` as a presence claim.**
The residual inductive step (388 labels, not a census) and the fallback options are stated in
that document.
