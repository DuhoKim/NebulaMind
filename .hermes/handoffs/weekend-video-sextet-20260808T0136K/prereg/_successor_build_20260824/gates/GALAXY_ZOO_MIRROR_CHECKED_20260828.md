# Blanc's Galaxy Zoo lead, checked against the sources

**Blanc, 2026-08-28:** *"My recollection is that Galaxy Zoo ran mirrored-subset experiments on GZ1
and found a real handedness bias… I have not verified that against any paper… treat that as a lead to
check, not a fact to build on."*

**Checked. The recollection is correct in substance. The numbers matter more than the fact, and one
of them is material to this study's framing in a way nobody has raised.**

## Confirmed — the experiment is real

**Land et al. (2008)**, *"Galaxy Zoo: The large-scale spin statistics of spiral galaxies in the Sloan
Digital Sky Survey"*, [arXiv:0803.3247](https://arxiv.org/abs/0803.3247). Authors: Land, Slosar,
Lintott, Andreescu, Bamford, Murray, Nichol, Raddick, Schawinski, Szalay, Thomas, Vandenberg.

Volunteers re-classified a subset with images **horizontally flipped**. Reported percentages:

    original   CCW 6.032%   CW 5.525%
    mirrored   CCW 5.942%   CW 5.646%

**Raw GZ1 asymmetry before correction: ~15% more counterclockwise than clockwise.** Attributed to
human perception or the user interface, not to sky. **Residual after mirroring: ~1.5–2%**, with
binomial `P ≈ 0.13` and `P ≈ 0.21` — **not statistically significant in Land's own analysis.**

## The number that matters most here, and it is not the residual

**The uncorrected classification bias was ~15%. The amplitude this study tests is 4%.**

**An unmeasured classifier bias was nearly four times the signal.** That is the strongest available
argument for why the mirror test is a prerequisite rather than a refinement, and it comes from the
same survey family, on the same task, in the published record. It belongs in the study's motivation.

## Material to the framing, and not previously raised in this lane

**Land et al. 2008 found no dipole.** From the abstract: the winding sense is *"consistent with
statistical isotropy"*, with *"no significant dipole signal, and thus no evidence for overall
preferred handedness"* — and, after correcting for bias, that **previous studies** *"may also be
affected and explained by a bias effect."*

**That is a published null on ~37,000 spirals, and it predates the Longo claim this study exists to
test.** The successor should say so. A preregistration that tests a contested claim without recording
that the contest already has a null on the other side is incomplete motivation.

## Contested, which is the honest state

A later reanalysis ([arXiv:2302.06530](https://arxiv.org/pdf/2302.06530)) argues the residual 1.5–2%
*"agrees in both direction and magnitude"* with asymmetries from other methods and telescopes, i.e.
that it is real rather than pure artefact. **So the literature is split**, which is consistent with
this lane's target of contested-and-tractable questions.

## What it does NOT give us — the point I made before checking, which survives

**The published amplitude cannot substitute for measuring our instrument.** Land's bias is **human
perceptual and interface bias in volunteers**. `BS-3` is an **automated weighted instrument**
(`weights 83008c1c…`). A CNN's chirality asymmetry arises from initialisation, augmentation and
training-set imbalance — a different mechanism with no reason to share magnitude or sign.

**Use it as motivation and as an order-of-magnitude expectation. Do not use it as a value.** The
`antisymmetry_receipt` field in BS-3 still has to be filled by measurement.

## One unresolved discrepancy, flagged rather than smoothed

Sources disagree on the mirrored subset's size: one description gives **~11,000 galaxies**, another
**91,303**. **I have not resolved which is the mirrored subset and which is a different GZ1 sample**,
and the primary PDF did not parse for direct quotation. If the figure is ever cited in the
preregistration, it must be read from the paper body first.
