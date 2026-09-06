# SIGNATURE RECORD — option A selection rule V15 — 2026-09-06

**Signed document:** `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md` — file NOT modified by this record (see "Stop" below).

**Duho's verbatim words (chat, relayed by Blanc 2026-09-06 09:04 KST):**
> V15 signed: fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1

**SIGNATURE UTC (T_sign), stamped by Blanc from `date -u` at relay time:** 2026-09-06T00:04:07Z
**Relay timestamp:** 2026-09-06 09:04 KST (Blanc, chat channel). Blanc recomputed the on-disk digest before sending: equal.

## Independent hash checks by Hwao (2026-09-06 09:05:53 KST below), all on the untouched file
| route | result |
|---|---|
| `shasum -a 256` on disk | fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1 |
| Python `hashlib.sha256` on disk | fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1 |
| `miniprereg_pins/signature_preimage.py` (DUHO SIGNATURE blanked; UTC line as on disk = blank) | fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1 |
| git blob at HEAD 2b89536d6 on `feat/paper-workflow-v2` (pushed 04:07 KST, before the signature) | fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1 |
| both V15 seat reports, first line ACCESS_SHA | fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1 |

All five equal the digest Duho stated. **The digest he signed is the digest of the file exactly as gated.**

## Derived, from the signed formula (no beacon read performed)
T_pulse = first whole minute ≥ T_sign + 600 s = 2026-09-06T00:15:00Z (09:15 KST). NOT fetched. `beacon_record.collect` refuses before T_pulse and runs at any later time; NIST archives every pulse; RETRY governs until T_pulse + 24 h = 2026-09-07T00:15:00Z, after which the drand fallback applies if NIST is still not authenticable. No clock in the signed text expires by waiting for decision 4.

## Stop — the §17 two-step instruction cannot be followed on THIS document without changing what was signed
The relay says: fill SIGNATURE UTC first, then run `signature_preimage.py`, stop on mismatch. The helper blanks ONLY the `DUHO SIGNATURE:` line; the `SIGNATURE UTC:` line is inside the preimage. Proven on a scratch copy (deleted): with `SIGNATURE UTC: 2026-09-06T00:04:07Z` written in, the preimage becomes e607e95582a4d19874e66de2bdc5c8ae77d1c3ef7729c17a56da032390f988b8 ≠ fdd9eedd…. So the two-step procedure would report a mismatch by construction, and writing the UTC into the file would also change `rule_sha256`, the digest that the signed text itself binds every later step to (`beacon_record.collect(fetch, T_sign, rule_sha256, statement_bytes, now)` refuses a statement that does not contain the rule digest and T_sign; the builder refuses `REFUSE-RULE-DIGEST`).

The signed text's own definition, §10 order step (1), verbatim: "This rule is signed: Duho's chat statement of its digest with UTC T_sign, retained verbatim as Blanc's relay text." That is satisfied by the words above plus the UTC. Under that definition the signature lives in the statement (this record), and the file stays byte-identical at fdd9eedd….

Not reconciled by Hwao. Per the relay: STOPPED, told Blanc. V15 untouched; no beacon read; nothing else executed.
