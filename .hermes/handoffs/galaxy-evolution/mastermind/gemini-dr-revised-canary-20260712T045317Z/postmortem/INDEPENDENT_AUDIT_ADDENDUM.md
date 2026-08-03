# Independent audit addendum — closed C1

UTC: 2026-07-12T05:54:00Z
Packet: `gemini-dr-revised-canary-20260712T045317Z`
Status: local-only addendum; the pinned canonical post-mortem remains immutable.

## Verified additions

The delayed independent read-only audit confirms the existing C1 failure and adds the following concrete defects that were not fully enumerated in the canonical post-mortem.

### C2 — structure/completeness: FAIL

- `body.md:96`: ASTRID validation citation field is empty rather than `NONE_FOUND`.
- `body.md:9-60`: several calibration-target entries name observables without the requested observational dataset.
- `body.md:148-159`: multiple observables-map cells use bare `NOT_REPORTED` without a source or `NONE_FOUND`; all five ASTRID cells at line 153 are bare.
- `body.md:151`: FIRE outflow/hot-halo `EMERGENT` cells lack cell-specific support.
- `body.md:175`, `177`, `179`: GAP entries lack a citation and the required absence token.
- `body.md:62-76`, `105-119`, `161-167`: narrative padding appears inside ledger/map sections.

### C3 — uncertainty: FAIL

Clear examples without a source uncertainty or `UNCERTAINTY_NOT_QUOTED_BY_SOURCE` include:

- tuned values `0.002` and `2` at line 13;
- halo-mass scale `10^12 M_sun` at line 16;
- supernova energy `10^51` ergs at lines 64-66;
- `0.3 dex` to several dex at line 97;
- `k ~ 1-10 h Mpc^-1` at lines 131-141.

Metadata, citation identifiers, simulation-name suffixes, and formatting-only math fragments are not scientific quantitative claims.

### C4 — same-unit citation labeling: FAIL

In addition to lines 96 and 129, clear failures occur at:

- line 153: five ASTRID `NOT_REPORTED` map claims have neither a same-unit citation nor `UNCITED_NOT_USABLE`;
- lines 175 and 177: named-simulation validation-gap claims lack either token;
- line 179: generic validation-gap claim lacks either token.

A later links-ledger entry cannot cure a same-unit C4 omission.

### C6 — estimand/fraction labeling: FAIL

This is a deterministic contract failure, not only a manual-review concern:

- repeated SIMBA, ASTRID, and ROMULUS simulation-observation comparisons at lines 115, 117, and 119 lack a matched/unmatched comparability label;
- gas-fraction statements at lines 83-91 and map claims at lines 148-150 and 158-159 omit applicable tracer, selection, denominator, and redshift qualifiers.

Whether a supplied matched/unmatched label is scientifically truthful remains manual-review-only.

### C7 — links ledger: FAIL plus advisory padding

- cited `https://arxiv.org/html/2501.16602v1` at line 72 is absent from the ledger;
- cited `https://arxiv.org/html/2605.13843v1` at line 105 is absent from the ledger.

Unused ledger rows are advisory padding under the original one-way C7 rule. The revised C1r contract intentionally tightens C7 to bidirectional set equality.

## Representation boundary

Not model defects:

- missing literal Markdown heading sigils in captured `innerText`;
- tab-rendered tables;
- MathJax/subscript fragments split across physical lines.

C1r therefore preserves immutable `innerText` and a structured rendered-DOM capture. A link attached to the same logical DOM cell counts as a checkable same-cell citation under C1r. Hidden links outside the answer body, citation pills outside the logical unit, and links on later blocks do not rescue C4.

## Required C1r hardening

Before arming:

1. prohibit simulation-observation comparison prose outside Section 2, or require an exact comparability token in the same logical unit;
2. make the validator scan all logical blocks for unlabeled comparison candidates, not only Section-2 rows;
3. reject bare Section-4 `NOT_REPORTED` cells that omit `NONE_FOUND`;
4. retain fail-closed manual review for scientific correctness, true selection matching, and source support.
