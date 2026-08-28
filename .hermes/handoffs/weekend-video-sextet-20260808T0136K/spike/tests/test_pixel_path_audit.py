from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from astropy.io import fits

SPIKE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SPIKE_DIR))

from pixel_path_audit import (
    audit_header,
    audit_fits_file,
    convert_fits_to_npy,
    create_synthetic_spiral_fits,
    inject_synthetic_spiral,
    mirror_synthetic_fits,
    recover_synthetic_chirality,
    scramble_wcs,
    fits_to_array,
)


def make_cd_header(*, cd11: float, cd22: float) -> fits.Header:
    header = fits.Header()
    header["NAXIS"] = 2
    header["NAXIS1"] = 9
    header["NAXIS2"] = 9
    header["CTYPE1"] = "RA---TAN"
    header["CTYPE2"] = "DEC--TAN"
    header["CRVAL1"] = 180.0
    header["CRVAL2"] = 0.0
    header["CRPIX1"] = 5.0
    header["CRPIX2"] = 5.0
    header["CD1_1"] = cd11
    header["CD1_2"] = 0.0
    header["CD2_1"] = 0.0
    header["CD2_2"] = cd22
    return header


def test_cd_determinant_states_pixel_to_sky_parity_explicitly() -> None:
    preserving = audit_header(make_cd_header(cd11=1.0e-4, cd22=1.0e-4))
    reversing = audit_header(make_cd_header(cd11=-1.0e-4, cd22=1.0e-4))

    assert preserving.matrix_source == "CD"
    assert np.isclose(preserving.determinant, 1.0e-8)
    assert preserving.parity == "PRESERVING"
    assert preserving.certainty == "DETERMINATE_LINEAR_WCS"

    assert reversing.matrix_source == "CD"
    assert np.isclose(reversing.determinant, -1.0e-8)
    assert reversing.parity == "REVERSING"
    assert reversing.certainty == "DETERMINATE_LINEAR_WCS"


def test_pc_cdelt_determinant_includes_axis_scale_signs() -> None:
    header = make_cd_header(cd11=1.0e-4, cd22=1.0e-4)
    for key in ("CD1_1", "CD1_2", "CD2_1", "CD2_2"):
        del header[key]
    header["PC1_1"] = 0.0
    header["PC1_2"] = 1.0
    header["PC2_1"] = 1.0
    header["PC2_2"] = 0.0
    header["CDELT1"] = -2.0e-4
    header["CDELT2"] = 3.0e-4

    result = audit_header(header)

    assert result.matrix_source == "PC*CDELT"
    assert np.isclose(result.determinant, 6.0e-8)
    assert result.parity == "PRESERVING"


def test_singular_wcs_is_indeterminate_and_fails_closed() -> None:
    header = make_cd_header(cd11=0.0, cd22=1.0e-4)

    with np.testing.assert_raises_regex(ValueError, "singular or non-finite"):
        audit_header(header)


def test_numerically_indeterminate_wcs_fails_closed() -> None:
    header = make_cd_header(cd11=1.0, cd22=1.0 + 1.0e-15)
    header["CD1_2"] = 1.0
    header["CD2_1"] = 1.0

    with np.testing.assert_raises_regex(ValueError, "numerically indeterminate"):
        audit_header(header)


def test_partial_cd_matrix_fails_closed_instead_of_falling_back_to_pc() -> None:
    header = make_cd_header(cd11=-1.0e-4, cd22=1.0e-4)
    del header["CD2_2"]
    header["CDELT1"] = -1.0e-4
    header["CDELT2"] = 1.0e-4

    with np.testing.assert_raises_regex(ValueError, "incomplete CD matrix"):
        audit_header(header)


def test_non_celestial_axes_fail_closed() -> None:
    header = make_cd_header(cd11=-1.0e-4, cd22=1.0e-4)
    header["CTYPE1"] = "LINEAR"
    header["CTYPE2"] = "LINEAR"

    with np.testing.assert_raises_regex(ValueError, "celestial longitude/latitude"):
        audit_header(header)


def test_unmodelled_distortion_fails_closed_instead_of_overclaiming_linear_parity() -> None:
    header = make_cd_header(cd11=-1.0e-4, cd22=1.0e-4)
    header["CTYPE1"] = "RA---TAN-SIP"
    header["CTYPE2"] = "DEC--TAN-SIP"
    header["A_ORDER"] = 2
    header["A_2_0"] = 0.01
    header["B_ORDER"] = 2
    header["B_0_2"] = -0.01

    with np.testing.assert_raises_regex(ValueError, "distortion keywords"):
        audit_header(header)


def test_native_fits_array_preserves_dtype_values_and_fits_row_order(tmp_path: Path) -> None:
    data = np.array([[101, 102, 103], [201, 202, 203]], dtype=np.int16)
    path = tmp_path / "row_order.fits"
    fits.PrimaryHDU(data=data, header=make_cd_header(cd11=1.0e-4, cd22=1.0e-4)).writeto(path)

    converted = fits_to_array(path, row_order="fits-native")

    assert converted.row_order == "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW"
    assert converted.array_transform_determinant == 1
    assert converted.data.dtype.kind == data.dtype.kind
    assert converted.data.dtype.itemsize == data.dtype.itemsize
    assert np.array_equal(converted.data, data)
    assert converted.data[0, 0] == 101  # FITS pixel (x=1, y=1)
    assert converted.data[1, 0] == 201  # FITS pixel (x=1, y=2)


def test_top_left_view_is_explicit_vertical_flip_and_lossless(tmp_path: Path) -> None:
    data = np.array([[101, 102, 103], [201, 202, 203]], dtype=np.int16)
    path = tmp_path / "row_order.fits"
    fits.PrimaryHDU(data=data, header=make_cd_header(cd11=1.0e-4, cd22=1.0e-4)).writeto(path)

    converted = fits_to_array(path, row_order="top-left")

    assert converted.row_order == "TOP_LEFT_VERTICAL_FLIP_FROM_FITS_NATIVE"
    assert converted.array_transform_determinant == -1
    assert converted.data.dtype.kind == data.dtype.kind
    assert converted.data.dtype.itemsize == data.dtype.itemsize
    assert np.array_equal(converted.data, np.flipud(data))
    assert np.array_equal(np.flipud(converted.data), data)


def test_npy_conversion_round_trips_exact_bytes_and_writes_transform_receipt(tmp_path: Path) -> None:
    data = np.array([[1.25, -0.0], [np.nan, 8.5]], dtype=np.float32)
    path = tmp_path / "science.fits"
    fits.PrimaryHDU(data=data, header=make_cd_header(cd11=-1.0e-4, cd22=1.0e-4)).writeto(path)

    receipt = convert_fits_to_npy(path, tmp_path / "science.npy", row_order="fits-native")
    loaded = np.load(tmp_path / "science.npy")
    expected = fits_to_array(path).data

    assert loaded.dtype == expected.dtype
    assert loaded.tobytes() == expected.tobytes()
    assert receipt["lossless_byte_equal"] is True
    assert receipt["array_transform_determinant"] == 1
    assert receipt["wcs_parity"] == "REVERSING"


def test_injected_spiral_recovers_known_sky_chirality_for_both_wcs_parities(
    tmp_path: Path,
) -> None:
    for wcs_parity in ("PRESERVING", "REVERSING"):
        for chirality in (-1, 1):
            path = tmp_path / f"{wcs_parity.lower()}_{chirality:+d}.fits"
            create_synthetic_spiral_fits(
                path, wcs_parity=wcs_parity, sky_chirality=chirality
            )

            result = recover_synthetic_chirality(path, row_order="fits-native")

            assert result["expected_sky_chirality"] == chirality
            assert result["recovered_sky_chirality"] == chirality
            assert result["status"] == "PASS"


def test_explicit_top_left_transform_preserves_chirality_but_silent_flip_is_detected(
    tmp_path: Path,
) -> None:
    path = tmp_path / "top_left.fits"
    create_synthetic_spiral_fits(path, wcs_parity="PRESERVING", sky_chirality=1)

    explicit = recover_synthetic_chirality(
        path, row_order="top-left", honor_array_transform=True
    )
    silent = recover_synthetic_chirality(
        path, row_order="top-left", honor_array_transform=False
    )

    assert explicit["recovered_sky_chirality"] == 1
    assert explicit["status"] == "PASS"
    assert silent["recovered_sky_chirality"] == -1
    assert silent["status"] == "FAIL_SILENT_ROW_FLIP_DETECTED"


def test_scrambled_wcs_null_flips_header_parity_and_is_detected(tmp_path: Path) -> None:
    path = tmp_path / "base.fits"
    scrambled = tmp_path / "scrambled.fits"
    create_synthetic_spiral_fits(path, wcs_parity="PRESERVING", sky_chirality=-1)

    result = scramble_wcs(path, scrambled)

    assert result["original_wcs_parity"] == "PRESERVING"
    assert result["scrambled_wcs_parity"] == "REVERSING"
    assert result["expected_sky_chirality"] == -1
    assert result["recovered_sky_chirality"] == 1
    assert result["status"] == "PASS_FAULT_DETECTED"


def test_mirrored_synthetic_frame_is_bit_exact_and_signed_recovery_swaps(
    tmp_path: Path,
) -> None:
    original = tmp_path / "original.fits"
    mirrored = tmp_path / "mirrored.fits"
    create_synthetic_spiral_fits(
        original, wcs_parity="REVERSING", sky_chirality=-1
    )

    receipt = mirror_synthetic_fits(original, mirrored)
    original_result = recover_synthetic_chirality(
        original, row_order="fits-native"
    )
    mirrored_result = recover_synthetic_chirality(
        mirrored, row_order="fits-native"
    )

    assert receipt["pixels_exact_horizontal_mirror"] is True
    assert receipt["wcs_header_unchanged"] is True
    assert original_result["recovered_sky_chirality"] == -1
    assert mirrored_result["recovered_sky_chirality"] == 1
    assert (
        mirrored_result["recovered_sky_chirality"]
        == -original_result["recovered_sky_chirality"]
    )
    assert receipt["status"] == "PASS_EXACT_MIRROR_SWAP"


def test_synthetic_spiral_injected_into_calibration_pixels_preserves_wcs_and_recovers(
    tmp_path: Path,
) -> None:
    base = tmp_path / "calibration.fits"
    data = np.arange(16 * 16, dtype=np.float32).reshape(16, 16)
    fits.PrimaryHDU(
        data=data,
        header=make_cd_header(cd11=-7.27777777777778e-05, cd22=7.27777777777778e-05),
    ).writeto(base)

    for sky_chirality in (-1, 1):
        injected = tmp_path / f"injected_{sky_chirality:+d}.fits"
        receipt = inject_synthetic_spiral(
            base, injected, sky_chirality=sky_chirality
        )
        recovery = recover_synthetic_chirality(
            injected, row_order="fits-native"
        )

        assert receipt["base_shape"] == [16, 16]
        assert receipt["wcs_cards_unchanged"] is True
        assert receipt["wcs_cards_sha256_before"] == receipt["wcs_cards_sha256_after"]
        assert len(receipt["wcs_cards_sha256_before"]) == 64
        assert receipt["status"] == "PASS_SYNTHETIC_INJECTION"
        assert recovery["expected_sky_chirality"] == sky_chirality
        assert recovery["recovered_sky_chirality"] == sky_chirality
        assert recovery["status"] == "PASS"


def test_chirality_harness_refuses_non_synthetic_fits(tmp_path: Path) -> None:
    path = tmp_path / "not_synthetic.fits"
    data = np.arange(25, dtype=np.float32).reshape(5, 5)
    fits.PrimaryHDU(data=data, header=make_cd_header(cd11=-1.0e-4, cd22=1.0e-4)).writeto(path)

    with np.testing.assert_raises_regex(ValueError, "synthetic calibration frames only"):
        recover_synthetic_chirality(path, row_order="fits-native")


def test_file_audit_reports_sha_shape_matrix_and_row_order_without_chirality(
    tmp_path: Path,
) -> None:
    path = tmp_path / "calibration.fits"
    data = np.arange(20, dtype=np.float32).reshape(4, 5)
    fits.PrimaryHDU(data=data, header=make_cd_header(cd11=-1.0e-4, cd22=1.0e-4)).writeto(path)

    result = audit_fits_file(path, row_order="fits-native")

    assert result["input_path"] == str(path.resolve())
    assert len(result["input_sha256"]) == 64
    assert result["shape"] == [4, 5]
    assert result["dtype"] == ">f4"
    assert result["ctype"] == ["RA---TAN", "DEC--TAN"]
    assert result["radesys"] is None
    assert result["matrix_source"] == "CD"
    assert result["wcs_parity"] == "REVERSING"
    assert result["row_order"] == "FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW"
    assert result["chirality_computed"] is False


def test_cli_audit_prints_machine_readable_checker_output(tmp_path: Path) -> None:
    path = tmp_path / "cli.fits"
    data = np.arange(20, dtype=np.float32).reshape(4, 5)
    fits.PrimaryHDU(data=data, header=make_cd_header(cd11=-1.0e-4, cd22=1.0e-4)).writeto(path)

    completed = subprocess.run(
        [sys.executable, str(SPIKE_DIR / "pixel_path_audit.py"), "audit", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert result["wcs_parity"] == "REVERSING"
    assert result["chirality_computed"] is False


def test_cli_harness_outputs_every_synthetic_frame_and_fault_receipt(tmp_path: Path) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(SPIKE_DIR / "pixel_path_audit.py"),
            "harness",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert [frame["name"] for frame in result["frames"]] == [
        "synthetic_preserving_minus",
        "synthetic_preserving_plus",
        "synthetic_reversing_minus",
        "synthetic_reversing_plus",
        "synthetic_preserving_minus_scrambled_wcs",
        "synthetic_reversing_minus_mirrored",
    ]
    assert all(frame["audit"]["chirality_computed"] is False for frame in result["frames"])
    assert all(frame["native_conversion"]["lossless_byte_equal"] is True for frame in result["frames"])
    assert all(Path(frame["native_conversion"]["output_path"]).is_file() for frame in result["frames"])
    assert all(item["status"] == "PASS" for item in result["recoveries"])
    assert result["top_left_conversion_control"]["lossless_byte_equal"] is True
    assert result["top_left_conversion_control"]["array_transform_determinant"] == -1
    assert result["silent_row_flip_control"]["status"] == "FAIL_SILENT_ROW_FLIP_DETECTED"
    assert result["scrambled_wcs_control"]["status"] == "PASS_FAULT_DETECTED"
    assert result["mirror_control"]["receipt"]["status"] == "PASS_EXACT_MIRROR_SWAP"
    assert result["mirror_control"]["original_recovery"]["recovered_sky_chirality"] == -1
    assert result["mirror_control"]["mirrored_recovery"]["recovered_sky_chirality"] == 1
    assert result["summary"] == "PASS_SYNTHETIC_PIXEL_PATH_AUDIT"


def test_cli_inject_reports_calibration_wcs_and_known_sign_recovery(tmp_path: Path) -> None:
    base = tmp_path / "base.fits"
    output = tmp_path / "injected.fits"
    data = np.zeros((16, 16), dtype=np.float32)
    fits.PrimaryHDU(
        data=data,
        header=make_cd_header(cd11=-7.27777777777778e-05, cd22=7.27777777777778e-05),
    ).writeto(base)

    completed = subprocess.run(
        [
            sys.executable,
            str(SPIKE_DIR / "pixel_path_audit.py"),
            "inject",
            str(base),
            str(output),
            "--sky-chirality",
            "1",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert result["injection"]["status"] == "PASS_SYNTHETIC_INJECTION"
    assert result["audit"]["wcs_parity"] == "REVERSING"
    assert result["recovery"]["recovered_sky_chirality"] == 1
    assert result["recovery"]["status"] == "PASS"


def test_cli_scramble_reports_injected_wcs_fault_detection(tmp_path: Path) -> None:
    original = tmp_path / "original.fits"
    scrambled = tmp_path / "scrambled.fits"
    create_synthetic_spiral_fits(
        original, wcs_parity="PRESERVING", sky_chirality=-1
    )

    completed = subprocess.run(
        [
            sys.executable,
            str(SPIKE_DIR / "pixel_path_audit.py"),
            "scramble-wcs",
            str(original),
            str(scrambled),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    result = json.loads(completed.stdout)

    assert completed.stderr == ""
    assert result["status"] == "PASS_FAULT_DETECTED"
    assert result["original_wcs_parity"] == "PRESERVING"
    assert result["scrambled_wcs_parity"] == "REVERSING"
