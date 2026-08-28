# KUN WHY-STUDY INTRO FOUR-LANE PACKET

Created: 2026-08-09 21:38 KST

Authoritative orders read:

- `HWAO_SPIN_WHY_INTRO_ORDER_20260809T2125K.md`
- `HWAO_WHY_STUDY_INTRO_FOUR_LANES_20260809T2131K.md`

## Scope

The spin why-study diagnosis is extended to:

- `fesc`
- `brightend`
- `mzr-anchor`
- `mzr-census`

All four lanes remain fail-closed with active `SOURCE_FREEZE.json` absent. This order does not authorize
any result claim and does not authorize Yui to build these four lanes before the spin pattern is validated
by Duho.

## Current State

Freshness check after reading the order found:

- `reviews/LANA_SPIN_WHY_MOTIVATION.md` exists post spin-order.
- No post-order Lana four-lane motivation/boundary packet found yet.
- No four-lane Goru/Yui/Tori why-study packet found yet.

Current status: **HOLD AWAITING LANA FOUR-LANE MOTIVATION PACKET**.

## Per-Lane Adversarial Traps

### fesc

Overclaim block:

- "There is a photon-budget shortfall" is a result claim.
- Any sentence implying the lane has established a shortfall, deficit, crossing, significance, or required
  escape-fraction behavior is a block.

Vacuity block:

- An intro that only says "we test the photon budget carefully" is method setup, not why-study motivation.
- The motivation must explain why an ionizing-photon budget question matters if a shortfall existed, while
  staying conditional.

### brightend

Overclaim block:

- "JWST found too many bright early galaxies" is a result claim and not this lane's to assert.
- Any sentence implying confirmed abundance tension, excess, or cosmological surprise is a block.

Vacuity block:

- An intro that only says "we compare catalogs and eligibility" is method setup.
- The motivation must explain why the bright end of early-galaxy counts is worth testing without asserting
  what the counts show.

### mzr-anchor

Overclaim block:

- "The mass-metallicity relation evolves" is a result claim.
- Any sentence implying a measured evolution, offset, sign, or deficit is a block.

Vacuity block:

- An intro that only says "we build anchors" is method setup.
- The motivation must explain why anchoring metallicity measurements matters before asking whether any
  evolution can be assessed.

### mzr-census

Overclaim block:

- "The archive is inadequate" is a result claim.
- Any sentence implying the archival record fails, is incomplete, or cannot answer the question is a block.

Vacuity block:

- A borrowed metallicity-physics opening is wrong for this lane.
- The motivation must be data-informatics: why it matters to know whether archive metadata can support a
  later eligibility/measurement question at all.

## Gates

- No result claims of any kind.
- No lane may state a finding while active `SOURCE_FREEZE.json` is absent.
- No public/frontend/cockpit replacement, YouTube, DB, deploy, Git, billing/config, or secrets action.
- Preserve all prior candidates; new versioned artifacts only.
- No seat may label anything accepted.

## Kun Review Trigger

Kun review begins only after Lana provides per-lane source-grounded motivations, primary-source quotes, and
sentence-level claim boundaries. Yui build remains blocked for these four lanes until Duho validates the
spin why-study pattern.
