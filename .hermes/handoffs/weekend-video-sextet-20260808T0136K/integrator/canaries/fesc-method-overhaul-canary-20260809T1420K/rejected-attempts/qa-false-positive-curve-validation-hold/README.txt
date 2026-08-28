Preserved first encoded-QA HOLD.

The renderer correctly removed the curve icon branch and rejects curve icon parameters. The initial QA guard falsely matched the string used by that validation rejection rather than an available `elif kind=="curve":` rendering branch. No candidate bytes changed; only the QA predicate was corrected before rerunning.
