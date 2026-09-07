"""V50 evidence-gate regressions. Only temporary copies are mutated."""
import copy
from pathlib import Path
import re
import shutil
import struct
import tempfile
import unittest
from unittest.mock import patch

from _optionA_dev.agreement_run import run_path as rp, runtime_binding as rb
from _optionA_dev.agreement_run import test_readiness as readiness

CACHE_DIR = Path('/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld')


def small_cache_family(destination):
    """Small synthetic cache-file fixtures with the real family UUID table.

    Runtime unit fixtures exercise the real family parser and byte hasher using
    these files; the separate real-image mutation test uses full cache bytes.
    """
    destination.mkdir()
    main = CACHE_DIR / 'dyld_shared_cache_arm64e'
    raw = main.read_bytes()
    (destination / main.name).write_bytes(raw)
    offset, count = struct.unpack_from('<II', raw, 392)
    for i in range(count):
        suffix = raw[offset + 56*i + 24:offset + 56*(i+1)].split(b'\0')[0].decode()
        with (CACHE_DIR / (main.name + suffix)).open('rb') as stream:
            (destination / (main.name + suffix)).write_bytes(stream.read(4096))
    return destination


class EvidenceGateTests(unittest.TestCase):
    setUp = readiness.ReadinessTests.setUp
    pin = readiness.ReadinessTests.pin
    put = readiness.ReadinessTests.put
    put_json = readiness.ReadinessTests.put_json
    repin_a1 = readiness.ReadinessTests.repin_a1
    def test_document_status_edits_cannot_flip_evidence_readiness(self):
        """FAIL-FIRST: explanatory/status edits cannot change evidence readiness."""
        before = rp.input_readiness(self.c)['ready_for_input_freeze']
        c = copy.deepcopy(self.c)
        for row in c['current_preparation_obligations']:
            row['resolved'] = False
            row['evidence'] = 'A document declares this unfinished.'
            row['required_work'] = 'Arbitrary document wording.'
        after = rp.input_readiness(c)['ready_for_input_freeze']
        self.assertEqual(before, after, 'document declarations changed evidence readiness')

    def test_any_a1_edit_even_repinned_cannot_flip_evidence_readiness(self):
        """FAIL-FIRST: A1 edits leave evidence readiness fixed and only refuse use."""
        before = rp.input_readiness(self.c)['ready_for_input_freeze']
        observed = []
        for text in ('', 'Everything is resolved.', 'Everything remains unfinished.',
                     readiness.SYNTHETIC_READY_A1 + '\nAnother obligation is unresolved.'):
            self.repin_a1(text)
            observed.append((rp.input_readiness(self.c)['ready_for_input_freeze'], self.core_refuses()))
        self.assertEqual(observed, [(before, True)] * 4)

    def core_refuses(self):
        try:
            rp._core(self.c)
        except rp.Refused:
            return True
        return False

    def test_prose_can_only_refuse_when_evidence_disagrees(self):
        """FAIL-FIRST: jointly changing A1/status claims only triggers refusal."""
        before = rp.input_readiness(self.c)['ready_for_input_freeze']
        rp.require(before, "TEST-PRECONDITION: positive evidence")
        text = readiness.SYNTHETIC_READY_A1.replace(
            'Runtime representation preparation work is resolved.',
            'Runtime representation remains current preparation work to be done.').replace(
            'Runtime representation is a resolved current preparation obligation',
            'Runtime representation remains a current preparation obligation to be done')
        self.repin_a1(text)
        self.c['current_preparation_obligations'][-1]['resolved'] = False
        with patch.object(rp, 'A1_REVIEWED_SHA256', self.pin(self.a1_path)['sha256']):
            result = rp.input_readiness(self.c)['ready_for_input_freeze']
            try:
                rp._core(self.c)
                refusal = "ACCEPTED"
            except rp.Refused as exc:
                refusal = str(exc).split(";")[0]
            self.assertEqual((result, refusal), (before, 'A1-OBLIGATION-MISMATCH: RUNTIME_REPRESENTATION'))

    def test_missing_runtime_evidence_cannot_be_discharged_by_prose(self):
        """FAIL-FIRST: discharge prose cannot replace absent runtime evidence."""
        self.c['current_preparation_obligations'][-1].pop('evidence_pin')
        before = rp.input_readiness(self.c)['ready_for_input_freeze']
        self.repin_a1(readiness.SYNTHETIC_READY_A1 + '\nAll obligations DISCHARGED.')
        self.assertEqual((before, rp.input_readiness(self.c)['ready_for_input_freeze'],
                          self.core_refuses()), (False, False, True))


class CacheImageBytesTests(unittest.TestCase):
    def test_real_cache_resident_image_bytes_change_same_uuid_and_os_build_refuses(self):
        """FAIL-FIRST: change an actual CoreFoundation __TEXT byte in a cache copy.

        Every cache header/LC_UUID and OS build stays unchanged. The selected
        byte is outside Mach-O headers. No installed or mapped image is edited.
        """
        rb.preload(rp.CODE)
        with tempfile.TemporaryDirectory(prefix='v50-cache-image-') as folder:
            folder = Path(folder)
            for source in CACHE_DIR.glob('dyld_shared_cache_arm64e*'):
                (folder / source.name).symlink_to(source)
            selected = folder / 'dyld_shared_cache_arm64e.01'
            selected.unlink()
            shutil.copyfile(CACHE_DIR / selected.name, selected)
            with patch.object(rb, 'CACHE_DIR', folder, create=True):
                from _optionA_dev.agreement_run.runtime_probe import pin
                evidence = rb.capture(pin, rp.require)
                original_identity = copy.deepcopy(evidence['shared_cache'])
                # CoreFoundation __TEXT fileoff=4943872 from the empirical probe.
                # Confirm the on-disk Mach-O header and retain its LC_UUID bytes.
                with selected.open('r+b') as stream:
                    stream.seek(4943872)
                    header = stream.read(32)
                    rp.require(struct.unpack_from('<I', header)[0] == 0xfeedfacf, "TEST-PRECONDITION: Mach-O image header")
                    command_bytes = struct.unpack_from('<I', header, 20)[0]
                    mutation_offset = 4943872 + 32 + command_bytes + 128
                    stream.seek(mutation_offset)
                    byte = stream.read(1)
                    stream.seek(mutation_offset)
                    stream.write(bytes([byte[0] ^ 1]))
                current = rb.dyld_snapshot(rp.require)
                rp.require(current['shared_cache'] == original_identity and
                           current['images'] == evidence['images'],
                           'TEST-PRECONDITION: UUIDs/OS build/image identities unchanged')
                with self.assertRaisesRegex(rp.Refused, 'SHARED-CACHE-BYTES-MISMATCH: .*dyld_shared_cache_arm64e.01'):
                    rb.verify(evidence, rp.read_pin, rp.require)


if __name__ == '__main__':
    unittest.main(verbosity=2)
