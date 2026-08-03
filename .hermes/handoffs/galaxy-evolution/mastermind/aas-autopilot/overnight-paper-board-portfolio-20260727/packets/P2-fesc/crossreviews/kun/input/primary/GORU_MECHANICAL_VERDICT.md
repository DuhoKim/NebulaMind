# Goru Mechanical Verdict

**Recommended Relationship:** `CANONICAL_PLUS_SUPPORTING`

## Justification
The `fesc002` pipeline run serves as the foundational methodological demonstration (a single z~6 calculation showing the photon-budget shortfall). The frontier manuscript takes this methodology and systematically scales it to a 232-point landscape mapping to explore the parameter space fully (SFRD normalization, clumping factor, ionizing efficiency). The frontier manuscript is the canonical synthesis, and `fesc002` is the supporting pipeline method.

## Mechanical Realities & Gaps
- The `fesc002` run claims to be literature-grounded on "6 papers, 5 passages", yet the citation entailment gate explicitly checked 0 claims.
- The 6 papers in `lit_refs` do not perfectly match the 5 papers in `lit_reflist` (Lewis20 is missing from the list).
- Crucial proxy calibration sources explicitly listed in the provenance (Chisholm+22, Flury+22, Simmonds+24) are entirely absent from the `lit_refs` and bypassed the citation entailment checks.
- Simmonds+24 is mechanically cross-wired in the novelty gate with two different 2024 JADES papers.
- Therefore, the citation-entailment gap is mechanically real: the true foundational proxies for f_esc (LzLCS and JADES calibrations) have not been mechanically verified by the entailment gate.
