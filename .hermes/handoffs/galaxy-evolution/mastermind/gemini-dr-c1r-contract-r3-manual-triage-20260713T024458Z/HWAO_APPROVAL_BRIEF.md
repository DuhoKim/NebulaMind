# Hwao approval relay — offline contract-r3 draft + manual-queue triage

Packet: `gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z`
Approval received from Duho: **“okay then go ahead with Hwao's rec for now”**
Approval time anchor: `2026-07-13T02:44:58Z`

## Approved objective

Execute the one next move recommended in `gemini-dr-c1r-chip-validator-repair-20260713T010203Z/HWAO_FINAL_SYNTHESIS.md`:

1. produce an **offline contract-r3 draft** that resolves the identified contract-design pressures;
2. produce an **offline triage packet for all 73 MANUAL_REVIEW_REQUIRED entries**;
3. stop before implementation, source verification, or any live canary.

## Required r3 decisions

The draft must make explicit, reviewable choices for:

- what counts as a simulation–observation comparison and where the rule applies in Section 1;
- whether the four-qualifier numeric rule applies to every quoted fraction, only population/statistical quantities, or another precisely stated class;
- which Section-2 citation channel is authoritative: in-Result citation, dedicated Citation cell, or an explicitly defined relation between them;
- ledger uniqueness, non-empty short names, index↔source integrity, and duplicate/near-duplicate handling;
- one GAP item per paragraph/logical unit;
- any validator/fixture consequences as a design matrix only, not implemented code.

The draft must not silently weaken fail-closed behavior. Every change needs: current rule, observed pressure, proposed r3 wording, rationale, positive example, negative example, and validator implication.

## Manual queue triage

Use the authoritative 73 entries in the repaired `readjudication/validator_result_v2.json`. Account for every entry exactly once and classify it into a bounded lane such as:

- `VERIFY_SOURCE_FIDELITY`
- `VERIFY_SCIENTIFIC_COMPARABILITY`
- `VERIFY_UNCERTAINTY_OR_SCOPE`
- `CONTRACT_R3_CHANGE`
- `IGNORE_FOR_THIS_CONTRACT_TEST`

You may refine names, but Hwao must pin definitions. “Ignore” means no further action in this contract test; it must never mean scientifically accepted. Preserve exact clause/code/source location and a short reason. Reconcile the category arithmetic to 73.

## Coordination request

Hwao remains coordinator. Please write `HWAO_PLAN.md` in this packet with:

- bounded phases and exact deliverables;
- lane assignments for Hwao/Lana/Goru/Kun/Tori;
- review/countersign requirements;
- stop conditions;
- final marker.

Do not ask any lane to start until the plan exists. Tori will relay assignments after reading it.

## Inputs of record

- repaired packet: `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/`
- current contract: sealed packet `../gemini-dr-revised-canary-20260712T045317Z/prompt/C1r.md`
- manual queue: repaired packet `readjudication/validator_result_v2.json`
- residue summary: repaired packet `readjudication/READJUDICATION_SUMMARY.json`
- Hwao recommendation: repaired packet `HWAO_FINAL_SYNTHESIS.md`
- T14 adjudication: repaired packet `HWAO_T14_DEVIATION_ADJUDICATION.md`
- Lana countersign: repaired packet `design/LANA_T14_COUNTERSIGN.md`

## Hard boundaries

- New packet only for all outputs.
- Prior repair packet and sealed C1r packet are immutable inputs.
- No live Gemini or other model web run.
- No browser/computer-use.
- No network research, provider API, source retrieval, or source-fidelity checking yet.
- No product DB/wiki/API write or publication.
- No dashboard/cockpit write.
- No deploy/restart.
- No git write, commit, push, merge, rebase, or reset.
- No cron/background job.
- No provider-account, quota, billing, OAuth, credential, or secret action.

## Completion boundary

This approved step ends with a reviewed contract-r3 draft, a complete 73-entry triage ledger, independent arithmetic/custody receipts, and Hwao’s final recommendation. A validator implementation or live one-simulation canary requires a separate explicit user gate.

TORI_RELAY_USER_APPROVAL_CONTRACT_R3_TRIAGE_20260713T024458Z
