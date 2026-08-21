# Chasing the two published Smolin papers — result: not obtainable without institutional access

Duho: *"get the two smolin papers through a library route"*. Seven routes tried. **Both closed.**
Recording the negative properly, with a positive control, so nobody repeats it.

## The targets, identifiers now exact

| # | paper | identifier |
|---|---|---|
| 6 | Smolin, *"Did the Universe evolve?"*, Class. Quantum Grav. **9**, 173–191 (1992) | DOI **10.1088/0264-9381/9/1/016** (resolved via Crossref this session — our bibliography carried the citation but not the DOI) |
| — | Smolin, *"Cosmological natural selection as the explanation for the complexity of the universe"*, Physica A **340**, 705–713 (2004) | DOI **10.1016/j.physa.2004.05.021** |

## Routes tried

| # | route | CQG 1992 | Physica A 2004 |
|---|---|---|---|
| 1 | Crossref metadata | resolved (DOI recovered) | resolved |
| 2 | OpenAlex OA locations | `is_oa: false`, status **closed** | `is_oa: false`, **closed**; only a RePEc pointer back to ScienceDirect |
| 3 | NASA ADS scanned article service | 404 | 404 |
| 4 | INSPIRE file store | record exists, **0 documents**, no eprint | record exists, **0 documents** |
| 5 | Semantic Scholar open PDF | `isOpenAccess: false`, no PDF | `isOpenAccess: false`, no PDF |
| 6 | ADS `link_gateway` — ADS_SCAN / PUB_PDF / EPRINT_PDF | 404 on all three | — |
| 7 | CORE aggregator | `totalHits: 0` | — |

**Positive control (route 6), because a negative from a broken method is worthless:** the same
gateway, same query shape, returns **200** and redirects to `arxiv.org/pdf/2007.04175` for Ferdman
2020 and `arxiv.org/pdf/1706.09438` for Tauris 2017. The method works; the 404s are real.

Neither paper has an arXiv eprint. CQG 1992 predates Smolin's arXiv record on this topic, and the
Physica A paper was never posted.

## Why this one is harder than the PLB erratum chase

The 2026-08-20 erratum chase failed on all 8 routes but still *won* something — the published
Elsevier XML of the original PLB paper, free from the INSPIRE file store. That worked because
INSPIRE holds publisher-deposited documents for many hep titles. **INSPIRE holds no document for
either Smolin paper**, so the same trick has nothing to bite on.

## What remains, and it is not mine to do

Institutional access — an IOP subscription for CQG and ScienceDirect for Physica A, through a
university proxy or an interlibrary document request. **I do not enter credentials**, so that route
is Duho's to exercise if he wants it. If he does, both are single-article requests, and the pages
that matter are few: for CQG 1992 the statement of the selection argument and any stated
neutron-star bound; for Physica A 2004 the sentence Brown–Lee–Rho cite for "the upper mass limit of
neutron stars be as low as possible".

## What is actually at stake — smaller than it looks

Track C's finding rests on Smolin's own words in astro-ph/9712189 (unpublished), and the two
published papers would **upgrade its source class rather than likely change its content**: the
local-maximum structure, the 2.5 M⊙ threshold and the absence of any 4% binary test are all stated
there in his own voice. But that expectation is exactly the kind of thing that should not be
asserted before reading, so Track C stays **context-grade** and B-18 stays **UNVERIFIED-AT-GATE**
until one of them is read.

## Not suggested

Contacting the author. Duho declined that route during the erratum chase and the reasoning has not
changed.

— Tori, 2026-08-21 KST. Literature hosts only (crossref, openalex, inspirehep, semanticscholar,
adsabs, core). portal.nersc.gov untouched. No credentials entered anywhere.
