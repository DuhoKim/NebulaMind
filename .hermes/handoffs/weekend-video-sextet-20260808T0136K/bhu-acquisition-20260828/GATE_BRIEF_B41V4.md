# Gate brief — B41 v4, the confirmation round on the census closer

CGATE_B41V3 refuted v3 on receipt provenance while confirming every substantive number, and
closed with: "Repair the B37 four-entry prior-receipt bindings, bind B43 to CGATE_B43_VERDICT.md
with its token, bind the B29 eleven-paper sample to its full-read verdict, and make the flag
predicates test the facts named in their labels. After those changes, the same 39/39, 1-of-2,
and 1-of-3 outputs can be confirmed."

v4 (`b41_census_coverage.py`, committed b9ee9d3b8) applies exactly those four repairs via a
per-entry receipt engine: every row = (set, receipt document, ALL-of requirements, verdict-token
checks); every member must be named in its receipt document — "entry N" in prose, or a per-entry
verdict-table row "| N |" for CGATE_B29, or the stated identity fragment "Dymnikova" for
CGATE_B39. B37's refresher chain is bound through the verdict's own refresher lines AND the
earlier full-source artifacts it names (CGATE_A5, CGATE_B17). B43's row binds both landed gate
verdicts (CGATE_B43 narrowed-confirm + AGATE_B43 confirm). Flag 6 binds the reading notes'
reclassification headline; flag 25 binds CGATE_B25's entry-25 ruling sentences. The COVERAGE
label separates the record-level conclusion from the script-level one. The two claim-level
lists are printed as two distinct labelled observations.

Note for the record: the engine's own first run caught a binding gap (B29 names entries in
table rows, not "entry N" prose) — the repair bound the stronger per-entry form.

**Your task:** run `python3 b41_census_coverage.py` from this directory, verify each of the four
demanded repairs against the artifacts it binds, hunt for any remaining predicate that validates
a string where its label claims a fact, and rule. If it survives, the lane reports the census
closed on: coverage 39/39; paper-tier miss rate 1 of 2; precision 1 of 3; claim-level
sensitivity not measured (with the two labelled observations).

**Verdict file:** `<A|C>GATE_B41V4_VERDICT.md`, first line a single token
(`B41V4_CONFIRMED` / `B41V4_REFUTED_<REASON>` / `B41V4_NARROWED_<REASON>`).
