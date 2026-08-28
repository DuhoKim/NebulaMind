# Erratum chase — Phys. Lett. B 701, 672 (2011) — RESULT

Duho, 2026-08-20: "chase the erratum through a library route". Tori, BHU lane.
Target: the content of the erratum to Poplawski, Phys. Lett. B 694, 181 (2010),
DOI 10.1016/j.physletb.2011.05.047 — left UNVERIFIED-AT-GATE by Gate 1 because
no permitted host exposed its text.

## Verdict: the erratum text is NOT publicly obtainable. Gate 1's finding stands,
now established by exhaustion rather than by a single 403.

## Routes tried, and what each returned

| route | result |
|---|---|
| arXiv 1007.0587 version history | only v1 (4 Jul 2010) and **v2 (2 Nov 2010)** — both PREDATE the May 2011 erratum. The author never folded the correction into the preprint. |
| INSPIRE-HEP record 860461 | erratum present in metadata (`publication_info` material=`erratum`, both DOIs listed) but **no erratum document**. Did yield the publisher full text of the ORIGINAL — see win below. |
| Crossref | metadata + Elsevier PII `S037026931100565X`; full-text links point at `api.elsevier.com`, which requires an institutional API key. |
| ScienceDirect (PII direct) | **HTTP 403**, as at Gate 1. |
| Semantic Scholar | claims `isOpenAccess: true` with an `openAccessPdf` — **but the PDF is arXiv 1007.0587, the 2010 preprint**. False positive. |
| OpenAIRE | `bestaccessright: OPEN` — again resolving only to the same 2010 preprint. False positive. |
| OpenAlex | `is_oa: false`, `oa_status: closed`, `any_repository_has_fulltext: false` — **the only aggregator that reports this honestly**. |
| CORE / NASA ADS | require API keys (301 / 401). |

**Aggregator warning worth keeping:** two major indexes advertise this erratum as
open access and hand back the pre-erratum preprint. A less careful check would
"find the erratum" and be reading the very text the erratum corrects.

## What the chase DID win: the published version, free, and it is quotable

INSPIRE's file store served Elsevier's own published full-text XML of the
original article (PII S0370269310011561), pinned here as
`sources/elsevier_plb694_published.xml` (sha256 c85c48c5…, 121 KB).

This upgrades the audit's evidence, because the two audited numbers can now be
quoted from the **published record** rather than from the preprint:

- **ε_R = 1.1 × 10¹¹⁶ J m⁻³** — verbatim in the published text, with the claim
  that this is "greater than the Planck energy density by a few orders of
  magnitude". Track A1 recomputed 7.65 × 10¹¹⁶ (×6.95). The discrepancy is
  therefore against the journal of record, not a preprint typo — which is what
  the quarantine assumed but could not previously show.
- **Ω_S = −8.6 × 10⁻⁷⁰** — verbatim in the published text, matching the value
  Phase 2 reproduced at the coherent edge of its bracket.
- The published article contains **no erratum notice** (the XML predates it).

## Consequence for the gated record — none of it changes

The Phase 2 conclusion is unaffected: both numbers stay quarantined with the
audit's recomputations in their place, and whether the erratum corrects ε_R
remains unknown. What changes is confidence in the *provenance* of the
quarantined values.

## Remaining route — one, not two

1. **Institutional access.** Any subscribing library resolves this in seconds.
   Credentials are not something I will enter, so this is Duho's to do if he
   wants it. Nothing downstream is waiting on it.

## Retracted: contacting the author

An earlier version of this file listed "ask the author" as a second route.
**Withdrawn on Duho's challenge (2026-08-20), and he was right to push.**

We have spent two days auditing this author's work adversarially — 77 verdict
rows across four papers, two arithmetic errors, a branch contradiction, an
unstated Planck-regime caveat, and his own sequel disavowing his earlier
foundation. Writing to request a document while holding an unpublished critique
is either not straightforward (if the audit goes unmentioned) or opens
correspondence about unreviewed findings in Duho's name (if it does) — which
cuts against the standing rule that this work gets external-theorist review
before anything leaves the lane.

And the cost/benefit never justified it: the erratum's content changes none of
the gated conclusions. The quarantined numbers already have independent
recomputations in their place. Curiosity is not a reason to spend a stranger's
attention.

If BHU ever moves toward a publication claim, contacting the author becomes a
courtesy owed as part of review — a different act, for a different reason, and
still Duho's call to make.
