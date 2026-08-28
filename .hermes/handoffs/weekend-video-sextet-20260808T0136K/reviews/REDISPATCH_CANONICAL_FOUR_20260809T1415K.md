# RE-DISPATCH — Goru, Kun, Tori: stamp the FOUR CANONICAL hashes

Filed 2026-08-09 14:15 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"re-dispatch all three against the four current hashes."*

Hwao retains coordination and accept/hold. **Lana is through on all four** (`LANA_OVERHAUL.md`,
14:10 KST). This closes the gap for the other three domains.

## Why a re-dispatch — no seat's work was wrong, but the targets moved

Two fix waves landed today. Your packets each bound to whichever hashes existed when you ran:

| seat | filed | covered | missing on the canonical set |
|---|---|---|---|
| Goru | 14:02 | `d6014ac0` ✓, `acfb7fee` ✓, `c772e643` ✓ | **mzr-anchor — Section 7 reviewed `…0245K` and calls it "unchanged"**; `c892f3fa…` appears nowhere (0 occurrences) |
| Kun | 14:06 | `d6014ac0` ✓, `973daba3` | **fesc/brightend covered at `47eb0d0b…`/`6e0f4b09…` — superseded**; mzr-anchor at `973daba3…` — superseded |
| Tori | 13:50 | `47eb0d0b`, `6e0f4b09` | **both superseded**; mzr-census and mzr-anchor not at canonical hashes |

Only **mzr-census `d6014ac0…`** currently has all four seats on the same artifact.

## The four canonical hashes — verified disk == freeze == QA at 14:15 KST

| lane | directory | SHA-256 | bytes | QA |
|---|---|---|---|---|
| mzr-census | `…canary-20260809T0320K` | `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` | 9,539,823 | PASS 28/28 |
| fesc | `…canary-20260809T1345K` | `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0` | 10,056,847 | PASS 28/28 |
| brightend | `…canary-20260809T1345K` | `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8` | 9,812,969 | PASS 28/28 |
| mzr-anchor | `…canary-20260809T1406K` | `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584` | 9,722,369 | PASS 28/28 |

All four are **frozen with complete packets** — `POST_ENCODE_FREEZE.json`, `encoded_qa.json`,
`RECEIPT.json`, source and provenance manifests, contact sheets. The earlier incomplete mzr-anchor
`…1300K` is superseded and should not be reviewed.

## The delta is small — scope your re-run accordingly

Every outstanding change is a **`short_title`-only** edit. No narration was rewritten; audio was
reused byte-identically from each predecessor; plotted geometry is unchanged from the versions you
already cleared.

| lane | change since your packet |
|---|---|
| mzr-census | none — `d6014ac0…` is what you reviewed |
| fesc | `A photon-budget mismatch has two explanations` → **`An apparent …`** |
| brightend | `An archival gap has two explanations` → **`An apparent …`** |
| mzr-anchor | `A metallicity offset has two explanations` → **`An apparent …`** |

Origin: Kun's mzr-anchor claim-drift HOLD, which Duho ordered fixed and Lana generalised across the
portfolio — a persistent header that presupposes the phenomenon asserts what the narration
conditionalizes.

**Useful fact for Kun's reproducibility row:** `c892f3fa…` was built twice — once with the archived
renderer `7d42ea80…` and once with the shared renderer `71953059…` — and both produced **byte-identical
output**. So the newer renderer's `peak_curve`/`peak_plane` changes do not affect this lane, and the
diff versus `973daba3…` remains title-only.

## Specific asks

**GORU** — re-stamp Section 7. It currently reports mzr-anchor as *"unchanged from the prior review"*
against `…0245K`; the lane's title was changed at 13:00 and the canonical hash is `c892f3fa…`. Your
other three lanes need only confirmation that the title edit did not disturb state counts, section
durations or graphics share.

**KUN** — fesc/brightend at the canonical hashes, plus mzr-anchor `c892f3fa…`. Audio is byte-identical
to predecessors, so wpm and A/V deltas should be unchanged — verify rather than assume. All four now
carry candidate-local `provenance/` snapshots, so the rebuild row is testable on every lane.

**TORI** — the persistent chrome at full resolution on the canonical bytes. Your 1,389-frame geometry
sweep still applies: the plots are unchanged, only the header text differs.

## Seat availability at dispatch, recorded honestly

| seat | pane | state |
|---|---|---|
| Goru | `%33` | **idle** — *"standing by for any further checks"* |
| Kun | `%25` | **BLOCKED on a confirmation prompt** — a rebuild command awaiting *"Press enter to confirm"*. It is already targeting the canonical fesc/brightend dirs. This seat cannot proceed until a human clears that prompt; no other seat may press keys into it. |
| Tori | `%23` | **busy** — mid-task, plan 5/7 |

Dispatched by file. Nothing was pasted into any pane.

Independent packets, append-only, preserve disagreements. No lane has a `SOURCE_FREEZE.json`; all four
remain method-only, `video_reportable_now` false. A 28/28 machine QA is not semantic authorization.
