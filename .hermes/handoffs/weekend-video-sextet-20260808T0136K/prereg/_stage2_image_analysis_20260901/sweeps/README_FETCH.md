# DR10-south sweep fetcher

`fetch_sweeps.py` acquires only the manifest entries serving footprint (a). It
streams each response to a `.part` file, verifies it against the NERSC
release-wide published SHA-256 list fetched once at startup, and only then
renames it into `sweeps/data/`. It does not open FITS files or inspect pixels.

For compatibility with the exact V11 §7.9 acquisition-receipt shapes, the
field named `brick` contains the sweep filename; that filename is the identity
key for sweep acquisition. Failed attempts are journaled as `FETCH-FAILED`.
Digest mismatches are moved to `sweeps/quarantine/` and journaled as
`SHA-MISMATCH-QUARANTINED`.

From the preregistration directory, Hwao can launch the ruled fetch with stdin
closed and a persistent combined log:

```sh
nohup python3 sweeps/fetch_sweeps.py \
  --manifest sweeps/sweep_manifest_v1.json --footprint a \
  --dest sweeps/data --journal sweeps/sweep_fetch_receipts.jsonl \
  --workers 8 --delay 0.2 --timeout 600 \
  --published-hashes https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/10.0/legacysurvey_dr10_south_sweep_10.0.sha256sum \
  </dev/null >sweeps/sweep_fetch.log 2>&1 &
```

Preview the selected plan without fetching the checksum list or any payload:

```sh
python3 sweeps/fetch_sweeps.py --footprint a --dry-run
```

Use `--limit N` for a bounded acquisition test. A present file is skipped only
after its SHA-256 is recomputed and matches the published release list.
