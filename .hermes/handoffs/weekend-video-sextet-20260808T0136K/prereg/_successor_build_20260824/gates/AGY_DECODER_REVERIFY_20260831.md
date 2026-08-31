I have verified the repairs for the three prior defects:

1. **F1 (Non-JSON constants & non-finite floats):** The `parse_constant` lambda correctly raises `DecodeRefusal` directly inside `json.loads` for the exact tokens `NaN`, `Infinity`, and `-Infinity`, and the exception perfectly propagates out. For the `1e999` overflow (which natively parses to `inf` without triggering `parse_constant`), the new `math.isfinite(obj)` check in `_json_guard` catches the non-finite float node and refuses it. The added `allow_nan=False` in `json.dumps` ensures canonicalization acts as a final invariant check.
2. **F2 (Depth semantics):** The depth logic has been shifted from an entry-only check to a level-of-self check. A 9th-level container (like the exact `[[[[[[[[[]]]]]]]]]` counterexample) now enters the guard at `depth=8`, evaluates `8 + 1 > 8`, and is refused despite being empty. Meanwhile, the 8-level boundary case `[[[[[[[[]]]]]]]]` enters its deepest level at `depth=7`, passes the check, and since it has no children, is correctly accepted.
3. **F3 (Fixtures):** The controls have been completely rewritten to be sound. `EvilDict` instances are now explicitly fed to the shipped `_json_guard`, which rightfully rejects them via the new type-exact else branch (`type(obj) not in ...`). Furthermore, the positive output walk verifies that `decode_json` only yields pure, unpolluted data structures.

I systematically hunted for new defects in the changed regions, focusing on boundary limits, type bypassing, escape sequence decomposition, and exception propagation:
- The type-exact else branch safely rejects all subclasses (e.g., `EvilFloat`, `EvilInt`) since it tests exact identity. The tuple `(str, int, bool, type(None))` explicitly covers `bool`, which Python otherwise treats as a subclass of `int`.
- The NFC probe spelled as `"e\u0301".encode()` correctly simulates editor-proof bytecode. Python's parser evaluates the `\u0301` escape into a decomposed string literal, which is encoded to UTF-8 bytes and then correctly caught by the runtime `unicodedata.normalize("NFC", s) != s` check in `decode_string`.
- Exception propagation cleanly surfaces `DecodeRefusal` from deep inside the `json.loads` C-extension callback without getting swallowed by `JSONDecodeError`.

The decoder correctly enforces the bounds outlined in the draft, and the changed logic is airtight.

SEAT: AGY
VERSION: DEC-V2
VERDICT: SOUND
COUNT: 0
F-lines: NONE
