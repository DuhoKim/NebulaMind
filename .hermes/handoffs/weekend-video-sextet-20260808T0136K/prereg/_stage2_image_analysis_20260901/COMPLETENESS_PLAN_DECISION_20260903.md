# COMPLETENESS GATE — PLAN DECISION (Hwao, 2026-09-03 01:0x KST, under Duho's overnight ruling "Hwao a")

**Decision:** the TAP route in `completeness_gate/PLAN.md` is APPROVED as the definitive
no-magnitude crossmatch source (NOIRLab Astro Data Lab, complete DR10-south Tractor relation,
all-candidate 1.0-arcsec cone JOIN on uploaded GZ1 chunks, no magnitude/flux/quality predicate,
client-side binary64 recomputation authoritative at exactly 1.0 arcsec). The local per-brick
Tractor sweep stays the fallback if the service cannot prove uncapped, untruncated results.

**Why not tonight's run yet:** the draft's real backend is a stub (only the synthetic source is
exercised). Order of work: (1) codex implements the TAP backend with a metadata-only probe and a
single-chunk live dry run; (2) agy referees the whole gate to PINNABLE; (3) the §7.11 seal gate
runs at acquisition completion (~07:00 KST); (4) the definitive crossmatch starts, ONE worker,
polite pacing, expected 12–30 wall-clock hours, resumable, receipts per chunk. It will NOT finish
overnight; its receipt lands during 2026-09-03/04. Reported in the morning report via Blanc.

**Boundaries unchanged:** catalogue-only; no pixel opened, rendered, or measured; V9 signature
pending relay; audio hold; text reports.
