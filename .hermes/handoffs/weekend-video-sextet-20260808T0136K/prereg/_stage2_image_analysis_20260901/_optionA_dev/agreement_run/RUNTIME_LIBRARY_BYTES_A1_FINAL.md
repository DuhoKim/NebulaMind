# Runtime library bytes — 2026-09-07

FINAL names this bounded authoring deliverable; it does not mean adoption or complete INPUT closure. The actual run_path environment enforcement passes. The literal individual-library closure remains incomplete.

There are 1,521 real file pins: all 1,520 prior observations rehashed with zero mismatch, plus select_sample.py. run_path._environment reads every runtime.files entry. Prior observed source/resource/bytecode entries are retained and rehashed; this does not claim every historical resource was independently reopened by a scientific operation today. Each file has its own digest and read-purpose annotations.

The offline probe loads actual run dependencies, scores all 96 existing configurations on an in-memory generated tensor, decodes generated RICE_1 FITS, verifies a synthetic-key BLS signature, and builds the default TLS context/opener without network. It invokes no RunPath stage or real selection.

Python 3.9.6; NumPy 1.26.4; py_ecc 8.0.0; Astropy 6.0.1. The 68 loaded extension-module names and their on-disk digests appear below and in the JSON. Module aliases may share a file. py_ecc itself has zero loaded extensions in this probe: its Python files are individually pinned, as are loaded transitive native dependencies including cytoolz and pydantic_core.

The driver compares interpreter, Python/NumPy versions, platform/machine, NumPy core/FFT hashes and basenames, and five thread variables equal to 1. It also enforces the exact PYTHONPATH, disabled bytecode writing, and py_ecc 8.0.0. env_lock.scope is descriptive and not compared. Full measured values follow.

## Exact unresolved library representation

dyld reports 422 images: 76 have readable file artifacts, 346 do not. Every absent image name appears individually in RUNTIME_DEPENDENCIES_A1_FINAL.json:dyld_loaded_images as NAMED_PLACEHOLDER, sha256=null, due_stage=INPUT, with its producer/remedy.

The measured running shared-cache UUID is f2e86c536052388bba715a0c9b569413. A UUID is not a content digest. /usr/lib/libSystem.B.dylib and /usr/lib/libobjc.A.dylib do not exist as individually readable files. A Cryptex cache main file exists, but it is a container rather than an individual-library representation; no aggregate digest is substituted. The two checked dyld_shared_cache_util locations are absent; no wider absence claim is made.

Blocked operation: produce a standalone on-disk SHA-256 for each of the 346 absent image files. Concrete remedy: an owner-authorized scope must create OS/cache-UUID-matched per-image extraction artifacts and map them to loaded images, or explicitly resolve the cached-image representation in final A1 before review/adoption. Such extraction artifacts exceed this task's file whitelist. A relocated memory hash is not a stable hash of a nonexistent original file.

On-disk Mach-O/extension digests identify artifacts, not ASLR/fixup-dependent process pages. Python auditing begins after bootstrap and cannot certify every native resource read. The stated probe does not cover all FITS formats or network error paths. Passing package enforcement does not pin the missing cached images.

## Runtime command and output

This command created the JSON with exclusive write. A later reproduction must compare bytes in an authorized new location; overwriting this retained file is refused.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/_optionA_dev/_venv_bls/lib/python3.9/site-packages" /Library/Developer/CommandLineTools/usr/bin/python3 -W error::ResourceWarning - <<'PY'
from pathlib import Path
import hashlib, json, sys, os, io, ctypes, importlib.util, ssl, platform
ROOT=Path.cwd()
BASE=ROOT/"_optionA_dev/agreement_run"
opened=set()
def audit(event,args):
    if event=="open" and isinstance(args[0],(str,bytes)):
        p=os.fsdecode(args[0])
        if p and not p.startswith("<"):
            opened.add(str(Path(p).absolute()))
sys.addaudithook(audit)
from _optionA_dev.agreement_run import run_path as rp
from _optionA_dev.agreement_run import select_sample
from _optionA_dev.drand_only import verify_drand_v2 as vd
from _optionA_dev.fourier_chirality import fourier_chirality as fc
from study_renderer import render_chain_v3 as chain
from astropy.io import fits
from astropy.wcs import WCS
import astropy, numpy as np, py_ecc
def pin(path):
    path=Path(path).resolve()
    return {"path":str(path),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()}
# Generated in-memory FITS and synthetic-key BLS only. No real run stage.
yy,xx=np.indices((180,180),dtype=float)
x,y=xx-89.5,yy-89.5
r=np.hypot(x,y)
plane=2+np.exp(-r/45)*(1+.7*np.cos(2*np.arctan2(y,x)+4*np.log1p(r)))
w=WCS(naxis=2)
w.wcs.ctype=["RA---TAN","DEC--TAN"];w.wcs.crval=[40.,10.]
w.wcs.crpix=[90.5,90.5];w.wcs.cd=np.array([[-.262/3600,0],[0,.262/3600]])
stream=io.BytesIO()
fits.HDUList([fits.PrimaryHDU(),fits.CompImageHDU(
    np.arange(180*180,dtype=np.int32).reshape(180,180),compression_type="RICE_1")]).writeto(stream)
with fits.open(io.BytesIO(stream.getvalue()),memmap=False) as hdus:
    assert np.array_equal(hdus[1].data,np.arange(180*180).reshape(180,180))
rendered=chain.render_object(plane,np.zeros((180,180),dtype=np.int32),
    np.ones((180,180),dtype=np.int32),w,40.,10.,"0400p100",chain.pr.r_t_validation())
scores=[rp.score_object(fc.Estimator(cfg),rendered["tensor"],1) for cfg in fc.enumerate_configs()]
assert len(scores)==96 and all(s["status"]=="SCORED" for s in scores)
message=b"A1 v42 offline synthetic runtime probe"
assert vd.G2Basic.Verify(vd.G2Basic.SkToPk(5),message,vd.G2Basic.Sign(5,message))
context=ssl.create_default_context()
from urllib.request import build_opener
opener=build_opener()
rp.stage_statistic("validation",[{"status":"SCORED","match":True}]*1900+[{"status":"UNSCORED"}]*100)
prior_text=(BASE/"RUNTIME_EVIDENCE_20260907.md").read_text()
prior=json.loads(prior_text.split("<!-- A1-RUNTIME-JSON -->\n"+chr(96)*3+"json\n")[1].split("\n"+chr(96)*3)[0])
paths=set()
roles={}
def add(path,role):
    p=Path(path).resolve()
    if p.is_file():
        s=str(p); paths.add(s);roles.setdefault(s,set()).add(role)
for p in prior["files"]:
    # Existing inventory is confined to runtime sources/resources, never study data.
    actual=pin(p["path"])
    assert actual==p, "Prior pin changed: "+p["path"]
    add(p["path"],"prior-v41-observation-rehashed-now; run_path._environment hashes every runtime.files entry")
add(sys.executable,"interpreter")
extensions=[]
for name,m in sorted(tuple(sys.modules.items())):
    p=getattr(m,"__file__",None)
    if p and not p.startswith("<"):
        add(p,"loaded-module:"+name)
        if p.endswith((".so",".dylib")):
            extensions.append({"module":name,**pin(p)})
        if p.endswith(".py"):
            cache=importlib.util.cache_from_source(p)
            if Path(cache).is_file():
                add(cache,"existing-bytecode-for-loaded-source")
for p in tuple(opened):
    # Exclude this probe's evidence read; it is provenance, not a run dependency.
    if Path(p).resolve()==(BASE/"RUNTIME_EVIDENCE_20260907.md").resolve(): continue
    add(p,"observed-open-during-offline-probe")
for p in ssl.get_default_verify_paths():
    if isinstance(p,str) and Path(p).is_file():
        add(p,"TLS-default-CA-file")
lib=ctypes.CDLL(None)
lib._dyld_image_count.restype=ctypes.c_uint32
lib._dyld_get_image_name.argtypes=[ctypes.c_uint32]
lib._dyld_get_image_name.restype=ctypes.c_char_p
images=[]
for i in range(lib._dyld_image_count()):
    name=os.fsdecode(lib._dyld_get_image_name(i))
    if Path(name).is_file():
        add(name,"dyld-loaded-image")
        images.append({"loaded_image_name":name,"status":"REAL",**pin(name)})
    else:
        images.append({"loaded_image_name":name,"status":"NAMED_PLACEHOLDER","sha256":None,
            "due_stage":"INPUT","producer":"OS-matched individual image extraction and mapping, or owner-adopted representation resolution",
            "reason":"dyld reports a loaded image; no individual readable file exists at this name"})
files=[{**pin(p),"read_purposes":sorted(roles[p])} for p in sorted(paths)]
import numpy.fft._pocketfft_internal as fft
observed={
    "interpreter":sys.executable,"python":sys.version.split()[0],"numpy":np.__version__,
    "platform":platform.platform(),"machine":platform.machine(),
    "numpy_core_sha256":pin(np.core._multiarray_umath.__file__)["sha256"],
    "numpy_core_basename":Path(np.core._multiarray_umath.__file__).name,
    "numpy_fft_sha256":pin(fft.__file__)["sha256"],
    "numpy_fft_basename":Path(fft.__file__).name,
    "thread_env":{v:os.environ.get(v) for v in rp.THREAD_VARS}}
lock_pin=pin(ROOT/"_optionA_dev/fourier_chirality/env_lock.json")
lock=json.loads(Path(lock_pin["path"]).read_bytes())
assert all(lock.get(k)==v for k,v in observed.items())
assert os.environ.get("PYTHONPATH")==rp.PYTHONPATH and sys.dont_write_bytecode
missing=[x for x in images if x["status"]=="NAMED_PLACEHOLDER"]
runtime={
    "schema":"A1-RUNTIME-DEPENDENCIES-1","authoring_only":True,
    "literal_individual_library_closure_complete":not missing,
    "py_ecc_version":py_ecc.__version__,"numpy_version":np.__version__,"astropy_version":astropy.__version__,
    "interpreter":pin(sys.executable),"python_version":sys.version,
    "invocation":{"PYTHONPATH":os.environ["PYTHONPATH"],"PYTHONDONTWRITEBYTECODE":os.environ["PYTHONDONTWRITEBYTECODE"]},
    "env_lock":lock_pin,"env_lock_values":lock,"enforced_observed_values":observed,
    "non_enforced_env_lock_fields":sorted(set(lock)-set(observed)),
    "files":files,"loaded_extension_modules":extensions,"dyld_loaded_images":images,
    "counts":{"prior_rehashed":len(prior["files"]),"real_files":len(files),"extension_modules":len(extensions),
              "dyld_images":len(images),"dyld_without_individual_files":len(missing)},
    "observation_scope":"Offline module imports, all 96 real estimators on generated tensor, generated RICE_1 FITS decode, synthetic-key BLS, default TLS context/opener without network. Prior observed inventory retained and rehashed.",
    "limits":["No claim to all FITS formats or every native resource read.",
              "Python audit hook starts after bootstrap; unavailable dyld names have no invented digest.",
              "On-disk .so/Mach-O hashes identify artifacts, not ASLR/relocated in-memory pages.",
              "py_ecc loads Python source; zero extension modules under py_ecc itself in this probe. Transitive loaded native modules are individually listed.",
              "scope field in env_lock is descriptive and not compared by run_path._environment."]
}
path=BASE/"RUNTIME_DEPENDENCIES_A1_FINAL.json"
with path.open("xb") as f: f.write(rp.canonical(runtime))
enforcement=rp._environment(lock_pin,pin(path))
print(json.dumps({"runtime_pin":pin(path),"counts":runtime["counts"],"interpreter":runtime["interpreter"],
 "versions":{"python":sys.version.split()[0],"numpy":np.__version__,"py_ecc":py_ecc.__version__,"astropy":astropy.__version__},
 "enforced_observed_values":observed,"non_enforced_env_lock_fields":runtime["non_enforced_env_lock_fields"],
 "environment_enforcement":"PASS","prior_pin_mismatches":0,"synthetic_configurations_scored":len(scores),
 "synthetic_RICE_1":"PASS","synthetic_BLS":"PASS","TLS_without_network":"PASS",
 "loaded_extension_modules":extensions,
 "loaded_library_representation":"BLOCKED: "+str(len(missing))+" image names have no individual readable file"},indent=2,sort_keys=True))

PY
```

```text
{
  "TLS_without_network": "PASS",
  "counts": {
    "dyld_images": 422,
    "dyld_without_individual_files": 346,
    "extension_modules": 68,
    "prior_rehashed": 1520,
    "real_files": 1521
  },
  "enforced_observed_values": {
    "interpreter": "/Library/Developer/CommandLineTools/usr/bin/python3",
    "machine": "arm64",
    "numpy": "1.26.4",
    "numpy_core_basename": "_multiarray_umath.cpython-39-darwin.so",
    "numpy_core_sha256": "e870618cf0f8a4b73a928649aba064eee859f8e25a7912344c979f1d03679194",
    "numpy_fft_basename": "_pocketfft_internal.cpython-39-darwin.so",
    "numpy_fft_sha256": "cfc7c758921da384994a66578d289d6c8aa710756a6af64a28f964b90fd5f546",
    "platform": "macOS-26.6.2-arm64-arm-64bit",
    "python": "3.9.6",
    "thread_env": {
      "MKL_NUM_THREADS": "1",
      "NUMEXPR_NUM_THREADS": "1",
      "OMP_NUM_THREADS": "1",
      "OPENBLAS_NUM_THREADS": "1",
      "VECLIB_MAXIMUM_THREADS": "1"
    }
  },
  "environment_enforcement": "PASS",
  "interpreter": {
    "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/bin/python3.9",
    "sha256": "bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e"
  },
  "loaded_extension_modules": [
    {
      "module": "_asyncio",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_asyncio.cpython-39-darwin.so",
      "sha256": "bbba582366903239855e308f83ae2758320e77a2014c34959bc2876cb8b6b531"
    },
    {
      "module": "_bisect",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_bisect.cpython-39-darwin.so",
      "sha256": "94f808d63ed02de29622d339138adb922e328be50bda4cf554f46149534a58f1"
    },
    {
      "module": "_blake2",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_blake2.cpython-39-darwin.so",
      "sha256": "ace7a5d932bbaa749474c1dadcde5c2de4f3bd1ab3b4eca7e97bbec9ab3a6f96"
    },
    {
      "module": "_bz2",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_bz2.cpython-39-darwin.so",
      "sha256": "bf0c0f25e8721ee2684829b6cff1a7261d441392fc84d8f2a8def9d3f8d58217"
    },
    {
      "module": "_contextvars",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_contextvars.cpython-39-darwin.so",
      "sha256": "1906b2d8fb4cacf40f3bf95e470b0b94f1f42483deb71541298d7e2fee7926b4"
    },
    {
      "module": "_csv",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_csv.cpython-39-darwin.so",
      "sha256": "e2b9aaebd4db30ff61724d57dc23c4a13ab6799bdf6f70e8ac0050b6f2372f49"
    },
    {
      "module": "_ctypes",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_ctypes.cpython-39-darwin.so",
      "sha256": "7949fb8a2fdf9d2a5645a78c2fd4f4081371983f2043d44b812363ccb41eaff0"
    },
    {
      "module": "_datetime",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_datetime.cpython-39-darwin.so",
      "sha256": "892aa474d0699fd4d17e2028fa1e0f9894e16f7b4859e04d38e37935ae0e6bea"
    },
    {
      "module": "_decimal",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_decimal.cpython-39-darwin.so",
      "sha256": "de0cb5ff503790abb46af8d168a54dae59b1c630cc4c79aff3964d906637f7b8"
    },
    {
      "module": "_hashlib",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_hashlib.cpython-39-darwin.so",
      "sha256": "da802e76e50f627108a9a8a4a77d703af94bfb56dc4fc4c9560c297c5313bb44"
    },
    {
      "module": "_heapq",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_heapq.cpython-39-darwin.so",
      "sha256": "9613d8b26ff63aee06ae46e69a44eea726a97fded23ff721fd97e4bd6a58a1a7"
    },
    {
      "module": "_json",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_json.cpython-39-darwin.so",
      "sha256": "abc9b5ea12a96d7552ec34298fbbba6784427fd6304cbe2757a4bbc35194ba13"
    },
    {
      "module": "_lzma",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_lzma.cpython-39-darwin.so",
      "sha256": "928be7907b453d723def994592169b6179610091edbe809e07045b108a69a495"
    },
    {
      "module": "_opcode",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_opcode.cpython-39-darwin.so",
      "sha256": "555a6a629124de05815383f47dac6925c0558f05d61021cb2a822ccc8da3f76a"
    },
    {
      "module": "_pickle",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_pickle.cpython-39-darwin.so",
      "sha256": "d1c4c0f568defedcbdcea1335155bcd905061f7b8131d33afbfe29a60bb21f53"
    },
    {
      "module": "_posixsubprocess",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_posixsubprocess.cpython-39-darwin.so",
      "sha256": "f23b2e40e280e5a66bfc4c545d038ce4b6f541a17f1c84697d3ef9e02688c952"
    },
    {
      "module": "_queue",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_queue.cpython-39-darwin.so",
      "sha256": "6828c5757ffd5d102199f0ae9de1acd03d96c534ea746492c598298020e145ce"
    },
    {
      "module": "_random",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_random.cpython-39-darwin.so",
      "sha256": "43855012adae33e49bc8008b03ba0a27f47f9600612b8ba3fe84f70554ff45ba"
    },
    {
      "module": "_scproxy",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_scproxy.cpython-39-darwin.so",
      "sha256": "ede6234dd7c27ca22b7eea8eb3a555e5855009ebaa5b979f11097212bf42ca72"
    },
    {
      "module": "_sha3",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_sha3.cpython-39-darwin.so",
      "sha256": "0fa9ff6e0c522355b660d8ec0017c85831282ea6c4bb010a5a93ca7e9e939162"
    },
    {
      "module": "_sha512",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_sha512.cpython-39-darwin.so",
      "sha256": "521c7e610ba05d1562e90d43370d09a07575dbd90922dc89119dae3bdf4a4713"
    },
    {
      "module": "_socket",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_socket.cpython-39-darwin.so",
      "sha256": "39873fc9469e386b8f7c6a0d2cbb4f50ab1fae50f83f7d4cc33beb961f83125b"
    },
    {
      "module": "_ssl",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_ssl.cpython-39-darwin.so",
      "sha256": "4d337c5a44dfee4ee32a2b460594dc5dce08decea2e98cd190edb60f2ce5cd6a"
    },
    {
      "module": "_struct",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_struct.cpython-39-darwin.so",
      "sha256": "20dbbcea553b43fec32dc2a740f1cb82f04c0bfc56a87f76f777b7c0f1d6ffc5"
    },
    {
      "module": "_uuid",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_uuid.cpython-39-darwin.so",
      "sha256": "1229d8849401ebb80fb9fe7e1a43feb6609b92fc9d0ff2e1eca409536ab2f709"
    },
    {
      "module": "_zoneinfo",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/_zoneinfo.cpython-39-darwin.so",
      "sha256": "f9539fcf932d9fe487f89778563daa42fcdb3c684f915ff6d7298b8d77bfcf12"
    },
    {
      "module": "array",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/array.cpython-39-darwin.so",
      "sha256": "15c85d5c882dfebd9aa7d6117af3f90b50cd39c98d7591a26b408a6a4b621e74"
    },
    {
      "module": "astropy.io.ascii.cparser",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/io/ascii/cparser.cpython-39-darwin.so",
      "sha256": "836a8ae1729ff8c22f80361acf06ee24054472479dcc070350c0ba50b5bdb1b1"
    },
    {
      "module": "astropy.io.fits._utils",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/io/fits/_utils.cpython-39-darwin.so",
      "sha256": "4dce2d1804003607d3978f00008dc3b0fad6fff8b05e8d4dc202566590ddc4f7"
    },
    {
      "module": "astropy.io.fits.hdu.compressed._compression",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/io/fits/hdu/compressed/_compression.cpython-39-darwin.so",
      "sha256": "b80ed4d27841c618b96d6caf8ad82fc165f5e9e06407e2f202010a5a5a3cc892"
    },
    {
      "module": "astropy.io.votable.tablewriter",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/io/votable/tablewriter.cpython-39-darwin.so",
      "sha256": "92ce9bff66dc50c96d4d17d35107ca5e82354be234e0b66790f575db9cba2bd1"
    },
    {
      "module": "astropy.table._column_mixins",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/table/_column_mixins.cpython-39-darwin.so",
      "sha256": "7d0e01e84a80c51e517d1540a1786a4fd73feefb077d5fa92892d682f2d32712"
    },
    {
      "module": "astropy.table._np_utils",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/table/_np_utils.cpython-39-darwin.so",
      "sha256": "82d53094fe2db02da1ae86703aedb3ab96a5627f5b07ea421b1ffcd895fbf55b"
    },
    {
      "module": "astropy.time._parse_times",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/time/_parse_times.cpython-39-darwin.so",
      "sha256": "84ebed9f0cf8747df363034894d7b846cedb366eab09b9410fd8c772ff6d0689"
    },
    {
      "module": "astropy.utils._compiler",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/utils/_compiler.cpython-39-darwin.so",
      "sha256": "931da0fb551553e4ce1333bdd1a4ea784f5a6b6bf24b2ba592d402bc6c0e1cf0"
    },
    {
      "module": "astropy.utils.xml._iterparser",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/utils/xml/_iterparser.cpython-39-darwin.so",
      "sha256": "adcef4d2841871341cac36502fd8b1d68bffb0c2d2ae24a0d1384b5448f847e2"
    },
    {
      "module": "astropy.wcs._wcs",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/astropy/wcs/_wcs.cpython-39-darwin.so",
      "sha256": "4f52ecd503d6f416bd70caa61112ab0529ab0bf3720bab9b02e1c7050e83d7d0"
    },
    {
      "module": "binascii",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/binascii.cpython-39-darwin.so",
      "sha256": "89b39e24b8caa32965ec0d8ae803395cba7a21a6002ca310c3e70ac37ef1fe10"
    },
    {
      "module": "cytoolz.dicttoolz",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/_venv_bls/lib/python3.9/site-packages/cytoolz/dicttoolz.cpython-39-darwin.so",
      "sha256": "d36a15c863a57e009b30c492ce6236d032a4a2a20d9013d67fa3fb8cedaa8b12"
    },
    {
      "module": "cytoolz.functoolz",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/_venv_bls/lib/python3.9/site-packages/cytoolz/functoolz.cpython-39-darwin.so",
      "sha256": "fa6c2e6d4e0c570e1e57f44febf883b285fba4b56a4d37a70dbbfe14ceb06028"
    },
    {
      "module": "cytoolz.itertoolz",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/_venv_bls/lib/python3.9/site-packages/cytoolz/itertoolz.cpython-39-darwin.so",
      "sha256": "b2967fcd9383080b31044e6c4f431ad86aecca15bb2f827037fafc9f8f3b89d1"
    },
    {
      "module": "cytoolz.recipes",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/_venv_bls/lib/python3.9/site-packages/cytoolz/recipes.cpython-39-darwin.so",
      "sha256": "35d8df1bcfa8eb05043cc97ab22704e4ab7a3a831c412fea3fe987691db692a1"
    },
    {
      "module": "cytoolz.utils",
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/_venv_bls/lib/python3.9/site-packages/cytoolz/utils.cpython-39-darwin.so",
      "sha256": "06c1bd09345a82813e185c7c1d8aab26c8b30acedca1ba6fc53c0d655d62d7f3"
    },
    {
      "module": "erfa.ufunc",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/erfa/ufunc.abi3.so",
      "sha256": "7a6d8767e8d6caceb4fcf3ed56aa055a61d5216f57aa0c022d7dae273a1a2127"
    },
    {
      "module": "fcntl",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/fcntl.cpython-39-darwin.so",
      "sha256": "68aad0eb29df74714954713b8945301be9a3d8ac9a0a74d38906221c55684a18"
    },
    {
      "module": "grp",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/grp.cpython-39-darwin.so",
      "sha256": "0ca46024557a5d1ae45a76609d7355dce3f6444195c15b15dd8ff2c45f1b7a44"
    },
    {
      "module": "math",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/math.cpython-39-darwin.so",
      "sha256": "481a699baee3ebeee9f6c0d5976a6b7b41036d6d6f8ebb8eecd30c1da97a51b1"
    },
    {
      "module": "mmap",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/mmap.cpython-39-darwin.so",
      "sha256": "83b75c143039c8a84c420a52bd9f45a282bec65abd3a0e355fe284d11ffbc15b"
    },
    {
      "module": "numpy._core._multiarray_umath",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so",
      "sha256": "e870618cf0f8a4b73a928649aba064eee859f8e25a7912344c979f1d03679194"
    },
    {
      "module": "numpy.core._multiarray_tests",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/core/_multiarray_tests.cpython-39-darwin.so",
      "sha256": "9fdcecbf1325d89b700ab1bbc4694958d794fc073abce666b4ca1a9926c2d609"
    },
    {
      "module": "numpy.core._multiarray_umath",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so",
      "sha256": "e870618cf0f8a4b73a928649aba064eee859f8e25a7912344c979f1d03679194"
    },
    {
      "module": "numpy.fft._pocketfft_internal",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/fft/_pocketfft_internal.cpython-39-darwin.so",
      "sha256": "cfc7c758921da384994a66578d289d6c8aa710756a6af64a28f964b90fd5f546"
    },
    {
      "module": "numpy.linalg._umath_linalg",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/linalg/_umath_linalg.cpython-39-darwin.so",
      "sha256": "f8c19b528952ee81dfb723f2cadab00076febc3091654cc1244880d877fef7bf"
    },
    {
      "module": "numpy.random._bounded_integers",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/_bounded_integers.cpython-39-darwin.so",
      "sha256": "6e297ea492a9ac6ee567a6adcd71619f7b4bc1ea35b5d4d2f145666b64cac78c"
    },
    {
      "module": "numpy.random._common",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/_common.cpython-39-darwin.so",
      "sha256": "a299abb9c8c9a397ce153b3b8f2802ee04d1500146a22292c9aae268ce423980"
    },
    {
      "module": "numpy.random._generator",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/_generator.cpython-39-darwin.so",
      "sha256": "59e9f292a1e3d0540fc0139b51052605bf9a259e10f7c176db3506f86d3bd790"
    },
    {
      "module": "numpy.random._mt19937",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/_mt19937.cpython-39-darwin.so",
      "sha256": "df655e25f3ecf55c5331683bc13b0d2a6c90b4e53800fa3a30b265ddd984bc1f"
    },
    {
      "module": "numpy.random._pcg64",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/_pcg64.cpython-39-darwin.so",
      "sha256": "9395ae76c6358fdd1404de1aa502d3eb1eaee03577de8baf5abe4e2a7f334afb"
    },
    {
      "module": "numpy.random._philox",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/_philox.cpython-39-darwin.so",
      "sha256": "34afb5ee651b61456835ae435b9fa34612706f7db5098667e0c2ff3a41b017bc"
    },
    {
      "module": "numpy.random._sfc64",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/_sfc64.cpython-39-darwin.so",
      "sha256": "6395de6fe4a6edc82fd4c440dbe567f29f93c43fee0de52127a9f973a077b6a2"
    },
    {
      "module": "numpy.random.bit_generator",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/bit_generator.cpython-39-darwin.so",
      "sha256": "8f07bb63a03a6e861d2e6731fdc890d57a1d89b54be6d73ef104ce66d920e924"
    },
    {
      "module": "numpy.random.mtrand",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/numpy/random/mtrand.cpython-39-darwin.so",
      "sha256": "db0f9b8f5fd32a449a03d258530b399752aa3eade68ae6268d78f300023456db"
    },
    {
      "module": "pydantic_core._pydantic_core",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/pydantic_core/_pydantic_core.cpython-39-darwin.so",
      "sha256": "10e800093b5725f783cd52f37cb419f39ed42862ada2f1a5bf65a47b1d43e1e7"
    },
    {
      "module": "select",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/select.cpython-39-darwin.so",
      "sha256": "f1ba7ae457f69c2f9c28f40a518e8ec3b3ee55c93e53b26838b1a7ca40446a7f"
    },
    {
      "module": "termios",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/termios.cpython-39-darwin.so",
      "sha256": "49e86cfde6e41411a6426b7a2bb4e219ae5ac6bfa6c47c71cb5c0c7ceef75c39"
    },
    {
      "module": "unicodedata",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/unicodedata.cpython-39-darwin.so",
      "sha256": "99c9fde6e5c331bf7ae23f618fa973ec4cd4cb927e9eb674d7c9f16f45abf716"
    },
    {
      "module": "yaml._yaml",
      "path": "/Users/duhokim/Library/Python/3.9/lib/python/site-packages/yaml/_yaml.cpython-39-darwin.so",
      "sha256": "5293be326ca6ac0ff74f98f9c880815eb50d448de4568e4e1e2549127908155c"
    },
    {
      "module": "zlib",
      "path": "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/lib-dynload/zlib.cpython-39-darwin.so",
      "sha256": "7ea07df71547078514c569e682f97f9fb6657efbd8b9d161973567bc2aa49474"
    }
  ],
  "loaded_library_representation": "BLOCKED: 346 image names have no individual readable file",
  "non_enforced_env_lock_fields": [
    "scope"
  ],
  "prior_pin_mismatches": 0,
  "runtime_pin": {
    "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/agreement_run/RUNTIME_DEPENDENCIES_A1_FINAL.json",
    "sha256": "b59533dd3eb5be84493baba2c6fb8db01fc10845a3b23d105348e73045f89f51"
  },
  "synthetic_BLS": "PASS",
  "synthetic_RICE_1": "PASS",
  "synthetic_configurations_scored": 96,
  "versions": {
    "astropy": "6.0.1",
    "numpy": "1.26.4",
    "py_ecc": "8.0.0",
    "python": "3.9.6"
  }
}

EXIT_CODE=0
```

## System image probe

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$PWD/_optionA_dev/_venv_bls/lib/python3.9/site-packages" /Library/Developer/CommandLineTools/usr/bin/python3 - <<'PY'
import json,ctypes,os
from pathlib import Path
from _optionA_dev.agreement_run import run_path as rp
import numpy,py_ecc
from astropy.io import fits
from astropy.wcs import WCS
lib=ctypes.CDLL(None)
result={}
try:
    f=lib._dyld_get_shared_cache_uuid
    f.argtypes=[ctypes.POINTER(ctypes.c_ubyte)];f.restype=ctypes.c_bool
    uuid=(ctypes.c_ubyte*16)()
    ok=f(uuid)
    result["shared_cache_uuid_available"]=bool(ok)
    result["shared_cache_uuid_hex"]=bytes(uuid).hex() if ok else None
except AttributeError:
    result["shared_cache_uuid_available"]=False
result["paths"]=[]
for name in ["/usr/lib/libSystem.B.dylib","/usr/lib/libobjc.A.dylib",
             "/System/Library/dyld/dyld_shared_cache_arm64e",
             "/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/dyld_shared_cache_arm64e",
             "/usr/bin/dyld_shared_cache_util",
             "/Library/Developer/CommandLineTools/usr/bin/dyld_shared_cache_util"]:
    p=Path(name)
    row={"path":name,"exists":p.exists(),"is_file":p.is_file(),"readable":os.access(name,os.R_OK)}
    if p.exists(): row["bytes"]=p.stat().st_size
    result["paths"].append(row)
print(json.dumps(result,indent=2,sort_keys=True))

PY
```

```text
{
  "paths": [
    {
      "exists": false,
      "is_file": false,
      "path": "/usr/lib/libSystem.B.dylib",
      "readable": false
    },
    {
      "exists": false,
      "is_file": false,
      "path": "/usr/lib/libobjc.A.dylib",
      "readable": false
    },
    {
      "exists": false,
      "is_file": false,
      "path": "/System/Library/dyld/dyld_shared_cache_arm64e",
      "readable": false
    },
    {
      "bytes": 573440,
      "exists": true,
      "is_file": true,
      "path": "/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/dyld_shared_cache_arm64e",
      "readable": true
    },
    {
      "exists": false,
      "is_file": false,
      "path": "/usr/bin/dyld_shared_cache_util",
      "readable": false
    },
    {
      "exists": false,
      "is_file": false,
      "path": "/Library/Developer/CommandLineTools/usr/bin/dyld_shared_cache_util",
      "readable": false
    }
  ],
  "shared_cache_uuid_available": true,
  "shared_cache_uuid_hex": "f2e86c536052388bba715a0c9b569413"
}

EXIT_CODE=0
```

The v42 report carries this receipt's actual final-byte SHA-256.
