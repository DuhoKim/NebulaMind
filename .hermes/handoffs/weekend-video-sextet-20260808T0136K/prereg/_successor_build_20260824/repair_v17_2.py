import re
import hashlib

filepath = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V17_20260827.md"

with open(filepath, "r") as f:
    text = f.read()

# Fix the table replacement which I probably missed.
old_table = "| BS-2a ⚠ **DESIGN, CLASS P — REFUSED / UNFILLED** | Hwao | **acceptance design**: the numeric confidence threshold **and the named authority that sets it**, retry/failure semantics, the evidence schema for exclusion reasons (a)–(d), the ledger schema, the recomputation code and its fixtures. Gated as text AND code **before any image byte**. V12 placed this in Class E while §2.7 called it a class-P prerequisite. **BS-6 is blocked until a new BS-2a design passes gates that removes the confidence/amplitude dependency and implements the hermetic integrity verifier.** | `run_production_verdict`, pre-verdict validator | BS-2f, BS-6 |"

new_table = "| BS-2a ⚠ **DESIGN, CLASS P — REFUSED / UNFILLED** | Hwao | **acceptance design**: the numeric confidence threshold **and the named authority that sets it**, retry/failure semantics, the evidence schema for exclusion reasons (a)–(b), the ledger schema, the recomputation code and its fixtures. Gated as text AND code **before any image byte**. V12 placed this in Class E while §2.7 called it a class-P prerequisite. **BS-6 is blocked until a new BS-2a design passes gates that removes the confidence/amplitude dependency and implements the hermetic integrity verifier.** | `run_production_verdict`, pre-verdict validator | BS-2f, BS-6 |"

text = text.replace(old_table, new_table)

with open(filepath, "w") as f:
    f.write(text)

with open(filepath, "rb") as f:
    print(hashlib.sha256(f.read()).hexdigest())
