import re

with open("PREREG_SUCCESSOR_DRAFT_V25_20260827.md", "r") as f:
    text = f.read()

# Fix C2
old_c2 = "| C2 | **Cutout integrity verifier** — `verify_cutout_integrity` symbol and digest to be pinned at BS-2a (**presently REFUSED / UNFILLED**). Must be a **hermetic worker** with a strict allowlist over imports, executable and model weights, filesystem, network, and subprocesses, verified by runtime attestation. | reads **only** cutouts via row B and fixed parent lists. Computes and writes the separate authenticated **acceptance-evidence projection** exporting only authenticated predicate bits (`parent_attempt_present`, `byte_integrity_pass`, `canonical_shape_pass`), and an **exact-parent stage-completion artifact** closing the omission channel. Recomputes all cutout digests inside the sealed boundary; never exports them. | P2, after row C, before row D | BS-2a (design), the cutout-completion receipt | the acceptance-evidence projections, one per parent object, and the stage-completion artifact | executing the classifier; emitting any field outside the schema; failing the hermetic runtime attestation |"

new_c2 = "| C2 | **Cutout integrity verifier** — `verify_cutout_integrity` symbol and digest to be pinned at BS-2a (**FILLED**). No hermetic worker, capability allowlist or blindness fixture is required. | reads **only** cutouts via row B and fixed parent lists. Computes and writes the separate authenticated **acceptance-evidence projection** exporting only authenticated predicate bits (`parent_attempt_present`, `byte_integrity_pass`, `canonical_shape_pass`), and an **exact-parent stage-completion artifact** closing the omission channel. Recomputes all cutout digests inside the sealed boundary; never exports them. | P2, after row C, before row D | BS-2a (design), the cutout-completion receipt | the acceptance-evidence projections, one per parent object, and the stage-completion artifact | executing the classifier; emitting any field outside the schema |"

text = text.replace(old_c2, new_c2)

# Fix Rule 2
old_rule2 = "2. **The exceptions are the table's rows, or they do not exist.** No process that touches a χ-bearing object may run before the lock unless a row names it. BS-2a is **REFUSED / UNFILLED**, and processes requiring it (Rows C2, E) cannot run until a new design passes gates that does not rest on handedness amplitude."
new_rule2 = "2. **The exceptions are the table's rows, or they do not exist.** No process that touches a χ-bearing object may run before the lock unless a row names it. BS-2a is **FILLED**, so processes requiring it (Rows C2, E) can now run."

text = text.replace(old_rule2, new_rule2)

with open("PREREG_SUCCESSOR_DRAFT_V25_20260827.md", "w") as f:
    f.write(text)
