# AGY MINI-PREREGISTRATION REFEREE REPORT

## FINDINGS

**F1 [FATAL] — Unexecutable Core / Missing Identities (Clause 16.1)**
*Dimension: D2 (Executability without judgment)*
Clause 16.1 commands the sealing of the `BS-4 fixture`, `rendering configuration`, `software lock/environment record`, `published checksum source`, and `verdict program` before pixel access. However, none of these artifacts are assigned a specific file path or a frozen SHA-256 pin anywhere in the draft, and the text does not supply the verdict program's code. A seat with no context cannot execute this mechanically because it would have to write the verdict program and invent the configurations. Two honest seats would disagree on which files to seal. Because the true SHAs and code are unknown, this cannot be safely repaired in place.
*Repair:* Explicitly define the exact file paths and SHA-256 hashes for each of these five dependencies in Section 2 (Fixed input identities), or pin the executable code for them within the document.

**F2 [FATAL] — Missing BS-4 Executable Definition (Clause 10.1)**
*Dimension: D3 (The sign protocol) / D5 (Geometry fidelity)*
The draft claims to inherit the parent's BS-4 sign-anchor language but strips all actionable mechanics. Clause 10.1 merely name-drops the "frozen expected absolute sign convention" without defining it. In contrast, the frozen parent text (lines 124-129) explicitly defines `A_LONGO = +0.0408` in the East-of-North convention and requires the `BATTERY-SIGN` fixture to demonstrate an injected `-0.0408` sky is never called `REPRODUCED`. Without these constants, the absolute-sign anchor is subjective and unenforceable.
*Repair:* Import the explicit BS-4 language from the parent text into Section 10, specifically defining `A_LONGO = +0.0408` and the `BATTERY-SIGN` refusal criteria.

**F3 [MINOR] — Ambiguous GZ1_OBJID String Formatting (Clause 6.2)**
*Dimension: D2 (Executability without judgment)*
Clause 6.2 hashes the "ASCII decimal GZ1_OBJID with no sign, whitespace, or leading zero". While unambiguous for most integers, specifying the exact formatting function or treating it formally as a base-10 string conversion prevents edge-case parsing ambiguity.
*Repair:* Change to "ASCII base-10 string representation of the integer GZ1_OBJID with no sign, whitespace, or leading zero".

## DIMENSION EVALUATIONS

**D1 BLIND SAFETY: PASS.** 
The tier filter explicitly prioritizes Tier A and B (4.1-4.4) and applies the protected-parent filter before any image access (4.6, 15.3). At measurement time, a machine guard compares every coordinate against the protected pins at a 1.0-arcsec radius before opening (15.4), ensuring the realized Tier-C sample is strictly disjoint. Any new matches surfaced by the complete match are safely caught by Tier A/B priority and excluded from Tier C.

**D2 EXECUTABILITY WITHOUT JUDGMENT: FAIL.**
Verified SHAs and row counts for `gz1_t2.csv.gz` (667,944 rows), `gz1_t3.csv.gz` (225,268 rows), `positions_selected_cut.csv` (49,211 rows), `positions_selected.csv` (65,060 rows), and `successor_ref_v9.py` exactly match the draft's claims against disk. However, the core dependencies listed in F1 are entirely missing their pins, leaving the sealing process unexecutable.

**D3 THE SIGN PROTOCOL: FAIL.**
The split rule, mapping-decision margin (0.10), and `UNDETERMINED-SIGN` triggers are exact and mathematically sound. Disjointness prevents data reuse between mapping and estimation (6.7). However, the protocol fails because the BS-4 absolute sign anchor is critically name-dropped without its operational definition (F2).

**D4 STATISTICAL HONESTY: PASS.**
The Wilson interval states a clear confidence level (95%) and z-value (12.5). The estimand precisely targets the frozen estimation-split object set (12.1-12.2). The power floor is mathematically derived from the interval width at p=0.5 (11.2). Outcome bands are fixed rigidly (13.12), and the claims boundary robustly forbids transfer, accuracy, and flagship modification (14.2-14.8).

**D5 GEOMETRY FIDELITY: PASS.**
The draft correctly enforces the parent's R-B constants in Section 8 without drift or softening. It asserts "exactly 128 by 128 pixels", "0.262 arcsecond per pixel", "CRPIX1=CRPIX2=64.5", "north-up and east-left", "parity is strictly preserved", "exactly one deterministic bilinear reprojection", "stitched before reprojection" (stitch-neighbours-first), and the "wrong parity refuses the cutout and yields WRONG-PARITY-REFUSAL" (wrong-parity-Jacobian refusal).

**D6 CUSTODY & RECEIPTS: PASS.**
Receipt definitions strictly enumerate their required fields (7.9, 16.5, 16.7). The signature scheme is highly defined, mandating a hash over the document with only the value after `DUHO SIGNATURE:` blanked out by an immediate LF (17.1-17.4). Honest seats cannot disagree on the byte preimage.

**D7 SCOPE CREEP: PASS.**
The draft strictly adheres to Ruling #55. It operates on Tier C only, holds Tier B, protects the P0 blind (Tier A), explicitly separates the acquisition scope, and does not authorize any flagship label rescue or `a-hat` calibration.

SEAT: AGY
VERSION: MINIPREREG-REFEREE-V1
VERDICT: NOT-SIGNABLE
COUNT: 3
