#!/Library/Developer/CommandLineTools/usr/bin/python3
"""Metadata-only manifests. Existing outputs are verified, never overwritten.

Only GZ1_OBJID/RA/DEC prefixes of guarded_pool.csv and GZ1_OBJID of the
failed CSV are decoded. Remaining fields are discarded without CSV parsing.
Full source hashes are opaque integrity operations. No legacy code is imported.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shlex
import sys

INTERPRETER = '/Library/Developer/CommandLineTools/usr/bin/python3'
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXPECTED = {
'AGREEMENT_RUN_AMENDMENT_A1_20260907.md': '61e253cef941de58b6be805faacc12822d0a31900ae8309f160ad976618ac069',
'AGREEMENT_RUN_INPUT_CONTRACT_20260907.md': 'b2d9ecf56b78febc86cc52ecf73240f3e9c83ba11729dcd76b2dc46219b42cc9',
'OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md': 'fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1',
'_optionA_dev/corpus_identity/build_guarded_pool.py': 'e9b00ef4f50ce93c980cf6c5e0581276c46e6fa9a56ed46daa6d4eb95d2f52f3',
'_optionA_dev/corpus_identity/guarded_pool_receipt.json': '2ee4399ce791540bd1cb26a73f0bbf5a77362df9be670886811e38c171d8936d',
'_optionA_dev/corpus_identity/guarded_pool.csv': '2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155',
'scratch/survey-bricks-dr9-north.fits.gz': '2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb',
'validation_bricks/_bricks_without_r_coverage.txt': 'ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe',
'VALIDATION_SELECTION_V29_20260905.csv': '5643555c75670a695cd9144455a956440125c1019ebd1fb028a7ee21889014c7',
}

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def prefixes(path, header, count):
    """Project known unquoted numeric prefix; never decode/parse label suffix."""
    with path.open('rb') as stream:
        if stream.readline().rstrip(b'\r\n') != header:
            raise ValueError('Unexpected header: ' + str(path))
        for line in stream:
            values = []
            for _ in range(count):
                field, comma, line = line.partition(b',')
                if not comma or not field or b'"' in field:
                    raise ValueError('Malformed metadata prefix: ' + str(path))
                values.append(field.decode('ascii'))
            del line  # Includes label fields; never decoded, parsed or emitted.
            yield values


def objid(value):
    if re.fullmatch(r'[1-9][0-9]*', value) is None:
        raise ValueError('Noncanonical decimal identifier')
    return int(value)


def encode_ids(ids):
    return ''.join(str(i) + '\n' for i in sorted(set(ids))).encode('ascii')


def main():
    if Path(sys.executable).resolve() != Path(INTERPRETER).resolve():
        raise RuntimeError('Wrong interpreter')
    expected_pythonpath = str(ROOT / '_optionA_dev/_venv_bls/lib/python3.9/site-packages')
    if os.environ.get('PYTHONPATH') != expected_pythonpath or not sys.dont_write_bytecode:
        raise RuntimeError('Use the documented environment')
    import numpy as np
    from astropy.io import fits
    import astropy

    hashes = {name: digest(ROOT / name) for name in EXPECTED}
    if hashes != EXPECTED:
        raise RuntimeError('Input digest mismatch')
    receipt = json.loads((ROOT / '_optionA_dev/corpus_identity/guarded_pool_receipt.json').read_text())
    if receipt['guarded_pool_sha256'] != hashes['_optionA_dev/corpus_identity/guarded_pool.csv']:
        raise RuntimeError('Guarded pool receipt mismatch')
    pool = []
    for oid, ra, dec in prefixes(ROOT / '_optionA_dev/corpus_identity/guarded_pool.csv',
                                b'GZ1_OBJID,RA,DEC,G', 3):
        ra, dec = float(ra), float(dec)
        if not (math.isfinite(ra) and math.isfinite(dec) and 0 <= ra < 360 and -90 <= dec <= 90):
            raise ValueError('Invalid coordinate')
        pool.append((objid(oid), ra, dec))
    if len(pool) != receipt['guarded_pool_count'] or len({r[0] for r in pool}) != len(pool):
        raise RuntimeError('Pool count/uniqueness failure')
    failed_rows = [objid(r[0]) for r in prefixes(ROOT / 'VALIDATION_SELECTION_V29_20260905.csv',
                                               b'GZ1_OBJID,RA,DEC,G,DR9N_BRICK', 1)]
    failed = set(failed_rows)
    if len(failed_rows) != 2000 or len(failed) != 2000:
        raise RuntimeError('Failed source count differs from 2000')
    if not failed <= {r[0] for r in pool}:
        raise RuntimeError('Failed identifiers outside guarded pool')
    registry_rows = (ROOT / 'validation_bricks/_bricks_without_r_coverage.txt').read_text('ascii').splitlines()
    if any(re.fullmatch(r'[0-9]{4}[pm][0-9]{3}', r) is None for r in registry_rows):
        raise ValueError('Malformed no-r registry')
    registry = set(registry_rows)
    with fits.open(ROOT / 'scratch/survey-bricks-dr9-north.fits.gz', memmap=False) as hdus:
        table = hdus[1].data
        names = np.asarray(table['brickname']).copy()
        ra1, ra2, dec1, dec2 = [np.asarray(table[c], dtype=np.float64).copy()
                                for c in ('ra1', 'ra2', 'dec1', 'dec2')]
    if not all(np.isfinite(a).all() for a in (ra1, ra2, dec1, dec2)):
        raise ValueError('Nonfinite brick boundaries')
    eligible = []
    after_brick = 0
    for oid, ra, dec in pool:
        # Lower edges inclusive, upper edges exclusive, binary64 throughout.
        ra_match = np.where(ra1 <= ra2, (ra1 <= ra) & (ra < ra2),
                            (ra1 <= ra) | (ra < ra2))
        matches = np.flatnonzero(ra_match & (dec1 <= dec) & (dec < dec2))
        if len(matches) > 1:
            raise RuntimeError('Ambiguous half-open brick assignment')
        if len(matches) == 0:
            continue
        after_brick += 1
        brick = str(names[matches[0]]).strip()
        if brick not in registry:
            eligible.append(oid)
    if len(eligible) != len(set(eligible)):
        raise RuntimeError('Duplicate eligible identifier')
    payloads = {
        HERE / 'eligible_ids_20260907.txt': encode_ids(eligible),
        HERE / 'failed_set_ids_20260907.txt': encode_ids(failed),
    }
    command = ('PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=' + shlex.quote(expected_pythonpath)
               + ' ' + INTERPRETER + ' ' + shlex.quote(str(Path(__file__).resolve())))
    code_hash = digest(Path(__file__).resolve())
    lines = [
        '# Metadata-only input derivation receipt — 2026-09-07', '',
        '**Eligible count / population of the requested eligible file: %d.**' % len(eligible), '',
        'Authoring only. No pixels or evaluation labels interpreted; no anchor, round, draw, split, holdout opening or attempt.', '',
        'Scope: the current task explicitly requests the entire guarded pool restricted ONLY by brick existence and the no-r registry. '
        'No failed-set or dry-run subtraction is applied to eligible_ids. A1 describes a post-exclusion subset of 7,410 instead; '
        'this file implements the explicit current task, so its count must not be represented as that post-exclusion A1 population. '
        'The dry-run exclusion file was not read. No existing document is amended.', '',
        '## Exact command (produces both ID outputs and both reports)', '', '```sh', command, '```', '',
        'Interpreter: `%s`; Python `%s`; NumPy `%s`; Astropy `%s`.' %
        (sys.executable, sys.version.replace('\n', ' '), np.__version__, astropy.__version__), '',
        '## Counts at every stage', '',
        '| Output | Stage | Rows |', '|---|---|---:|',
        '| eligible_ids_20260907.txt | Guarded pool | %d |' % len(pool),
        '| eligible_ids_20260907.txt | After half-open brick test | %d |' % after_brick,
        '| eligible_ids_20260907.txt | After no-r registry | %d |' % len(eligible),
        '| eligible_ids_20260907.txt | Final ascending unique IDs | %d |' % len(eligible),
        '| failed_set_ids_20260907.txt | Source CSV data rows / projected IDs | %d |' % len(failed_rows),
        '| failed_set_ids_20260907.txt | After deduplication | %d |' % len(failed),
        '| failed_set_ids_20260907.txt | Final ascending unique IDs | %d |' % len(failed), '',
        'Failed-set pool/brick/no-r stages: not applicable; this output is exactly the source ID column.',
        'Pool provenance receipt: original %d; guard removed %d; guarded %d (existing receipt; not rebuilt).'
        % (receipt['pool_count'], receipt['guard_dropped_count'], receipt['guarded_pool_count']),
        'Survey-bricks rows: %d. No-r registry rows: %d; unique bricks: %d. '
        'Brick-test removals: %d; no-r removals: %d.' %
        (len(names), len(registry_rows), len(registry), len(pool)-after_brick, after_brick-len(eligible)), '',
        '## Deterministic procedure', '',
        'Read the existing guarded pool, projecting only GZ1_OBJID, RA, DEC. '
        'Apply dec1 <= DEC < dec2 and ra1 <= RA < ra2, with RA-wrap intervals using RA >= ra1 OR RA < ra2. '
        'All coordinates and boundaries use binary64. Require at most one matching survey brick; '
        'retain only matching bricks absent from the no-r registry. No exposure or checksum-catalogue filter. '
        'Project only GZ1_OBJID from the failed CSV. Sort both outputs numerically, deduplicate, and write ASCII decimal IDs with LF endings.', '',
        'Known CSV headers are checked; only the unquoted numeric prefixes are decoded. '
        'Label-bearing suffixes are discarded without parsing or display. Whole-file hashing is opaque. '
        'The legacy builder is hashed/read as provenance, never imported or executed. '
        'Reruns recompute all outputs and compare existing bytes, refusing differences without overwriting.', '',
        '## SHA-256 of every task input read', '', '| Input | SHA-256 |', '|---|---|',
    ]
    for name, value in hashes.items():
        lines.append('| `%s` | `%s` |' % (name, value))
    lines.extend(['| `%s` | `%s` |' % (INTERPRETER, digest(Path(INTERPRETER))), '',
                  'The table covers all task data and instruction/provenance inputs; package imports are the named environment, '
                  'not a claimed complete runtime dependency closure.', '',
                  '## SHA-256 of producer and generated ID outputs', '', '| Output | SHA-256 |', '|---|---|',
                  '| `%s` | `%s` |' % (Path(__file__).relative_to(ROOT), code_hash)])
    for path, data in payloads.items():
        lines.append('| `%s` | `%s` |' % (path.relative_to(ROOT), hashlib.sha256(data).hexdigest()))
    lines.extend(['', 'Both ID files use the exact command above. The script is the retained authoring source; '
                  'it is executed, not self-generated.', '',
                  'A report cannot embed its own final SHA-256 without a self-reference. '
                  'The receipt digest is in _tmp_v39_inputs_REPORT.md; the evidence-report digest is emitted on stdout. '
                  'No requested metadata count or ID digest is uncomputed. The post-exclusion A1 population is not computed '
                  'because that subtraction is outside the current output definition and its dry-run input was not read.', ''])
    receipt_path = HERE / 'INPUTS_RECEIPT_20260907.md'
    receipt_data = '\n'.join(lines).encode('utf-8')
    payloads[receipt_path] = receipt_data
    report_path = ROOT / '_tmp_v39_inputs_REPORT.md'
    payloads[report_path] = (receipt_data + ('\nReceipt SHA-256: `%s` (`%s`).\n' %
        (hashlib.sha256(receipt_data).hexdigest(), receipt_path.relative_to(ROOT))).encode('utf-8'))
    # Validate every pre-existing target before creating anything; never edit it.
    for path, data in payloads.items():
        if path.exists() and path.read_bytes() != data:
            raise RuntimeError('Refusing to change existing output: ' + str(path))
    for path, data in payloads.items():
        if not path.exists():
            with path.open('xb') as stream:
                stream.write(data)
        print(str(path.relative_to(ROOT)) + ' sha256=' + digest(path))
    print('eligible population=%d; pool=%d; after brick=%d; after no-r=%d; failed=%d' %
          (len(eligible), len(pool), after_brick, len(eligible), len(failed)))

if __name__ == '__main__':
    main()
