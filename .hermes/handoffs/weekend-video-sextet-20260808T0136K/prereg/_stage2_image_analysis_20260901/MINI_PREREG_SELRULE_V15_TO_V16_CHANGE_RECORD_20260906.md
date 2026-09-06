# CHANGE RECORD — option A selection rule V15 (SIGNED) → V16 DRAFT — prospective sampling amendment — 2026-09-06 11:17 KST

**Authority to draft:** Duho, via codex voice, confirmed in chat 2026-09-06 11:08 KST ("yes, that was me via Codex voice"; the voice instruction, recorded by Codex at 11:05:26 KST: "Amend the plan... and make it... run as soon as possible"); dispatched by Blanc 11:06 KST with hard constraints, restated 11:08 and 11:11. **Not approved. Not signed. V15 as signed (fdd9eedd…, 2026-09-06T00:04:07Z) remains operative; no beacon read under this draft.**

**Target:** `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V16_20260906.md` SHA-256 `fe1487bd1be7dcd3b27798727d2d39f2b5f54d21d74faffdaaaa9f059450f488` (= preimage; signature lines blank). **Disclosed diff:** `V15_TO_V16.diff` SHA-256 `62107857ea7ffd456a1a057e620d59f298d5a40ebd5c50064ea6cca959cc2ce0` — 19 changed lines: title; the version paragraph; §3b order step (1) (approval channel) and the new (1a) (order made visible); the evidence-bytes sentence; the outcomes sentence; the LIMIT (i) sentence; the new §3c; three pin substitutions in E3; the §7 builder command; the §10 cost line; one sentence at line 59. Nothing else moved.

## Blanc's constraints, and where each is met
| constraint | where |
|---|---|
| the already-public 00:15Z pulse INELIGIBLE, excluded by name | code: `EXCLUDED_T_PULSE = ("2026-09-06T00:15:00Z",)` → `T-PULSE-EXCLUDED` in collect and verdict; text: §3b (1a) names NIST pulse 1928801 and drand round 6440756 |
| do not shorten a constant and inherit an existing pulse; re-derive T_pulse from the NEW approval time by the same formula | `pulse_time` unchanged (fixture asserts equality with V15's); T_sign := approval UTC; `MIN_T_SIGN = 2026-09-06T02:20:00Z` refuses any earlier T_sign → `T-SIGN-PREDATES-AMENDMENT`; the constant that changed (`FALLBACK_AFTER_H` 24 → 0) cannot reach an old pulse because the old T_sign is refused |
| preserve V15 and the RETRY evidence | V15 file and `SIGNATURE_RECORD_SELRULE_V15_20260906.md` untouched; RETRY record 1c1d9d4b… retained and cited in V16's version paragraph; supersession is prospective |
| state what expediting costs | §3c: NIST primary given up in practice (10 minutes instead of 24 h); provenance rests on ≥2-of-4 relay agreement without BLS verification; a signed-then-superseded V15 row in the register |
| a reader must SEE request → authorisation → approval → pulse | §3c timeline + code refusals; this record's timeline below |
| text must describe the channel that will actually be used (11:15) | §3b (1) rewritten to the adopted codex-conversation procedure with Blanc's digest check and its stated limits |

## Code first
| file | SHA-256 | run |
|---|---|---|
| `_optionA_dev/beacon_v2/beacon_record_expedited.py` (17 lines differ from the pinned `beacon_record.py` 023c4d7d…) | f420521a838412b64e61ffc2204b68a3edb017101713e38a3fc201ab530b8fc7 | — |
| `_optionA_dev/beacon_v2/test_beacon_record_expedited.py` | 76a98873188612771fb0c9376997f34aa1822638344bcef1e777239e70b8f3ac | Ran 10 tests in 0.024s  OK  |
| `_optionA_dev/corpus_identity/build_corpus_identity_v16.py` (4 lines differ from `build_corpus_identity.py` 3090af77…) | 4d9cc7a79c956a3ef61b67d25d57e1be624bab0d5a66cf3350ddeac7947b0ca2 | — |
| `_optionA_dev/corpus_identity/test_build_corpus_identity_v16.py` | 30483e2a3035242e10f786e1ab1e3edc10a847d1fd42c50b9a622467c7560dca | Ran 3 tests in 0.015s  OK  |
| V15's `test_beacon_v2.py` (unchanged) | c8689eef… | OK |
Fail-on-old assertions: the same expedited record at T_pulse + 1 min → V16 verdict ACCEPT-DRAND, V15 verdict RETRY; V15's collect does not even gather drand then; the V16 builder accepts where the V15 builder refuses `BEACON-NOT-ACCEPTED (RETRY)`. NIST stays binding when authenticable and VOIDs drand at build time (unchanged). Every REFUSE token the expedited source can emit is exercised.

## Defect recorded (Blanc 11:15 KST)
The V16 file was created as an unedited copy of V15 at 11:13 KST and was byte-identical to the signed V15 (same digest fdd9eedd…) until the edits at 11:16 KST. Blanc caught it by `cmp` before any approval step. It was never presented for approval. Option (a) taken: real edits made; digest now fe1487bd1be7dcd3b27798727d2d39f2b5f54d21d74faffdaaaa9f059450f488. Lesson filed: a successor file is created and edited in one step, never staged under its name.

## Timeline (KST)
V15 signed 09:04 (T_sign 00:04:07Z) → RETRY beacon read 10:56 (T_pulse 00:15Z public) → finding 11:01 → Codex-recorded voice instruction 11:05 → Blanc dispatch 11:06 → Duho's chat confirmation 11:08 → approval procedure adopted 11:11 → code + fixtures 11:12–11:14 → V16 copy 11:13 (identical, defect) → V16 edits 11:16 → this record 2026-09-06 11:17 KST → two-seat gate → approval on final bytes (T_sign') → T_pulse' = first whole minute ≥ T_sign' + 600 s → collect → identity.
