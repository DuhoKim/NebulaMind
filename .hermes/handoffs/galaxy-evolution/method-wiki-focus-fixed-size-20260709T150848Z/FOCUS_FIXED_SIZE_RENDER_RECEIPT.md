# Static method selector focus fixed-size receipt

- marker: `NEBULAMIND_METHOD_WIKI_FOCUS_FIXED_SIZE_20260709T150848Z`
- updated_utc: `2026-07-09T15:09:13.935579+00:00`
- result: current method card remains focused, but the focus state is layout-neutral and does not add the `CURRENT METHOD` badge or change card height.
- selector width now matches the default dynamic wiki column (`max-width:56rem`).
- safety: DB/page_versions/live product wiki publish/backend restart/trust recompute/deploy/git all 0.

## Outputs
- `packet-gated-paper-to-wiki-reconciliation`: width_fixed=True, current_anchor=True, badge_absent=True, tabs=True, header=True
- `source-first-paper-adjudication`: width_fixed=True, current_anchor=True, badge_absent=True, tabs=True, header=True
- `debate-map-to-wiki-rebuild`: width_fixed=True, current_anchor=True, badge_absent=True, tabs=True, header=True

Working backups: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method-wiki-focus-fixed-size-20260709T150848Z/working-backup-before-focus-fixed-size`
