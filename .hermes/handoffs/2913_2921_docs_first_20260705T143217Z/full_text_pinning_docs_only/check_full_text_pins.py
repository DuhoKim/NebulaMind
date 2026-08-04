#!/usr/bin/env python3
"""Verify docs-only 2913/2921 full-text pins without DB or SQL.

Reads FULL_TEXT_PINNING_PACKET.json and local extracted PDF text files.
Checks: source text hashes, quote offsets, quote membership, and no SQL/apply artifacts
inside this docs-only pinning directory.
"""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path
ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind')
PIN_DIR = ROOT/'.hermes/handoffs/2913_2921_docs_first_20260705T143217Z/full_text_pinning_docs_only'
PACKET = PIN_DIR/'FULL_TEXT_PINNING_PACKET.json'

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    pkt=json.loads(PACKET.read_text())
    failures=[]
    for source_id, meta in pkt['sources'].items():
        p=ROOT/meta['text_path']
        if not p.exists():
            failures.append(f'missing text file {source_id}: {p}')
            continue
        got=sha256(p)
        if got != meta['text_sha256']:
            failures.append(f'text sha mismatch {source_id}: {got} != {meta["text_sha256"]}')
    for pin in pkt['pins']:
        p=ROOT/pkt['sources'][pin['source_id']]['text_path']
        text=p.read_text(errors='ignore')
        quote=pin['quote']
        off=pin['char_offset']
        if text[off:off+len(quote)] != quote:
            found=text.find(quote)
            failures.append(f'quote offset mismatch evidence {pin["evidence_id"]} role {pin["role"]}; find={found} expected_offset={off}')
        if quote not in text:
            failures.append(f'quote not found evidence {pin["evidence_id"]} role {pin["role"]}')
    blocked=[]
    for path in PIN_DIR.rglob('*'):
        name=path.name.lower()
        if path.is_file() and (name.endswith('.sql') or name.startswith('apply') or 'rollback' in name or 'migration' in name):
            blocked.append(str(path))
    if blocked:
        failures.append('blocked artifact names: '+', '.join(blocked))
    out={
        'status':'PASS' if not failures else 'FAIL',
        'failures': failures,
        'pin_count': len(pkt.get('pins', [])),
        'source_count': len(pkt.get('sources', {})),
        'db_writes':0,
        'sql_apply_artifacts':0 if not blocked else len(blocked),
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    (PIN_DIR/'VERIFY_FULL_TEXT_PINNING_PACKET.json').write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    return 0 if not failures else 1
if __name__ == '__main__':
    raise SystemExit(main())
