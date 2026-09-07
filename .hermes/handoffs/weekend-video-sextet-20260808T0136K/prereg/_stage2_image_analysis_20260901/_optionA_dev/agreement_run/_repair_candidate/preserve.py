"""Opaque byte snapshots only; no study inputs are decoded or selected."""
import hashlib
import json
from pathlib import Path
import sys

LANE = Path.cwd()
BASE = LANE / '_optionA_dev/agreement_run'
OUT = BASE / '_repair_candidate'

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return {'sha256': h.hexdigest(), 'bytes': path.stat().st_size}

def snapshot():
    core = json.loads((BASE / 'INPUT_MANIFEST_A1_CORE.json').read_bytes())
    paths = {LANE / rel for rel in core['code']}
    paths.update(BASE.glob('*.py'))
    paths.update(BASE / name for name in ('INPUT_MANIFEST_A1_CORE.json',
        'RUNTIME_PINS_A1_CORE.json', 'INPUT_FREEZE_C_20260907.json'))
    paths.update(LANE / name for name in ('AGREEMENT_RUN_AMENDMENT_A1_20260907.md',
        'SEED_REFUSED_RUNTIME_REGISTRATION_20260907.md', 'A1_ADOPTION_RECORD_20260907.md'))
    paths.add(Path('/Users/duhokim/work/Trio/hwao-network-runtime-repair-20260907.md'))
    journals = {}
    for name in ('OUT_A1', 'OUT_A1_FRESH'):
        rows = {str(p.relative_to(LANE / name)): digest(p)
                for p in sorted((LANE / name).rglob('*')) if p.is_file()}
        # Digest of canonical relative-path / size / content-digest manifest.
        raw = json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()
        journals[name] = {'files': rows, 'manifest_sha256': hashlib.sha256(raw).hexdigest()}
    return {'files': {str(p): digest(p) for p in sorted(paths)}, 'journals': journals}

current = snapshot()
if sys.argv[1] == 'before':
    with (OUT / 'preservation.before.json').open('x') as stream:
        json.dump(current, stream, indent=2, sort_keys=True)
    print('BASELINE-SAVED', len(current['files']), 'files;',
          {n: j['manifest_sha256'] for n, j in current['journals'].items()})
else:
    before = json.loads((OUT / 'preservation.before.json').read_bytes())
    (OUT / 'preservation.after.json').write_text(json.dumps(current, indent=2, sort_keys=True))
    assert before == current, 'PRESERVATION-MISMATCH'
    print('BYTE-IDENTICAL', len(current['files']), 'files;',
          {n: j['manifest_sha256'] for n, j in current['journals'].items()})
