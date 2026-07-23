# Paper backups — pre/post Quartet rewrites

Durable snapshot of the four papers the Quartet rewrote on 2026-07-23, captured
**outside** the `.hermes/handoffs` scratch tree so it survives a scratch cleanup.
Each paper folder holds the manuscript **before** and **after** the rewrite, plus
its figures — every `after.tex` / `before.tex` is standalone-compilable with
`tectonic` against the figures in the same folder.

`before.pdf` = the exact PDF that was live before the rewrite.
`after.pdf`  = the current live-deployed PDF (fetched from the live-deploy public dir).
Verify integrity with: `shasum -a 256 -c SHA256SUMS.txt`

| Folder | Paper | What changed |
|---|---|---|
| p1_z9-10-metallicity-deficit | #1 z≈9–10 unlensed metallicity deficit | Abstract + intro reframed to lead with the enrichment-vs-metal-poor debate; +4 citations. No number/claim changed. |
| p4_tng-massive-galaxy-abundance | #4 TNG massive-galaxy abundance | Itemized 0.46–0.55 dex budget (+10 cites), TNG aperture pinned (+0.13 dex → shift 0.20 dex), ε≈0.20 ΛCDM benchmark, z7–9 demoted. |
| p3_scaling-relations-withdrawn | #3 scaling relations z0→JWST | Main claim WITHDRAWN (z<6 SFMS elevation = selection artifact); folded toward #6/#1. |
| p6_tng-calibration-validation | #6 TNG calibration ≠ validation | Strengthened: sim-vs-obs gap reframed as a conservative lower bound; +0.13 dex mass-basis fix. |

## Rollback (per paper)
To restore a paper to its pre-rewrite state:
1. Recompile `before.tex` in its folder (`tectonic before.tex`) — or use the saved `before.pdf` directly.
2. Copy the resulting PDF over the live-deploy asset (overwrites serve immediately):
   - #1 → `.../public/studies/z9-10-unlensed-metallicity-deficit.pdf`
   - #4 → `.../public/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf`
   - #3 → `.../public/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf`
   - #6 → `.../public/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf`
3. Revert the board card + history.json entry if the rollback should also un-record the directive.

Note: #3 and #6 originals were never overwritten in the scratch tree; #1 and #4
source `.tex` were updated in place but the pre-rewrite versions are the `before.tex` here.

_Generated 2026-07-23 14:16 UTC._
