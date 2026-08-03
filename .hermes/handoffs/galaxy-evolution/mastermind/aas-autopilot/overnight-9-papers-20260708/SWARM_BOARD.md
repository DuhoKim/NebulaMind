# Overnight 9-paper swarm board

Marker: `OVERNIGHT_9_PAPERS_SWARM_BOARD_20260708T134000Z`

The first setup was too narrow: one Tori/Hermes worker plus a morning rollup. The corrected overnight setup uses separated durable lanes. Each lane writes only under its own lane directory unless explicitly instructed by the integrator.

## Active lane roles

- Hwao/Fable director lane: coordination, task slicing, paper-by-paper priority, omitted-topic map.
- Lana manuscript lane: deep paper-writing critique and AASTeX improvement drafts.
- Goru data lane: mechanical robustness, counts, SDSS-derived tables/figures, manifest checks.
- Kun reproducibility lane: compile/reproducibility, exact commands, hash/manifest verification.
- Literature/source lane: public arXiv/Semantic Scholar/source grounding and bibliography gaps.
- Tori integration lane: original hourly generalist/receipt worker plus morning rollup.

## Visible tmux board

Durable cron/background lanes are real but are not visible as panes. A visible tmux window has therefore been created for the user's pane board:

`ge-mastermind:overnight-9-papers`

Panes:

- `Hwao-director-visible`
- `Lana-manuscript-visible`
- `Goru-data-visible`
- `Kun-repro-visible`
- `Literature-source-visible`
- `External-CLI-visible`
- `Tori-integration-visible`

These panes run lane-local loops until 2026-07-09 08:05 KST and write reports under `visible-panes/<lane>/reports/`. They do not replace the durable cron workers; they make the active swarm visible.

## Single-writer rule

To avoid cron races, lanes do not all edit the same manuscript files. Each lane writes lane-local artifacts:

- `lanes/hwao/`
- `lanes/lana/`
- `lanes/goru/`
- `lanes/kun/`
- `lanes/literature/`

The morning rollup or a later user-approved integration pass may merge the best lane outputs into revised manuscripts/PDFs. If a lane creates direct manuscript revisions, it must put them under `revision-drafts/<lane>/`, not overwrite current public-linked PDFs.

## Safety

No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/extra-cron-from-cron/billing/OAuth/external submission. Current live/public pages stay untouched overnight.
