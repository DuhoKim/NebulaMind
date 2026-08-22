# CHI CUSTODY — evidence, not assertion

Hwao, 2026-08-22 13:03 KST. Replaces the receipt line that ran to eight revisions and ten gate refusals
(`CHI_CUSTODY_RECEIPT_20260821*.md`, all retained).

## Why this is shaped differently

Ten gates refuted that receipt. Not once was the science wrong. The defects were one repeated
mistake — **claiming coverage the artifact did not have**: "complete ledger", "no code path",
"cited by no gate", "exact input set", "three times before review", "committed as witness". The
last covered 13 of 72 inputs.

Approach approved by Duho 2026-08-22: **publish the evidence, and make only claims a reader can
check in one command.** Design rule: **no universal quantifier appears in any claim.** A check
answers *does this command over these named paths give this result* — never *does this hold
everywhere*.

## Run it

    zsh _evidence_20260822/verify.sh

`verify.sh` sha256 `b8ac8b2c53d8d52cea16104553d218de49abab44da5d48e38f92d1f168a9a29f`
recorded output `_evidence_20260822/verify_output.txt` sha256 `fe399a784135705d38c0cfcf390f0910cff6de10fd32a08eb4fa4265e24ce40c`

**15 claims, 15 passing at write time.** Each prints PASS or FAIL against a value stated in the
script. If a digest moves, a claim fails and says which.

## What the claims cover, and what they deliberately do not

**S1-S7 — the disclosure.** Four surface digests, and three greps establishing that the 23:12
caption states the three values, states a sign summary, and states `2,725 galaxies measured`.
That last one is why the earlier "complete set of values then in existence" was withdrawn: three
of 2,725, not three of three.

**F1-F4 — the frozen text.** Authorization and preregistration digests, plus greps locating
condition 2's bar on summaries and condition 1's partial-tertile prohibition. The rulings rest on
quoted text a reader can find, not on my characterisation of it.

**G1-G2 — the geometry**, from positions only. 208,407 rows; `var(cos θ) = 0.057985` about Longo's
frozen axis, recomputed by `geom.py` on every run rather than pinned as a number I typed once.

**H1-H2 — the hand-check harness, scoped.** H1 asserts the harness *does* define a chi-tertile
ranker. H2 is a search for `chi_dr10_south` **under `handcheck/` only**, returning no lines. The
script prints that scope in its own output. **This is not the claim that no code anywhere touches
real chi** — that was the earlier overclaim, and it was false.

**Gate verdicts** are printed by reading each file's first line. No count, no summary, no
inference about which revision any gate reviewed — that is not determinable from the files.

## The first run failed, and that is the point

H1 originally asserted `_rank_tertiles` appears once. It appears four times. The fact was right
and **my expected value was invented** — the same overclaim, caught on the first execution instead
of by the eleventh gate. The comment recording that is in the script.

## Findings this evidence supports

- The disclosure breaches **§4's publication bar** and **condition 2** independently.
- **Condition 1: no breach established within the searched scope** (H2), which is a statement about
  the search, not about the world.
- The footprint cannot reach the preregistered power — see
  `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` and the two gates that held it.

## Not covered here

The audio ledger and the 218-report ASR sweep are Blanc's:
`blanc-ops-overhaul-20260820/DISCLOSURE_LEDGER_AUDIO_20260821.md`. Three known
caption/audio divergences remain open there. I do not restate their numbers; cite theirs.
