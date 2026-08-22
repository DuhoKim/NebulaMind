# Published-only BHU bibliography — the corrected base layer

Hwao, 2026-08-19 15:44 KST. Duho, verbatim: **"it doesn't look like a published paper, is it? can
you also make a list of published paper that has anything to do with BHU cosmology? and start
from there, not a single unpublished paper?"**

Scope label: BHU is Duho's personal side-interest, not a NebulaMind research programme.

## The deliverable

`BHU_PUBLISHED_BIBLIOGRAPHY.md` — every peer-reviewed, journal-published paper materially about
black-hole-universe cosmology (universe-inside-a-black-hole, baby universes via black holes,
CNS, torsion-bounce parentage, interior-cosmology matchings). Per paper:

1. Full citation + DOI + journal, **publication status VERIFIED from the journal/DOI page or
   ADS, never from arXiv metadata alone**;
2. One-sentence core claim;
3. Testability class: CALIBRATED-FALSIFIER (states a number+threshold) / QUALITATIVE-DIRECTIONAL
   / CONSISTENCY-ONLY / PROSPECT (points at other instruments);
4. Status in our record (already adjudicated: BLR 2008 = falsified via limb 2; already
   characterized in the packet; new to us);
5. Audit-worthiness for a future strict-model night, with one line of reasoning.

Ranked closing section: the 3–5 strongest published targets to "start from", each with what a
strict treatment would test. Explicitly EXCLUDE preprint-only/pop-ph items into a separate
"context, not base" appendix (arXiv:1910.10819 goes there, with the Phase 1 audit cross-ref).

## Sources to mine

- The derivation packet `../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` §1.1–1.6 (b244ea0a,
  verify) — Pathria 1972 Nature; Good 1972; Smolin 1992 CQG + Life of the Cosmos; BLR 2008 PRL;
  Popławski 2010 PLB (+ his PRD/other published series); Frolov–Markov–Mukhanov 1989/90;
  Easson–Brandenberger 2001 JHEP; Dymnikova; the 2025 Nucl. Phys. B baby-universe paper;
  Khakshournia 2010; Stuckey-class pedagogy if published.
- The local corpus: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/bhu-track-20260805T2000K/BHU_LITERATURE_BASELINE.json`
  (core-bhu: 59 entries) — many carry journal refs; Gaztañaga's series and Roupas 2022 from the
  Phase 0 sweep.
- Fresh ADS/arXiv/journal searches to catch anything the packet's own coverage caveat admits
  missing. Literature hosts only; never portal.nersc.gov.

## Seats

- **Goru** (`GORU_BIBLIO_SWEEP.md` + `GORU_BIB_DONE.md`/`GORU_BIB_COMPLETE`): the candidate
  sweep — everything claiming BHU relevance with its claimed venue; cast wide, verify nothing.
- **Lana-2** (fresh seat; `BHU_PUBLISHED_BIBLIOGRAPHY.md` + `LANA2_BIB_DONE.md`/`LANA2_BIB_COMPLETE`):
  verification + classification + ranking. Every "published" verdict carries the DOI resolved or
  the ADS bibcode with journal field, checked this session. A paper that cannot be verified
  published goes to the appendix with the reason.
- **Miru** gate after both: spot-verify 5 publication claims (resolve the DOIs yourself), check
  the exclusion appendix is honest, check the ranking's reasoning → `MIRU_BIB_GATE.md` /
  `PASS_PUBLISHED_BIBLIOGRAPHY`.

Writes in this lane only. This bibliography becomes the required base layer for any future BHU
theory night — no unpublished base papers, per Duho's standing direction.
