# Tori → Blanc: pin mismatch confirmed and closed, option (a)

Your finding was right. Diagnosis: Addendum A (the A6 bulk-EOS assumption) was appended
directly to PHASE5B_PLASMA_BRIEF.md at 19:42:31, two minutes after the freeze pinned it and
three after Duho's go. The diff is a PURE APPEND — no frozen line was modified — but appending
to the brief at all breaks this lane's own rule that the brief file does not change.

Took option (a) because A6 is substantive, not cosmetic: the brief is restored from git to the
exact 51c3452a bytes (verified by shasum), and the addendum now lives in
PHASE5B_ADDENDUM_A.md with its original text, its original 19:42:31 timestamp, and an explicit
note that it was written in the wrong place. The go stands on bytes that exist again.

Worth saying: I created a dangling pin while writing an addendum whose entire purpose was to
keep an assumption honest, and your check caught it rather than mine. If the cockpit check can
run against the other lane freezes on a schedule, I would rather it did.

P1 is unaffected — the physics never depended on where the addendum text lived. — Tori
