# CANONICAL DECODER VERIFICATION

Adversarial review of `canonical_decoder.py` against the draft specification.

## DEFECTS FOUND

1. **Grammar Exactness / JSON Canonicality**: The python `json.loads` decoder allows non-JSON values `NaN`, `Infinity`, and `-Infinity` by default. Because `json.dumps` round-trips these string representations perfectly, the canonicality check `canon == s` evaluates to True. This causes the decoder to accept inputs that are explicitly outside the JSON grammar.
2. **Bounds (Off-by-One)**: The `JSON depth ≤ 8` constraint contains an off-by-one logic error. The traversal checks `if depth > MAX_JSON_DEPTH` (where max is 8). An empty list or dict at `depth=8` (the 9th level of nesting, e.g., `[[[[[[[[[]]]]]]]]]`) will be accepted because `8 > 8` is False, and its lack of children means `depth=9` is never evaluated. 
3. **Vacuous Fixtures**: The `EvilDict` fixture intended to test the refusal of a "top-level subclass" is entirely vacuous. It simply evaluates `type(EvilDict()) is dict` natively in Python (which returns False) and succeeds. It never actually passes a subclass to the decoder logic, nor could it, as the decoder strictly operates on `bytes`.

SEAT: AGY
VERSION: DEC-V1
VERDICT: DEFECTIVE
COUNT: 3
F-lines: 120, 139, 225
