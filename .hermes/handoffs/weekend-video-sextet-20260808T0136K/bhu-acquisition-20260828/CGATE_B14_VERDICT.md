ADJUDICATION_INCOMPLETE_MISSED_ENTRY44

# B14 adversarial adjudication

## 1. Candidates 4 and 39

Both hand rulings are correct.

### Candidate 4

The flagged block is not bibliography entry 4. It is the later ranked audit target headed `**4. Roupas 2022 — entry 21.**`. Its mention of a “μHz–Hz, LISA-class” band describes a proposed signal band and does not assert a LISA measurement result. The real bibliography entry 4 is Knutsen (2009) and contains no LISA claim. Candidate 4 is therefore a false positive.

There is also a parser defect more serious than the adjudication notes. The regex matches every bold numbered heading, including the five numbered headings in the ranked-target section. `blocks[num]=...` then silently overwrites the genuine entries 1–5 with those later audit-target blocks. The reported “58 entry blocks” is the size of the dictionary after overwriting, not proof that exactly 58 entry headings were parsed. The “no duplicate numbers” check is tautological because dictionary keys are necessarily unique. Thus B14 did not actually screen genuine entries 1–5 at all.

### Candidate 39

The flagged `Planck` is the Planck unit/density, not the Planck satellite or collaboration. The entry reports a theoretical bounce density and the source's validity concern; it asserts no external experimental result. Candidate 39 is a false positive.

## 2. Candidate 54

Candidate 54 is real in the narrow sense B14 tests. The bibliography says the paper “Cites Planck PR3's 3σ preference for Ω_k ≈ −0.04 and same-direction ACT/DESI trends,” while the block supplies no citation marker for any of those external results.

I checked the pinned source, `2505.23877_clean.txt`, rather than relying on the bibliography. At line 480 the paper itself says Planck PR3 revealed a 3σ preference and gives \(\Omega_k\simeq-0.04\pm0.01\); it then characterizes ACT as showing a slight positive-curvature preference and DESI as echoing that trend. So the bibliography accurately describes what the source paper claims/cites.

Calling this defect weaker than entry 51's former bare CMS assertion is fair. Entry 54 is explicitly a report about the citations and claims made by its own source paper, so the entry's paper supplies provenance for the fact that those claims were made. Entry 51 formerly stated present CMS status directly, with no measurement source at all. Nevertheless, entry 54 still leaves the underlying measurements unreceipted in the bibliography and repeats a materially misleading aggregate characterization: the existing phase-6 citation audit found the Planck number dataset-specific, the ACT paper's own summary contrary to the “same-direction” gloss, and the cited DESI analysis assuming \(\Omega_K=0\) rather than measuring a same-direction curvature trend. It is a real but weaker citation-custody defect.

## 3. Missed instrument-free experimental-status claim

**Entry 44 is a clear miss.** Its entry says:

> states its own base model is “already ruled out at >5σ” (exact scale-invariance vs the observed red tilt)

That is an assertion of experimental/observational status, including a quantitative significance, without naming an instrument and without pinning an external measurement source below the entry's own DOI line. The entry DOI can substantiate that Pourhasan, Afshordi, and Mann made the concession, just as entry 54's DOI can substantiate what its authors cited; it does not independently receipt the observed spectral tilt or the claimed \(>5\sigma\) exclusion. It is therefore at least the same weaker, testimony-through-the-source defect assigned to entry 54 and is invisible to B14's fixed instrument list.

This is not merely a hypothetical wording pattern: it is an actual fourth corpus candidate/finding that the requested instrument-free attack recovers. Accordingly, the three-candidate adjudication is incomplete.

Other status language outside the instrument list exists, especially in the heavily amended entry 31, but much of entry 31 now names papers/arXiv identifiers and methods, so it is not the clean missed bare case. Entry 44 is clean: no instrument, explicit observational comparison, explicit significance, and no external receipt in its block.

## 4. Script controls and scope

The script reproduces 4/4 and exits 0, but the controls do not validate corpus completeness:

- The parse check cannot detect duplicate headings because duplicates have already been destroyed by dictionary assignment.
- The positive control checks entry 51 only after the same overwrite-prone parse.
- The negative control establishes that a citation marker can remove a detected candidate; it does not establish that the marker supports the relevant claim.
- The separation check merely proves that some detected blocks contain citation-shaped strings and others do not.
- The instrument/status window can create proximity false positives, as entries 4 and 39 show.
- Most importantly, the fixed instrument vocabulary necessarily misses entry 44's `ruled out at >5σ` formulation.

## Bottom line

The adjudicator correctly rejects candidates 4 and 39, correctly accepts 54 as a real but weaker custody defect than entry 51's former CMS sentence, and appropriately declines to claim corpus completeness. The concrete audit is nevertheless incomplete: entry 44 is an uncited instrument-free experimental-status assertion that B14 misses, and the parser silently replaces real entries 1–5 with duplicate numbered audit-target headings.
