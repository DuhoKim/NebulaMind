# KUN_CONFIRM_V9

Timestamp: 2026-08-13 KST

## Verdict

HOLD_RENDER_ON_SHORTHAND_AUDIT.

This review is bound to these exact files:

- `NARRATION_DRAFT_V9.md` - SHA-256 `85f111d366c5d11d912e4f7db5586f10b491b12b1c5091d3f94d822c388190b3`
- `STORYBOARD_DRAFT_V9.json` - SHA-256 `c9824b95453be7e67d6066f3810648dc8d588a8c3210546ec9caa5ee74710d7a`
- `CLAIM_LINE_LEDGER_V9.md` - SHA-256 `aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa`
- `V9_SHORTHAND_AUDIT.json` - SHA-256 `2cd55bd9698ec11ccf002b3e1810ab51408bfdbe18f4bca3fa51314e46931624`

The V8 claim-safety pass still carries, and the description repairs are present in `bhu_description_v3.txt` at SHA-256 `2a8da3d3cd158339c6b178b31442fb17b51dd328adbeb38738517b5ebf4bc762`.

## What Passed

The V8-to-V9 diff is clean. In both `NARRATION_DRAFT_V9.md` and `STORYBOARD_DRAFT_V9.json`, the only content change is Card 04 narration:

> "One proposal -- called cosmological natural selection -- says universes have children: every black hole buds off a new universe with slightly different physics."

The full phrase "cosmological natural selection" is now spoken exactly once. Nothing else in the storyboard or narration moved.

The shorthand audit is directionally right. It correctly catches that BHU, CW/CCW, mass notation, uncertainty notation, and percentage labels can be earned in script but still appear visually before their witness phrase. The proposed render rule "reveal no earlier than the witness phrase" is the right class of constraint.

## Blocking Defect

The audit is not sufficient because it exempts the one case that motivated V9.

Audit entry:

> `"form": "CNS"`  
> `"status": "EARNED_IN_FIRST_SENTENCE"`  
> `"render_timing": "Heading may remain; the full name is the opening spoken phrase as Lana required."`

But the viewer-facing Card 04 assertion heading is:

> "One CNS chain puts a low ceiling on neutron-star mass"

That heading is an on-screen label, visible at card start under the storyboard's assertion-heading contract. The full phrase is spoken in the first narration sentence, but the initialism still appears on screen before it is visually earned. That is exactly the visual-channel failure the V9 shorthand audit was supposed to close.

For a public video made easier to understand, a muted viewer should not meet "CNS" as an unexplained heading. The audit's "Heading may remain" exception is therefore not an adequate render guarantee.

## Repair That Clears It

Use one of these repairs:

1. Preferred source repair: change the Card 04 heading in narration and storyboard to:

> "One cosmological-natural-selection chain puts a low ceiling on neutron-star mass"

2. Acceptable render-rule repair only if the source strings must remain unchanged: the renderer must not show the Card 04 heading until after the spoken phrase "cosmological natural selection" has appeared in captions/audio, and the first visible heading state must include the full phrase, not bare "CNS."

The first repair is cleaner because it preserves the full-card assertion-heading rule and avoids a renderer-only exception.

## Final Ruling

HOLD until the CNS heading is visually earned. No other V9 claim-safety blocker found.
