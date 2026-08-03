# ROUND 1 EXECUTION BRIEF — Tori lead, WonE writer assistant

Window: start immediately; overnight loop hard-stops at 10:00 KST 2026-07-15.
Authority: Duho explicitly assigned Tori/Goru as workers. Hwao coordinates freeze policy and hard stop only.

## Assignment

- Tori: integrate papers 01–04 and independently validate all nine round-1 outputs.
- WonE: integrate papers 05–09 only.
- Goru does not edit TeX; after round-1 custody, Goru runs serialized Deep Research review and gap re-research.
- Garu watches only.

## Inputs

- Drafts: `integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/NN_*/aastex/*_integrated.tex`
- Reference packets: `dr-research-lane-9-20260714/packets/paper_NN_*_dr_packet.md`

## Outputs

- Candidate TeX only: `dr-revised-20260714/round1/paper_NN_r1.tex`
- Per-paper source receipts: `dr-revised-20260714/round1/receipts/paper_NN_sources.json`
- Per-paper revision notes: `dr-revised-20260714/round1/receipts/paper_NN_revision.md`

## Non-negotiable revision contract

1. Preserve every original draft line byte-for-byte and in the same order. Round 1 is additive only: insert literature/context paragraphs and bibliography entries around the unchanged original. This mechanically preserves every measured SDSS invariant, table value, figure caption, claim boundary, and selection disclosure exactly.
2. Real data only. Do not introduce a new NebulaMind measurement, mock/synthetic/toy/placeholder value, invented sample size, or invented source identifier.
3. Association, denominator, and proxy wording stays non-causal. Literature is interpretation support, caveat, or future-observable motivation; it does not become a measured project result.
4. Add a source to prose only with a real `\citep{...}` call and an inline `\bibitem` whose DOI, arXiv ID, ADS bibcode, or stable journal metadata can be checked independently. Prefer 2–4 strong sources per paper. Skip any packet source with inconsistent year/identifier/title, future/unsettled metadata, aggregator-only evidence, or unclear fit.
5. Cite only sources present in that paper's DR packet. Do not copy a source across papers unless it independently appears in both packets.
6. Log every integrated source with citation key, role, identifier, and verification basis. Log skipped candidates with a concise reason; never force a quota.
7. Keep all original bibliography entries. Insert new `\bibitem` entries before `\end{thebibliography}`.
8. Do not edit integrated source drafts, any published/live root, DB/API/wiki/trust state, autopilot lanes, deployment/runtime, git state, billing/auth/account settings, or browser conversations. No commit/push/publish.
9. Do not append the live broker ledger. Round-1 TeX work is file-local and browser-free.

## Per-paper receipt minimum

JSON fields: `paper_id`, `round`, `source_tex`, `source_tex_sha256`, `source_packet`, `source_packet_sha256`, `output_tex`, `output_tex_sha256`, `original_lines_preserved_in_order`, `added_sources[]`, `skipped_sources[]`, `association_not_causal`, `real_data_only`, `drafts_only`, `generated_utc`.

Each revision note must summarize the inserted section, sources added/skipped, and explicitly state that every original line remains in order and no original measurement text changed.

## Done markers

WonE finishes only when papers 05–09 plus ten receipts exist and ends its pane report with:

`WONE_ROUND1_05_09_COMPLETE`

Tori accepts round 1 only after independent hash/subsequence/citation/bibliography/receipt validation of all nine outputs.
