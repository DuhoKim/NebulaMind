import sys
import hashlib

with open('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V23_20260827.md', 'r') as f:
    text = f.read()

# Blocker 1: BS-2v coverage test is still self-referential
bs2v_old = "| BS-2v ⚠ **DESIGN, CLASS P — UNFILLED** | Hwao | **`VOID` conversion**: handle every enumerated void antecedent. The converter must define a canonical closed antecedent registry with stable IDs and exact source/phase/failure-effect for each `VOID` branch in §5 and §6. It requires a fixture coverage receipt that verifies exact set equality between manifest IDs and exercised IDs (`set(fixture.antecedent_id) == set(converter.branch_id)`). Missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate and leaves BS-6 blocked. | `VOID_converter` | BS-6 |"
bs2v_new = "| BS-2v ⚠ **DESIGN, CLASS P — UNRESOLVED** | Hwao | **`VOID` conversion**: handle every enumerated void antecedent. The normative registry in §7.1 must be **pinned by digest in the preregistration itself** (as a `registry_digest` field bound in the slot schema), and the gate must compare the converter's emitted IDs and the exercised fixture IDs **against that pinned digest's contents**, which the converter does not author and cannot alter. Missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate on mismatch. Because the registry cannot be pinned before the converter exists, this gate is marked **unresolved** — a third round of rewording will not make a self-comparison independent. | `VOID_converter` | BS-6 |"
if bs2v_old not in text:
    print("Warning: bs2v_old not found")
text = text.replace(bs2v_old, bs2v_new)

# Blocker 2: BS-2v has no authenticated receipt schema in §11
bs2v_schema_old = "- **`VOID` conversion:** Implement a converter (`BS-2v`) that handles every enumerated void antecedent. It must define a canonical closed antecedent registry with stable IDs and exact source/phase/failure-effect for each `VOID` branch. It requires a fixture coverage receipt that verifies exact set equality between manifest IDs and exercised IDs. Missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate. This is a pre-BS-6 dependency."
bs2v_schema_new = "- **`VOID` conversion:** Implement a converter (`BS-2v`) that handles every enumerated void antecedent. It must define a canonical closed antecedent registry with stable IDs and exact source/phase/failure-effect for each `VOID` branch. The receipt must conform to a **canonical authenticated receipt schema**, including: registry digest, converter implementation digest, ordered normative IDs, exercised IDs, uniqueness and count closure, per-ID source/phase/failure-effect, and result classification (all authenticated). The gate must compare the converter's emitted IDs and the exercised fixture IDs against the pinned §7.1 digest's contents. Missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate. This is a pre-BS-6 dependency."
if bs2v_schema_old not in text:
    print("Warning: bs2v_schema_old not found")
text = text.replace(bs2v_schema_old, bs2v_schema_new)

# Change 4: §10 trace replacement
with open('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/gates/GENERATED_TRACE.md', 'r') as f:
    generated_trace = f.read()

section_10_reason = "The finding→change mapping required by §6.3 is now expressed as finding IDs referenced from the referee reports. A characterisation of a change can be falsified by a later edit without the sentence changing, as happened when the V16→V17 row went from accurate to inaccurate untouched. An observation of what the bytes did cannot be falsified, so this table expresses only what the bytes did.\n\n"

# Find the start of §10
start_10 = text.find("## §10 Gate plan and repair trace")
# Find the start of the next section
end_10 = text.find("Next: both referee seats on this text", start_10)

if start_10 != -1 and end_10 != -1:
    old_sec_10 = text[start_10:end_10]
    new_sec_10 = "## §10 Gate plan and repair trace\n\n" + section_10_reason + generated_trace + "\n\n"
    text = text.replace(old_sec_10, new_sec_10)
else:
    print("Could not find section 10 bounds")

# Change 5: §7 counts
count_old = "(Lint assertion: the prose count equals the parsed table count and the DESIGN inventory matches the VALUE/DESIGN classification.)"
count_new = "(These class counts are emitted from the table by `tools/prereg_counts.py` and are not to be hand-edited.)"
if count_old not in text:
    print("Warning: count_old not found")
text = text.replace(count_old, count_new)

# Also update the title to V24 and base sha
text = text.replace("# PREREGISTRATION DRAFT V23", "# PREREGISTRATION DRAFT V24")

v23_repair = "> **V23 is a repair of V22.** It repairs `PREREG_SUCCESSOR_DRAFT_V22_20260827.md`, sha256\n> `9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3` — independently verified."
v24_repair = "> **V24 is a repair of V23.** It repairs `PREREG_SUCCESSOR_DRAFT_V23_20260827.md`, sha256\n> `134433199c85ea4566eab7aae146455518d92d314893b3cba7a6a413163454b7` — independently verified."
text = text.replace(v23_repair, v24_repair)

out_path = '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V24_20260827.md'
with open(out_path, 'w') as f:
    f.write(text)

h = hashlib.sha256(text.encode('utf-8')).hexdigest()
print(f"sha256: {h}")

