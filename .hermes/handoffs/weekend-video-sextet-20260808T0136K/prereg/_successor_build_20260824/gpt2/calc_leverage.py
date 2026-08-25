#!/usr/bin/env python3
"""Count-weighted angular leverage calculator and deterministic fixtures."""

from __future__ import annotations

import numpy as np

AXIS_RA_DEG = 217.0
AXIS_DEC_DEG = 32.0
FIXTURE_SEED = 20260824
FIXTURE_SIZE = 200_000
N_EQ_REQUIREMENT = 100_000.0


def _unit_vector(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    ra_rad = np.deg2rad(ra_deg)
    dec_rad = np.deg2rad(dec_deg)
    cos_dec = np.cos(dec_rad)
    return np.column_stack(
        (cos_dec * np.cos(ra_rad), cos_dec * np.sin(ra_rad), np.sin(dec_rad))
    )


_AXIS_VECTOR = _unit_vector(
    np.array([AXIS_RA_DEG]), np.array([AXIS_DEC_DEG])
)[0]


def _validate_inputs(
    ra_deg: np.ndarray, dec_deg: np.ndarray, n_gal: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    ra = np.asarray(ra_deg, dtype=float)
    dec = np.asarray(dec_deg, dtype=float)
    counts = np.asarray(n_gal, dtype=float)

    if ra.ndim != 1 or dec.ndim != 1 or counts.ndim != 1:
        raise ValueError("ra_deg, dec_deg, and n_gal must be one-dimensional arrays")
    if not (ra.shape == dec.shape == counts.shape):
        raise ValueError("ra_deg, dec_deg, and n_gal must have identical shapes")
    if ra.size == 0:
        raise ValueError("input arrays must not be empty")
    if not np.all(np.isfinite(ra)) or not np.all(np.isfinite(dec)):
        raise ValueError("coordinates must be finite")
    if np.any((dec < -90.0) | (dec > 90.0)):
        raise ValueError("declinations must lie in [-90, 90] degrees")
    if not np.all(np.isfinite(counts)):
        raise ValueError("n_gal must be finite")
    if np.any(counts < 0.0) or np.any(counts != np.floor(counts)):
        raise ValueError("n_gal must contain non-negative integer counts")
    if np.sum(counts) <= 0.0:
        raise ValueError("total galaxy count must be positive")

    return ra, dec, counts


def cosine_to_axis(ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    """Return cos(theta) between each ICRS position and the fixed axis."""
    ra = np.asarray(ra_deg, dtype=float)
    dec = np.asarray(dec_deg, dtype=float)
    if ra.ndim != 1 or dec.ndim != 1 or ra.shape != dec.shape:
        raise ValueError("ra_deg and dec_deg must be same-shaped one-dimensional arrays")
    if not np.all(np.isfinite(ra)) or not np.all(np.isfinite(dec)):
        raise ValueError("coordinates must be finite")
    if np.any((dec < -90.0) | (dec > 90.0)):
        raise ValueError("declinations must lie in [-90, 90] degrees")
    return np.clip(_unit_vector(ra, dec) @ _AXIS_VECTOR, -1.0, 1.0)


def _statistics(cos_theta: np.ndarray, counts: np.ndarray) -> dict[str, float | int]:
    total_float = float(np.sum(counts))
    total = int(total_float)
    mean_c = float(np.dot(counts, cos_theta) / total_float)
    var_c = float(np.dot(counts, (cos_theta - mean_c) ** 2) / total_float)
    leverage = total_float * var_c
    return {
        "N_total": total,
        "mean_c": mean_c,
        "var_c": var_c,
        "leverage": leverage,
        "N_eq": 3.0 * leverage,
    }


def calculate_leverage(
    ra_deg: np.ndarray, dec_deg: np.ndarray, n_gal: np.ndarray
) -> dict[str, float | int]:
    """Calculate count-weighted population statistics for all input bricks."""
    ra, dec, counts = _validate_inputs(ra_deg, dec_deg, n_gal)
    return _statistics(cosine_to_axis(ra, dec), counts)


def polar_select(
    ra_deg: np.ndarray, dec_deg: np.ndarray, n_gal: np.ndarray, q: float
) -> dict[str, float | int]:
    """Apply POLAR(q), accepting whole bricks in descending abs(cos(theta))."""
    ra, dec, counts = _validate_inputs(ra_deg, dec_deg, n_gal)
    if not np.isfinite(q) or not 0.0 < q <= 1.0:
        raise ValueError("q must be finite and satisfy 0 < q <= 1")

    cos_theta = cosine_to_axis(ra, dec)
    order = np.argsort(-np.abs(cos_theta), kind="stable")
    cumulative = np.cumsum(counts[order])
    threshold = q * float(np.sum(counts))
    final_position = int(np.searchsorted(cumulative, threshold, side="left"))
    selected = order[: final_position + 1]

    result = _statistics(cos_theta[selected], counts[selected])
    result["N_accept"] = result.pop("N_total")
    return result


def _radec_at_axis_cosines(cos_theta: np.ndarray, azimuth: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Construct positions having specified axis cosine and random azimuth."""
    reference = np.array([0.0, 0.0, 1.0])
    basis_x = np.cross(reference, _AXIS_VECTOR)
    basis_x /= np.linalg.norm(basis_x)
    basis_y = np.cross(_AXIS_VECTOR, basis_x)

    transverse = np.sqrt(np.maximum(0.0, 1.0 - cos_theta**2))
    vectors = (
        cos_theta[:, None] * _AXIS_VECTOR
        + transverse[:, None]
        * (
            np.cos(azimuth)[:, None] * basis_x
            + np.sin(azimuth)[:, None] * basis_y
        )
    )
    ra_deg = np.rad2deg(np.arctan2(vectors[:, 1], vectors[:, 0])) % 360.0
    dec_deg = np.rad2deg(np.arcsin(np.clip(vectors[:, 2], -1.0, 1.0)))
    return ra_deg, dec_deg


def _sample_positions(
    rng: np.random.Generator, cos_theta: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    azimuth = rng.uniform(0.0, 2.0 * np.pi, cos_theta.size)
    return _radec_at_axis_cosines(cos_theta, azimuth)


def _fixture_row(
    name: str,
    result: dict[str, float | int],
    analytic_var: float,
) -> str:
    error = abs(float(result["var_c"]) - analytic_var)
    requirement = "PASS" if float(result["N_eq"]) >= N_EQ_REQUIREMENT else "FAIL"
    return (
        f"{name:<20} {int(result['N_total']):>9d} "
        f"{float(result['mean_c']):>12.8f} {float(result['var_c']):>12.8f} "
        f"{analytic_var:>12.8f} {error:>12.8f} "
        f"{float(result['leverage']):>14.3f} {float(result['N_eq']):>14.3f} "
        f"{requirement:>10}"
    )


def run_fixtures() -> None:
    """Generate and print all fixed-seed fixture results."""
    rng = np.random.default_rng(FIXTURE_SEED)
    counts = np.ones(FIXTURE_SIZE, dtype=np.int64)

    full_c = rng.uniform(-1.0, 1.0, FIXTURE_SIZE)
    full_ra, full_dec = _sample_positions(rng, full_c)
    full_result = calculate_leverage(full_ra, full_dec, counts)

    polar_cap_c = rng.choice(np.array([-1.0, 1.0]), FIXTURE_SIZE) * rng.uniform(
        0.8, 1.0, FIXTURE_SIZE
    )
    polar_cap_ra, polar_cap_dec = _sample_positions(rng, polar_cap_c)
    polar_cap_result = calculate_leverage(polar_cap_ra, polar_cap_dec, counts)

    equatorial_c = rng.uniform(-0.2, 0.2, FIXTURE_SIZE)
    equatorial_ra, equatorial_dec = _sample_positions(rng, equatorial_c)
    equatorial_result = calculate_leverage(equatorial_ra, equatorial_dec, counts)

    selected = polar_select(full_ra, full_dec, counts, 0.25)
    selected_row = {
        "N_total": selected["N_accept"],
        "mean_c": selected["mean_c"],
        "var_c": selected["var_c"],
        "leverage": selected["leverage"],
        "N_eq": selected["N_eq"],
    }

    print(f"fixed_seed={FIXTURE_SEED}")
    print(f"axis_icrs_deg=({AXIS_RA_DEG:.1f}, {AXIS_DEC_DEG:.1f})")
    print(f"N_eq_requirement={N_EQ_REQUIREMENT:.0f}")
    print()
    print(
        "fixture                N_gal       mean_c        var_c analytic_var    abs_error"
        "       leverage           N_eq N_eq>=100k"
    )
    print("-" * 131)
    print(_fixture_row("full_sphere", full_result, 1.0 / 3.0))
    print(_fixture_row("abs_c_gt_0.8", polar_cap_result, (1.0 + 0.8 + 0.8**2) / 3.0))
    print(_fixture_row("abs_c_lt_0.2", equatorial_result, 0.2**2 / 3.0))
    print(_fixture_row("POLAR(0.25)", selected_row, (1.0 + 0.75 + 0.75**2) / 3.0))
    print()
    print("fixture_checks")
    print(
        "full_sphere_var_within_0.01_of_one_third="
        + ("PASS" if abs(float(full_result["var_c"]) - 1.0 / 3.0) <= 0.01 else "FAIL")
    )
    print(
        "polar_0.25_var_exceeds_0.75="
        + ("PASS" if float(selected["var_c"]) > 0.75 else "FAIL")
    )
    print(f"polar_0.25_N_accept={int(selected['N_accept'])}")


if __name__ == "__main__":
    run_fixtures()
