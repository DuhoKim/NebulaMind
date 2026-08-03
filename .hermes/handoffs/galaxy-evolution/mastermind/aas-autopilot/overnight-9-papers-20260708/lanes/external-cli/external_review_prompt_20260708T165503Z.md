# External read-only review request — NebulaMind overnight 9-paper swarm

You are an external read-only reviewer. You may use read-only file inspection commands under the read-only sandbox solely to inspect the named local files (for example: `python3 -c` reads, `sed -n`, `wc`, or equivalent). Do not write files. Do not modify the repo. Do not use network/web. Do not access secrets. Do not use git write operations. Return the critique on stdout only.

## Scope
Critique these three active Galaxy Evolution AAS pilot revision drafts, which have not yet received a successful external CLI critique in this lane:

1. M1 RP-2 — SDSS density proxy for environmental quenching
   - `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/revision-drafts/m1_rp2_environment_quenching/m1_rp2_environment_quenching_lana_revision.tex`
   - `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/revision-drafts/m1_rp2_environment_quenching/CHANGES.md`
2. M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up
   - `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/revision-drafts/m1_rp3_maintenance_heating/m1_rp3_maintenance_heating_lana_revision.tex`
   - `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/revision-drafts/m1_rp3_maintenance_heating/CHANGES.md`
3. M2 P1 — high-excitation optical-AGN denominator for outflow escape/recycling tests
   - `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/revision-drafts/m2_p1_outflow_escape_recycling/m2_p1_outflow_escape_recycling_lana_revision.tex`
   - `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/lana/revision-drafts/m2_p1_outflow_escape_recycling/CHANGES.md`

Helpful context:
- `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/OVERNIGHT_BRIEF.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/SWARM_BOARD.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_source_packet_20260708T143233Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/goru/ticks/GORU_TICK_20260708T141459Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/hwao/HWAO_DIRECTOR_TICK_20260708T160831Z.md`

## Return format
For each paper, cover:
- structure/paper-readiness issues;
- missing evidence or citation classes;
- overclaiming or scope leakage;
- reproducibility gaps (methods, denominators, thresholds, uncertainty conventions, figure/table portability);
- concrete publish-quality next steps.

Then provide a cross-paper prioritized action list. Keep the review grounded in the local files; if a fact is not in the files, label it as a gap rather than inventing it.
