# YUI last authorized Flow x1 retry receipt

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Actor: Yui, Flow operator on Mac Studio
Authorization: `receipts/DUHO_RETRY_FLOW_X1.md`
Authorization SHA-256: `e23a6f46a937f335e48db5f59955e289bbb252261eb7c4b1eef5af166fceb1b7`
Authorization marker: `DUHO_RETRY_FLOW_X1_20260714`

## Exact target and challenge state

- Flow project: `a22b5b61-833d-4e62-857b-4a7030b93bfa`
- window/tab: `1/1`
- fresh retry target lease: `L00027`, broker lease epoch `27`
- page-scoped challenge before submit: false
- challenge signals: none
- visible Flow-page challenge dialogs: zero
- target remained the same through the submit and final inspection

The Chrome toolbar/profile badge was out of scope.

## x1 UI setting

A temporary exact-target lease set was used only to change the Flow output count through the visible UI:

- config target `L00024`
- desktop-control `L00025`
- focus `L00026`

The output-count menu initially showed `x2` selected. Yui performed an accessibility `AXPress` on the visible `1x` radio control. DOM verification then showed:

- `1x`: selected true
- `x2`: selected false
- `x3`: selected false
- `x4`: selected false

The menu was dismissed and the config control showed `Video · 8s · 1x`. The temporary config leases were released before fresh retry leases were acquired.

Immediately before the actual submission, the exact config control showed `Video · 4s · 1x`. It remained x1 and was more bounded than the prior 8-second setup. After the failed submission, the empty composer displayed its default `Video · 8s · 1x` state again.

## Serialized retry submission

Fresh retry leases:

- exact target: `L00027`
- Studio desktop-control: `L00028`
- Studio focus: `L00029`
- non-secret prompt clipboard: `L00031`, released after paste
- shared-account submission: `L00033`, released immediately after the submit moment

An earlier account lease `L00032` expired before any submission action. It was released; no Return/Create action was dispatched under it.

The exact project, clean page-challenge state, 151-character prompt, and `1x` configuration were verified immediately before submission.

One and only one Return-key submission was dispatched at `2026-07-14T09:30:44Z` under account lease `L00033`. Broker action evidence:

- target submit allowed: ledger epoch `152`
- focused Return allowed: ledger epoch `153`
- desktop Return allowed: ledger epoch `154`
- serialized account submit allowed: ledger epoch `155`
- account lease released: ledger epoch `156`

Prompt:

> One softly glowing electric-cyan sphere rotates slowly against a deep-black empty background, static camera, minimal scene, cinematic soft bloom, 16:9.

## Result

- the composer cleared back to its placeholder, confirming Flow accepted the submit action
- one result card appeared, matching the x1 setting
- the result card reported only `Failed`
- no generated video was associated with the new retry result
- no error code or explanatory failure text appeared on the card or its visible ancestors
- the page remained on the exact leased Flow project
- page-scoped challenge remained false

A separate visible notification said `Nothing to paste from the clipboard.` It came from the earlier prompt-input setup and was not attached to the failed result card, so it is not reported as the generation failure reason.

Conclusion: the last authorized x1 retry also failed with no visible reason.

## Observable credits

Pre-existing local credit capture:

- `24,872` remaining
- capture time: `2026-07-14T03:06:45Z`
- this capture was stale and predated both the first x2 attempt and this retry

Live Flow profile dialog after this retry:

- `24,838 Google Flow credits`
- observed after the submit at approximately `2026-07-14T09:32Z`

Observable difference from the stale capture: 34 fewer credits. This difference cannot be attributed to this x1 retry because the baseline was over six hours old and predates other Flow activity. Flow exposed no per-job debit, refund event, or transaction timestamp. No refund was observable at receipt time.

## Stop and teardown

This was the Duho-authorized LAST retry.

- no additional retry
- no batch scaling
- no account investigation performed by Yui
- account-submission lease released
- target, desktop-control, focus, and clipboard leases released
- live Yui retry leases after teardown: zero
- broker frozen: false
- ledger before receipt append: `VERIFY_OK OK (168 entries)`

Hwao should now treat this as an account-investigation handoff, not authorization for another Flow submission.

YUI_FLOW_LAST_X1_RETRY_FAILED_20260714T093044Z
