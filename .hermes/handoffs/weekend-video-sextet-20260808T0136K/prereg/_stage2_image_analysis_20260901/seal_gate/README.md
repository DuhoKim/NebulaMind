# Tier-C seal gate — draft V1

This unpinned, run-side draft implements the freeze-time gate prescribed by
Mini-prereg V9 §§7.9–7.11 and 16.3/16.7c. It is for referee review and must not
be treated as frozen or executable authority until a later amendment-free
freeze record pins it.

`seal_gate.py` checks the acquisition-completion set, terminal receipt state,
OK-receipt hashes, absence of the ruled acquisition process, and binds the
acquisition journal's whole-file SHA-256 and line count. It independently
fetches the one allowed NERSC checksum filename for every manifest entry,
binds the selected fetched lines in manifest order with exactly one LF each,
rehashes each on-disk file, and cross-checks the final OK receipt. Network
fetching is disabled unless `--fetch` is supplied; `run_gate()` accepts a
fetcher callable so tests never use the network.

The same single chained seal receipt includes the Git custody evidence required
by §7.11: index blob ID, SHA-256 of blob content, live script, and pinned copy,
plus the `git diff --quiet` exit status. The receipt digest follows §7.10
(canonical sorted compact JSON body, excluding `receipt_digest`, LF
terminated), and `data_integrity_pass` is derived by the §16.7c iff rule.

The gate treats an extra regular file in the bricks directory as
`DATA-INTEGRITY-FAIL`: V9 §7.8 explicitly rules that missing, **extra**,
duplicate, substituted, or hash-mismatched required files fail. The gate does
not inspect unrelated directories.

This program performs no FITS/pixel access, rendering, measurement, instrument
call, deletion, quarantine, acquisition, or write to `acquire/`. Inputs and
bricks are read-only. It emits exactly one JSON receipt to stdout and exits
nonzero with `status: REFUSE` and `verdict: DATA-INTEGRITY-FAIL` on failure;
the caller is responsible for appending that receipt to the separately
authorized chained seal journal.

Example (only after pinning and with deliberate network authorization):

```sh
python seal_gate/seal_gate.py \
  --manifest PATH/tier_c_manifest_v1.json \
  --journal PATH/tier_c_fetch_receipts.jsonl \
  --bricks-dir PATH/bricks_tier_c \
  --live-script PATH/acquire/fetch_bricks.py \
  --pinned-copy miniprereg_pins/fetch_bricks_pinned.py \
  --predecessor-digest 64_HEX_DIGEST --fetch
```

Run the isolated synthetic suite with:

```sh
cd seal_gate && python3 -m unittest -v test_seal_gate.py
```
