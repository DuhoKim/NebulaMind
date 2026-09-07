"""Check-time runtime identity, never loaded-page attestation.

Only observed import artifacts are collected; no installed package tree sweep.
Sources AND every existing standard cache candidate are pinned conservatively:
Python does not expose retrospectively which cache was actually read. Built-in
and frozen code is represented by the pinned executable/Python framework.
dyld cache images use platform identity, not fabricated per-image bytes.
"""
import ctypes
import importlib
import importlib.machinery
import importlib.util
import os
from pathlib import Path
import platform
import struct
import sys

SCHEMA = "A1-RUNTIME-REPRESENTATION-1"
CACHE_MECHANISM = ("dyld active shared-cache UUID + kern.osversion + machine + "
                   "cache architecture; per-image loaded path + LC_UUID + "
                   "Mach-O CPU type/subtype + confirmed cache residency")


def _api(lib, name, args, result):
    fn = getattr(lib, name)
    fn.argtypes, fn.restype = args, result
    return fn


def dyld_snapshot(require):
    """Use dyld's active-process APIs; ASLR addresses are evidence of residency
    only and are not persisted or hashed. Missing SPI/identity fails closed.
    """
    require(sys.platform == "darwin", "RUNTIME-PLATFORM: dyld requires Darwin")
    try:
        lib = ctypes.CDLL(None)
        count = _api(lib, "_dyld_image_count", [], ctypes.c_uint32)
        name = _api(lib, "_dyld_get_image_name", [ctypes.c_uint32], ctypes.c_char_p)
        header = _api(lib, "_dyld_get_image_header", [ctypes.c_uint32], ctypes.c_void_p)
        image_uuid = _api(lib, "_dyld_get_image_uuid",
                          [ctypes.c_void_p, ctypes.c_void_p], ctypes.c_bool)
        cache_uuid = _api(lib, "_dyld_get_shared_cache_uuid", [ctypes.c_void_p], ctypes.c_bool)
        contains = _api(lib, "_dyld_shared_cache_contains_path", [ctypes.c_char_p], ctypes.c_bool)
        cache_range = _api(lib, "_dyld_get_shared_cache_range",
                           [ctypes.POINTER(ctypes.c_size_t)], ctypes.c_void_p)
        sysctl = _api(lib, "sysctlbyname", [ctypes.c_char_p, ctypes.c_void_p,
                     ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p, ctypes.c_size_t], ctypes.c_int)
    except AttributeError as exc:
        require(False, "RUNTIME-IDENTITY-API-UNAVAILABLE: " + str(exc))
    uuid = ctypes.create_string_buffer(16)
    require(cache_uuid(uuid) and any(uuid.raw), "SHARED-CACHE-UUID-UNAVAILABLE")
    uuid_hex = uuid.raw.hex()
    size = ctypes.c_size_t()
    start = cache_range(ctypes.byref(size))
    require(start and size.value >= 16, "SHARED-CACHE-RANGE-UNAVAILABLE")
    cache_magic = ctypes.string_at(start, 16).decode("ascii").strip("\0 ")
    require(cache_magic.startswith("dyld_v1"), "SHARED-CACHE-HEADER: " + cache_magic)
    length = ctypes.c_size_t()
    require(sysctl(b"kern.osversion", None, ctypes.byref(length), None, 0) == 0
            and 0 < length.value < 1024, "OS-BUILD-UNAVAILABLE: kern.osversion")
    build = ctypes.create_string_buffer(length.value)
    require(sysctl(b"kern.osversion", build, ctypes.byref(length), None, 0) == 0,
            "OS-BUILD-UNAVAILABLE: kern.osversion")
    identity = {"mechanism": CACHE_MECHANISM, "uuid": uuid_hex,
                "os_build": build.value.decode("ascii"), "machine": platform.machine(),
                "cache_architecture": cache_magic.split()[-1]}
    images = []
    initial_count = count()
    for index in range(initial_count):
        raw_name, address = name(index), header(index)
        require(raw_name and address, "DYLD-IMAGE-UNAVAILABLE: index " + str(index))
        path = os.fsdecode(raw_name)
        require(image_uuid(address, uuid) and any(uuid.raw), "DYLD-LC-UUID-UNAVAILABLE: " + path)
        magic, cpu, subtype = struct.unpack("<Iii", ctypes.string_at(address, 12))
        require(magic == 0xfeedfacf, "DYLD-MACH-O-UNSUPPORTED: " + path)
        resident = bool(start <= address < start + size.value and contains(raw_name))
        exists = Path(path).is_file()
        require(exists or resident, "RUNTIME-UNBINDABLE-IMAGE: " + path +
                "; no standalone file and not confirmed in active shared cache")
        images.append({"path": path, "lc_uuid": uuid.raw.hex(), "cpu_type": cpu,
                       "cpu_subtype": subtype, "in_shared_cache": resident,
                       "binding": "FILE-SHA256" if exists else "DYLD-CACHE-IDENTITY"})
    require(count() == initial_count, "DYLD-IMAGE-SET-CHANGED-DURING-CHECK")
    return {"shared_cache": identity, "images": sorted(images, key=lambda x: x["path"])}


def preload(code):
    """Import the adapter's declared dependencies, without running a stage.
    TLS setup uses local trust configuration, with no request or socket.
    """
    for rel in code:
        importlib.import_module(rel[:-3].replace("/", ".").removesuffix(".__init__"))
    from astropy.io import fits
    from astropy.wcs import WCS
    from py_ecc.bls import G2Basic
    import ssl
    from urllib.request import build_opener
    ssl.create_default_context()
    build_opener()
    # platform.platform() is itself an env_lock operand; mac_ver reads the
    # system plist and lazily imports plistlib/pyexpat on this interpreter.
    platform.platform()


def module_snapshot(require):
    """Describe actual module origins plus standard cache candidates.
    Namespace packages have no code bytes; built-in/frozen modules have no
    standalone artifacts. Generated fileless helper names are enumerated, not
    hashed or treated as standalone imports; this does not attest their memory.
    """
    result = []
    for name, module in sorted(tuple(sys.modules.items())):
        if module is None:
            continue
        spec = getattr(module, "__spec__", None)
        path = getattr(module, "__file__", None)
        origin = getattr(spec, "origin", None)
        # The embedding caller/interactive entry is outside this API's import
        # inventory. The declared adapter itself is always a pinned import.
        if name in ("__main__", "__mp_main__"):
            continue
        if path:
            require(Path(path).is_file(), "RUNTIME-MODULE-FILE-UNAVAILABLE: " + name + ": " + path)
            row = {"module": name, "path": str(Path(path).resolve()), "binding": "FILE-SHA256"}
            if path.endswith(".py"):
                # __cached__ can be mutated; derive the interpreter's standard
                # candidate as well, and bind both if different and present.
                candidates = {importlib.util.cache_from_source(path)}
                if getattr(module, "__cached__", None):
                    candidates.add(module.__cached__)
                row["cache_candidates"] = sorted(str(Path(p).resolve()) for p in candidates)
            result.append(row)
        elif origin in ("built-in", "frozen"):
            result.append({"module": name, "binding": origin})
        elif spec is not None and origin is None and getattr(spec, "submodule_search_locations", None) is not None:
            result.append({"module": name, "binding": "namespace"})
        else:
            # e.g. six.moves: generated code belongs to its pinned producer;
            # record the name explicitly so new fileless modules cannot pass.
            result.append({"module": name, "binding": "generated-fileless"})
    return result


def capture(pin, require):
    native = dyld_snapshot(require)
    modules = module_snapshot(require)
    # dyld itself is not one of its enumerated client images.
    paths = {str(Path(sys.executable).resolve()), "/usr/lib/dyld"}
    for row in modules:
        if "path" in row:
            paths.add(row["path"])
        paths.update(p for p in row.get("cache_candidates", []) if Path(p).is_file())
    paths.update(str(Path(r["path"]).resolve()) for r in native["images"] if r["binding"] == "FILE-SHA256")
    return {"schema": SCHEMA, **native, "modules": modules,
            "files": [pin(p) for p in sorted(paths)]}


def verify(evidence, read_pin, require):
    require(isinstance(evidence, dict) and evidence.get("schema") == SCHEMA,
            "MISSING-RUNTIME-EVIDENCE: RUNTIME_REPRESENTATION")
    require(isinstance(evidence.get("files"), list) and evidence["files"], "MISSING-RUNTIME-ARTIFACTS")
    files = {}
    for pin in evidence["files"]:
        read_pin(pin)
        path = str(Path(pin["path"]).resolve())
        require(path not in files, "DUPLICATE-RUNTIME-ARTIFACT: " + path)
        files[path] = pin
    def bound(path):
        path = str(Path(path).resolve())
        require(path in files, "MISSING-RUNTIME-ARTIFACT: " + path)
    bound(sys.executable)
    bound("/usr/lib/dyld")
    native = dyld_snapshot(require)
    require(evidence.get("shared_cache") == native["shared_cache"],
            "SHARED-CACHE-IDENTITY-MISMATCH: active dyld cache UUID/OS build/architecture/mechanism")
    expected_images = {}
    for row in evidence.get("images", []):
        require(isinstance(row, dict) and isinstance(row.get("path"), str), "RUNTIME-IMAGE-SCHEMA")
        require(row["path"] not in expected_images, "DUPLICATE-RUNTIME-IMAGE: " + row["path"])
        expected_images[row["path"]] = row
        if row.get("binding") == "FILE-SHA256":
            bound(row["path"])
        else:
            require(row.get("binding") == "DYLD-CACHE-IDENTITY" and row.get("in_shared_cache") is True
                    and "sha256" not in row, "RUNTIME-CACHE-REPRESENTATION: " + row["path"])
    for row in native["images"]:
        path = row["path"]
        require(path in expected_images, "UNREGISTERED-RUNTIME-IMAGE: " + path)
        require(row == expected_images[path], "RUNTIME-IMAGE-IDENTITY-MISMATCH: " + path)
    expected_modules = {}
    for row in evidence.get("modules", []):
        require(isinstance(row, dict) and isinstance(row.get("module"), str), "RUNTIME-MODULE-SCHEMA")
        name = row["module"]
        require(name not in expected_modules, "DUPLICATE-RUNTIME-MODULE: " + name)
        expected_modules[name] = row
        if "path" in row:
            bound(row["path"])
        for path in row.get("cache_candidates", []):
            if Path(path).is_file():
                bound(path)
    for row in module_snapshot(require):
        name = row["module"]
        require(name in expected_modules, "UNREGISTERED-RUNTIME-MODULE: " + name + ": " + row.get("path", row["binding"]))
        require(row == expected_modules[name], "RUNTIME-MODULE-IDENTITY-MISMATCH: " + name + ": " + row.get("path", row["binding"]))
    return {"schema": SCHEMA, "verified_files": len(files),
            "observed_modules": len(module_snapshot(require)),
            "observed_images": len(native["images"]), "shared_cache": native["shared_cache"]}
