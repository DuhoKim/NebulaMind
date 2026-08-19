# tools/attic — retired, kept for the record (2026-08-20 overhaul)

- render_ge_autopilot_dashboard.py — the V1 dashboard renderer. RETIRED because
  it wrote to the SAME output path as v2: running it by accident silently
  replaced the live dashboard with a smaller, events-blind page.
- tmux_board_snapshot.py / tmux_board_summary.py — superseded by
  nm_paper_run_dashboard.crew_live().
- nm_septet_cockpit_feed.py — superseded by build_septet_matrix() in v2.
