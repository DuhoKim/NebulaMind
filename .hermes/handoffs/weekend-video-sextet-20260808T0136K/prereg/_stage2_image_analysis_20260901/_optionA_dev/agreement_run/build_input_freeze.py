#!/Library/Developer/CommandLineTools/usr/bin/python3
"""Bounded C authoring preflight for the 2026-09-07 dispatch.

Rehash current, explicitly registered files only. Never import run_path or
execute a study stage. Under this dispatch EVERY obligation needs concrete
members now; A1's necessarily future members therefore cause a refusal.
No partial C is written on refusal. The report is the blocked deliverable.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import sys
import unittest
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CORE = HERE / 'INPUT_MANIFEST_A1_CORE.json'
RUNTIME = HERE / 'RUNTIME_PINS_A1_CORE.json'
OUTPUT = HERE / 'INPUT_FREEZE_C_20260907.json'
REPORT = ROOT / '_tmp_c_freeze_REPORT.md'
INTERPRETER = '/Library/Developer/CommandLineTools/usr/bin/python3'
ADOPTED = '6b9ecc79210046fa4c6611953184ece75818214bf4e962e4ac2e308243616e9f'
# Exact permitted snapshot: a changed register cannot introduce new data reads.
CORE_SHA = 'e9222abf13485a36017d09dbd5be4c50597478882acc773626102416f9a26710'
RUNTIME_SHA = '73145a0600a11548018eb3763ce1d1d880d6b882ee9f349da88bc0e7b4e4c5e3'
ADOPTION_SHA = '672e3547776691fca450252c9cf6f6d8fdc5969a98055a10c509725483da5487'
GROUP_MAP = {
    'INPUT_ANCHOR': ['INPUT_ANCHOR'],
    'UNFIXED_DRAW_AND_BEACON_RECORD_PATHS': [
        'DESIGNATION_AND_SEED_EVIDENCE', 'DRAW_RECORD_AND_LISTS'],
    'UNFIXED_STAGE_DATA_READ_PATHS': ['STAGE_ACCESS_DATA_AND_REUSED_OUTPUTS'],
    'UNFIXED_TUNING_EVIDENCE_PATHS': ['STAGE_ACCESS_DATA_AND_REUSED_OUTPUTS'],
    'UNFIXED_WINNER_CONFIG_PATH': ['WINNER_AND_WINNER_FREEZE'],
}


class Blocked(ValueError):
    pass


def fingerprint(path):
    path = Path(path)
    if not path.is_file():
        raise Blocked('MISSING-FILE: ' + str(path))
    h, size = hashlib.sha256(), 0
    try:
        with path.open('rb') as stream:
            for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
                size += len(block)
                h.update(block)
    except OSError as exc:
        raise Blocked('UNREADABLE-FILE: ' + str(path) + ': ' + str(exc)) from exc
    return dict(path=str(path), resolved_path=str(path.resolve()),
                bytes=size, sha256=h.hexdigest())


def verify_pin(pin):
    path, expected = pin.get('path'), pin.get('sha256')
    if not isinstance(path, str) or not Path(path).is_absolute():
        raise Blocked('MISSING-ACTUAL-PATH: ' + str(path))
    if not isinstance(expected, str) or not re.fullmatch('[0-9a-f]{64}', expected):
        raise Blocked('MISSING-DIGEST: ' + path)
    actual = fingerprint(path)
    for key in ('sha256', 'bytes', 'resolved_path'):
        if key in pin and actual[key] != pin[key]:
            raise Blocked('%s-MISMATCH: %s; expected=%s; actual=%s' %
                          (key.upper(), path, pin[key], actual[key]))
    return actual


def checked_json(path, expected):
    # Verify the same bytes decoded, rather than reopening after verification.
    raw = path.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected:
        raise Blocked('SHA256-MISMATCH: ' + str(path) + '; actual=' + actual)
    return json.loads(raw)


def unresolved_groups(core):
    """Do not treat a template, a readiness flag or a missing row as evidence."""
    rows = core.get('placeholders', [])
    expected = {name for names in GROUP_MAP.values() for name in names}
    names = [row.get('name') for row in rows]
    problems = []
    for name in sorted(expected | set(names)):
        matches = [row for row in rows if row.get('name') == name]
        if name not in expected or len(matches) != 1:
            problems.append('OBLIGATION-MEMBERSHIP: %s; rows=%d' % (name, len(matches)))
            continue
        row = matches[0]
        members = row.get('members', [])
        for index, member in enumerate(members):
            path, digest = member.get('path'), member.get('sha256')
            if (not isinstance(path, str) or not Path(path).is_absolute() or
                    not isinstance(digest, str) or
                    re.fullmatch('[0-9a-f]{64}', digest) is None):
                label = member.get('binding') or member.get('path_template') or '(unspecified)'
                problems.append('UNEXPANDED-OBLIGATION: %s.members[%d] %s; '
                                'actual path and individual SHA-256 absent; due=%s' %
                                (name, index, label, row.get('due_stage')))
        if not members:
            problems.append('EMPTY-OBLIGATION: ' + name)
    return problems


def require_complete(core):
    problems = unresolved_groups(core)
    if problems:
        raise Blocked('\n'.join(problems))


def audit_current(core, runtime):
    groups = {
        'CORE current files': core['files'],
        'Runtime interpreter and explicit extensions': runtime['files'],
        'Runtime representation individual files': runtime['representation']['files'],
        'Runtime complete dyld cache family': runtime['representation']['cache_bytes']['files'],
        'Input aliases': list(core['inputs'].values()),
        'Code aliases': [dict(path=str(ROOT / p), sha256=h) for p, h in core['code'].items()],
        'Adopted procedure and source registers': [
            dict(path=str(ROOT / 'AGREEMENT_RUN_AMENDMENT_A1_20260907.md'), sha256=ADOPTED),
            dict(path=str(ROOT / 'A1_ADOPTION_RECORD_20260907.md'), sha256=ADOPTION_SHA),
            dict(path=str(CORE), sha256=CORE_SHA),
            dict(path=str(RUNTIME), sha256=RUNTIME_SHA)],
        'Required failed-ID provenance (opaque hash only)': [
            dict(path=str(ROOT / 'VALIDATION_SELECTION_V29_20260905.csv'),
                 sha256='5643555c75670a695cd9144455a956440125c1019ebd1fb028a7ee21889014c7'),
            dict(path=str(HERE / 'inputs/INPUTS_RECEIPT_20260907.md'),
                 sha256='6f6e3857d73fbc1bee1f2d60af3f9a3368a665f14a600c0f573f1a194bee81cf')],
    }
    verified, failures = {}, []
    # Every distinct listed path is freshly streamed; repeated aliases must agree.
    for group, pins in groups.items():
        for pin in pins:
            path = pin['path']
            try:
                if path not in verified:
                    verified[path] = dict(verify_pin(pin), groups=[])
                for key in ('sha256', 'bytes', 'resolved_path'):
                    if key in pin and pin[key] != verified[path][key]:
                        raise Blocked('ALIAS-%s-MISMATCH: %s' % (key.upper(), path))
                if group not in verified[path]['groups']:
                    verified[path]['groups'].append(group)
            except (Blocked, OSError) as exc:
                failures.append(str(exc))
    selections = []
    for name in ('eligible', 'exclusion', 'failed'):
        pin = core['inputs'][name]
        raw = Path(pin['path']).read_bytes()
        lines = raw.splitlines()
        if hashlib.sha256(raw).hexdigest() != pin['sha256']:
            failures.append('SELECTION-RECHECK-MISMATCH: ' + pin['path'])
        if not lines or any(re.fullmatch(rb'[1-9][0-9]*', line) is None for line in lines):
            failures.append('MALFORMED-IDS: ' + pin['path'])
        elif len({int(line) for line in lines}) != len(lines):
            failures.append('DUPLICATE-IDS: ' + pin['path'])
        elif name in ('eligible', 'failed') and list(map(int, lines)) != sorted(map(int, lines)):
            failures.append('UNSORTED-IDS: ' + pin['path'])
        selections.append(dict(name=name, path=pin['path'], sha256=hashlib.sha256(raw).hexdigest(),
                               ids=len(lines), bytes=len(raw)))
    return sorted(verified.values(), key=lambda p: p['path']), selections, failures


def main():
    if (Path(sys.executable).resolve() != Path(INTERPRETER).resolve() or
            os.environ.get('PYTHONPATH') != str(ROOT / '_optionA_dev/_venv_bls/lib/python3.9/site-packages') or
            not sys.dont_write_bytecode):
        raise Blocked('Use the specified interpreter/PYTHONPATH and PYTHONDONTWRITEBYTECODE=1.')
    log, pins, selections, failures = [], [], [], []
    core = None
    capture = io.StringIO()
    suite = unittest.defaultTestLoader.discover(str(HERE), pattern='test_build_input_freeze.py')
    tests = unittest.TextTestRunner(stream=capture, verbosity=2).run(suite)
    if not tests.wasSuccessful():
        failures.append('SELF-TEST-FAILED')
    try:
        core = checked_json(CORE, CORE_SHA)
        runtime = checked_json(RUNTIME, RUNTIME_SHA)
        verify_pin(dict(path=str(ROOT / 'AGREEMENT_RUN_AMENDMENT_A1_20260907.md'), sha256=ADOPTED))
        pins, selections, pin_failures = audit_current(core, runtime)
        failures.extend(pin_failures)
        log.append('CURRENT-PIN-VERIFICATION: %d unique paths rehashed; %d failure(s)' %
                   (len(pins), len(pin_failures)))
        for row in selections:
            log.append('SELECTION-INPUT: {name}; ids={ids}; bytes={bytes}; sha256={sha256}; path={path}'.format(**row))
        # This dispatch cannot pass while actual future members are unavailable.
        require_complete(core)
        failures.append('FUTURE-DATA-READ-EXCLUDED: this bounded authoring tool does not read later-stage data.')
    except (Blocked, OSError, ValueError, KeyError) as exc:
        failures.extend(str(exc).splitlines())
    log.extend(failures)
    log.append('C-WRITTEN: false; no complete C exists and no C digest is claimed')
    log.append('INPUT-FREEZE-BLOCKED')
    lines = ['# INPUT FREEZE C preparation — 2026-09-07', '',
             'Authoring result: **INPUT-FREEZE-BLOCKED**. C was not created.', '',
             'Checked at UTC: ' + datetime.now(timezone.utc).isoformat(), '',
             'Adopted procedure SHA-256: `' + ADOPTED + '`; adoption is recorded separately in '
             '`A1_ADOPTION_RECORD_20260907.md`. Adopted A1 bytes were not edited.', '',
             'Exact blocker: CORE supplies null group paths/digests and member templates or binding names '
             'for five future groups. These are not actual individually hashed artefacts. '
             'The dispatch requires EVERY group expanded now. A1 lines 84–98 says future seed/draw/winner '
             'digests cannot exist at C and must not be fabricated. This is not a finding that A1 itself '
             'requires later-stage artefacts before C, and does not call for changing adopted A1.', '',
             'No output directory or run-specific member inventory is supplied for these groups. '
             'No archive, fixture, unrelated run or protected-data file was searched for substitutes. '
             'Absence here means absence of actual bindings in the supplied current inventory; '
             'it is not a claim that no historical file exists anywhere.', '',
             'C commit ID: no git was used; the requested field would be '
             '`TO_BE_FILLED_AT_ANCHORING` in a complete C. No C digest is available.', '',
             'Only the required historical failed-source CSV was opaquely hashed for provenance; '
             'no labels were decoded, no protected stage data were opened, and no run code was imported '
             'or executed. No anchor, publication, designation, selection, draw or holdout access occurred.', '',
             'This routine verifies file existence, sizes, resolved paths and SHA-256 values. '
             'It does not certify runtime loading, code-object correspondence or scientific readiness. '
             'File verification is at check time, without a filesystem lock.', '',
             '## Reproduction', '', '```sh',
             'PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=' + str(ROOT / '_optionA_dev/_venv_bls/lib/python3.9/site-packages') +
             ' ' + INTERPRETER + ' -B ' + str(Path(__file__).resolve()), '```', '',
             '## Verifier output (verbatim)', '', '```text', *log, '```', '',
             '## Test output (verbatim)', '', '```text', capture.getvalue().rstrip(), '```', '',
             '## A1 obligation correspondence', '',
             '| A1 obligation | CORE obligation group(s) |', '|---|---|']
    for a1, names in GROUP_MAP.items():
        lines.append('| `' + a1 + '` | ' + ', '.join('`' + name + '`' for name in names) + ' |')
    if core:
        lines.extend(['', '## Unresolved member evidence from CORE', ''])
        for row in core['placeholders']:
            lines.extend(['### ' + row['name'], '', 'Due: ' + row['due_stage'] + '.', '',
                          row['reason'], '', '```json', json.dumps(row['members'], indent=2), '```', ''])
    lines.extend(['', '## Expanded current inventory — individually recomputed', '',
                  'These verified current files do not discharge the unresolved future groups.', '',
                  '| Actual absolute path | Bytes | Current SHA-256 | Inventory membership |', '|---|---:|---|---|'])
    for pin in pins:
        lines.append('| `{path}` | {bytes} | `{sha256}` | {groups} |'.format(
            **dict(pin, groups='; '.join(pin['groups']))))
    lines.extend(['', 'C SHA-256: unavailable; C was not created.', '',
                  'INPUT-FREEZE-BLOCKED — actual paths and individual digests are absent from CORE for '
                  'INPUT_ANCHOR, DESIGNATION_AND_SEED_EVIDENCE, DRAW_RECORD_AND_LISTS, '
                  'STAGE_ACCESS_DATA_AND_REUSED_OUTPUTS, and WINNER_AND_WINNER_FREEZE.'])
    REPORT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(log))
    print('REPORT: ' + str(REPORT))
    return 2


if __name__ == '__main__':
    sys.exit(main())
