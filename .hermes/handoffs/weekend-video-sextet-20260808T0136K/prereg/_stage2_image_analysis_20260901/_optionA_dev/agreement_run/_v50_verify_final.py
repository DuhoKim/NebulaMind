"""Read-only final V50 verification; no study stages are invoked."""
import hashlib
import json
from pathlib import Path
from _optionA_dev.agreement_run import run_path as rp
from _optionA_dev.agreement_run.runtime_probe import measure, pin

base = rp.ROOT / '_optionA_dev/agreement_run'
cpath = base / 'INPUT_MANIFEST_A1_CORE.json'
c = json.loads(cpath.read_bytes())
computed = rp.input_readiness(c)
rp.require(computed['ready_for_input_freeze'], 'FINAL-EVIDENCE-NOT-READY')
rp.require(computed['checks'] == c['readiness']['checks'] and
           computed['ready_for_input_freeze'] is c['ready_for_input_freeze'], 'FINAL-STORED-READINESS-MISMATCH')
rp._a1_consistency(c, computed)
rp.require(rp._core(c) == c["inputs"], "FINAL-CORE-CONSUMER")
runtime = rp.json_pin(c['inputs']['runtime'])
fresh = measure()
rp.require(fresh == runtime['representation'], 'FRESH-PROCESS-REPRESENTATION-MISMATCH')
before = json.loads((base / '_v50_preservation.json').read_bytes())
rp.require({k:v for k,v in c['inputs'].items() if k != 'runtime'} == before['inputs'], 'NON-RUNTIME-INPUT-CHANGED')
rp.require({k:v for k,v in c['code'].items() if not k.startswith('_optionA_dev/agreement_run/')} == before['code'], 'EXCLUDED-CODE-CHANGED')
for name, rel in [('medium', 'medium_perturbation.py'), ('selection', 'select_sample.py')]:
    rp.require(pin(base / rel)['sha256'] == before[name], 'RETAINED-CODE-CHANGED: ' + rel)
reviewed = """TOCTOU: extension modules are hashed and later imported with no lock between.
Even the immediate pre-import recheck evidences disk bytes at check time, not
the bytes the loader used (or an extension already loaded in this process)."""
for path in [rp.ROOT / rp.A1_SOURCE, base / 'run_path.py', base / 'RUNTIME_REPRESENTATION_20260907.md']:
    rp.require(reviewed in path.read_text(), 'REVIEWED-TOCTOU-WORDING-MISMATCH: ' + str(path))
result = {'computed': computed, 'fresh_runtime_reproduces_exactly': True,
          'cache_files': len(fresh['cache_bytes']['files']),
          'cache_bytes': sum(p['bytes'] for p in fresh['cache_bytes']['files']),
          'cache_resident_images': sum(r['in_shared_cache'] for r in fresh['images']),
          'module_names': len(fresh['modules']), 'dyld_images': len(fresh['images']),
          'import_native_files': len(fresh['files']),
          'non_runtime_inputs_and_excluded_code_preserved': True, 'reviewed_TOCTOU_restored': True,
          'pins': [pin(p) for p in [rp.ROOT / rp.A1_SOURCE, base / 'run_path.py',
                                   base / 'runtime_binding.py', base / 'runtime_probe.py',
                                   base / 'runtime_authoring.py', cpath, Path(c['inputs']['runtime']['path'])]]}
print(json.dumps(result, sort_keys=True), flush=True)
