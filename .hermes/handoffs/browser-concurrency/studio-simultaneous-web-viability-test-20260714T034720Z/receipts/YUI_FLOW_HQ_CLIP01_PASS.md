# YUI Flow HQ regeneration — clip_01 quality gate PASS

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Actor: Yui, Flow operator on Mac Studio
Authorization: direct Duho message in the active session
Source prompts: `/Users/duhokim/HermesOps/scripts/clips/prompts.txt`
Prompts SHA-256: `af40e8f413cfa107d4f99350282d75f85cbc73991bb0812c20785778f21f0138`

## Exact Flow configuration

- project: `a22b5b61-833d-4e62-857b-4a7030b93bfa`
- model: `Veo 3.1 - Quality`
- Lite used: no
- output count: `1x`
- duration setting: `8s`
- aspect ratio: `16:9`
- displayed cost: `100 credits`
- page-scoped challenge: false
- target drift: none

The full model/count/duration/cost configuration and exact prompt were reverified immediately before the serialized submit.

## Submission and settlement

- source prompt: line 1
- submit account lease: `L00054`
- expected pre-submit result cards: 3
- one and only one submit was dispatched
- immediate card label: provisional `Failed`
- the account-submission lease was released immediately after acceptance
- no retry was made
- read-only settlement polling continued instead of treating the early label as final
- settled result cards: 4 total
- new settled media id: `76e43fa7-d356-4df9-8df3-d3de6d39497a`
- settled prompt match: exact
- final media state: playable, readyState 4
- duration: 8.000 seconds
- resolution: 1280x720
- failed cards after settlement: zero

## Saved artifact

- path: `/Users/duhokim/HermesOps/scripts/clips/clip_01_hq.mp4`
- original preserved: `/Users/duhokim/HermesOps/scripts/clips/clip_01.mp4`
- overwrite used: false
- bytes: 5,758,796
- video codec: H.264
- audio codec: AAC
- frame rate: 24 fps
- SHA-256: `49089859d7198d38649018da840b9ed33b63249288d2f1cccae2b3cbe0cb181b`

## Visual quality gate

Four representative frames from the 8-second output were inspected and compared with the existing clip_01.

PASS:

- `NebulaMind` is spelled correctly and remains recognizable/legible
- the wordmark is visibly present, unlike the original clip_01, which resolves into an abstract spiral mark without the requested wordmark
- electric-cyan and magenta edge glow is present
- deep-space background and fine gold star field are present
- the animation is visually coherent across sampled frames
- no malformed letters or structural scene break were observed
- bright gold/star flares briefly pass over portions of the wordmark in middle frames, but the wordmark remains readable and the effect is consistent with the requested star field
- suitable to continue the authorized HQ batch

## Credits

- live pre-submit balance: 24,838
- live post-settlement balance: 24,738
- observable delta: 100 credits
- this exact delta matches the displayed 100-credit generation cost
- no separate refund event was visible

Clip_01 passed the Duho quality gate. Yui may continue prompts 2–13 sequentially under the same authorization, one submission at a time, with settlement polling and non-overwriting HQ saves.

YUI_FLOW_HQ_CLIP01_PASS_20260714
