# Method

Marker: OVERNIGHT_PAPER_BOARD_PACKET_B_KUN_METHOD_V1

I treated the run JSON `gates.citation_entailment.all` arrays as the authoritative list of checked citations. I did not add citations from draft text, reference lists, PDFs, public sources, databases, or browser retrieval.

## Source Stability

Before producing deliverables, I ran SHA256 verification from the immutable Lab root against `baseline/INPUT_SHA256.txt`. All 38 baseline entries returned `OK`. This satisfied the packet's source-drift stop rule.

## Run Scope

I searched the top-level baseline run JSON files for `citation_entailment`, `lit_reflist`, and `lit_refs`. The only runs with citation gates were:

- `gated-e2e-demo`
- `gated-halt-demo`
- `fesc002`

I also checked the scoped `expected_value` gates and found verdicts of `TENSION`, `INSUFFICIENT`, and `TENSION`, respectively; none was `CONTRADICTS`.

## One-to-One Matching Rule

For each object in `gates.citation_entailment.all`, I copied:

- `key` as `citation_key`
- `sentence` exactly as stored in JSON, including truncation where present
- `supported` as `gate_verdict` (`true` -> `supported`; `false` -> `unsupported`)
- `reason` exactly as stored in JSON for the CSV, preserving embedded newlines

For the Markdown map, embedded gate-reason newlines are rendered as `<br>` only to keep the table readable; the CSV preserves the literal newline text.

## Kun Adjudication Rule

`kun_adjudication` is a mechanical agreement/disagreement against the stored gate row, not an external literature review. I marked `agree` when the row's `supported` boolean and the row's `reason` were internally consistent enough to reproduce the gate verdict for that `key`.

What counted as supported:

- The stored gate row had `supported: true`.
- The stored reason named or semantically matched the citation key's claim.

What counted as unsupported:

- The stored gate row had `supported: false`.
- The stored reason stated that the compared passage did not mention the required author/work/topic or did not cover the cited sentence content.

For `fesc002`, `checked: 0`, `all: []`, and `unsupported: []` mean no citations were checked. I therefore did not create checked-and-supported rows for `fesc002`; instead I recorded the run's references as not checked by the citation gate.

## Corrected Candidate Rule

For each unsupported citation, I chose exactly one packet-approved fix label. I used only fix label `(b) remove the unsupported citation entirely` for all three unsupported rows. The candidate text removes the unsupported citation and the immediately dependent clause where needed so no uncited scientific claim remains. I introduced no citation not already present in the run's `lit_reflist`/`lit_refs`, introduced no new numerical value, and did not weaken or delete any caveat.

