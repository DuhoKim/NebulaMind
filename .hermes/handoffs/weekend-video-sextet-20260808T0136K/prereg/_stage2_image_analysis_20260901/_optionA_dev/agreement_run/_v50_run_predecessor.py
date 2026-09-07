"""Replay the exact rejected V49 modules in this isolated test process only."""
import hashlib
from pathlib import Path
import unittest
from _optionA_dev.agreement_run import run_path as rp, runtime_binding as rb
base = Path(__file__).resolve().parent
sources = [('runtime_binding', rb, '59bb235a2ec2fffe39967ed272fe61e470b2beb01277281ddd688956f8598a47'),
           ('run_path', rp, 'e904281bbf93e5c3ff50121f81fa7ca8185c76cd8fb40fb368fb0629e2c1d825')]
print('\nFINAL TEST BODIES AGAINST EXACT REJECTED V49 MODULE BYTES; modules loaded only in this process', flush=True)
for name, module, expected in sources:
    raw = (base / ('_v50_original_' + name + '.txt')).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected
    print(name + ' original sha256=' + expected, flush=True)
    exec(compile(raw, module.__file__, 'exec'), module.__dict__)
print('Final test source sha256=' + hashlib.sha256((base / 'test_evidence_gate.py').read_bytes()).hexdigest(), flush=True)
from _optionA_dev.agreement_run import test_evidence_gate
result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(test_evidence_gate))
print('EXACT_PREDECESSOR_EXIT_CODE=' + str(int(not result.wasSuccessful())), flush=True)
raise SystemExit(not result.wasSuccessful())
