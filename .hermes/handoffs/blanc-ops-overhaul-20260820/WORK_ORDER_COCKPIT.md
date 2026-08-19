# Work order — cockpits (from P0 survey, 01:3x KST)

Executor: Blanc (single-writer surface; not delegating renderer surgery).
gpt/codex exec seat gets the contained audio-page builds instead.

## C1. Persona rename, user-visible layer (v2 + nm_paper_run_dashboard.py)
Seats → engine names per 08-19 reform; coordinators keep Hwao/Tori/Blanc.
Seat map: Lana→claude-seat, Goru→agy, Kun→kimi, Tori(seat)→gpt2, Yui→gpt1.
MUST rename nm_paper_run_dashboard.py SEATS/SEAT_MATCH in the same pass (matrix
string-matches staffed names). Also the dormant fallback cards (:1090, :1092,
:1861), freshness-limit keys, :2505 JS ordering array, flowbox strings
(:2407-2408, :2437), roles dict (:411-414), ROLE_ORDER, lane_usage_counts.
Events feed roles (tori-bhu, hwao-director) are COORDINATOR names — keep.

## C2. Honesty layer
- Renderer heartbeat in header: "rendered Xm ago" (renderer alive) separate
  from "sources Xh old" (data age). Header pill, not buried provenance.
- Survey Autopilot panel (source 17d stale) + run-estimates panel: reuse the
  usage-card freshness machinery — grey + "STALE since <date>" instead of
  posing as live.
- Headline health driven by the freshest signal (events feed, appended minutes
  ago) not the stalest (autopilot-status.json, 33h).

## C3. Performance + payload hygiene
- read_events(): tail-read the 22 MB events log (seek from end), not read_text().
- Drop corpus_scaleup + overnight_report from the payload (built, serialized,
  never displayed).
- seated=None bug in build_septet_matrix (:277 area).

## C4. Navigation + housekeeping
- ge-autopilot.html gets a links row: spin-parity, bhu-lane2, index, listen page.
- index.html: point live-steering/mobile/baseline links at the FRESH copies
  (agent-reports) not the 07-05 orphans; fix the false "renderer is a .bak"
  comment; delete the four cockpit-root orphan copies.
- Archive the v1 renderer footgun (render_ge_autopilot_dashboard.py writes the
  SAME output path as v2) + dead tools (tmux_board_*, nm_septet_cockpit_feed)
  into tools/attic/ with a note. KEEP pipeline-board/run-page (dormant, wired).
- Sweep ~450 *.backup-* files from cockpit root into cockpit/_attic/ (move, not
  delete).

## C5. Scheduling (prepare, do NOT install)
Nothing schedules rendering — pages freeze when my session sleeps. Prepare
com.nebulamind.cockpit-render.plist (10-min full render pass) + install
one-liner; hand to Duho in the morning (persistence installs need his word;
the MacBook listener precedent was explicitly authorized, this one is not yet).
Tonight my cron ticks keep it fresh.

## Out of scope tonight
Full mobile page for ge-autopilot (v2 responsive CSS is adequate); design-token
unification across the four CSS families (flag only); stable-cockpit template
redesign.
