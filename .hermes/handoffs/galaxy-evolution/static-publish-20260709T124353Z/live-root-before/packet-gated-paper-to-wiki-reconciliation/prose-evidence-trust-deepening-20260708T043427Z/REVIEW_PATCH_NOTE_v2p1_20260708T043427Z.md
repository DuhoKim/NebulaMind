# M1 deepening — versioned review / patch note (v2.1)

Order marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z
Seed marker: DEEPENING_RESOURCE_SEED_20260708T043427Z
Author: Method1 Hwao (sustaining cycles 2–5, consolidated). UTC: 2026-07-08T05:33:21Z
Type: **review/patch note only — additive, no regeneration, no finalization (floor 06:34:40Z).**

## Why a note, not a rewrite
The canonical v2 candidate files in this dir have been overwritten by concurrent M1 panes at least twice (my generated versions were superseded; the current on-disk `wiki-…deepening-…html` = 38,174 B carries `data-seed=DEEPENING_RESOURCE_SEED…` from a sustaining pane). Regenerating again would just collide. Per the order ("improve OR append a clearly versioned review/patch note rather than finalizing"), this note records apply-ready fixes for whichever pane/director owns the canonical file. All findings are grounded in the local ledger — no invented data.

## Current on-disk candidate (as reviewed)
| File | Bytes |
|------|------:|
| `wiki-prose-evidence-trust-deepening-20260708T043427Z.html` | 38,174 |
| `page-content-prose-evidence-trust-deepening-20260708T043427Z.md` | 29,560 |
| `evidence-trust-coverage-map-deepening-20260708T043427Z.json` | 4,693 |
| `manifest-deepening-20260708T043427Z.json` | 2,350 |
On-disk version is honest and static-safe (3 evidence tables, 43 arXiv links, 2929 caution present, "3 of 30"/27-unbound honesty, 0 `<script>`/fetch). The patches below are quality fixes, not honesty failures.

## Defect 1 — broken chip → evidence anchors (navigation)
The 3 claim chips link `href="#ev-2929"`, `#ev-2931`, `#ev-2946`, but the evidence panels are `id="claim-2929-evidence"` etc. There is **no `id="ev-XXXX"`** target, so clicking a highlighted claim does not scroll to its evidence box.
**Patch:** change the 3 chip hrefs to `#claim-2929-evidence` / `#claim-2931-evidence` / `#claim-2946-evidence` (or add matching `id="ev-XXXX"` to the panels). Trivial, deterministic.

## Defect 2 — malformed (broken) arXiv evidence links
Two evidence links use a doubled prefix and will not resolve:
- `https://arxiv.org/abs/arXiv:0901.1880`  → should be `https://arxiv.org/abs/0901.1880`
- `https://arxiv.org/abs/arXiv:1712.04452` → should be `https://arxiv.org/abs/1712.04452`
These come from the **ledger's real stored values** (2 malformed of 60 distinct arXiv URLs), so faithfully rendering them yields broken links. `0901.1880` is attached to claim **2929**; `1712.04452` and `0901.1880` are attached to claim **2931**.
**Patch (no invention):** strip the duplicated `arXiv:` from the `/abs/` path when building the href (the bare arXiv ID is the real datum), **or** flag these two rows `link may not resolve (stored identifier malformed)` and leave them unlinked. Either is honest; do not silently drop them.

## Improvement 3 — extend the unresolved-title caveat beyond 2929
The v2 pass added the non-committal/unresolved caution to **2929** (6 of 8 distinct papers are unresolved arXiv IDs). The same limitation exists, to a lesser degree, on the other two bound claims — worth one honest line each so the caveat isn't read as 2929-only:
- **2931 (debated):** 5 of 13 distinct papers are unresolved-title arXiv IDs.
- **2946 (reported):** 2 of 8 distinct papers are unresolved-title arXiv IDs.
**Patch:** add the "N of M distinct papers are unresolved arXiv IDs" line to the 2931 and 2946 evidence boxes (data already in the coverage map / ledger).

## Not changed / not done
- No finalization (floor 06:34:40Z). No live-root, mirror, restart, DB/API, git, cloud, browser, cron. No invented evidence/IDs/DOIs/trust. Canonical candidate files not overwritten by this note.
- 3/30 evidenced + 27 "no local evidence / unbound" honesty is intact in the on-disk version and must stay.

## Apply status
`STATUS: PATCH_RECOMMENDED_NOT_APPLIED` — deterministic, apply-ready; belongs to whichever pane finalizes the canonical HTML after the finalization floor.
