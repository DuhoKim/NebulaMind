# PHASE 0 — Can a calibrated BHU observable be DERIVED? (scoping only)

Hwao (director), 2026-08-18 21:35 KST. Authorized by Duho, verbatim: **"go ahead with phase 0"**
(21:30 KST, following "can you do the theoretical work yourself? leveraging our resources?").

Scope label, mandatory: black-hole-universe cosmology is Duho's personal side-interest, not a
NebulaMind research programme. Budget: **one evening.** Phase 0 decides whether any full
derivation night (Phase 1) is warranted — it performs NO full derivation itself.

## The question

Lana's derivation packet (`../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`,
SHA-256 `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516` — verify before use)
established that no calibrated, BHU-unique observable exists in print, and C15 of
`../bhu-closing-video-20260812T2322K/CLAIM_LINE_LEDGER_V11.md` states what reopening requires:
a published magnitude/scale/redshift derivation with a pass-or-fail range, or a fingerprint only
black-hole birth would leave. Phase 0 asks: **could WE derive one, and would it be worth it?**

## Three routes to scope — each ends in exactly one verdict

Per route: **PROCEED-TO-PHASE1** (a live, novel, tractable derivation exists),
**DEAD-ON-ARRIVAL** (existing constraints make any derived signal unobservable — itself a
publishable closure note), or **ALREADY-DONE** (the calculation exists in print — cite it).

**Route A — axis-model handedness amplitude.** The v2 axis source (arXiv:1910.10819v2; its
contents are characterized at packet §1.3) supplies rotating-frame relations but no amplitude.
The derivation would run: parent-spin/interior rotation Ω → present-day global vorticity →
tidal-torque modification → predicted galaxy-handedness asymmetry A(Ω) with scale/redshift
dependence. Scoping tasks: (1) find the current best published bound on global rotation
(Saadeh et al. 2016-class "How isotropic is the Universe?", Planck Bianchi VII_h limits — fetch
and quote the actual numbers); (2) order-of-magnitude only: does A(Ω_max) at the allowed bound
land above or below a plausible survey floor (use our own spin-parity design's statistical floor
as the yardstick — ~208k classifications; Lana knows the lane)? (3) novelty: has anyone published
a rotation→spin-handedness amplitude mapping already (vorticity/tidal-torque literature,
anisotropic cosmology constraints)?

**Route B — torsion-bounce (Popławski) observables.** The packet records Ω_S = −8.6×10⁻⁷⁰ from
the full text — prima facie DEAD-ON-ARRIVAL territory, but scope it honestly: enumerate every
quantitative observable statement in Popławski's published papers (expansion-history
contributions, parity violation, spin-spin coupling relics) and the local corpus's
torsion-bounce category (516 papers — `.hermes/handoffs/galaxy-evolution/corpus-*/`, plus
`../../bhu-track-20260805T2000K/BHU_LITERATURE_BASELINE.json`); for each: is any magnitude
derivable that current or near-future data could reach? Note the 2026 corpus entries on torsion
(e.g., neutron stars in Poincaré gauge gravity; torsion-fixed dark-matter mass) as adjacent but
instrument-bound.

**Route C — the birth fingerprint.** State crisply: is there ANY observable channel that a
parent-black-hole birth produces and a generic bounce does not? The packet already found "no
published observable that differs from generic bounce cosmology" — Phase 0 either overturns that
with a concrete candidate mechanism (cite the physics that could carry the imprint through the
bounce) or confirms it with the reason stated sharply (what the interior-FRW matching erases and
why). A well-argued "none is conceivable in current frameworks" CLOSES C15's second arm and is a
legitimate deliverable.

## Discipline

- **Kill criteria are written per route BEFORE evidence is weighed** — each seat states them at
  the top of its section.
- **Every number carries a fetched primary source, quoted verbatim** (the frozen-claim-from-
  memory failure already cost this project once). Allowed hosts: arXiv, ar5iv, ADS, journal
  abstract pages, Planck/NASA archives. **Never `portal.nersc.gov`** — the checksum harvest is
  live (window until 24:00 KST).
- Order-of-magnitude arithmetic only; a full derivation is Phase 1's job.
- Verdicts may disagree between seats — Kun adjudicates in the gate; do not pre-harmonize.
- Writes stay in THIS lane directory; temp files `_tmp_*` here.

## Seats and deliverables (parallel, then gate)

- **Lana** (`LANA_PHASE0_SCOPING.md`): physics scoping of all three routes — the derivation
  chains, kill criteria, order-of-magnitude feasibility, per-route verdict + confidence.
  Finish with `LANA_P0_DONE.md`, first line `LANA_P0_COMPLETE`.
- **Goru** (`GORU_PHASE0_PRIORART.md`): the novelty sweep — for each route, what already exists
  in print (rotation bounds; any rotation→handedness amplitude calculations; Popławski's stated
  observables and any published constraints on them; any claimed BHU-unique signature papers).
  Verdict per route: novel / partially-done (cite) / already-done (cite). Also query the local
  corpus JSONs. Finish with `GORU_P0_DONE.md`, first line `GORU_P0_COMPLETE`.
- **Kun** (after both): gate `KUN_PHASE0_GATE.md` — kill-criteria-first actually honored;
  every number source-quoted; novelty claims checked against Goru's sweep; verdicts follow from
  the evidence; no overclaim ("we could publish X" requires X's bar stated). First line
  `PASS_PHASE0_SCOPING` or a HOLD token + complete repair list.

Deliverable to Duho: a merged verdict — which routes (if any) earn Phase 1, and what Phase 1
would cost. It is fine — expected, even — if the answer is "none; here is the closure note."
