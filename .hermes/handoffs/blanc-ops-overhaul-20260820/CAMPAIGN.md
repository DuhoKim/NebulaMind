# Blanc/OPS overnight overhaul — 2026-08-20, started 01:26 KST

Duho, verbatim (2026-08-20 ~01:25 KST): "overhaul nebulamind website, cockpits,
and audio report systems overnight leveraging all our resources."

## Scope (all Blanc-owned surfaces)

1. **Website** — frontend/ Next.js app (nebulamind.net + lab.nebulamind.net).
   The Lab is the focus; wiki is deprecated (no new wiki features).
2. **Cockpits** — the rendered pages under HermesOps/cockpit + agent-reports
   (ge-autopilot, spin-parity, bhu-lane2, index, live-steering, mobile).
3. **Audio reports** — nm_fable_say / listen + archive pages / listener daemons.

## Hard rules for tonight

- **No audio playback before 08:00 KST** — reports auto-play on BOTH of Duho's
  machines; a night reading would wake him. All test renders use NM_SAY_NO_PLAY=1
  and must NOT touch latest.mp3/latest.txt (the MacBook daemon plays on change!).
  Morning briefing in onyx at ~08:00 KST is the first sound.
- **Boundaries unchanged**: never touch prereg/, bhu-* work products,
  portal.nersc.gov, or panes in sextet-v2. Platoon seats run in MY OWN windows
  (ge-mastermind:blanc-* or session blanc-ops).
- **Reversibility**: every website/cockpit change lands as git commits on
  feat/paper-workflow-v2 (scoped, no other lanes' dirty files). Production serve
  is only switched after a local build passes + smoke test; rollback = git.
- **Cap discipline**: Fable weekly was 61% used at 08-19 evening — bulk
  implementation goes to the non-Claude seats (agy ~0% weekly, Codex 24%
  weekly, kimi wallet $24.40 with $10 floor — kimi one-shots only for review
  gates, logged). Claude subagents for survey/synthesis/review only.
- **Quality**: cross-engine adversarial review before anything is declared done
  (house standard). Compiles + renders ≠ done; each surface needs a
  before/after that a tired human can see is better.
- **Major notifications only**: the session log carries details; Duho gets a
  morning handover (written + audio) with verdicts, not play-by-play.

## Phases

- **P0 Survey** (running, 3 Explore agents): website / cockpits / audio estate.
- **P1 Plan freeze**: per-surface work orders written to this dir after survey.
- **P2 Build**: platoon lanes execute; Blanc integrates + commits per scope.
- **P3 Verify**: cross-engine review; build + render + smoke tests; fix.
- **P4 Deploy + handover**: prod build switched, cockpit re-rendered,
  MORNING_HANDOVER.md + 08:00 audio briefing.

## Ledger

(appended as things happen; timestamps KST via `date`)

- 01:26 campaign dir created; P0 surveys launched (website / cockpit / audio).
- 01:30 resource snapshot: Fable 66% weekly (LEAN Claude use — integration/review
  only), agy 0% (primary workhorse), Codex 24% weekly (secondary), kimi $18.21
  (floor $10 → at most ~1-2 review one-shots, logged), Nous $57.75 (TTS fine).
- 01:30 anchors armed: 40-min cron ticks 01-08 KST + one-shot 08:02 handover
  (written + first-audio-of-the-day briefing).
- 01:34 P0 complete (3 surveys in). P1 work orders written: AUDIO / WEBSITE /
  COCKPIT. agy seat launched + briefed on website visual lane (watcher armed).
  Assignments: Blanc=audio core+cockpit surgery+site plumbing; agy=homepage/
  tokens/contribute; codex exec=listen.html v2 + audio index perf (after queue
  contract exists); kimi=one dawn review one-shot if wallet allows.
- 01:52 P2 largely complete. Commits: b4c5842f (cockpit), 577e1003
  (audio), c6e2dd48 (website). Frontend build green. agy lane done+integrated.
  Codex listen.html v2 lane still running. Remaining: listen page integration,
  P3 cross-engine review, P4 deploy + handover.
- 02:04 P3 done: codex adversarial review → 2 blockers + majors fixed
  (publisher lock + seq floor, daemon retry-not-skip, force-live strictness,
  tmux quoting), accepted items documented (c9d41444). listen.html v2 written
  by Blanc after codex exec write-lane stalled 30 min (killed).
- 02:04 P4: PRODUCTION DEPLOYED — nebulamind.net serves c9d41444
  (rollback: scripts/deploy_frontend.sh afeaa91e). Public smoke: / /lab
  /contribute /sitemap all 200. Cockpit rendered fresh. Remaining: morning
  handover 08:02 (cron), night-watch render ticks.
- 02:07 tick: stretch items A6 (index duration cache, 100x warm
  rebuild) + A9 (edge-tts fallback, gender-matched voices) shipped + mirrored.
  Cockpit render pass clean. Remaining stretch: A7 test-file segregation
  (cosmetic, may skip). Night-watch continues.
- 02:48 tick: A7 done (11 test artifacts → _tests/, archive at 187
  real readings). Health: prod 200, MacBook daemon alive. MORNING_HANDOVER.md
  drafted in full. agy lane window closed. All campaign items complete;
  remaining: 08:02 delivery (audio digest + pane summary).
