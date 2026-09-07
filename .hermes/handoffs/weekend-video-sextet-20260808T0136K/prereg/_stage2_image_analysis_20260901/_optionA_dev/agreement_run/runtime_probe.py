"""Reproduce the bounded, offline runtime inventory; never invoke a RunPath stage.

Run from the lane root using the required interpreter/environment:
python3 -m _optionA_dev.agreement_run.runtime_probe
Prints JSON to stdout; caller explicitly chooses the authoring output file.
This probe module is included among the pinned sources it observes.
"""
import io
import json
from pathlib import Path
import sys

from _optionA_dev.agreement_run import run_path as rp
from _optionA_dev.agreement_run import runtime_binding as rb


def pin(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"path": str(path), "resolved_path": str(path),
            "sha256": rp.sha(raw), "bytes": len(raw)}


def measure():
    rb.preload(rp.CODE)
    import numpy as np
    from astropy.io import fits
    from astropy.wcs import WCS
    from py_ecc.bls import G2Basic
    # These are generated numeric arrays and a synthetic key/message, never
    # real pixels/labels, selection inputs, a beacon round or study execution.
    plane = np.arange(64, dtype=np.int32).reshape(8, 8)
    stream = io.BytesIO()
    fits.HDUList([fits.PrimaryHDU(), fits.CompImageHDU(plane, compression_type="RICE_1")]).writeto(stream)
    with fits.open(io.BytesIO(stream.getvalue()), memmap=False) as hdus:
        rp.require(np.array_equal(hdus[1].data, plane), "PROBE-RICE-1")
    wcs = WCS(naxis=2)
    wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    wcs.wcs.crval = [40., 10.]
    wcs.all_pix2world([[1., 1.]], 0)
    np.fft.fft2(plane)
    message = b"A1 V49 offline runtime identity probe"
    rp.require(G2Basic.Verify(G2Basic.SkToPk(5), message, G2Basic.Sign(5, message)), "PROBE-BLS")
    result = rb.capture(pin, rp.require)
    result["probe"] = {"module": "_optionA_dev.agreement_run.runtime_probe",
                       "operations": ["declared code imports", "generated RICE_1 FITS encode/decode",
                                      "generated TAN WCS transform", "NumPy FFT", "synthetic-key BLS",
                                      "default TLS context/opener without network"],
                       "network_requests": 0, "real_study_stages": 0}
    result["limits"] = [
        "TOCTOU: extension modules are hashed and later imported with no lock between. Even the immediate pre-import recheck evidences disk bytes at check time, not the bytes the loader used (or an extension already loaded in this process).",
        "Both source and existing standard cache candidates are pinned conservatively; Python exposes no retrospective proof of which cached bytes it read. Bytecode-write suppression does not prevent cache reads.",
        "Cache-image byte binding is SHA-256 of every complete active cache-family file on disk, linked by the main cache UUID and its subcache table. It is check-time file-byte binding under the TOCTOU disclosure above.",
        "New observed module origins, cache candidates and dyld images must match the register at pre-access and pre-record checks or refuse."
    ]
    return result


if __name__ == "__main__":
    # Ensure the probe also has its ordinary import identity, so its source is
    # included even though the embedding __main__ entry is outside the API.
    from _optionA_dev.agreement_run.runtime_probe import measure
    sys.stdout.buffer.write(rp.canonical(measure()))
