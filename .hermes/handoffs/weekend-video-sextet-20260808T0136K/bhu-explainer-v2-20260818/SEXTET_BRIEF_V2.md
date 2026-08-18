# SEXTET BRIEF V2 — BHU explainer remake (easier + the BHU chain explained)

Hwao (director), 2026-08-18 17:20 KST. Seats do the work; Hwao coordinates and relays only.

## Why this lane exists — Duho's direction, verbatim

> "remake the video, now make it, easier to understand, explainning how it can be relataed to BHU cosmology"

Given 2026-08-18 ~17:15 KST, after watching v1 (`../bhu-neutron-star-explainer-20260817/build/BHU_NEUTRON_STAR_EXPLAINER_LOCAL_REVIEW.mp4`, Kun-gated `PASS_RENDERED_EXPLAINER`).

Two required changes, and only these:

1. **Easier to understand.** v1 assumed the viewer already knew what the black-hole-universe idea,
   cosmological natural selection, and the Brown–Lee–Rho chain were. v2 assumes none of that.
   Short sentences. Every term defined at first use or dropped. A viewer with no physics
   background should be able to say afterwards what was tested and what happened.
2. **Explain how the neutron-star result relates to BHU cosmology.** v2 must walk the chain
   instead of naming it: universe-inside-a-black-hole idea → Smolin's cosmological natural
   selection (universes reproduce through black holes; slightly mutated constants; selection →
   constants near-optimal for black-hole production) → its stated falsifiable consequence, a low
   neutron-star mass ceiling (Brown–Bethe ≈ 1.5 M☉ via the kaon-condensate route) → the paper's
   own 2 falsifiers → what published pulsar measurements say → per-link verdict → what survives
   for the wider BHU family.

## Scope label (mandatory, from frame zero)

Black-hole-universe cosmology is Duho's personal side-interest, not a NebulaMind research
programme. Nothing in v2 presents it otherwise.

## Authorities (pinned)

| Key | File (relative to this lane) | SHA-256 | Status |
|---|---|---|---|
| A | `../bhu-mass-adjudication-20260817/C08_MASS_ADJUDICATION_20260817.md` | `5e3b9a0e7122f670d4f9558cc0f6a570f6962c754b905fb2b2047469c156317a` | gated `PASS_C08_ADJUDICATION` |
| P | `../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` | `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516` | V11's sole authority; hash re-verified by Hwao 2026-08-18 17:05 KST |
| L | `../bhu-closing-video-20260812T2322K/CLAIM_LINE_LEDGER_V11.md` | `aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa` | predecessor ledger (C01–C16 + exclusions) |
| V1 | `../bhu-neutron-star-explainer-20260817/` (SCRIPT, CLAIM_LEDGER, STORYBOARD, VISUALS, gates) | see `build/FREEZE.json` there | fully gated; v1 sentences are pre-mapped and reusable verbatim |

Seats verify hashes themselves before relying on a file. P is cited at line level exactly like A;
its §1.4 (lines 259–278) carries the CNS mechanism and the Brown–Lee–Rho chain; §0 (143–167) the
five-programmes finding; §1.1 (171–184) Pathria 1972 — **V11 excludes Pathria BODY claims
([VERIFY]); the accessible-abstract statements characterised at P 180–182 remain usable.**

## What must NOT be said (unchanged from v1, non-negotiable)

- not "the black-hole-universe idea is falsified" / "BHU is falsified" — one chain fails as its
  authors stated it; at least 5 programmes disagree (L C02);
- not "Smolin's hypothesis is refuted" — the flagship prediction is gone, which is different;
- not "we measured" / "we discovered" — the numbers are the pulsar community's;
- the 2.35-solar-mass light-curve star must not appear, not even as an aside;
- no invented mechanisms: the gated record states THAT the source's 4% binary rule exists and
  what it says, not WHY it holds. State it as the source's own rule; do not explain its origin.
- direction of the CNS claim follows the source: CNS's *stated falsifiable consequence* is a LOW
  mass ceiling (P 262–264). Do not restate it as our inference.

## New-claims policy (the v1 FLAG lesson)

Any definitional/textbook sentence v2 needs for accessibility (what a black hole is, what a
neutron star is, what "constants" means) is **cut or sourced, never softened**. Lana fetches and
pins definitional sources (`DEFINITIONAL_SOURCES.md`: verbatim quote, URL, access datetime, and a
saved local copy with SHA-256) from literature/observatory hosts only (arXiv, ar5iv, ADS, NASA
public pages). Sentences then map to D-rows like any other claim.

## Structure contract (carried from v1, per Duho's standing video rules)

- Stakes → what was done → bounded verdict complete in Panel 01, inside ~35 seconds.
- Assertion heading on every panel; a heading is a claim.
- No divider cards. End on the verdict, never on caveats.
- 4–6 minutes hard (240–360 s). Numbers as digits. Mass phrasing: "times the Sun's mass".
- Total narration ≤ 730 words; Panel 01 ≤ 72 words.

## Order of work and seat boundaries

1. **Yui** — `SCRIPT.md` + `STORYBOARD.json` (schema `nebula-explainer-storyboard-v1`, as v1).
   Brief: `YUI_SCRIPT_BRIEF.md`. Reuse v1's already-mapped sentences wherever they fit.
2. **Lana** — `CLAIM_LEDGER.md` (one row per factual sentence; MAPPED / FLAG / framing) +
   `DEFINITIONAL_SOURCES.md`. FLAGs go back to Yui: cut or source.
3. **Goru** — `VISUALS.md` v2 against the ledgered script. Deterministic geometry; closed-world
   viewer text; Panel "mass ladder" honesty rule carried from v1 (quoted 68.3% interval above the
   2.00 line; soft endpoint-free stricter-credibility halo crossing it; no invented lower bound).
4. **Kun** — packet gate over SCRIPT + STORYBOARD + CLAIM_LEDGER + VISUALS →
   `KUN_PACKET_GATE_V2.md`, first line `PASS_EXPLAINER_PACKET` or the required repairs.
5. **Tori** — `build/` here, adapting `../bhu-neutron-star-explainer-20260817/build/`
   (pipeline.py EXPECTED_HASHES → v2 files; render_cards for the v2 panel set; build_audio,
   assemble, qa_final, freeze as-is in approach). Output `BHU_EXPLAINER_V2_LOCAL_REVIEW.mp4`.
   The decoded-audio ASR word-diff against the gated script is not optional.
6. **Kun** — render gate → `KUN_RENDER_GATE_V2.md`.

## Hard boundaries (every seat)

- Local pipeline only: Pillow + ffmpeg + Hermes managed gateway TTS/ASR. **No Veo, no Flow, no
  image API, no credits, no upload, no publication, no visibility change.**
- **Do not touch `portal.nersc.gov`** — the checksum harvest is live at frozen pacing.
- All writes stay inside this lane directory. Temp files: `_tmp_*` here, never /tmp or scratchpads.
- Seats are launched with auto-approve flags; if you hit a permission prompt anyway, stop and
  say so in your deliverable rather than waiting silently.
- Rendering v2 locally is authorised by Duho's direction above; uploading is not.

— Hwao
