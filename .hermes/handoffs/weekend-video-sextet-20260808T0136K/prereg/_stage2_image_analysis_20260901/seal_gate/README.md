# Tier-C seal gate — draft V4

This unpinned, run-side draft implements the freeze-time gate prescribed by
Mini-prereg V11 §§7.9–7.11 and 16.3/16.7c. It is for referee review and must not
be treated as frozen or executable authority until a later amendment-free
freeze record pins it.

`seal_gate.py` checks the three-plane acquisition-completion set (image-r,
maskbits, and nexp-r), terminal receipt state in each plane journal,
OK-receipt hashes, absence of the ruled acquisition process, and binds the
acquisition journal's whole-file SHA-256 and line count. It independently
fetches the one allowed NERSC checksum filename for every manifest brick,
binds all three selected fetched lines in manifest/plane order with exactly one
LF each, rehashes every on-disk plane file, and cross-checks each final OK
receipt. Network
fetching is disabled unless `--fetch` is supplied; `run_gate()` accepts a
fetcher callable so tests never use the network.

The V4 journal parser accepts exactly the four receipt verdicts and shapes
written by the pinned acquisition script. `OK`, `OK-NO-PUBLISHED-SHA`, and
`SHA-MISMATCH-QUARANTINED` require exactly the seven keys `brick`, `bytes`,
`computed_sha256`, `published_sha256`, `url`, `utc`, and `verdict`;
`FETCH-FAILED` requires exactly `brick`, `error`, `url`, `utc`, and `verdict`.
An `OK` must have a non-null published digest equal to its computed digest.
`OK-NO-PUBLISHED-SHA` must have a null published digest and is treated as
non-OK for completion: like every non-OK receipt, it is admissible only when a
later `OK` exists for the same brick. Unknown verdicts and wrong shapes refuse
as `malformed_journal_schema`.

The V2 referee ruling rejects a checksum-name fallback: V10 §7.11 says
that the seal check MUST fetch
`legacysurvey_dr10_south_coadd_<AAA>_<brick>.sha256sum` at the §2.14 URL. The
three-name fallback in the pinned acquisition script is acquisition-time
behavior and is deliberately not copied into this seal gate.

The same single chained seal receipt includes the Git custody evidence required
by §7.11: the index blob ID must equal the default pinned value
`df704bed1c5fd872cf9dee9f4be2e88f64bb94a0` (overridable only via
`--expected-blob-id`), and the receipt binds the SHA-256 of blob content, live
script, pinned copy, plus the `git diff --quiet` exit status. The receipt digest follows §7.10
(canonical sorted compact JSON body, excluding `receipt_digest`, LF
terminated), and `data_integrity_pass` is derived by the §16.7c iff rule.

`--seal-journal PATH` supplies the distinct chained seal journal. An absent or
empty file gives the §7.10 genesis predecessor of 64 zeroes. Otherwise the
predecessor is the last canonical record's `receipt_digest`, after that record's
digest is recomputed and verified. A malformed, non-canonical, or mismatched
last record refuses as `seal_journal_chain_broken`. By default the gate only
prints its receipt. `--append` is required to append it to the seal journal, so
tests and dry runs do not write.

The gate treats an extra regular file in the bricks directory as
`DATA-INTEGRITY-FAIL`: V10 §7.8 explicitly rules that missing, **extra**,
duplicate, substituted, or hash-mismatched required files fail. The gate does
not inspect unrelated directories.

This program performs no FITS/pixel access, rendering, measurement, instrument
call, deletion, quarantine, acquisition, or write to `acquire/`. Inputs and
bricks are read-only. It emits exactly one JSON receipt to stdout and exits
nonzero with `status: REFUSE` and `verdict: DATA-INTEGRITY-FAIL` on failure.
Unexpected exceptions are converted to refusal receipts whose reason names the
exception class and message.

Example (only after pinning and with deliberate network authorization):

```sh
python seal_gate/seal_gate.py \
  --manifest PATH/tier_c_manifest_v1.json \
  --journal PATH/tier_c_fetch_receipts.jsonl \
  --bricks-dir PATH/bricks_tier_c \
  --live-script PATH/acquire/fetch_bricks.py \
  --pinned-copy miniprereg_pins/fetch_bricks_pinned.py \
  --seal-journal PATH/tier_c_seal_receipts.jsonl \
  --fetch
```

Add `--append` only for the authorized seal-journal write.

Run the isolated synthetic suite with:

```sh
cd seal_gate && python3 -m unittest -v test_seal_gate.py
```
