# GPT1 BRIEF — DR10.1 south sweep-catalog inventory (receipted, listing-only)

You are seat gpt1 in Hwao's successor-build lane. Read this whole brief before acting.

## Mission

Produce a complete inventory of the Legacy Surveys **DR10 south sweep catalog files** (the
version used for DR10.1 photometry — determine which subdirectory that actually is by reading
the portal listings, do not assume) with, per file: URL, filename, size in bytes. This inventory
is the input for a later paced catalog fetch; you fetch NO catalog files yourself.

## Where to look

Start at `https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/` and read the
directory listing(s). If there are versioned subdirectories (e.g. `10.0/`, `10.1/`), inventory
each and say in your receipt which exists and what distinguishes them per the listing. If a
listing does not show sizes, use HTTP HEAD requests — politely: sequential, about one request
per second, and if you need per-file HEADs for a large set, cap at the listing pages plus a
10-file HEAD spot-check and record sizes as absent for the rest rather than hammering.

## Deliverables (write ONLY inside this directory, `gpt1/`)

1. `sweep_inventory.jsonl` — one JSON object per file: `{"url": ..., "filename": ...,
   "size_bytes": <int or null>}`.
2. `DONE_GPT1.md` — your receipt. Every count in it must be produced by a command shown with
   its output (e.g. `wc -l sweep_inventory.jsonl`), never typed from memory. Include: which
   sweep version directories exist, file count per directory, total bytes where known, the
   commands you ran, and a `shasum -a 256 sweep_inventory.jsonl` line. If something was not
   enumerated (timeout, listing truncation), SAY SO explicitly — never present a partial
   inventory as complete.

## Hard boundaries

- Write only inside `gpt1/`. Temp files: `gpt1/_tmp_*`.
- No bulk downloads: directory listings and at most ~10 HEAD requests.
- No API keys, no paid services, no credentials of any kind.
- Do not read or modify anything under `_tori_transfer_20260819/`, `_sharded_20260823/`, or
  `/Users/duhokim/NebulaMindData/`.
- When finished, the LAST thing you write is `DONE_GPT1.md` (it is the completion marker).
