Verified the local seat state before ruling: /Users/duhokim/gates/ contains only AGY_REPLAY_VERIFY_20260831.md — a sibling seat report (RPH-V1 on replay_harness.py, DEFECTIVE/5). The decoder artifact is not resident on this machine, so this ruling binds the ladder record plus the DEC-V2 verdict, per exact-regate discipline. Ruling:

KGATE_DECODER: PIN-READY

1. Scope check: the only gate file on this seat is the sibling RPH-V1 DEFECTIVE report on replay_harness.py; per exact-regate rule, sibling-order reads do not bind this seat. Decoder judged solely on its brief + DEC-V2.
2. F1 closure is layered, not pointwise: parse_constant refuses the three tokens, _json_guard's non-finite check closes the 1e999 overflow path that bypasses parse_constant, and allow_nan=False canonicalization is an invariant. Controls cover NaN, Infinity, -Infinity, [1e999]. Non-vacuous.
3. F2 closure has the right control shape: depth redefined at the container itself, refused empty-or-not; controls pair the exact 9-level empty counterexample (refuse) with the 8-level boundary (accept). The acceptance side is what makes the refusal meaningful.
4. F3 closure eliminates the vacuity class by construction: foreign nodes (top-level and nested subclass) are fed through the ONE shipped _json_guard, plus a positive type-exact walk of real decode_json output. No native type() theater remains.
5. DEC-V2 is an independent adversarial seat that ran real probes and hunted the actual residual loci of the repairs (bool-vs-int identity, runtime escape decomposition, C-extension callback exception propagation). SOUND / 0 stands as the named gate artifact.
6. The NFC-literal erasure catch (ASCII escape after Write normalization) is evidence the fixtures themselves are alive, not decorative.
7. Residues (a)-(c) are declared design lanes, each consistent with the SS6.1 grammar as stated: decimal-string vs JSON-number lane split; NFC on decoded strings with JSON byte-identity via canon==s; pure bytes->value, no I/O, single file, stdlib+numpy. None is an undisclosed defect.
8. Reject-by-default posture (unknown fields, out-of-grammar bytes, length mismatch, trailing bytes) plus decoder-definition-as-grammar is the correct epistemic order for a class-P prereg pin.
9. Seat caveat, stated for the record: the decoder bytes are not local to this machine, so no independent sha256 was computed here; freeze mechanics are the backstop.
10. Binding condition of the pin (semantics, not a hold): the SS11 class-P slot must capture sha256 of the exact v2 bytes DEC-V2 verified; any post-verdict edit re-opens this gate automatically via hash mismatch.
11. No unblocking condition outstanding.
