CLEARED_HAWKING_DEMOTION

# CGATE REGATE5 Confirmation Verdict

## Ruling

The required repair clears the hold.

The prior hold was narrow: p9 and `BHU_CLOSED_ROUTES.md` had made the exact factor-of-two
temperature comparison do discriminating-measurement work it cannot do. That defect is now
removed in the live artifacts I inspected. The repaired position is the defensible one:

- the naive Schwarzschild calculation gives two distinct temperatures, not a degeneracy;
- an ideal thermometer could distinguish `1.3269e-30 K` from `2.6538e-30 K` if both were
  well-defined observables;
- section B is now explicitly supporting only, and is framed as a scale/distinctiveness point;
- the closure no longer rests on the exact factor of two.

I therefore do not continue `HOLD_HAWKING_DEGENERACY_OVERCLAIM`.

## Artifact Checks

`p9_hawking.py` now says in its module docstring that the original B claim was wrong, that a
factor of two is not a degeneracy, and that section B only supports the weaker claim that a
horizon temperature of order `hbar H / k_B` is not distinctive evidence for BHU. Runtime B1
also prints the needed correction directly: the two temperatures differ by exactly two, and an
ideal thermometer could tell them apart.

`P9_HAWKING_RECEIPT.md` preserves the old overclaim in strike-through, labels it withdrawn,
and appends a correction accepting the gate's point. Its bottom line is reordered so that
"not defined for this model" is first, the Wien wavelength argument is second, detectability is
third, and distinctiveness is fourth/supporting only. That is the right direction.

`BHU_CLOSED_ROUTES.md` C2 also withdraws the old "not discriminating / decisive" reason in a
boxed block and demotes the exact factor-of-two point to supporting. The status line is no
longer relying on the factor-of-two comparison.

The kickoff's relative path `bhu-daily-20260827/script_hawking.WITHDRAWN.md` does not exist
inside this directory. The file does exist one level up as
`../bhu-daily-20260827/script_hawking.WITHDRAWN.md`, and it correctly marks the published
audio script paragraph as withdrawn while leaving the source transcript byte-intact. I treat
that as a path-reference slip, not a failure of the Hawking demotion.

## Independent Reading

The repaired closure is still not a proof that no conceivable added horizon-thermodynamics
model could ever produce an observable. But that is not the live claim. The live claim is that
the Smoller-Temple artifacts audited here do not themselves define the Hawking observable, and
that importing the Schwarzschild formula would report a property of an added model, not a
source-pinned BHU prediction. That is sound.

I also do not see the reordering as an overcorrection. "Not defined for this model" is doing
real work: the source text has a TOV-fluid exterior, white-hole orientation, no Hawking
radiation construction, and an assignable background temperature. The tidy statement that the
Hawking and optical routes close on the same missing exterior physics should not be promoted
into a theorem, but as a diagnosis of this lane's source gap it is fair.

On claim 4, I agree with the narrower codex framing from the previous verdict. The sentence
"the two tested closures each contain a cancellation, at different locations" is low-value but
not false or vacuous if kept as a receipt sentence about two closure experiments. It should not
be promoted as a model result.

## Reproduction Record

Commands run from this directory:

| command | observed result |
|---|---:|
| `python3 p9_hawking.py` | exit 0, `SELF-CHECKS: 16/16 passed` |
| `python3 p1c_rigorous_sweep.py` | exit 0, `10/10 checks passed` |
| `python3 p6_path_transfer.py` | exit 0, `6/6 checks passed` |
| `python3 p7_signed_sweep.py` | exit 0, `4/4 checks passed` |
| `python3 p8_thick_limit.py` | exit 1, expected negative check, `2/3 checks passed` |
| `python3 p10_flatness_redo.py` | exit 1, expected anchor mismatch, `2/4 checks passed` |
| `python3 p11_claim1_boost.py` | exit 0, `8/8 passed` |

Additional source checks:

- `rg -n -i "hawking" ../bhu-reading-20260823/sources/math-ph_0302036_clean.txt ../bhu-reading-20260823/sources/smoller_temple_1997_clean.txt`
  found two Hawking hits in `math-ph_0302036_clean.txt`, both in the references, and none in
  the 1997 file.
- Source greps found the white-hole event-horizon language, the entropy-satisfying orientation,
  and the assignable `T0` passage used by the receipt.
- `../bhu-daily-20260827/script_hawking.WITHDRAWN.md` exists and marks the published script's
  exact overclaim as withdrawn.

Conclusion: the p9 demotion resolves the hold. Phase 5b may pass in the limited reduced sense
described by the prior verdict, with Hawking closed only as a source-pinned route supplied by
these artifacts, not as an exclusion of all conceivable added thermodynamic models.
