# FINDING — two defects inside the SIGNED Tier-C V35 (operative), exposed by the V37 gate — 12:08 KST

Found by codex (CODEX_TIERC_V37_SEATB.md, items 1 and its [MAJOR] follow-on), reproduced and confirmed by the author. Both live in V35's own pinned code and text, unchanged by V36/V37. Filed under Blanc's binding rule 1 (text ≠ script → STOP and file for Duho).

1. **Protected radius truncated.** §8.14 prescribes r_T = min(64, max(23, 2·shape_r/0.262)) with no rounding. `miniprereg_pins/protected_region.py` (V35 pin 6767403a87ca4c98…, unchanged) returns `int(...)`. Reproduced: shape_r = 3.1309 → formula 23.9, helper 23; a flagged output pixel at distance 23.505 from the centre is inside the prescribed T and is NOT refused. Consequence: on the main path, contamination between r = 23 and the true r_T (up to 0.99 px) is accepted where the signed text refuses it. The validation path (r_T = 23 exactly) is unaffected. Attempt 1 (the §9B gate of 2026-09-05) ran on the validation path only.
2. **§8.9d versus §8.14a.** §8.9d flags an output pixel by its nearest-neighbour source pixel; §8.14a's rationale says carriage "spreads a rejected source pixel across up to four output pixels" and counts "what the contamination actually touched". Under bilinear image sampling with a fractional offset, a replaced source pixel contributes to output pixels whose nearest-neighbour flag lies elsewhere — codex's executed counterexample: flag at (41,56) outside T, replaced value reaching (42,56) and (42,57) inside T, object SCORED. The text promises a protection the pinned predicate does not implement.

## What this does and does not touch
- Nothing has run under V37; V35 stays operative; the frozen 12,217 remain untouched; attempt 1's result stands on the validation path where (1) does not bite.
- Option A's development path (V15 §6 / V37) would inherit both unless amended.

## Duho's decision (through Blanc): the scope of the next Tier-C version
(a) V38 amends §8.14/§9B.2d/§8.15b to compute r_T in binary64 without truncation (new protected_region pin) AND restates §8.14a to the nearest-neighbour predicate actually frozen, disclosing its cost; or (b) V38 changes the flag predicate to full-stencil protection (a design change, separately gated); or (c) stop the amendment track. Until ruled, no V38 is drafted.
