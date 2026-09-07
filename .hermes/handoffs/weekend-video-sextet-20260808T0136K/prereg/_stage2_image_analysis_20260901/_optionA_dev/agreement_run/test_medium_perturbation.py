"""Synthetic rasters only; no catalogue, FITS file, real label or RNG is used.

POSITIVE-REGRESSION means a new producer's contract check, not a predecessor
reproduction claim. There is no predecessor MEDIUM perturbation producer.
Every test method has one outcome assertion, as scripts/failfirst_kit.py requires.
"""
import ast
import contextlib
import inspect
import json
import sys
import unittest
from unittest.mock import patch

from _optionA_dev.agreement_run import medium_perturbation as mp
import numpy as np

def raster(objid=0, kind="unchanged"):
    yy, xx = np.indices((180, 180), dtype=np.float64)
    dx, dy = xx - 89.5, yy - 89.5
    r = np.hypot(dx, dy)
    theta = np.arctan2(dy, dx)
    radial = 4.0 * np.log(np.maximum(r, 0.5) / 8.0)
    disk = np.exp(-r / 18.0)
    image = 1.0 + disk * (1.0 + 0.8 * np.cos(2.0 * (theta - radial)))
    maskbits = np.zeros((180, 180), dtype=np.int32)
    nexp = np.ones((180, 180), dtype=np.int32)
    if kind == "flip":
        medium = (np.cos(2.0 * (theta + radial)) > 0.8) & (r > 4.0) & (r < 55.0)
        image[medium] += 12.0 * disk[medium]
        maskbits[medium] = 1 << 11
    elif kind == "unchanged":
        maskbits[30, 30] = 1 << 11
    elif kind == "negative":
        image = np.fliplr(image).copy()
        maskbits[30, 30] = 1 << 11
    elif kind == "tie":
        image[:] = 1.0
        maskbits[30, 30] = 1 << 11
    elif kind == "off_raster":
        maskbits[0, 0] = 1 << 11
    elif kind != "none":
        raise ValueError(kind)
    scale = 0.262 / 3600.0
    return {"objid": objid, "stage": "tuning", "image": image,
            "maskbits": maskbits, "nexp": nexp, "ra": 40.0, "dec": 10.0,
            "brick": "0400p100", "wcs": {"crpix": (90.5, 90.5),
                "crval": (40.0, 10.0), "cd": ((-scale, 0.0), (0.0, scale))}}


# Audit hooks observe even aliases of open/socket/subprocess, unlike patching a
# single import name. Installed only by this synthetic test module, never by the
# producer. Already-loaded renderer configuration is preparation code metadata.
_guard_active = False
_io_events = []


def _deny_io(event, args):
    if _guard_active and (event == "open" or event.startswith("socket.") or
                          event.startswith("subprocess.") or
                          event in ("os.system", "os.exec", "os.posix_spawn")):
        _io_events.append(event)
        raise AssertionError("PRODUCER I/O FORBIDDEN: " + event)


sys.addaudithook(_deny_io)


@contextlib.contextmanager
def no_io():
    global _guard_active
    _io_events.clear()
    _guard_active = True
    try:
        yield
    finally:
        _guard_active = False


class CannotRead:
    def __array__(self, *args, **kwargs):
        raise AssertionError("external array conversion was accessed")

    def __iter__(self):
        raise AssertionError("external reader was accessed")

    def __repr__(self):
        raise AssertionError("label value was inspected")


class MediumPerturbationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = tuple(raster(i, kind) for i, kind in enumerate(
            ("flip", "unchanged", "negative", "none")))
        cls.original_images = tuple(obj["image"].tobytes() for obj in cls.inputs)
        # Every substantive fixture executes the real renderer and all 96
        # Estimator.chi instances. No scripted chi return values are used.
        cls.disclosure = mp.produce_tuning_disclosure(cls.inputs)
        cls.tie = mp.produce_tuning_disclosure((raster(10, "tie"),))
        cls.off = mp.produce_tuning_disclosure((raster(11, "off_raster"),))
        refused = raster(12, "unchanged")
        refused["nexp"][89, 89] = 0
        cls.refused = mp.produce_tuning_disclosure((refused,))
        # Exactly 32,398 accepted source pixels: 16,199 ones and 16,199
        # threes. The two MEDIUM pixels have value 100. Lower median = 1,
        # whereas the ordinary even-count median would be 2.
        even = raster(13, "none")
        even["maskbits"][80, 80:82] = 1 << 11
        accepted = np.flatnonzero(even["maskbits"].ravel() == 0)
        even["image"][:] = 100.0
        even["image"].ravel()[accepted[:16199]] = 1.0
        even["image"].ravel()[accepted[16199:]] = 3.0
        cls.even = mp.produce_tuning_disclosure((even,))
        p = cls.disclosure["objects"][0]["pairs"][0]
        print("\nSYNTHETIC EVIDENCE: config_index=0 kept_chi=%r replaced_chi=%r"
              " sign_flipped=%r; all 96 configurations report 1/3."
              % (p["kept"]["chi"], p["replaced"]["chi"], p["sign_flipped"]))

    def test_no_medium_has_no_pair(self):
        """POSITIVE-REGRESSION: a raster without MEDIUM has no perturbation pair."""
        self.assertEqual(self.disclosure["objects"][3]["pairs"], [])

    def test_medium_elsewhere_in_brick_has_no_pair(self):
        """POSITIVE-REGRESSION: the per-raster covariate determines membership."""
        self.assertEqual(self.off["objects"][0]["pairs"], [])

    def test_real_chi_sign_change_is_a_flip(self):
        """POSITIVE-REGRESSION: the masked opposing spiral flips every real scorer."""
        self.assertTrue(all(p["sign_flipped"] is True
                            for p in self.disclosure["objects"][0]["pairs"]))

    def test_two_actual_chi_values_are_reported(self):
        """POSITIVE-REGRESSION: both nonzero chi values exhibit opposite signs."""
        p = self.disclosure["objects"][0]["pairs"][0]
        self.assertLess(p["kept"]["chi"] * p["replaced"]["chi"], 0.0)

    def test_same_negative_sign_is_not_a_flip(self):
        """POSITIVE-REGRESSION: retaining a negative sign reports no flip."""
        self.assertTrue(all(p["sign_flipped"] is False
                            for p in self.disclosure["objects"][1]["pairs"]))

    def test_same_positive_sign_is_not_a_flip(self):
        """POSITIVE-REGRESSION: retaining a positive sign reports no flip."""
        self.assertTrue(all(p["sign_flipped"] is False
                            for p in self.disclosure["objects"][2]["pairs"]))

    def test_rate_is_flips_over_eligible_objects(self):
        """POSITIVE-REGRESSION: each configuration has one flip in three objects."""
        self.assertEqual({s["sign_flip_rate"] for s in self.disclosure["configurations"]},
                         {1 / 3})

    def test_rate_denominator_excludes_objects_without_medium(self):
        """POSITIVE-REGRESSION: four inputs provide three eligible MEDIUM objects."""
        self.assertEqual({s["eligible_objects"]
                          for s in self.disclosure["configurations"]}, {3})

    def test_lower_median_is_the_lower_observed_value(self):
        """POSITIVE-REGRESSION: the even-count replacement is one, not two."""
        self.assertEqual(self.even["objects"][0]["perturbation_lower_median"], 1.0)

    def test_replacement_chain_uses_that_lower_median(self):
        """POSITIVE-REGRESSION: the reused chain retains the same source fill."""
        self.assertEqual(self.even["objects"][0]["replaced_render"]["replacement_value"],
                         1.0)

    def test_medium_never_becomes_a_contamination_flag(self):
        """POSITIVE-REGRESSION: even central MEDIUM pixels flag neither arm."""
        row = self.disclosure["objects"][0]
        self.assertEqual((row["kept_render"]["F"], row["replaced_render"]["F"]), (0, 0))

    def test_zero_exposure_still_refuses_central_contamination(self):
        """POSITIVE-REGRESSION: the protected-region rule remains executed."""
        row = self.refused["objects"][0]
        self.assertEqual((row["kept_render"]["status"],
                          row["replaced_render"]["status"]), ("REFUSED", "REFUSED"))

    def test_tie_is_unknown_not_a_false_nonflip(self):
        """POSITIVE-REGRESSION: zero chi does not provide a comparable sign."""
        self.assertIsNone(self.tie["objects"][0]["pairs"][0]["sign_flipped"])

    def test_no_eligible_objects_has_null_rate(self):
        """POSITIVE-REGRESSION: a tie-only disclosure cannot report zero percent."""
        self.assertIsNone(self.tie["configurations"][0]["sign_flip_rate"])

    def test_refused_objects_are_explicit(self):
        """POSITIVE-REGRESSION: render refusal is retained in the unscored count."""
        self.assertEqual(self.refused["configurations"][0]["unscored_pairs"], 1)

    def test_all_existing_configurations_are_reported_in_order(self):
        """POSITIVE-REGRESSION: every existing configuration index is retained."""
        self.assertEqual([s["config_index"] for s in self.disclosure["configurations"]],
                         list(range(96)))

    def test_source_pixels_are_unchanged(self):
        """POSITIVE-REGRESSION: the paired computation leaves all input pixels intact."""
        self.assertEqual(tuple(obj["image"].tobytes() for obj in self.inputs),
                         self.original_images)

    def test_preprocessing_variant_is_refused(self):
        """POSITIVE-REGRESSION: no preprocessing selector exists in the API."""
        with self.assertRaises(TypeError):
            mp.produce_tuning_disclosure(self.inputs, preprocessing="local-annulus")

    def test_configuration_selection_is_refused(self):
        """POSITIVE-REGRESSION: no caller can select a configuration subset."""
        with self.assertRaises(TypeError):
            mp.produce_tuning_disclosure(self.inputs, config_index=0)

    def test_scorer_callback_is_refused(self):
        """POSITIVE-REGRESSION: an external scorer or reader cannot be requested."""
        with self.assertRaises(TypeError):
            mp.produce_tuning_disclosure(self.inputs, scorer=CannotRead())

    def test_label_argument_is_refused(self):
        """POSITIVE-REGRESSION: labels cannot be supplied to the public function."""
        with self.assertRaises(TypeError):
            mp.produce_tuning_disclosure(self.inputs, labels=CannotRead())

    def test_label_field_is_refused_without_reading_it(self):
        """POSITIVE-REGRESSION: surplus label metadata is rejected unread."""
        obj = raster()
        obj["label"] = CannotRead()
        with self.assertRaisesRegex(mp.DisclosureRefused, "LABEL-FREE"):
            mp.produce_tuning_disclosure((obj,))

    def test_label_bearing_wcs_metadata_is_refused(self):
        """POSITIVE-REGRESSION: nested WCS metadata cannot smuggle in labels."""
        obj = raster()
        obj["wcs"]["labels"] = CannotRead()
        with self.assertRaisesRegex(mp.DisclosureRefused, "NUMERIC-TAN-WCS"):
            mp.produce_tuning_disclosure((obj,))

    def test_lazy_batch_cannot_request_external_data(self):
        """POSITIVE-REGRESSION: a loader cannot execute while fetching objects."""
        with self.assertRaisesRegex(mp.DisclosureRefused, "EXACT-TUPLE"):
            mp.produce_tuning_disclosure(CannotRead())

    def test_array_conversion_hook_is_not_accessed(self):
        """POSITIVE-REGRESSION: numeric data cannot be supplied through a reader hook."""
        obj = raster()
        obj["image"] = CannotRead()
        with self.assertRaisesRegex(mp.DisclosureRefused, "PLAIN-NUMERIC"):
            mp.produce_tuning_disclosure((obj,))

    def test_object_dtype_cannot_carry_labels(self):
        """POSITIVE-REGRESSION: label-bearing objects cannot enter a pixel plane."""
        obj = raster()
        obj["image"] = np.empty((180, 180), dtype=object)
        with self.assertRaisesRegex(mp.DisclosureRefused, "PLAIN-NUMERIC"):
            mp.produce_tuning_disclosure((obj,))

    def test_non_tuning_stage_is_refused(self):
        """POSITIVE-REGRESSION: non-tuning pixels cannot enter the declared API."""
        obj = raster()
        obj["stage"] = "validation"
        with self.assertRaisesRegex(mp.DisclosureRefused, "TUNING-ONLY"):
            mp.produce_tuning_disclosure((obj,))

    def test_duplicate_objects_are_refused(self):
        """POSITIVE-REGRESSION: duplicate object IDs cannot inflate the denominator."""
        with self.assertRaisesRegex(mp.DisclosureRefused, "UNIQUE-INTEGER"):
            mp.produce_tuning_disclosure((raster(), raster()))

    def test_entire_batch_schema_is_checked_before_render(self):
        """POSITIVE-REGRESSION: labels in a later row refuse before any processing."""
        obj = raster(1)
        obj["labels"] = CannotRead()
        with patch.object(mp._chain, "render_object",
                          side_effect=AssertionError("render before validation")):
            with self.assertRaisesRegex(mp.DisclosureRefused, "LABEL-FREE"):
                mp.produce_tuning_disclosure((raster(0), obj))

    def test_producer_runs_with_all_external_io_denied(self):
        """POSITIVE-REGRESSION: a real paired run performs no label-capable I/O."""
        with no_io():
            result = mp.produce_tuning_disclosure((raster(20, "flip"),))
        self.assertEqual((_io_events, result["configurations"][0]["flips"]), ([], 1))

    def test_imports_exclude_label_loading_and_run_path(self):
        """POSITIVE-REGRESSION: the producer imports only fixed numeric components."""
        tree = ast.parse(inspect.getsource(mp))
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.append(node.module)
        self.assertEqual(set(imports), {"__future__", "os", "numpy", "astropy.wcs",
                         "study_renderer", "_optionA_dev.fourier_chirality"})

    def test_disclosure_is_strict_json_serializable(self):
        """POSITIVE-REGRESSION: retained output has no tensor bytes or NaN values."""
        serialized = json.dumps(self.disclosure, allow_nan=False)
        self.assertEqual(json.loads(serialized)["schema"], "A1-MEDIUM-PERTURBATION-1")


if __name__ == "__main__":
    unittest.main()
