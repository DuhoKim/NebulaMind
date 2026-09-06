# OPTION A — RUN RECORD (signed V15 fdd9eedd…, T_sign 2026-09-06T00:04:07Z) — opened 2026-09-06 10:55 KST

**Authorisation (Duho via Blanc, 10:54 KST / 01:54:03Z), verbatim:** "start the Tier-C run". Execute the signed V15 in the order the signed text prescribes, beginning at the beacon read.

## Conditions re-asserted before step 1 (all satisfied)
| condition | evidence |
|---|---|
| custody boundary VERIFIED | `CUSTODY_BOUNDARY_VERIFIED_RECEIPT_20260906.md` 09:31 KST — kernel-enforced 700 on home and child, duhokim read refused, exhibited verbatim |
| branch protection WITNESSED | `BRANCH_PROTECTION_WITNESS_RECEIPT_20260906.md/.json` 10:46 KST — non-fast-forward push REJECTED (GH006), tip unchanged; Duho enabled it via the codex CLI, confirmed in chat 10:52; API state re-read by Hwao 01:55Z |
| beacon source RULED (a) | Duho "a" 09:33 KST — rule as signed: NIST fetched, REFUSED if it does not authenticate, RETRY never a seed, drand from T_pulse + 24 h |
| engine pinned | codex-cli 0.153.4, gpt-6-astra, stamped `<report>.engine` in every dispatch (`ENGINE_CHANGE_RECORD_20260906.md`) |

## Blanc's binding conditions (held to)
1. The signed TEXT governs; where text and any script disagree, STOP and file — never fit the text to the script. 2. STOP AND TELL BLANC before the development draw opens labels. 3. Exactly ONE holdout attempt. 4. Abort conditions bind: file, stop, tell — no self-judging. 5. No frozen pixel of the 12,217 until the holdout has PASSED and the pass is recorded.

## Sequence re-checked against the now-true state (from `OPTION_A_RUN_SEQUENCE_AFTER_BRANCH_PROTECTION_20260906.md`), with what each step makes UNRECOVERABLE
| step | status / timing | command (exact) | what becomes unrecoverable |
|---|---|---|---|
| 0 branch protection | DONE 10:46 (receipt above) — the sequence's step 0 is superseded by the filed receipt; no further probe | — | nothing |
| 1 beacon read | NOW (T_pulse passed at 00:15Z; now < T_pulse + 24 h ⇒ signed text: RETRY, never a seed). Re-collect at **2026-09-07T00:15:00Z = 09:15 KST Monday** for the fallback | `python3 _optionA_dev/beacon_v2/beacon_record.py collect --t-sign 2026-09-06T00:04:07Z --rule-sha256 fdd9eedd… --signature-statement SIGNATURE_RECORD_SELRULE_V15_20260906.md --out _optionA_dev/beacon_record_T_pulse_20260906T0015Z_<utc>.json` then `verify` | nothing is spent; the record fixes the chronology publicly (a passed T_pulse with a filed record) |
| 2 corpus identity + seal + witness | after an ACCEPT record; prerequisite: seal-append helper (gap 1) written, tested, digest filed | builder command as filed | the split is FIXED and published: which 400 / 200 / 2,000 identities are development vs fresh can never be redrawn under this signature |
| 3 dev bricks: manifest → seal → fetch → render | after step 2 witness; prerequisite: manifest-driven adapter (gap 2) | as filed | the 600 development galaxies' PIXELS enter the lane — those objects are spent for development forever and can never serve as validation |
| — STOP AND TELL BLANC — | before step 4 | — | (Blanc's condition 2: labels about to open) |
| 4 tune | after Blanc's word | driver `tune` as filed | labels of the 400 are OPENED; every later rule change is post hoc; the tuning winner is fixed and sealed |
| 5 holdout, ONCE | after tuning-freeze witness | driver `holdout` as filed | the single attempt is consumed: FAIL closes option A for good; PASS fixes the candidate identity for good |
| 6 fresh fetch (Duho as nmcustody) + lift | only on a recorded PASS | custody addendum | the 2,000 fresh pixels leave the never-seen state once lifted; the frozen 12,217 are still untouched until V36/pipeline amendment govern them |

## Journal (append-only, KST)
