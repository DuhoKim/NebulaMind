# BS-2v Verification

BS-2c was not verified because `run/classp_candidates/BS-2c.json` does not exist. Verifying BS-2v alone.

1. Codex correctly determined that the frozen text mandates path B (a successor-layer receipt_strict entry). V134's §7 specifies that BS-2v has a normative registry pinned "as a `registry_digest` field bound in the slot schema". Furthermore, the text expressly prohibits emitting a slot receipt until it has a `SLOT_SCHEMA` entry. Because BS-2v was absent from the frozen v9 `SLOT_SCHEMA`, it required a successor-layer schema entry. The fix correctly provides this pinned entry in `receipt_strict.py` and emits the candidate strictly through it, genuinely resolving the absent-slot rule.
2. `run/classp_candidates/BS-2v.json` successfully passes its gate validation. The registry digest is correctly recomputed from the frozen §7.1, the converter SHA is recomputed on disk, and all fields are verified by `gates/bs2v_void_converter.py` without assertion errors. The superseded `BS-2v.REJECTED-UNBUILT-V1.json` remains untouched as the audit record.

SEAT: AGY
VERSION: BANK-VERIFY-V1
VERDICT: SOUND
COUNT: 0
F-lines: NONE
