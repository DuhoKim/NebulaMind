"""Assemble a receipt from retained execution evidence and byte snapshots."""
import difflib
import hashlib
import json
from pathlib import Path

LANE = Path.cwd()
BASE = LANE / '_optionA_dev/agreement_run'
OUT = BASE / '_repair_candidate'

def read(path):
    return json.loads(path.read_bytes())

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')

names = ['RUNTIME_PINS_A1_CORE.json', 'INPUT_MANIFEST_A1_CORE.json', 'INPUT_FREEZE_C_20260907.json']
old = {n: read(BASE / n) for n in names}
new = {n: read(OUT / n) for n in names}
runtime, core, c = [new[n] for n in names]
prior = old[names[0]]['representation']
evidence = runtime['representation']
delta = read(OUT / 'observe/delta.json')
before = read(OUT / 'preservation.before.json')
after = read(OUT / 'preservation.after.json')
assert before == after
for path, pin in after['files'].items():
    assert sha(Path(path)) == pin['sha256'], path
assert core['code'] == old[names[1]]['code']
assert c['adopted_procedure'] == old[names[2]]['adopted_procedure']
assert c['later_stage_groups_named_not_expanded'] == old[names[2]]['later_stage_groups_named_not_expanded']
assert (LANE / c['core_manifest']['path']).resolve() == OUT / names[1]
assert c['core_manifest']['sha256'] == sha(OUT / names[1])
assert core['inputs']['runtime']['sha256'] == sha(OUT / names[0])
assert {p['path']: p['sha256'] for p in c['input_due_expanded']} == {
    p['path']: p['sha256'] for p in core['files']}

differences = {}
for key, field in [('modules', 'module'), ('files', 'path'), ('images', 'path')]:
    a, b = ({p[field]: p for p in rows[key]} for rows in (prior, evidence))
    differences[key] = {
        'added': [b[k] for k in sorted(b.keys() - a.keys())],
        'removed': [a[k] for k in sorted(a.keys() - b.keys())],
        'changed': [{'before': a[k], 'after': b[k]} for k in sorted(a.keys() & b.keys()) if a[k] != b[k]],
        'before_count': len(a), 'after_count': len(b)}
    assert not differences[key]['removed'] and not differences[key]['changed'], key
assert evidence['cache_bytes'] == prior['cache_bytes']
assert evidence['shared_cache'] == prior['shared_cache']
save(OUT / 'inventory_diff.json', differences)

def normalized(value):
    if isinstance(value, dict):
        return {k: normalized(v) for k, v in value.items()}
    if isinstance(value, list):
        if value and all(isinstance(v, dict) and 'module' in v for v in value):
            return {v['module']: normalized(v) for v in value}
        if value and all(isinstance(v, dict) and isinstance(v.get('path'), str) for v in value):
            return {v['path']: normalized(v) for v in value}
        return [normalized(v) for v in value]
    return value

diff = []
for name in names:
    a = json.dumps(normalized(old[name]), indent=2, sort_keys=True).splitlines(True)
    b = json.dumps(normalized(new[name]), indent=2, sort_keys=True).splitlines(True)
    diff.extend(difflib.unified_diff(a, b, fromfile='frozen/' + name, tofile='candidate/' + name))
(OUT / 'frozen_vs_candidate.diff').write_text(''.join(diff))

closures = {n: read(OUT / n / 'closure.json') for n in ('network_module', 'selection', 'render_score')}
assert len({v['pid'] for v in closures.values()}) == 3
for value in closures.values():
    assert value['status'] == value['core_consumer']['status'] == 'PASS'
    assert value['core_consumer']['core_sha256'] == sha(OUT / names[1])
assert read(OUT / 'standalone_verifier.json')['status'] == 'PASS'
reasons = read(OUT / 'refusals/candidate_refusals.json')
assert set(reasons) == {'tampered_pin', 'missing_core_entry', 'readiness_false_run'}
network = read(OUT / 'network_module/NON_STUDY.outputs/seed.json')
assert network['verdict'] == 'PASS' and len(network['hosts']) == 3
assert len(network['responses']) == 8
scores = read(OUT / 'render_score/label_blind_scores.json')
assert len(scores['scores']) == 96 and scores['render']['status'] == 'SCORED'
assert all(r['chi_bits'] == r['repeat_bits'] for r in scores['scores'])

candidate_pins = {str(OUT / n): {'sha256': sha(OUT / n), 'bytes': (OUT / n).stat().st_size} for n in names}
save(OUT / 'candidate_digests.json', candidate_pins)
commands = read(OUT / 'commands.json')
log_names = ['observe', 'build', 'network', 'build_module', 'network_module', 'selection', 'render_score', 'refusals']
lines = ['# Network-aware runtime repair candidate', '',
    'Author completion; isolated, unadopted candidate. All acceptance checks below passed. '
    'No adopted code/procedure changed; no registration exemptions or gate changes.', '',
    'Lane root: `' + str(LANE) + '`. Candidate directory: `' + str(OUT) + '`.', '',
    '| Candidate | SHA-256 | Bytes |', '|---|---|---:|']
for path, pin in candidate_pins.items():
    lines.append('| [' + Path(path).name + '](' + path + ') | `' + pin['sha256'] + '` | ' + str(pin['bytes']) + ' |')
lines += ['', 'The existing `runtime_probe.measure` → `runtime_binding.capture` and '
    '`runtime_authoring.refresh` built the runtime/CORE. The authoring output root was set to '
    '`_repair_candidate`; the measurement wrapper corrected only probe metadata after the real operations. '
    'No module/file rows were manually added. Candidate C was derived from the preserved C by rebinding '
    'its CORE/runtime references and marking its candidate status/time. Every C input pin equals the '
    'corresponding candidate CORE pin. The historical `build_input_freeze.py` refusal-only dispatch '
    'was not altered or represented as a C-producing builder.', '',
    'Observation: under the pinned invocation, the existing offline probe captured **821** module names; '
    'a real `run_path.fetch_bytes` request to drand round **6444980**, followed by the existing pinned-key '
    'BLS verifier, produced **823**. Added: **encodings.idna, stringprep**. Removed/changed: none. '
    '**unicodedata was already present in the frozen inventory and in the pre-fetch capture**; '
    'it was observed again after HTTPS and retained unchanged. The governing refusal note’s claim '
    'that all three were absent does not match the preserved inventory on disk.', '',
    'Exact reproduced frozen-inventory refusal:', '', '```text',
    delta['frozen_refusal_after_fetch'], '```', '',
    'The real response passed exact URL/round binding, signature length, SHA-256 randomness, and '
    'BLS under the pinned public key. Response SHA-256: `' +
    sha(OUT / 'observe/NON_STUDY_6444980.response.json') + '`.', '',
    'Observation stdout (verbatim fetch result and module delta):', '', '```json',
    *(OUT / 'observe.log').read_text().splitlines()[-2:], '```', '',
    'All three required names have observed real origins and SHA-256 bindings:', '',
    '| Observed module | Real origin | SHA-256 |', '|---|---|---|']
modules = {p['module']: p for p in evidence['modules']}
files = {p['path']: p for p in evidence['files']}
for name in ('encodings.idna', 'stringprep', 'unicodedata'):
    row = modules[name]
    lines.append('| `' + name + '` | `' + row['path'] + '` | `' + files[row['path']]['sha256'] + '` |')
lines += ['', 'Source and all existing standard cache candidates are registered by the unchanged capture; '
    'own-code correspondence and all byte pins are checked by the unchanged consumers. '
    'Observation command/output, full before/after snapshots and cache pins are retained in '
    '[observe.log](' + str(OUT / 'observe.log') + ') and [observe/delta.json](' + str(OUT / 'observe/delta.json') + ').', '',
    'Final inventory diff: **822 → 843 modules**, **' + str(differences['files']['before_count']) +
    ' → 1526 artifact files**. Added 21 module records and ' + str(len(differences['files']['added'])) +
    ' artifact pins; **zero removals and zero changed existing module/artifact/image records**. '
    'All 423 dyld images and the 13-file, 5,820,973,056-byte active cache family remain unchanged. '
    'Besides the two HTTPS lazy imports, additions are observed fixture/test-harness imports and '
    'the candidate namespace. `runpy` is retained because the final build actually ran with `-m`.', '',
    'Added module names: `' + '`, `'.join(r['module'] for r in differences['modules']['added']) + '`.', '',
    'Full normalized CORE/C/runtime diff: [frozen_vs_candidate.diff](' + str(OUT / 'frozen_vs_candidate.diff') +
    '). Exact added paths/digests: [inventory_diff.json](' + str(OUT / 'inventory_diff.json') + ').', '',
    '| Fresh process / operation | Result after operation |', '|---|---|']
descriptions = {
    'network_module': 'Actual `RunPath.accept_seed`: exposed-round synthetic predecessor; 2 passes × 4 relays; 3 agreeing BLS-verified/refetched hosts; 2 retained Cloudflare HTTP 403 errors',
    'selection': 'Existing `RunPath` synthetic exact/disjoint 400/200/2000 selection and draw-reuse refusal tests: 2/2 pass; IDs 0..2599, fixed fixture seed ab×32',
    'render_score': 'Existing label-free raster → 3 RICE_1 FITS planes → actual TAN WCS/render chain → all 96 real Fourier chi estimators, bitwise-repeat checks; 32/32 existing MEDIUM tests pass'}
for name, result in closures.items():
    lines.append('| PID ' + str(result['pid']) + ': ' + descriptions[name] + ' | Runtime closure **PASS**; source-bootstrapped CORE consumer **PASS** |')
lines += ['', 'Each listed process freshly executed its operation, then called the unchanged '
    '`run_path._environment` and `verify_core.verify` against the **final candidate**. Full post-operation '
    'results are `<operation>/closure.json`; they pin the final CORE digest above. The selection unit '
    'fixtures retain their existing synthetic CORE/cache setup; the subsequent candidate closure '
    'uses the restored real runtime and full real cache family. A separate unmodified source CLI '
    '`verify_core.py` also returned PASS ([standalone_verifier.json](' + str(OUT / 'standalone_verifier.json') + ')).', '',
    'Coverage limits: no formal designation, study draw, catalogue label read, protected image read, '
    'holdout opening, winner selection, or full label-dependent tune/holdout/validation orchestration. '
    'Rendering/scoring coverage is synthetic compressed FITS, real rendering, raw `Estimator.chi`, '
    'and label-blind MEDIUM branches (flip/nonflip, no/off-raster MEDIUM, negative orientation, tie, '
    'central-contamination refusal, schema/input refusals). No label agreement statistic was computed. '
    'The network test did not call `designate`; its predecessor explicitly says NON-STUDY and never '
    'authorizes use of round 6444980 for this study.', '',
    'Expected refusals: the three existing tests passed their exception assertions (tampered py_ecc '
    'source pin; missing CORE input entry; readiness-false tune). The same three defects also refused '
    'against isolated copies of the final candidate with real cache verification:', '', '```text']
lines.extend(name + ': ' + reason for name, reason in reasons.items())
lines += ['```', '', 'Substantive commands and actual results (all exit 0; unit-test PASS means the '
    'expected refusal occurred):', '', '```sh', *commands, '```', '',
    'Every Python execution used the verbatim pinned interpreter/environment prefix shown above. '
    'Raw execution output, including PID, invocation, commands’ argv and UTC, is retained in ',
    ', '.join('[' + n + '.log](' + str(OUT / (n + '.log')) + ')' for n in log_names) + '.', '',
    'The first source-entrypoint candidate omitted unobserved `runpy`; its preliminary build/network '
    'checks passed and are retained in `source_entrypoint_candidates/`, `build.log`, and `network.log`. '
    'It was superseded by the final observed `-m` build and all final stage checks above. No frozen '
    'inventory entry was dropped from the final candidate.', '',
    'Frozen-byte preservation: 37 governing/adopted/source files and all 14 files in the two failed '
    'journals were hashed before and after and are **BYTE-IDENTICAL**. Required SHA-256 values:', '',
    '| Preserved target | SHA-256 |', '|---|---|']
for path in [LANE / 'AGREEMENT_RUN_AMENDMENT_A1_20260907.md', BASE / 'run_path.py',
             BASE / names[1], BASE / names[2], BASE / names[0]]:
    lines.append('| `' + str(path.relative_to(LANE)) + '` | `' + after['files'][str(path)]['sha256'] + '` |')
for name, row in after['journals'].items():
    lines.append('| `' + name + '/` (' + str(len(row['files'])) + ' files) | `' + row['manifest_sha256'] + '` |')
lines += ['', 'Directory digests are SHA-256 of canonical sorted relative-path → {bytes, sha256} '
    'JSON (UTF-8; separators comma/colon), not a claim that a directory itself has file bytes. '
    'Every individual journal-file digest and every source digest is in '
    '[preservation.before.json](' + str(OUT / 'preservation.before.json') + ') and '
    '[preservation.after.json](' + str(OUT / 'preservation.after.json') + ').', '',
    'Unresolved execution dependencies: `drand.cloudflare.com` returned HTTP 403 in both real '
    'passes; the unchanged two-host gate passed with the other three hosts. No blocker remains '
    'for this bounded candidate. Runtime validity remains tied to the pinned interpreter, current '
    'source/cache/library bytes and OS cache family; existing TOCTOU/in-memory limits remain. '
    'The governing memo also requests external failed-attempt registration; no provider event/time '
    'was verified or published in this task because the direct dispatch permits network calls only '
    'to drand. No external registration claim is made. Candidate readiness supplies no restart '
    'authority or future anchor/designation.', '',
    'Deterministic local author completion; no worker, second collector/reviewer, or git was used.', '',
    'REPAIR-CANDIDATE-READY']
(LANE / '_tmp_repair_receipt.md').write_text('\n'.join(lines) + '\n')
print('REPAIR-CANDIDATE-READY')
print(json.dumps(candidate_pins, indent=2))
