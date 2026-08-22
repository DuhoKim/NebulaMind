# Producer digest cross-check — Dustin Lang's list vs our transfer receipts

Hwao, 2026-08-22 20:29 KST. Task 26. **Preliminary run over the in-flight transfer; final run at completion.**

## Provenance

Dustin Lang delivered the offered list at 2026-08-22 03:41 KST (message `1a025a1349c92086`),
served from `portal.nersc.gov/project/cosmo/temp/dstn/` — a **temp directory**, so both files
were archived here immediately:

| file | bytes | lines | sha256 (16) |
|---|---|---|---|
| `dr10-r.txt` | 18,845,226 | 330,618 | `210ad0b5640559cc` |
| `dr10-r-path.sha256sum` | 40,666,014 | 330,618 | `e2f6adbe64e93ca5` |

330,618 entries — the full DR10-South r-band tree, of which our working set of 60,308 bricks is
the parent-bearing subset.

## Result of this run

    accepted 20,929   match 20,929   problem 0

Every brick accepted so far verifies against the producer's independent digest. Our transport
already checks each file against the published per-directory `.sha256sum`; this is a second
opinion produced by the data's author from the filesystem at NERSC, so agreement means:
tree-published digest, producer's filesystem digest, and our received bytes are one value,
20,929 times.

Rerun: `python3 crosscheck.py` (exits non-zero on a problem). Final run happens when the
transfer completes; only then does this become the full-sample claim for the paper's custody
paragraph.

## One comparison artifact, disclosed

The first run reported 140 bricks "not in Dustin's list". **They were in the list.** Those lines
use sha256sum's binary-mode format (`hash *path`) and the parser kept the `*` on the path. The
fix is in `crosscheck.py` with a comment; the phantom rows were all extreme-south bricks only
because that is where binary-mode lines happened to sit. Same failure class as the sign-format
false positive Blanc disclosed in their ASR sweep — the comparator, not the data.

## Boundary

Checksum text only; zero image bytes fetched beyond the two list files; no chi touched.
