# (iv-c) MAP WIDENING — CONFIRMED AS FILED — 2026-08-30 20:45 KST

**The principal's words, verbatim (direct message to Hwao's session, the third ruling of the
evening):**

> map widening confirmed as filed

**What this confirms — exactly the filed thing, nothing more.** The V93 filing
(`DECISIONS_FOR_DUHO.md`, "FILED (V93)"; filed under the coordinator's standing instruction
that any change to what the binding map may carry is filed, never taken silently): the
(iv-c) binding→key map's closed schema is WIDENED BY TWO FIELDS — the decision's
`(boot_epoch, monotonic_reading)` clock pair — because §3b's decide-within-D law needs
per-decision clock evidence and widening the RULED access-log event schema is not
authorised; the map carries the clock instead (CODEX-V92 F1). Non-χ by construction
(bounded decimals, quantized to `g`), and filed as reversible.

**Status change.** The widening was live-but-awaiting-confirmation through nineteen builds;
it is now a CONFIRMED part of the map's closed schema: `(request_key, decision
chain_position, decision event_digest, decision boot_epoch, decision monotonic_reading,
signature)`. The "reversible, awaiting confirmation" posture ends; reversal would now be a
new ruling, not a lapse.

**What this does NOT touch.** The ruled access-log event schema (untouched, as the filing
promised); the ruled refusal vocabulary; v9 (`6a9abbbd…`); the sealed/continuation
partition; the map's signature discipline.

**Fold plan (V113 — V112 is sha-pinned in a live round):** draft (iv-c) "the widening is
FILED with the coordinator per the standing instruction, reversible" → CONFIRMED with this
record cited; spec §3b "the widening is FILED with the coordinator" → CONFIRMED; the
DECISIONS_FOR_DUHO.md flag updated (this commit); superseded phrasing quoted dead per the
sweep discipline.

**Recorded also in the track's human-direction history** (direction #11 in
`spin-parity_history.json`).
