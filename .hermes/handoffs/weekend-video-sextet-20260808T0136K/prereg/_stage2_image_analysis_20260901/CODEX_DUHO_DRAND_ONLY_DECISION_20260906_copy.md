# Duho's decision: Hwao uses drand as the sole randomness source

Recorded by Codex from the active voice conversation on 2026-09-06 around 19:02 KST.

## Decision presented
Codex recommended using drand alone: a preselected future round, verification of authenticity, removal of choice between NIST and drand and of the fixed 24-hour fallback wait. Codex explicitly explained the trade-off: if drand is unavailable, wait rather than change to another source. Codex also stated that implementation and review were still being completed, and asked whether to choose this direction.

## User's exact reply
"해" ("Do it.")

## Authorized scope
The user has now CHOSEN the drand-only direction and accepted the availability trade-off above. This resolves the source-selection design choice. Please record and relay it to Hwao; complete the corresponding amendment, implementation, meaningful tests and independent reviews as already authorized. Do not ask the user to choose this same source direction again.

Preserve the prospectively fixed future-round rule, actual signature verification and pinned chain identity, sample sizes, exclusions, custody, blindness and the one-shot holdout. This is a prospective decision: do not use an already observed historical round from the exhibit as the study seed.

The user was not shown an exact finished amendment fingerprint in this exchange, and Codex did not say that the pending review had passed. Therefore this record is the source-direction decision, not a fabricated final-document signature, review verdict, sample draw, label opening or census restart approval. Finish the authorized work and bind any remaining final-version adoption through the agreed conversational process only when a concrete reviewed version exists.

No Tori design choice was approved by this reply; that discussion follows separately.

Attribution: only the quoted Korean reply is verbatim. The question context and scope above are Codex's faithful record and interpretation.
