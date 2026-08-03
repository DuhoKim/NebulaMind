I checked `provenance/REAL_DATA_SOURCE_CUSTODY.json` first. Provenance is present; the blocker here is citation verification, not missing custody.

**Findings**
1. `flagship_rp1/aastex/rp1_flagship_polished.tex:22,25,71,76`
   - Integrity blocker: the flagship’s core interpretive claims about BPT contamination, aperture/morphology degeneracy, and future mechanism tests depend on bibliography entries that are explicitly marked `source identifier unverified / do not integrate`.
   - Section-level fix: replace those citations with verified identifiers or remove the claim. Good verified replacements already available from the literature are:
     - `Cid Fernandes et al. 2010`, `arXiv:1012.4426`
     - `Stasińska et al. 2015`, `arXiv:1501.03812`
     - `Brinchmann et al. 2004`, `arXiv:astro-ph/0311060`
     - `Kauffmann et al. 2003`, `arXiv:astro-ph/0304239`
     - `Kewley et al. 2001`, `arXiv:astro-ph/0106324`
   - If you keep the broader BPT/retired-galaxy discussion, the prose needs to be narrowed so each sentence is supported by only verified sources.

2. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:19,24,95,105,138,160,197`
   - Integrity blocker: the supplement’s introduction and subsection scaffolding rely on a large number of unverified citation labels. That is not journal-safe as written because the sections read like literature-supported interpretation, not just background pointers.
   - Section-level fix: for the shared denominator intro, use only verified SDSS/BPT anchors:
     - `SDSS DR17`, `arXiv:2112.02026`
     - `York et al. 2000`, `arXiv:astro-ph/0006396`
     - `Brinchmann et al. 2004`, `arXiv:astro-ph/0311060`
     - `Kewley et al. 2001`, `arXiv:astro-ph/0106324`
     - `Kauffmann et al. 2003`, `arXiv:astro-ph/0304239`
   - For the subsection-level motivation, keep only verified anchors already present in the file where possible:
     - `Best et al. 2005`, `DOI: 10.1111/j.1365-2966.2005.09192.x`
     - `Hardcastle & Croston 2020`, `arXiv:2003.06137`
     - `Hirschmann et al. 2017`, `DOI: 10.1093/mnras/stx1907`
     - `Lin et al. 2020`, `DOI: 10.3847/1538-4357/abba69`
     - `Salim et al. 2007`, `DOI: 10.1086/519218`
     - `Salim et al. 2012`, `DOI: 10.1088/0004-637X/755/2/105`
     - `Piotrowska et al. 2022`, `DOI: 10.1093/mnras/stac532`
   - Everything else in those subsection citations should either be verified or explicitly kept as `unverified / do not integrate`.

3. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:93-95,126-160,170-197`
   - Journal-quality blocker: the atlas is over-cited in a way that blurs the line between verified observational support and literature-derived motivation. That is especially visible in the environment, maintenance-heating, mass-bin, gas-depletion, and simulation subsections.
   - Section-level fix: compress each subsection to one verified literature cluster plus one explicit missing-observables statement. Do not keep long chains of mixed verified/unverified references inside the same paragraph. Where a source cannot be verified, leave it out of the prose and keep the note as `unverified / do not integrate`.
   - Concrete example: the simulation section should not cite `eagle2015` unless you can verify it; if you want a verified forward-modeling anchor, use `Hirschmann et al. 2017` `DOI: 10.1093/mnras/stx1907` and keep the rest as future-work framing.

Overall: the data provenance is fine, but the manuscript is not yet citation-clean enough for journal-level pass because several sections still lean on unverified bibliography entries for substantive claims.

JOURNAL_LEVEL_PASS: NO