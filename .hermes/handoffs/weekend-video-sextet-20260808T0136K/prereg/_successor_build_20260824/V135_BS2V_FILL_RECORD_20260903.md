# V135 BS-2v fill record — 2026-09-03

V135 copies P0-signed V134 and changes only the preamble/amendment mechanism, the §7 BS-2v row, the §10 generated transition row, the §11 BS-2v inventory/build item, and the blank signature lines. No pixel was opened. V134, v9, `gates/`, `run/`, and all frozen files were not modified.

## Pins recomputed from disk

- V134: `9411fe3fa89915cca08d07da6573076af7c924d07e25416f9dd35be8eabb604f`
- P0 freeze manifest digest naming V134: `d1be4a3b61975c79f75d6bfafa75e117f69ae86e00dc81ea139a4884f62dc72a`
- §7.1 registry digest: `315ef0195d047bf22ff3164b98f7ec036d04f18869f8ab67b349fdede5ed9053`
- `gates/bs2v_void_converter.py`: `001cd94456449851a9d2f4cf0b7c857683c92129715bff5661ad5fd2a31338a4`
- `run/receipt_strict.py`: `f50d8c1d9c4c3cf80bc6ba3a32a6aaa618d79092670cdac2c79cc8b9711ddef1`
- schema: `BS2V-V1`; exact fields: `registry_digest`, `converter_sha256`, `normative_ids`, `exercised_ids`, `per_id`, `classifications`
- `run/classp_candidates/BS-2v.json`: `a1ad1790161f63e7a09f994886b61a7b38b08ab6bb863c52fe5fee665de33696`
- final V135 blank-signature-line digest: `c8f6fa4a70e82d065d86d51ae6456cec50ab4650974d1351bd49d3f59a4cdb8c`

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py PREREG_SUCCESSOR_DRAFT_V135_20260903.md`:

```text
void registry — PREREG_SUCCESSOR_DRAFT_V135_20260903.md
  antecedents      60
  §6.1 rows defined 22
  registry_digest  315ef0195d047bf22ff3164b98f7ec036d04f18869f8ab67b349fdede5ed9053
```

## Fixture outputs

```text
$ python3 gates/bs2v_void_converter.py
bs2v void converter fixtures: 13/13 green
$ python3 run/receipt_strict.py
receipt_strict fixtures: 7/7 PASS
```

## Trace generation and check

The generator was run before inserting its emitted current-transition row. Its emitted row was pasted verbatim:

```text
| V134 → V135 | `9411fe3fa89915cc` | `707b0fa9c2753d2c` | §11 (+5/−1), (preamble) (+3/−1), §7 (+1/−1) | no row-count change | **— none cited —** |
```

After insertion, rerunning `python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py .` necessarily changes the current result digest and adds the §10 insertion to the diff:

```text
| V134 → V135 | `9411fe3fa89915cc` | `715d72974d1ea124` | §11 (+5/−1), (preamble) (+3/−1), §7 (+1/−1), §10 (+1/−0) | no row-count change | **— none cited —** |
```

This is the self-reference condition V134's §10 already names. The required check was still run exactly; it failed for two independent inputs that cannot be repaired within the authorized two-file write boundary:

```text
$ python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py . --check PREREG_SUCCESSOR_DRAFT_V135_20260903.md
prereg trace check — PREREG_SUCCESSOR_DRAFT_V135_20260903.md
  MISSING: no §10 table row for V133 → V134
  SIDECAR MISSING: V134 → V135 is the current transition and is not mapped in gates/FINDINGS_MAP.md
  134 computed transition(s); 2 problem(s)
```

The first is inherited from V134. The second requires editing `gates/FINDINGS_MAP.md`, which was expressly outside the authorized write set. Therefore the hostile-referee result is NOT SIGNABLE and `TRACE_CHECK` is FAIL.

## Lint and counts

```text
$ python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py PREREG_SUCCESSOR_DRAFT_V135_20260903.md
prereg lint — PREREG_SUCCESSOR_DRAFT_V135_20260903.md
  §7 data rows: 25 (16 class P, 9 class E) — 23 carry a BS- identifier
  [string-registry-stale] the registry was generated from a different draft than the one under lint — regenerate: "**Generated from `PREREG_SUCCESSOR_DRAFT_V134_20260831.md`'s schema blocks by `r"
  98 finding(s), 1 blocking (97 advisory)

$ python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_counts.py PREREG_SUCCESSOR_DRAFT_V135_20260903.md
prereg counts — PREREG_SUCCESSOR_DRAFT_V135_20260903.md
  computed from the table: 16 class P, 9 class E (23 rows carry a BS- identifier)
  prose says filled: BS-2m  (not computed — a claim about receipts, not rows)
  prose already matches the table
```

The lint block requires a §7.1 edit, also outside the enumerated V135 changes. The 97 legacy advisories are summarized rather than duplicated here; the command's terminal count is pasted.

## Diff hunk headers

```text
@@ -1,5 +1,7 @@
@@ -927,7 +929,7 @@
@@ -1155,6 +1157,7 @@
@@ -1239,6 +1242,7 @@
@@ -1604,4 +1608,7 @@
```

SEAT: CODEX
VERSION: SUCCESSOR-DRAFT-V135
HUNKS: preamble; §7; §10; §11
TRACE_CHECK: FAIL

## Repairs R1-R3

Hwao's mechanical-repair ruling was applied before referee dispatch or signature. R1 replaces the
impermissible current-transition row with the generator's verbatim `V133 → V134` row. R2 maps
`V134 → V135` in `gates/FINDINGS_MAP.md` to `PRINCIPAL-20260903-1B2B`; grep confirms that
`gates/FINDINGS_MAP.md` is absent from `P0_PACKAGE_MANIFEST_20260831.txt`. R3 ran the generator named
by the full registry label exactly against V135; its generated block now names V135. V134, v9, and
run receipts remain byte-unchanged. No pixel was opened.

Generator and verification outputs:

```text
$ python3 ref/gen_string_field_registry.py PREREG_SUCCESSOR_DRAFT_V135_20260903.md
fields found 315  classified 315  FORBIDDEN-BY-DEFAULT 0  stale 0

$ python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py . --check PREREG_SUCCESSOR_DRAFT_V135_20260903.md
prereg trace check — PREREG_SUCCESSOR_DRAFT_V135_20260903.md
  134 computed transition(s); 0 problem(s)

$ python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py PREREG_SUCCESSOR_DRAFT_V135_20260903.md
prereg lint — PREREG_SUCCESSOR_DRAFT_V135_20260903.md
  §7 data rows: 25 (16 class P, 9 class E) — 23 carry a BS- identifier
  97 finding(s), 0 blocking (97 advisory)

$ python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_counts.py PREREG_SUCCESSOR_DRAFT_V135_20260903.md
prereg counts — PREREG_SUCCESSOR_DRAFT_V135_20260903.md
  computed from the table: 16 class P, 9 class E (23 rows carry a BS- identifier)
  prose says filled: BS-2m  (not computed — a claim about receipts, not rows)
  prose already matches the table

$ python3 /Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py PREREG_SUCCESSOR_DRAFT_V135_20260903.md
void registry — PREREG_SUCCESSOR_DRAFT_V135_20260903.md
  antecedents      60
  §6.1 rows defined 22
  registry_digest  315ef0195d047bf22ff3164b98f7ec036d04f18869f8ab67b349fdede5ed9053

$ python3 gates/bs2v_void_converter.py
bs2v void converter fixtures: 13/13 green

$ python3 run/receipt_strict.py
receipt_strict fixtures: 7/7 PASS
```

Post-repair V134→V135 draft diff hunk headers, with the generated registry sidecar hunk recorded
between §7 and §10 in the revision machinery:

```text
@@ -1,4 +1,6 @@                         preamble
@@ -927,7 +929,7 @@                     §7
@@ -1,6 +1,6 @@                         §7.1 generated block (`ref/STRING_FIELD_REGISTRY.md`)
@@ -1155,6 +1157,7 @@                   §10
@@ -1239,6 +1242,7 @@                   §11
@@ -1604,4 +1608,7 @@                   signature lines
```

Final V135 blank-signature-line digest: `c8f6fa4a70e82d065d86d51ae6456cec50ab4650974d1351bd49d3f59a4cdb8c`.

SEAT: CODEX
VERSION: SUCCESSOR-DRAFT-V135-R
TRACE_CHECK: PASS
LINT_BLOCKING: 0
DIGEST: c8f6fa4a70e82d065d86d51ae6456cec50ab4650974d1351bd49d3f59a4cdb8c

## Repair R4 (Hwao, 2026-09-03 12:1x KST) — agy V135-REFEREE-V1 finding 1 (wording-only, BLOCKING)
Preamble line 3: appended the two precedent constraints agy required, verbatim from its EXACT REPAIR:
"A mismatch is not a signature. The repository holds no cryptographic proof of a chat statement."
Applied by the coordinator (a quoted wording insertion, no design content), disclosed here; re-referee follows.
Trace check: 0 problems. Lint: 0 blocking. New V135 digest (SIGNATURE UTC and DUHO SIGNATURE lines blank): `0a09ba938e42412860a55d70f12c640d1f56c4e2801486a8dc200f3017a84598`.
