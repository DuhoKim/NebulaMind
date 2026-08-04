# PATCH LOG — Kun red-team patches applied (Lana)

- Lane: `agn-step6-map-pilot-20260803T1330Z` · applied 2026-08-03T13:27Z (22:27 KST)
- Source of patches: `KUN_MAP_REDTEAM.md` (verdict PASS_WITH_PATCHES) via `LANA_PATCH_BRIEF.md`.
- Ledger remained read-only ground truth; every edit re-verified against
  `docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/claim_status_ledger.jsonl` before writing.

| # | Patch | Files touched | Diff summary |
|---|-------|---------------|--------------|
| 1 | Fix R5 trace citations for 009/010; restate 008 provenance as ledger-only | `CONDENSATION_REPORT.md`, `AGN_STATUS_DEBATE_MAP_V1.md` | R5 Applied line + trace rows now cite the real legs (009/010 place via `qualifies`→2299_003; their `same_axis` links point at each other, not the seed — re-verified in ledger); 008's basis stated as ledger-only `qualifies`→2299_003 with the stance-matrix row demoted to corroboration, in both the report trace and map §7.1. |
| 2 | Scope the determinism claim: R1/R2/R3/R5/R6 mechanical; R4 argued per-case | `CONDENSATION_REPORT.md` | Merge-rule header rewritten to say plainly that R4's distinct-question test is semantic, argued per-case, and reviewable; section title de-claims "applied deterministically"; the K-section "re-running yields the same partition" line qualified to match. |
| 3 | Hoist `verification_status = pending` disclosure into the map header | `AGN_STATUS_DEBATE_MAP_V1.md` | New header bullet: all 16 entries are `pending`, every status label (incl. `widely_supported`) binds to pending-verification entries; closing footnote kept. |
| 4 | Finding 5(b): re-check ≥100 km/s against 002b spans `_02`/`_03` | `AGN_STATUS_DEBATE_MAP_V1.md` | Re-read both spans in the ledger: `span_2024MNRAS_528_4976D_03` carries "Half of the absorption profiles are blueshifted by at least 100 km s−1" VERBATIM → per the brief's branch, footnoted the span (no strike needed); footnote `[^kms]` added under Axis B with the verbatim quote. |
| 5 | Finding 4 nit: Axis A summary-table Status cell | `AGN_STATUS_DEBATE_MAP_V1.md` | A's Status cell now reads "per-side (see axis) — …", so table parsers see the explicit per-side marker instead of a bare two-value cell. |
| 6 | Finding 6 nit: R1 wording on Axis E seeding | `CONDENSATION_REPORT.md` | R1 now states only `clc_agn_011` seeds E; `clc_agn_004` joins E by R6, not by seeding — matching the trace table. |

Constraints honored: no content beyond the ledger introduced (patch 4's footnote quotes the ledger
span verbatim); writes confined to this lane directory; both artifacts updated in place.

LANA_AGN_STEP6_PATCHED_20260803
