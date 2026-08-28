# ⚠ DELEGATION TRANSFERRED — 2026-08-08 13:12 KST

**The `yui-video-integration` (Fable) seat's write authority is REVOKED.** It exhausted its Fable 5
limit before starting the overhaul build. Per Duho: no credits bought, no provider config changed.

**The single candidate writer is now `yui-overhaul-integrator`** — tmux session of that name,
existing `yui` Hermes profile (non-Fable, Hermes/Codex route), rooted at `integrator/`.

Verified at transfer: the old Fable seat is **idle**, holds no in-flight build, and produced no
overhaul candidate. It is read-only from now on — it may be read for history, and must not be
briefed, steered, or allowed to write. If it is ever resumed, it has no authority.

**Exactly one candidate writer exists.** Everything below applies to the new seat **except the
TTS clause**, which was superseded the same day — narration is now authorized for the spin
method-only overhaul. Where this file and `HWAO_OVERHAUL_ORDER.md` disagree, **the order wins**.

---

# Delegation — `yui-video-integration`, isolated-copy writer

Recorded 2026-08-08 ~02:02 KST by Hwao, per Duho's continuity handoff:

> keep a bounded Hwao integrator controller alive or delegate exactly one isolated-copy writer seat
> to yui-video-integration … it may consume paper-Yui requests and edit only integrator/
> candidate-workspace copies of renderer/storyboards, producing silent/versioned visual canaries;
> it may not edit repo/shared tools, invoke TTS, touch public/shared MP4 aliases, use Git, or publish.

*(Quoted as issued 2026-08-08 ~02:02 KST. The "invoke TTS" clause was superseded ~13:02 KST for the
spin method-only overhaul — see the TTS entry under FORBIDDEN. Every other prohibition in that
quote still stands.)*

**Exactly one** such seat exists. It is the only writer to `integrator/`.

## Why this seat exists

The narration controller finished its pass and exited. Recutting the voice answered a *consistency*
question; it did not touch the thing Duho actually complained about — **scientific presentation
structure**. This seat carries that work, and it is deliberately restricted to a sandbox because the
shared renderer feeds five lanes and the live cockpit.

## Write scope — ALLOWED

- `integrator/candidate-workspace/tools/*` — **copies** of `nm_paper_video.py`, `nm_paper_plot.py`,
  `nm_paper_narrate.py`, `nm_paper_tts.py`, seeded 02:02 KST.
- `integrator/candidate-workspace/storyboards/*` — **copies** of all five lane storyboards.
- `integrator/canaries/<name>-<stamp>/` — versioned visual canaries with receipts.
  **Narrated for the spin method-only overhaul** (see the TTS clause below); silent for everything else.
- `integrator/requests/` — reading paper-Yui requests; writing replies.

## Write scope — FORBIDDEN

- **`/Users/duhokim/NebulaMind/NebulaMind/tools/*`** — the repo's shared tools. Copies only.
- Any lane directory other than through `requests/`.
- **TTS — narrowly authorized, 2026-08-08 13:02 KST.** The blanket silent rule is **SUPERSEDED**
  for the spin method-only overhaul only. Duho watched the silent canary and said *"still without
  audio"*, which authorizes narration on that cut; `lanes/spin/STATUS.json` now reads
  `narration AUTHORIZED for method-only claims`, and `HWAO_OVERHAUL_ORDER.md` §2 specifies Alloy,
  speed 1.18, no music, 105-125 wpm, sentence-aligned.
  **Still forbidden:** narration on any OTHER lane's canary, and any narration of a blocked claim.
  Audio authorization does NOT change scientific reportability — `video_reportable_now` stays
  `false`.
- `frontend/public/videos/*`, any shared or aliased MP4, `paperVideos.ts`, the cockpit, DB, deploy.
- **Git** — no add, commit, push, merge, branch.
- Upload, publication, YouTube visibility, browser automation, billing, secrets.

## Source authority — the part that matters most

A **numeric-source-guard PASS is not semantic authorization.** That mistake was already made once
tonight and corrected: the spin-parity alloy candidate was reported PASS and had to be pulled back to
HELD. The guard proves a number appears in a cited file; it cannot judge whether the lane may state
the result at all.

Before rendering anything for a lane, **read that lane's `lanes/<lane>/SOURCE_FREEZE.json` and
`STATUS.json`** and honour `allowed_scope` / `forbidden_scope`.

Currently in force — `lanes/spin`, freeze `spin-method-canary-pass1-20260808T0153K`:

- `video_reportable_now: false`, decision **`BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY`**
- **Allowed**: frozen source/sample funnel · the predeclared asymmetry equation · handedness
  convention and alignment schematic · predeclared bias-control design · a clearly labelled
  unresolved-result boundary.
- **Forbidden**: T3/T4 headline or result figures · dipole-axis interpretation · cosmological parity
  violation · GRB, SN Ia, dark-energy, quasar or H0 context · black-hole-universe support · any new
  DESI Legacy Survey or Ganalyzer claim.

A semantic/status mismatch **blocks rendering**. It is never resolved by changing the visuals.

## First task

A **method-only** visual canary for spin-parity, entirely inside `allowed_scope`: how the sample was
frozen, what `A = (N_CW − N_ACW)/(N_CW + N_ACW)` is, how the handedness convention and mirroring
work, what bias controls were predeclared — and an explicit, clearly-labelled boundary saying the
result is not yet reportable and why. Silent. Versioned. Receipts per
`HWAO_WEEKEND_ORDER.md` §5.

That deck is useful regardless of how the A3.8 verdict lands, which is exactly why it is first.

## Stop conditions

Window end **2026-08-10 07:00 KST**; any closed gate; any semantic/source mismatch; a lane freeze
that forbids the intended scope. Halt and record — do not improvise around a gate.
