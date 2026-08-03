# YUI one bounded Flow job receipt

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Actor: Yui, Flow operator on Mac Studio
Authorization: `receipts/DUHO_RESUME_FLOW_TARGET.md`
Authorization SHA-256: `a4df4f18b54868ff2d58887932b06876ec5a2f2b33c6550dc229a0c14d4bf8ed`
Authorization marker: `DUHO_RESUME_FLOW_TARGET_20260714`

## Resume

- epoch-91 emergency freeze cleared under Duho authorization
- broker resume ledger epoch: `93`
- resume entry SHA-256: `5226e4d96dac6f49c208ff6c84ab44e6ba0582ab879f8201f85cbab57a10ca5d`
- post-reset broker PID: `88462`
- ledger after reset: `VERIFY_OK`

## Current Flow target inspection

Yui did not reuse either prior project id. A fresh read-only page probe after Duho's restore found:

- exact Flow project: `a22b5b61-833d-4e62-857b-4a7030b93bfa`
- window/tab: `1/1`
- title: `Google Flow - 7월 14일 오후 05:58`
- valid visible Flow composer: yes
- visible Create control: yes
- page challenge: false
- page challenge signals: none
- visible on-page dialogs: zero
- configuration: `Video · 8s`, 16:9, `x2`

The detector was scoped only to the Flow page URL/DOM/on-page modals. The Chrome toolbar profile badge was not considered.

## Leases and serialized submission

Fresh leases:

- exact target: `L00019`, broker epoch `19`, target `flow-project-a22b5b61`
- Studio desktop-control: `L00020`, broker epoch `20`
- Studio focus: `L00021`, broker epoch `21`
- bounded prompt clipboard: `L00022`, broker epoch `22`, released after paste
- global account-submission: `L00023`, broker epoch `23`, released immediately after the submit moment

The exact project id and page-challenge state were re-verified immediately before prompt input and immediately before submission. The account-submission action was journaled at ledger epoch `107`; the lease was released at ledger epoch `108`.

## Single bounded job

One and only one Return-key submit was dispatched at `2026-07-14T09:14:01Z` with the non-secret bounded prompt:

> One softly glowing electric-cyan sphere rotates slowly against a deep-black empty background, static camera, minimal scene, cinematic soft bloom, 16:9.

Post-submit evidence:

- composer returned to the 27-character placeholder (`What do you want to create?`)
- current project remained `a22b5b61-833d-4e62-857b-4a7030b93bfa`
- page challenge remained false
- visible on-page dialogs remained zero
- Flow created two result cards because the UI was configured for `x2`
- both result cards reported `Failed`
- visible videos: zero
- total video elements: zero
- no failure reason was exposed in the visible card DOM

This is a completed first-pass failure receipt, not a successful video result. No retry and no batch scaling were performed. Credit debit/refund state was not inferred from the failure cards.

## Teardown

- account-submission lease released
- exact target, desktop-control, focus, and clipboard leases released
- live Yui leases after teardown: zero
- broker frozen: false
- final ledger verification before receipt append: `VERIFY_OK OK (113 entries)`

Hwao must review this receipt before authorizing any retry or scale-up.

YUI_FLOW_ONE_BOUNDED_JOB_FAILED_20260714T091401Z
