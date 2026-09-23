#!/usr/bin/env python3
"""Assemble ref/reader_r2_v138/ — the NEW pinned reader tree of V138 §6.6: the R2 reader (V138-BS3-IDENTITY)
with the stage-6 EA-3 explicit-arithmetic repair imported through a spectral shim. Copies bytes; edits no source
of the R2 tree. Refuses if any source digest differs from the V138 constants. Writes MANIFEST.json (sha256 of
every file placed). No pixel, no network."""
import hashlib, json, pathlib, shutil, sys, datetime
R2=pathlib.Path('/Users/duhokim/work/Trio/SPIN_IMPROVEMENT_R2_20260908')
V1=pathlib.Path('/Users/duhokim/work/Trio/SPIN_IMPROVEMENT_20260908')
EA=pathlib.Path('/Users/duhokim/work/Trio/HWAO_CONTAMINATION_EXPERIMENT_20260909/stage-6-explicit-arithmetic/explicit_arithmetic_v3')
OUT=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/ref/reader_r2_v138')
EXPECT={ # V138 design constants (full digests where the text gives them; 16-hex prefixes otherwise)
 R2/'inference.py':'181eb44ae15265343ff43455ae823f8cede35c23d528bef390ccdddc57ea29b2',
 R2/'model.json':'7bf981726b40e13036217caf9394bcf02a733b92e1ccb3269345563b9284dab5',
 R2/'evidence.py':'2b62f1b65b41d5bd', R2/'geometry_features.py':'fa5be6e2557ef747',
 R2/'orientation_branch/orientation_features.py':'24d1c9d200a7e23e', R2/'spectral_branch/spectral.py':'a992f5829f40f3b8',
 V1/'candidate.py':'087a70e9c558f334',
 EA/'arithmetic.py':'20451d1d79f0c3b2', EA/'prototype.py':'60f89ec60643c91b', EA/'trace_io.py':'675532c4dbe88834',
 EA/'constants.json':'156e89a1eb207868', EA/'reference/spectral_original.py':'a992f5829f40f3b8',
}
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
bad=[(str(p),sha(p)[:16],e[:16]) for p,e in EXPECT.items() if not sha(p).startswith(e)]
if bad: sys.exit('REFUSED source digest mismatch: '+json.dumps(bad))
if OUT.exists(): sys.exit(f'REFUSED: {OUT} exists; a pinned tree is never overwritten')
T=OUT/'SPIN_IMPROVEMENT_R2_20260908'   # evidence.py resolves R = OUT and imports OUT/SPIN_IMPROVEMENT_20260908/candidate.py
for src,rel in [(R2/'inference.py','inference.py'),(R2/'model.json','model.json'),(R2/'evidence.py','evidence.py'),
                (R2/'geometry_features.py','geometry_features.py'),
                (R2/'orientation_branch/orientation_features.py','orientation_branch/orientation_features.py'),
                (R2/'spectral_branch/spectral.py','spectral_branch/spectral_original_r2.py'),
                (V1/'candidate.py','../SPIN_IMPROVEMENT_20260908/candidate.py'),
                (EA/'arithmetic.py','spectral_branch/ea3/arithmetic.py'),(EA/'prototype.py','spectral_branch/ea3/prototype.py'),
                (EA/'trace_io.py','spectral_branch/ea3/trace_io.py'),(EA/'constants.json','spectral_branch/ea3/constants.json'),
                (EA/'reference/spectral_original.py','spectral_branch/ea3/reference/spectral_original.py')]:
    d=(T/rel).resolve(); d.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(src,d)
(T/'spectral_branch/ea3/reference/__init__.py').write_text('')
(T/'spectral_branch/spectral.py').write_text('''"""V138 spectral shim — the R2 spectral feature set with the stage-6 EA-3 explicit-arithmetic repair.
FEATURE_NAMES/VARIANTS are the R2 originals (spectral_original_r2.py, sha256 a992f582...). features(image) is the
numeric body of EA-3 prototype.evaluate(all_features=True), transcribed here WITHOUT its record/identity wrapper
(which imports the experiment bundle's `common`): features 12/15 through ea.radial_fft / ea.phase_multilag,
sp_outer_fft234_whiten through ea.outer_fft234_whiten, the other nine through the original graph; the same
(forward - mirrored)/2 antisymmetric construction; the original nan_to_num sanitization for untouched features;
ea.ensure_finite on the result. Development-only evidence for the repair: explicit_arithmetic_v3/README.md.
This shim is part of the tree whose determinism V138 §6.6 tests; it is not evidence of determinism by itself."""
import sys
from pathlib import Path
import numpy as np
_D = Path(__file__).resolve().parent
for _p in (_D / 'ea3', _D):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import spectral_original_r2 as _orig
import arithmetic as _ea
import prototype as _p3
FEATURE_NAMES = _orig.FEATURE_NAMES
VARIANTS = _orig.VARIANTS
CANDIDATE_ID = _p3.CANDIDATE_ID
def features(image):
    _ea.check_runtime()
    v = np.asarray(image, dtype=np.float64)
    if v.ndim != 2 or v.shape[0] != v.shape[1] or v.shape[0] < 32 or not np.isfinite(v).all():
        raise ValueError(CANDIDATE_ID + ": finite square side >=32 required")
    scale = float(np.max(np.abs(v)))
    if scale:
        v = v / scale
    forward, _ = _p3._raw(v, True, False)
    reflected, _ = _p3._raw(np.fliplr(v), True, False)
    values = {name: (float(forward[name]) - float(reflected[name])) * 0.5 for name in _orig.FEATURE_NAMES}
    for name in values:
        if name not in _p3.TARGETS and name != _p3.REPAIRED_TARGET:
            values[name] = float(np.nan_to_num(values[name], nan=0., posinf=0., neginf=0.))
    _ea.ensure_finite(values)
    return {k: float(values[k]) for k in FEATURE_NAMES}
''')

man={'schema':'hwao-reader-r2-v138-tree-1','assembled_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
     'files':{str(p.relative_to(OUT)):sha(p) for p in sorted(OUT.rglob('*')) if p.is_file()},
     'external_dependencies_not_copied':['EXPLORATORY_COMPARISON_20260907/code/_optionA_dev/fourier_chirality (imported by candidate.py by absolute path; captured by the sys.modules pin at launch)',
                                         'SPIN_IMPROVEMENT_20260908/render_diagnostic.py + study_renderer (renderer, not instrument; pinned in STUDIO_APPROVAL_INPUTS.sha256)'],
     'sources':{str(k):v for k,v in EXPECT.items()}}
(OUT/'MANIFEST.json').write_text(json.dumps(man,indent=1,sort_keys=True)+'\n')
print(json.dumps({'tree':str(OUT),'files':len(man['files']),'manifest_sha256':sha(OUT/'MANIFEST.json')}))
