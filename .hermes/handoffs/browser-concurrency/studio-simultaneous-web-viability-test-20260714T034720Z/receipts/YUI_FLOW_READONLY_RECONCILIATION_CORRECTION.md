# YUI read-only Flow result reconciliation

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Actor: Yui, Flow operator on Mac Studio
Mode: read-only reconciliation; no submit, retry, delete, edit, or scale action

## Scope and custody

- exact project inspected: `a22b5b61-833d-4e62-857b-4a7030b93bfa`
- read target lease for exact project: `L00036`, mode `read`
- read target lease for Flow projects list: `L00038`, mode `read`
- no target write lease
- no desktop-control lease
- no focus lease
- no clipboard lease
- no account-submission lease
- no job submission or retry
- both read leases released

## Correct current result count in a22b5b61

The project currently contains exactly three result cards.

Current status:

1. media `ac8a1a26-bb1b-4a37-8ab9-7ee5d89aecda`: completed and playable; 4.01 seconds; 1280x720; media ready state 4 when opened
2. media `86270373-8adf-47a1-8141-fb2f63a8f35c`: completed and playable; 4.01 seconds; 1280x720; media ready state 4 when opened
3. media `cfa83faf-90ad-4085-9661-1d35eec95cee`: completed and playable; 4.01 seconds; 1280x720; media ready state 4 when opened

Current failed-card count: zero.

Each completed result detail view showed the exact submitted prompt:

> One softly glowing electric-cyan sphere rotates slowly against a deep-black empty background, static camera, minimal scene, cinematic soft bloom, 16:9.

The same prompt was used for both Yui submissions. The three completed-card count exactly matches the first x2 submission plus the later x1 submission. The UI did not expose per-card submit timestamps, so individual cards cannot be assigned definitively to one submit by timestamp; the count and exact prompt match provide strong attribution to the two Yui jobs.

## Correction of the earlier Failed observations

The earlier receipts accurately recorded what the UI showed approximately five seconds after each submit:

- first x2 submit: two cards then displayed `Failed`
- last x1 submit: one card then displayed `Failed`

Those were not final states. The same exact project now has zero Failed cards and three completed/playable cards carrying the exact Yui prompt. The evidence therefore supports an asynchronous/transient Flow state: the early `Failed` labels were premature, stale, or later replaced after backend completion.

The matching successful results are in `a22b5b61` itself. They are not successes found only in a different project.

This receipt supersedes the earlier receipts only as to final job outcome. The earlier receipts remain valid audit evidence of the transient UI state observed at that time.

## Visible Flow projects list

The read-only project-list scan found 12 visible project links.

- `a22b5b61-833d-4e62-857b-4a7030b93bfa`, listed as July 14 05:58, had a 1280x720 preview thumbnail and contains the three verified completed videos above.
- `ead24b58-8a20-466c-90a8-83a474ec9e34`, listed as July 14 11:22, also had an image thumbnail. A list thumbnail alone was not treated as proof of a completed video.
- the other ten visible project cards, including `3b2a3843-833c-429d-a6c6-36b9659351ae` and `94b7dd5c-5ff4-456e-b0d2-be1c5c3af162`, did not expose image thumbnails in the scanned DOM.

The Flow window was returned to the exact `a22b5b61` project after the list scan.

## Current credits

A live read-only Flow profile-dialog inspection showed:

- `24,838 Google Flow credits`

This is unchanged from Yui's immediate post-retry credit observation. Flow did not expose a per-job debit or refund transaction in the visible UI, so no per-result credit attribution is made.

## Corrected conclusion for Hwao

- total result cards in `a22b5b61`: 3
- completed/playable: 3
- failed now: 0
- all three match the exact Yui sphere prompt
- evidence strongly matches first x2 plus later x1
- earlier Failed reads were premature/transient, not final
- successes are in the intended `a22b5b61` project
- current credits: 24,838
- no read-only reconciliation action submitted, retried, edited, deleted, or scaled anything

Hwao should update the operational verdict from `last retry failed` to `both bounded submissions completed asynchronously: three playable outputs total` and should not infer an account failure from the transient early labels alone.

YUI_FLOW_READONLY_RECONCILIATION_CORRECTION_20260714
