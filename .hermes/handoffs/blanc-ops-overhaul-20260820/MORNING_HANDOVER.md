# Morning handover — overnight OPS overhaul (Blanc)

Campaign: Duho's order 2026-08-20 ~01:25 KST — "overhaul nebulamind website,
cockpits, and audio report systems overnight leveraging all our resources."
Status at drafting (02:5x KST): **all three surfaces overhauled, reviewed,
deployed.** Everything is committed on feat/paper-workflow-v2 and pushed.

## Website — LIVE on nebulamind.net (deployed c9d41444, ~02:15 KST)

- **New landing page** (built by the agy seat, integrated + fixed by Blanc):
  honest AI-scientist hero, the four Lab stages as entry points, latest
  flagship outputs ("descriptive draft under review" labels), video below the
  fold. Shared --lab-* tokens via labTheme.ts (was declared twice, drifting).
- **Contribute page** was light-styled on the dark chrome — literally an
  invisible title. Now dark.
- **IA**: Lab first in nav+footer (direct /lab — the old link 308'd through
  lab.nebulamind.net); wiki demoted to "Wiki (legacy)"; 404s point at the Lab;
  /april-fools and a stray 187 KB artifact deleted.
- **SEO**: the root canonical had marked EVERY page a duplicate of the
  homepage; /lab was absent from the sitemap while /explore (a bare redirect)
  sat at 0.9. Both fixed; metadata no longer claims an encyclopedia.
- **Perf**: Inter self-hosted via next/font (was a render-blocking Google
  Fonts link); nav stats poll 30s → 120s.
- **Deploys now deploy**: deploy_frontend.sh built the DEV checkout while
  cloudflared served the live worktree — a deploy pipeline that deployed
  nothing. It now targets the live worktree, takes a ref, prints its rollback
  (`scripts/deploy_frontend.sh afeaa91e` restores last night's site), and
  smokes / + /lab + /surveys.
- **Caught by smoke, not by build**: the new homepage crashed SSR (server
  component importing from a "use client" module — tsc and next build both
  pass on that bug). Data extracted to lab/flagshipData.ts; / renders 200.

## Cockpits (tailnet)

- **Naming reform finished on the boards**: sextet matrix and seat cards now
  say claude-seat / agy / kimi / gpt1 / gpt2; staffing still recognizes
  pre-reform lane artifacts (KUN_*, GORU_*) via aliases, so history stays
  staffed. nm_paper_run_dashboard seat tables renamed in the same pass.
- **Honest ages**: header now reads "rendered X ago · events X · status
  snapshot X" — three different staleness answers that used to be one
  misleading number. Health judges by the freshest signal: a live events feed
  no longer renders as system-wide STALE. The survey-autopilot panel admits
  its sidecar is 16 days old instead of posing as live.
- **Perf/housekeeping**: events log now tail-read (was a full 22 MB read per
  render); dead V1 renderer atticked (it silently overwrote v2's output path);
  346 backup files swept from the cockpit root; the four index-linked pages
  that had been 45-day orphans are now refreshed by every monitor pass;
  cross-page nav pills added to ge-autopilot (spin-parity, BHU, index, audio).
- **DECISION FOR YOU — scheduled rendering**: the cockpit still freezes when
  my session sleeps. A 10-minute LaunchAgent is prepared and tested at
  tools/cockpit-scheduling/ (install = 2 commands in its README). I did not
  install it: persistence on the Studio is your call.

## Audio reports

- **The burst-drop bug is dead**: the single-slot latest.mp3 latch dropped all
  but the last of any burst (your 08-19 Fable trios delivered only Blanc).
  Publishing now goes through a locked, monotonic queue.json; the MacBook
  daemon (v2.1, redeployed) and the new listen.html drain every unplayed
  reading in order and retry failures instead of skipping them.
- **Quiet hours are enforced by the pipeline** (22:30–08:00 KST): overnight
  readings render + queue silently and never touch the latch — no more
  remembering NM_SAY_NO_PLAY. `nm_morning_digest.sh` is the sanctioned first
  sound of the day. Tonight's own test readings stayed silent by construction.
- **Transcripts were regressed since 08-16** (no reading had a .txt, killing
  alignment and page transcripts) — fixed; every reading now writes its
  transcript and spawns alignment.
- **listen.html v2**: shows WHO is speaking (colored per-Fable identity from
  the single voices.json registry), live transcript, recent-readings list with
  on-demand play for quiet entries, legacy fallback.
- **Resilience**: edge-tts fallback with gender-matched voices — a $0 Nous
  balance now degrades the voices instead of hard-muting the system. Archive
  index rebuild 4.0s → 0.04s (duration cache). Test artifacts segregated to
  _tests/ (archive now counts 187 real readings).
- **Adversarially reviewed** (codex seat): 2 blockers + 4 majors found and
  fixed (publisher locking, seq durability, daemon retry semantics, force-live
  strictness, tmux quoting); accepted trade-offs documented in c9d41444.

## Flags / not done

- **kimi wrapper broken**: `~/.local/bin/kun` fails with `env: : No such file
  or directory` from non-interactive shells — the review went to codex
  instead. Worth a look before the next kimi gate.
- **Retention decision**: status-audio is 296 MB / 10 days and growing
  ~30 MB/day; nothing prunes. Proposal: move readings >30 days to cold
  storage — your call.
- **Live worktree now serves the feature branch** (detached at c9d41444+)
  instead of stale main (was 26 commits behind origin/main). Reconciling main
  is a separate decision.
- Not touched (deliberately): LabStages/WikiPageClient monoliths, /admin/*
  auth (frontend has none — flag), the 3 pre-existing ge_dashboard_renderer
  test failures, Mac Pro (excluded per your rule).

## Resource use

agy: homepage + tokens + contribute (its lane, ~40 min). codex: adversarial
review (the listen.html write-lane stalled 30 min and was killed; Blanc wrote
the page). kimi: $0 spent (wrapper broken). Claude: integration, cockpit
surgery, audio core, review fixes. Commits: b4c5842f, 577e1003, c6e2dd48,
1a2224a1, c9d41444, 3fc28916 (+ deploy-script fix). All pushed.
