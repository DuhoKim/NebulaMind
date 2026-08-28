# HWAO AUTHORITATIVE ORDER — two-hour sibling completion track

Issued 2026-08-09 16:20 KST by Hwao under `DUHO_TWO_HOUR_SIBLING_COMPLETION_20260809T1618K`.
Window start 16:18 · snapshots 16:38 / 17:18 / 17:58 / 18:18 · **earliest finalization 18:18** ·
hard local stop 18:33 if Duho has not checked in. Duho may stop or steer sooner.

## Where the four lanes actually stand

| lane | phase | verdict | freeze | last verified |
|---|---|---|---|---|
| fesc | `source_and_current_artifact_freeze` | IN_PROGRESS | ABSENT | 2026-08-07 |
| brightend | `source_status_freeze` | IN_PROGRESS | ABSENT | 2026-08-07 |
| mzr-anchor | `source_freeze_in_progress` | PENDING | ABSENT (has `SOURCE_HASHES_INITIAL`, `source_freeze/`) | 2026-08-07 |
| mzr-census | `INITIALIZED` | PENDING_SOURCE_AND_STATUS_FREEZE | ABSENT | 2026-08-08 |

All four video candidates **PASS as method-only local canaries**. That is a statement about the
deck, not about the science, and it unlocks nothing.

## The one hazard this run must not produce

Every lane is one file away from being allowed to state a result. The failure mode is therefore
obvious and must be named: **manufacturing a freeze in order to unlock a result-bearing video.**

A freeze is not a formality that clears a path. It is a claim that specific bytes support a
specific finding. So:

- **Fail-closed is the default and it is a real outcome.** A lane that ends the window with
  `SOURCE_FREEZE` absent and a precise account of what is missing has *succeeded* at this task.
  Duho's direction says so explicitly: a fail-closed blocker is useful progress and must be
  deepened, not bypassed.
- **Provenance is not permission.** That a number exists in an artifact, hashes correctly and is
  reproducible does not make it reportable.
- **No result may be invented or carried forward from a stale video.** The method-only decks state
  no findings; nothing can be back-read out of them.
- **Anchor and literature claims must be quoted from the primary source at freeze time.** A
  directional claim written from memory was frozen and sha-pinned once before and inverted a whole
  lane. Freeze gates check internal coherence, not external truth — only a quoted primary source
  does that.

## Role splits — the author of a freeze may not adjudicate it

| seat | role | writes |
|---|---|---|
| **Goru** | builds each lane's evidence inventory and a **proposed** freeze from actual lane artifacts — hashes, manifests, provenance, counts | `lanes/<lane>/` proposals + own report |
| **Lana** | science adjudication: is there a defensible, **non-circular** finding these bytes support, and what exactly is its boundary; verifies anchor claims against primary sources | own report only |
| **Kun** | adversarial: tries to **break** every proposed freeze; defaults to BLOCK under uncertainty; reproducibility and rebuild | own report + own scratch |
| **Tori** | custody, receipts, relay; decisive actual-frame sweeps on any new candidate; verifies gates stayed closed | own append-only packet + evidence |
| **Yui** | **sole candidate writer** — builds a result-bearing candidate only for a lane whose freeze has cleared all three adjudications | `integrator/` only |
| **Hwao** | coordination, snapshots, verdicts | orders and status only; no lane writes |

**A freeze flips `video_reportable_now` to true only with three independent passes: Lana on
science, Kun adversarially, Tori on provenance and custody.** Goru authored it, so Goru does not
clear it. I do not clear it alone either.

## Sequence

1. **Now → 16:38.** Goru inventories all four lanes. Lana begins the science boundary per lane.
   Kun rebuilds and pressure-tests. Tori takes custody of the current PASS set and confirms gates.
2. **16:38 → 17:18.** Proposed freezes where the artifacts genuinely support one; explicit
   fail-closed blockers where they do not. Adjudication begins.
3. **17:18 → 17:58.** Yui builds result-bearing candidates **only** for cleared lanes. Tori sweeps
   each new hash. Uncleared lanes deepen their blocker instead.
4. **17:58 → 18:18.** Private exact-hash watch/listen queue for Duho. Prepare — **do not apply** —
   exact-diff preflight packets for public/frontend replacement, upload and cockpit.

## Gates — unchanged, and no agent may relax them

No upload, publication, unlisting, deletion, public/frontend MP4 replacement, `paperVideos.ts`,
cockpit live-root mutation, DB/SQL, deploy/restart, Git write, browser/account mutation,
billing/provider/config change, secret access, or cron. Tailnet private playback is allowed;
cockpit-copy playback is not. Subscription-backed seats only — no credit purchase, no metered API
fallback.

**No agent may label anything `accepted_by_duho`.** Only Duho confers that, after check-in, on
exact video bytes he has watched.

Preserve every accepted, passing, failed and superseded candidate and all evidence. New versioned
directories only. Never write scratch inside a frozen candidate directory — that rule exists
because I broke it today with a defective instruction of my own.

## Reporting

Snapshot at each mark: per lane one line — freeze state, blocker, exact next action, gate status.
Report honestly if a seat is unavailable; do not fabricate a packet. Escalate to Hwao rather than
resolving a semantic/status mismatch visually.
