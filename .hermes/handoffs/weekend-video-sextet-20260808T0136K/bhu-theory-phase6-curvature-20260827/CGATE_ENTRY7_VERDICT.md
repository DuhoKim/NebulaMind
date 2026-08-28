UPHOLD_WEAK

# CGATE Entry 7 Verdict

Seat: Codex / CGATE
Date: 2026-08-28 KST
Lane: `bhu-theory-phase6-curvature-20260827`

I read `KICKOFF_GATE_ENTRY7.txt` in full, read the pinned APS version of record at `../reviews/_tori_bhu_reverify_sources_20260811/aps_vor_10.1103_PhysRevLett.101.091101_layout.txt`, checked the Publisher's Note at `../brown-erratum.txt`, and reproduced `python3 c5_entry7_audit.py`: 5/5 checks passed, exit 0.

My ruling is **UPHOLD_WEAK**. Entry 7 fired the Brown-Bethe / HLS / kaon-condensation instrument chain at `M >~ 2 Msun`. It did not license the stronger record statement that CNS itself was simply falsified at that threshold. For CNS, the source supports "serious doubt", "serious obstacle", or "put in doubt", not "falsified".

## Ruling on the Attack Points

### 1. Is the instrument/theory split imported because it is convenient?

No. The split is present in this paper's own text.

The abstract states a disjunction over a chain: a massive neutron star with mass `M >~ 2Msun` would "put in serious doubt or simply falsify" predictions including VM of HLS, kaon condensation, the Brown-Bethe maximum mass, and Smolin's CNS. That sentence alone does not assign the stronger limb to CNS.

The body then gives the paper's cleanest falsification sentence: finding a neutron star of mass `>~ 2Msun` "falsifies the VM of HLS theory", which in turn "falsifies the kaon condensation at ~3n0" (APS lines 42-45). CNS is not the object of that verb. Immediately before, CNS is described in softer terms: a neutron star appreciably exceeding the Brown-Bethe maximum "would count against the CNS scenario" (lines 51-55).

The conclusion confirms the same split. The direct mass observation would "present a serious obstacle to the BB and CNS scenarios" (lines 233-237). A different CCS/gravitational-wave route "would falsify the BB scenario and put in doubt the CNS theory" while also falsifying VM of HLS (lines 260-270). This is not an imported convenience; the paper repeatedly reserves unqualified "falsify" for the nuclear-physics mechanism and uses weaker language for CNS.

### 2. Should the contradiction be resolved by overturning Entry 31 instead?

No. The sources support correcting Entry 7's strong reading, not treating Entry 31 as moot.

The strong Entry 7 record says CNS died once `>~2 Msun` neutron stars were observed. Entry 31 says Smolin's own clean CNS refutation bar is `2.5 Msun` and remains unreached. Those cannot both be right as CNS-status claims. But Brown, Lee, and Rho do not clearly move Smolin's CNS death threshold down to `>~2 Msun`; they say the Brown-Bethe / kaon-condensation mechanism is falsified at that level and that CNS is seriously obstructed or put in doubt.

So the fair resolution is: Entry 7 has fired as to the instrument chain; Entry 31 remains the cleaner CNS falsifier at Smolin's own `2.5 Msun` bar unless separately demoted on other grounds. I do not overturn the Entry 31 `LIVE_CALIBRATED` ruling on the basis of Entry 7.

### 3. Is choosing limb 1 arbitrary?

It is better grounded than the prior limb-2 assignment for CNS.

The abstract alone is underdetermined: "serious doubt or simply falsify" is a disjunction over a chain. If that were the only evidence, either assignment would be weak. But the body and conclusion break the tie. The body explicitly attaches "falsifies" to VM/HLS and kaon condensation. The conclusion explicitly attaches "serious obstacle" to BB and CNS. The later CCS passage again says "falsify the BB scenario" but only "put in doubt the CNS theory." Choosing the weaker limb for CNS follows the authors' distribution of predicates.

### 4. Is the body's silence on CNS load-bearing?

It is load-bearing, but not alone.

The body is important because it is the one place where the authors state the clean `>~2 Msun` falsification rule without the abstract's disjunction. That rule stops at VM of HLS and kaon condensation. However, the silence would be less decisive if the rest of the paper otherwise called CNS falsified. It does not. The closing and CCS passage affirm weaker CNS language, so the ruling rests on the whole textual pattern, not silence alone.

### 5. Tier question

The tier should describe the claim's calibration; status needs a separate axis.

It is not inherently wrong for Entry 7 and Entry 31 to share `CALIBRATED-FALSIFIER` if both are author-stated observational tests with numerical thresholds. It is a record-keeping defect if the tier is then used in tallies without a `LIVE` / `FIRED` / `DEMOTED` status field. The correct representation is not to strip calibration from Entry 7, but to state status separately: Entry 7 is **CALIBRATED-FALSIFIER / FIRED as to the instrument chain / CNS only seriously obstructed**. Entry 31 can remain **CALIBRATED-FALSIFIER / LIVE** if its `2.5 Msun` CNS threshold is retained.

### 6. Reproduction and threshold

`python3 c5_entry7_audit.py` returned 5/5 checks and exit 0.

The Publisher's Note confirms the relation-sign issue: the abstract's second line should read as mass `M >~ 2M` and the abstract was corrected as of 2008-09-02. The local OCR renders the corrected relation as `M * 2M`, and the kickoff/audit interpretation as `>~2 Msun` is the right record-level reading.

## Record Correction

Entry 7 should not say "CNS falsified via limb 2" at `>~2 Msun`. It should say:

**FIRED as to the Brown-Bethe / VM-HLS / kaon-condensation instrument chain at `M >~ 2 Msun`; for CNS, the source supports serious doubt / serious obstacle / put in doubt, not simple falsification.**

That preserves Entry 7 as the worked example of a fired calibrated observational instrument while removing the overclaim that CNS itself died at the `>~2 Msun` observations.
