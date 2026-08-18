# Handover — night of 2026-08-18 (written 22:40 KST)

Any future session can execute Wednesday's chain from the records named here; nothing depends on
this session surviving.

## 1. BHU explainer v2 — remade, gated, published

Duho (17:15, verbatim): "remake the video, now make it, easier to understand, explainning how it
can be relataed to BHU cosmology". Full sextet chain in
`weekend-video-sextet-20260808T0136K/bhu-explainer-v2-20260818/`:
Yui script (10 panels, 625 words) → Lana ledger (66/66 MAPPED, 0 FLAG; 3 definitional sentences
pinned: NASA Imagine, Uzan 1009.5514, BLR 0802.2997 body) → Goru visuals → Kun
`PASS_EXPLAINER_PACKET` (8/8 incl. comprehension check) → Tori local build (341.3 s, exact ASR
word-diff) → Kun `PASS_RENDERED_EXPLAINER` (captions re-extracted byte-identical).

**Published UNLISTED on the NebulaMind channel: https://youtu.be/77CJRnb0q9o** (authorized
verbatim "upload it unlisted"; channel server-verified UCUHBNGk8ozEnisQRuchoS4Q). First upload
`qlcxQbkIYlI` landed on the personal channel (token misbinding, see §5) — **Duho still needs to
set it PRIVATE in YouTube Studio under the personal channel** (API cross-channel 403). Registry
`cockpit/videos/published.json` key `bhu-explainer-v2` carries the whole story.

## 2. Checksum harvest — running, guarded

47,811/60,308 (79%) at 22:39, 0.993–0.997 req/s, zero contradictions, no block event. Self-pauses
at window close 24:00 KST tonight; resumes Wed 12:00 KST; completes Wed ~13:30–14:00 KST.
Process is nohup-detached (survives session close). State = `receipts.jsonl`, never the heartbeat
(`prereg/_tori_harvest_20260817/RESUME_AFTER_REBOOT.md` has the resume command; used twice today
after the macOS-update reboot).

## 3. Longo prereg — two human decisions landed tonight

- **`PILOT_DECISION_20260818.md`** — Duho, verbatim: "go with the pilot, 150 labels" (§2b as
  written: 90 real / 40 synthetic / 20 retests; outcomes PASS-TO-FULL-HC1H or INCONCLUSIVE only).
- **`ACQUISITION_PREAUTH_20260818.md`** — Duho, verbatim: "pre-authorize the acquisition, run it
  after the cross-check passes". Conditions: harvest complete AND known-issues cross-check PASS.
  Authorizes execution under the frozen successor binding (`1371b110…`, mode 444) only; does NOT
  waive the transport-build Kun gate (BUILD_ONLY_STOP removal is gated) or the binding's pacing/
  prohibitions. Wednesday chain = tasks #8–#10 on the session board; a session-only cron
  (Wed 14:22) exists as a kick, but the records are the durable truth.

NERSC: Duho submitted the Iris account request tonight (username duhokim, project cosmo, project
contact listed as Stephen Bailey; institutional email duhokim81@cnu.ac.kr — the 24 h password
link lands THERE). Globus Connect Personal install still open (Duho). Lang thread: no reply since
08-16; don't nudge before ~Thu.

## 4. BHU theory Phase 0 — closed, with a gated closure note

Lane `weekend-video-sextet-20260808T0136K/bhu-theory-phase0-20260818/`. Duho: "go ahead with
phase 0", then "go ahead with the closure note if the gate passes".

- All three routes **DEAD-ON-ARRIVAL** (Lana scoping + Goru prior-art, independent, convergent;
  Kun `PASS_PHASE0_SCOPING` — re-fetched all sources, recomputed all arithmetic, adjudicated the
  one novelty disagreement).
- Route A headline: allowed global rotation caps handedness asymmetry at A ≲ 5×10⁻⁷;
  3σ needs ~18× every galaxy in the observable universe; classifying all 2×10¹² gives 0.74σ.
  Sample-complete kill. Route B ~66 orders under reach. Route C closed by causal-boundary
  argument (~0.75 confidence, framework-level).
- **`BHU_ROTATION_HANDEDNESS_CLOSURE_20260818.md` — gated `PASS_CLOSURE_NOTE`.** Research-note
  class by its own §opening; one novel element (bound→floor confrontation; mechanics are
  Li 1998's). **Where it goes (cockpit only / arXiv comment / nowhere) is Duho's open decision.**
- Net: C15 closed on both arms for the surveyed model classes; BHU line has no open theory
  question and no observational program beyond the spin measurement + NS-criterion watchpost.

## 5. Process faults logged tonight (fix before relying on lanes unattended)

- **argv-drop launch bug, 3×**: `hermes -z` (kun), `agy <prompt>` (goru, 2×) can drop the initial
  prompt (trust dialog eats it, or interactive boot ignores it). Working pattern: launch bare →
  verify seat is at its prompt → send absolute-path pointer with `tmux send-keys -l`.
- **Stale cwd**: seats reuse windows; "current directory" in a pointer is a bug. Absolute paths
  always.
- **`kun` profile default provider is dead** (`kimi-coding`, no key). Workaround used all night:
  `kun --provider nous -m moonshotai/kimi-k3`. Fix the profile default when convenient.
- **`agy_autoapprove_watch.sh` needs PATH**: run with `PATH="/opt/homebrew/bin:$PATH"` or it
  dies on bare `tmux` (cost Goru ~10 min tonight).
- **YouTube tokens**: upload-only `token.json` dead since 08-10 (restore it against NebulaMind
  when convenient); `token_manage.json` re-authorized tonight by Duho, now NebulaMind-bound.
  `RbgW_4U7bi0` (08-13, private) still sits on the personal channel.

## 6. Boundaries

Nothing published beyond the one authorized unlisted upload. Crew lanes never touched
`portal.nersc.gov` (harvest only, frozen pacing). No credits spent. K-8 untripped; no image byte
moved; acquisition remains conditional per §3. tmux session `sextet-v2` left alive deliberately
(scrollback is evidence).
