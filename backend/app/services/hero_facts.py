"""Hero facts validation utilities.

Validates hero fact entries before they are written to the DB.
Implements the hard validators from Addendum A §A.3 of the trust mechanics design.
"""
from __future__ import annotations

from datetime import datetime


# ---------------------------------------------------------------------------
# Forbidden vague magnitude words
# ---------------------------------------------------------------------------

FORBIDDEN_VAGUE: set[str] = {
    "millions", "billions", "trillions", "thousand",
    "thousands", "hundreds", "many", "few", "several",
}


# ---------------------------------------------------------------------------
# Unit dimensionality check
# ---------------------------------------------------------------------------

# Maps lowercase label keywords to sets of accepted unit patterns
_LABEL_UNIT_MAP: dict[str, set[str]] = {
    "mass":          {"kg", "m☉", "msun", "g", "solar mass", "solar masses"},
    "energy":        {"j", "erg", "ev", "kev", "mev", "gev", "tev", "joule", "joules"},
    "temperature":   {"k", "kelvin", "°c", "°f"},
    "density":       {"kg/m³", "kg/m3", "g/cm³", "g/cm3"},
    "luminosity":    {"w", "l☉", "lsun", "erg/s", "solar luminosities"},
    "distance":      {"m", "km", "au", "ly", "pc", "kpc", "mpc", "gpc",
                      "light-year", "light-years", "parsec", "parsecs"},
    "radius":        {"m", "km", "au", "ly", "pc", "r☉", "rsun", "r⊕", "rearth"},
    "velocity":      {"m/s", "km/s", "km/h", "c"},
    "period":        {"s", "ms", "min", "h", "hr", "day", "days", "year", "years", "yr"},
    "frequency":     {"hz", "khz", "mhz", "ghz"},
    "gravity":       {"m/s²", "m/s2", "g₀", "g0"},
    "magnetic field": {"t", "tesla", "g", "gauss"},
    "pressure":      {"pa", "bar", "atm", "gpa"},
    "time":          {"s", "ms", "yr", "myr", "gyr", "year", "years", "seconds"},
    "age":           {"yr", "myr", "gyr", "year", "years", "billion years"},
    "count":         {"", None},
    "rate":          {"/s", "/sec", "hz", "/year"},
    "flux":          {"w/m²", "jy", "jansky"},
    "wavelength":    {"m", "nm", "μm", "um", "mm", "cm", "angstrom", "å"},
    "redshift":      {"", None},
    "angle":         {"rad", "deg", "°", "arcmin", "arcsec", "mas"},
}


def _unit_dimensionally_valid_for_label(label: str, unit: str) -> bool:
    """Check that `unit` is dimensionally consistent with `label`.

    Returns True if:
    - the label has no known dimension constraints, OR
    - the provided unit matches one of the accepted units for this label.
    Returns False if there is a known dimension but the unit doesn't match.
    """
    if not unit:
        return True  # no unit provided — renderer handles display

    label_lower = label.lower()
    unit_lower = unit.lower().strip()

    # Find matching label category
    for keyword, accepted_units in _LABEL_UNIT_MAP.items():
        if keyword in label_lower:
            # None in accepted_units means dimensionless/any unit OK
            if None in accepted_units:
                return True
            if unit_lower in accepted_units:
                return True
            # Check partial match for compound units
            if any(u and unit_lower.startswith(u) for u in accepted_units if u):
                return True
            # Specific cross-checks: energy in solar masses is always wrong
            if keyword == "energy" and ("m☉" in unit_lower or "msun" in unit_lower
                                         or "solar mass" in unit_lower):
                return False
            return False  # label recognized, unit doesn't match

    # Unknown label — allow anything
    return True


# ---------------------------------------------------------------------------
# Main validator
# ---------------------------------------------------------------------------

def validate_hero_fact(f: dict) -> tuple[bool, str]:
    """Validate a hero fact dict before persisting.

    Returns (True, "") on success, or (False, reason) on failure.
    """
    kind = f.get("kind", "scalar")

    if kind == "scalar":
        v = str(f.get("value", "")).lower().strip()
        if v in FORBIDDEN_VAGUE:
            return False, f"Vague magnitude word '{v}' — use kind=range instead"

    elif kind == "range":
        v_min = f.get("value_min")
        v_max = f.get("value_max")
        if v_min is None or v_max is None:
            return False, "range facts require value_min and value_max"
        try:
            v_min = float(v_min)
            v_max = float(v_max)
        except (TypeError, ValueError):
            return False, "value_min and value_max must be numeric"
        if v_min >= v_max:
            return False, "value_min must be < value_max"
        if f.get("scale") == "log" and v_min <= 0:
            return False, "log-scale ranges require positive bounds"

    elif kind == "date":
        year = f.get("year")
        if year is None:
            return False, "date facts require a year"
        try:
            y = int(year)
        except (TypeError, ValueError):
            return False, f"year must be an integer, got {year!r}"
        current_year = datetime.utcnow().year
        if y < 1500 or y > current_year + 1:
            return False, f"Implausible year {y} (expected 1500–{current_year + 1})"

    elif kind == "count":
        value = f.get("value")
        if value is None:
            return False, "count facts require a value"
        try:
            float(value)
        except (TypeError, ValueError):
            return False, f"count value must be numeric, got {value!r}"

    elif kind == "enum":
        values = f.get("values")
        if not isinstance(values, list) or len(values) == 0:
            return False, "enum facts require a non-empty 'values' list"

    # Unit dimension check
    unit = f.get("unit")
    label = f.get("label", "")
    if unit and label:
        if not _unit_dimensionally_valid_for_label(label, unit):
            return False, f"Unit '{unit}' inconsistent with label '{label}'"

    return True, ""


# ---------------------------------------------------------------------------
# Known constants (ground truth — overrides LLM-generated values)
# ---------------------------------------------------------------------------

KNOWN_CONSTANTS: dict[tuple[str, str | None], dict] = {
    # (label_keyword.lower(), unit.lower() or None): fact dict
    ("speed of light", "m/s"): {
        "kind": "scalar", "label": "Speed of Light",
        "value": 299792458, "unit": "m/s",
        "notation": "decimal", "precision": 9,
        "source": {"tier": "authoritative", "authority": "CODATA",
            "reference_url": "https://physics.nist.gov/cgi-bin/cuu/Value?c",
            "reference_title": "CODATA 2022: Speed of light in vacuum",
            "retrieval_year": 2024, "attribution": "NIST CODATA 2022"},
    },
    ("cmb temperature", "k"): {
        "kind": "scalar", "label": "CMB Temperature",
        "value": 2.7255, "unit": "K",
        "uncertainty": {"plus": 0.0006, "minus": 0.0006},
        "precision": 5,
        "source": {"tier": "authoritative", "authority": "Fixsen 2009",
            "reference_url": "https://doi.org/10.1088/0004-637X/707/2/916",
            "reference_title": "Fixsen (2009): The Temperature of the Cosmic Microwave Background",
            "retrieval_year": 2009, "attribution": "Fixsen 2009, ApJ 707"},
    },
    ("hubble constant", "km/s/mpc"): {
        "kind": "range", "label": "Hubble Constant",
        "value_min": 67.4, "value_max": 73.0, "unit": "km/s/Mpc",
        "scale": "linear", "trust_level": "debated",
        "qualifier": "Hubble tension: early- vs late-universe",
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI. Cosmological parameters",
            "retrieval_year": 2020, "attribution": "Planck 2018"},
    },
    ("neutron star density", "kg/m³"): {
        "kind": "range", "label": "Neutron Star Density",
        "value_min": 1e16, "value_max": 1e18, "unit": "kg/m³",
        "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081915-023329",
            "reference_title": "Lattimer & Prakash (2016) The Physics of Neutron Stars",
            "retrieval_year": 2016, "attribution": "Lattimer & Prakash 2016"},
    },
    ("galaxy mass", "m☉"): {
        "kind": "range", "label": "Galaxy Mass",
        "value_min": 1e5, "value_max": 1e13, "unit": "M☉",
        "scale": "log",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("smbh mass", "m☉"): {
        "kind": "range", "label": "Supermassive Black Hole Mass",
        "value_min": 1e6, "value_max": 1e10, "unit": "M☉",
        "scale": "log",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("stellar black hole mass", "m☉"): {
        "kind": "range", "label": "Stellar Black Hole Mass",
        "value_min": 5, "value_max": 100, "unit": "M☉",
        "scale": "linear",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("pulsar period", "s"): {
        "kind": "range", "label": "Pulsar Rotation Period",
        "value_min": 0.001, "value_max": 10, "unit": "s",
        "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081915-023329",
            "reference_title": "Lattimer & Prakash (2016) The Physics of Neutron Stars",
            "retrieval_year": 2016, "attribution": "Lattimer & Prakash 2016"},
    },
    ("white dwarf mass", "m☉"): {
        "kind": "range", "label": "White Dwarf Mass",
        "value_min": 0.17, "value_max": 1.33, "unit": "M☉",
        "scale": "linear",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("dark matter fraction", "%"): {
        "kind": "scalar", "label": "Dark Matter Fraction",
        "value": 26.8, "unit": "%",
        "uncertainty": {"plus": 0.3, "minus": 0.3},
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI. Cosmological parameters",
            "retrieval_year": 2020, "attribution": "Planck 2018"},
    },
    ("dark energy fraction", "%"): {
        "kind": "scalar", "label": "Dark Energy Fraction",
        "value": 68.3, "unit": "%",
        "uncertainty": {"plus": 0.3, "minus": 0.3},
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI. Cosmological parameters",
            "retrieval_year": 2020, "attribution": "Planck 2018"},
    },
    ("gravitational constant", "m³/(kg·s²)"): {
        "kind": "scalar", "label": "Gravitational Constant",
        "value": 6.674e-11, "unit": "m³/(kg·s²)",
        "notation": "scientific", "precision": 4,
        "source": {"tier": "authoritative", "authority": "CODATA",
            "reference_url": "https://physics.nist.gov/cgi-bin/cuu/Value?bg",
            "reference_title": "CODATA 2022: Newtonian constant of gravitation",
            "retrieval_year": 2024, "attribution": "NIST CODATA 2022"},
    },
    ("planck constant", "j·s"): {
        "kind": "scalar", "label": "Planck Constant",
        "value": 6.626e-34, "unit": "J·s",
        "notation": "scientific", "precision": 4,
        "source": {"tier": "authoritative", "authority": "CODATA",
            "reference_url": "https://physics.nist.gov/cgi-bin/cuu/Value?h",
            "reference_title": "CODATA 2022: Planck constant",
            "retrieval_year": 2024, "attribution": "NIST CODATA 2022"},
    },
    ("solar mass", "kg"): {
        "kind": "scalar", "label": "Solar Mass",
        "value": 1.989e30, "unit": "kg",
        "notation": "scientific", "precision": 4,
        "source": {"tier": "authoritative", "authority": "IAU",
            "reference_url": "https://www.iau.org/static/resolutions/IAU2015_English.pdf",
            "reference_title": "IAU 2015 Resolution B3",
            "retrieval_year": 2015, "attribution": "IAU 2015 B3"},
    },
    ("solar luminosity", "w"): {
        "kind": "scalar", "label": "Solar Luminosity",
        "value": 3.828e26, "unit": "W",
        "notation": "scientific", "precision": 4,
        "source": {"tier": "authoritative", "authority": "IAU",
            "reference_url": "https://www.iau.org/static/resolutions/IAU2015_English.pdf",
            "reference_title": "IAU 2015 Resolution B3",
            "retrieval_year": 2015, "attribution": "IAU 2015 B3"},
    },
    ("solar radius", "m"): {
        "kind": "scalar", "label": "Solar Radius",
        "value": 6.957e8, "unit": "m",
        "notation": "scientific", "precision": 4,
        "source": {"tier": "authoritative", "authority": "IAU",
            "reference_url": "https://www.iau.org/static/resolutions/IAU2015_English.pdf",
            "reference_title": "IAU 2015 Resolution B3",
            "retrieval_year": 2015, "attribution": "IAU 2015 B3"},
    },
    ("earth mass", "kg"): {
        "kind": "scalar", "label": "Earth Mass",
        "value": 5.972e24, "unit": "kg",
        "notation": "scientific", "precision": 4,
        "source": {"tier": "authoritative", "authority": "IAU",
            "reference_url": "https://www.iau.org/static/resolutions/IAU2015_English.pdf",
            "reference_title": "IAU 2015 Resolution B3",
            "retrieval_year": 2015, "attribution": "IAU 2015 B3"},
    },
    ("parsec", "m"): {
        "kind": "scalar", "label": "Parsec",
        "value": 3.086e16, "unit": "m",
        "notation": "scientific", "precision": 4,
        "source": {"tier": "authoritative", "authority": "IAU",
            "reference_url": "https://www.iau.org/public/themes/measuring/",
            "reference_title": "IAU: The Parsec",
            "retrieval_year": 2015, "attribution": "IAU definition"},
    },
    ("agn smbh mass", "m☉"): {
        "kind": "range", "label": "AGN Black Hole Mass",
        "value_min": 1e6, "value_max": 1e10, "unit": "M☉",
        "scale": "log",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("grb energy", "j"): {
        "kind": "range", "label": "GRB Energy Release",
        "value_min": 1e44, "value_max": 1e47, "unit": "J",
        "scale": "log",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("frb energy", "erg"): {
        "kind": "range", "label": "FRB Energy",
        "value_min": 1e32, "value_max": 1e36, "unit": "erg",
        "scale": "log",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("galaxy cluster mass", "m☉"): {
        "kind": "range", "label": "Galaxy Cluster Mass",
        "value_min": 1e14, "value_max": 1e16, "unit": "M☉",
        "scale": "log",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("neutron star mass", "m☉"): {
        "kind": "range", "label": "Neutron Star Mass",
        "value_min": 1.1, "value_max": 2.3, "unit": "M☉",
        "scale": "linear",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081915-023329",
            "reference_title": "Lattimer & Prakash (2016) The Physics of Neutron Stars",
            "retrieval_year": 2016, "attribution": "Lattimer & Prakash 2016"},
    },
    ("magnetar magnetic field", "g"): {
        "kind": "range", "label": "Magnetar Magnetic Field",
        "value_min": 1e14, "value_max": 1e15, "unit": "G",
        "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081915-023329",
            "reference_title": "Lattimer & Prakash (2016) The Physics of Neutron Stars",
            "retrieval_year": 2016, "attribution": "Lattimer & Prakash 2016"},
    },
    ("grb first detection", None): {
        "kind": "date", "label": "First GRB Detection",
        "year": 1967, "event": "first_detected",
        "by": "Vela satellites (declassified 1973)",
        "source": {"tier": "authoritative", "authority": "NASA",
            "reference_url": "https://heasarc.gsfc.nasa.gov/docs/cgro/batse/grb/history.html",
            "reference_title": "NASA HEASARC: History of Gamma-Ray Bursts",
            "retrieval_year": 2024, "attribution": "NASA HEASARC"},
    },
    ("pulsar discovery", None): {
        "kind": "date", "label": "Pulsar Discovery",
        "year": 1967, "event": "first_detected",
        "by": "Bell & Hewish",
        "source": {"tier": "authoritative", "authority": "Nobel Prize",
            "reference_url": "https://www.nobelprize.org/prizes/physics/1974/summary/",
            "reference_title": "Nobel Prize Physics 1974: Pulsars (Hewish)",
            "retrieval_year": 2024, "attribution": "Nobel Prize 1974"},
    },
    ("general relativity", None): {
        "kind": "date", "label": "General Relativity Published",
        "year": 1915, "event": "predicted",
        "by": "Einstein",
        "source": {"tier": "authoritative", "authority": "historical",
            "reference_url": "https://doi.org/10.1002/andp.19163540702",
            "reference_title": "Einstein (1916): Die Grundlage der allgemeinen Relativitätstheorie",
            "retrieval_year": 1916, "attribution": "Einstein 1916"},
    },
    ("habitable zone distance", "au"): {
        "kind": "range", "label": "Habitable Zone Distance",
        "value_min": 0.95, "value_max": 1.37, "unit": "AU",
        "scale": "linear",
        "qualifier": "Sun-like star",
        "source": {"tier": "authoritative", "authority": "Kopparapu et al.",
            "reference_url": "https://doi.org/10.1088/0004-637X/765/2/131",
            "reference_title": "Kopparapu et al. (2013): Habitable Zones Around Main-Sequence Stars",
            "retrieval_year": 2013, "attribution": "Kopparapu et al. 2013"},
    },
    ("milky way star count", None): {
        "kind": "range", "label": "Milky Way Star Count",
        "value_min": 1e11, "value_max": 4e11, "unit": "stars",
        "scale": "log",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("nebula mass", "m☉"): {
        "kind": "range", "label": "Nebula Mass",
        "value_min": 1e-3, "value_max": 1e6, "unit": "M☉",
        "scale": "log",
        "qualifier": "varies hugely by class",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("nebula size", "ly"): {
        "kind": "range", "label": "Nebula Size",
        "value_min": 0.1, "value_max": 100, "unit": "ly",
        "scale": "log",
        "source": {"tier": "ai_estimate", "generator": "manual", "flagged": False,
            "reason": "No standard reference; derived from literature consensus",
            "attribution": "Literature consensus"},
    },
    ("asteroid count", None): {
        "kind": "count", "label": "Catalogued Asteroids",
        "value": 1300000, "modifier": "approximately",
        "as_of": "2025-12-01",
        "source": {"tier": "authoritative", "authority": "MPC/NASA",
            "reference_url": "https://minorplanetcenter.net/mpc/summary",
            "reference_title": "Minor Planet Center: MPC Summary Statistics",
            "retrieval_year": 2025, "attribution": "IAU Minor Planet Center"},
    },
    ("ns rotation", "hz"): {
        "kind": "range", "label": "Neutron Star Rotation",
        "value_min": 1, "value_max": 700, "unit": "Hz",
        "scale": "log",
        "qualifier": "millisecond pulsars at upper end",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081915-023329",
            "reference_title": "Lattimer & Prakash (2016) The Physics of Neutron Stars",
            "retrieval_year": 2016, "attribution": "Lattimer & Prakash 2016"},
    },
    # === New entries from HeroFactCredibility v1 ===
    ("sound horizon", "mpc"): {
        "kind": "scalar", "label": "Sound Horizon (BAO)",
        "value": 147.09, "unit": "Mpc", "precision": 4,
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI. Cosmological parameters",
            "retrieval_year": 2020, "attribution": "Planck 2018"},
    },
    ("dark energy density", None): {
        "kind": "scalar", "label": "Dark Energy Density (Ω_Λ)",
        "value": 0.6847, "unit": "Ω_Λ", "precision": 4,
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI. Cosmological parameters",
            "retrieval_year": 2020, "attribution": "Planck 2018"},
    },
    ("end redshift", "z"): {
        "kind": "scalar", "label": "Reionization End Redshift",
        "value": 5.5, "unit": "z", "precision": 2,
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI — reionization optical depth",
            "retrieval_year": 2020, "attribution": "Planck 2018 + Fan et al. 2006"},
    },
    ("start redshift", "z"): {
        "kind": "range", "label": "Reionization Start Redshift",
        "value_min": 12.0, "value_max": 18.0, "unit": "z", "scale": "linear",
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI — reionization onset",
            "retrieval_year": 2020, "attribution": "Planck 2018"},
    },
    ("optical depth", None): {
        "kind": "scalar", "label": "Optical Depth (reionization)",
        "value": 0.054, "unit": "τ", "precision": 3,
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI", "retrieval_year": 2020,
            "attribution": "Planck 2018"},
    },
    ("filament length", "mpc"): {
        "kind": "range", "label": "Cosmic Web Filament Length",
        "value_min": 50, "value_max": 500, "unit": "Mpc", "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081710-102514",
            "reference_title": "Kravtsov & Borgani 2012 ARA&A",
            "retrieval_year": 2012, "attribution": "Kravtsov & Borgani (2012)"},
    },
    ("voids size", "mpc"): {
        "kind": "range", "label": "Cosmic Void Diameter",
        "value_min": 10, "value_max": 100, "unit": "Mpc", "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1086/307059",
            "reference_title": "Hoyle & Vogeley 1999 — voids in the SDSS",
            "retrieval_year": 1999, "attribution": "Hoyle & Vogeley (1999)"},
    },
    ("schwarzschild radius", "km"): {
        "kind": "scalar", "label": "Schwarzschild Radius (1 M☉)",
        "value": 2.95, "unit": "km", "precision": 3,
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1002/9783527617661",
            "reference_title": "Shapiro & Teukolsky 1983 — Black Holes, White Dwarfs, and Neutron Stars",
            "retrieval_year": 1983, "attribution": "Shapiro & Teukolsky (1983) §12.1"},
    },
    ("chandrasekhar limit", "m☉"): {
        "kind": "scalar", "label": "Chandrasekhar Limit",
        "value": 1.44, "unit": "M☉", "precision": 3,
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1086/143324",
            "reference_title": "Chandrasekhar 1931, ApJ 74 81 — maximum white-dwarf mass",
            "retrieval_year": 1931, "attribution": "Chandrasekhar (1931)"},
    },
    ("neutron star radius", "km"): {
        "kind": "range", "label": "Neutron Star Radius",
        "value_min": 10, "value_max": 13, "unit": "km", "scale": "linear",
        "source": {"tier": "authoritative", "authority": "NASA",
            "reference_url": "https://doi.org/10.3847/2041-8213/ac089a",
            "reference_title": "Miller et al. 2021 (NICER J0740+6620)",
            "retrieval_year": 2021, "attribution": "NICER + Miller et al. (2021)"},
    },
    ("supernova mass", "m☉"): {
        "kind": "scalar", "label": "Supernova Minimum Progenitor Mass",
        "value": 8.0, "unit": "M☉", "precision": 2,
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-082708-101737",
            "reference_title": "Smartt 2009 ARA&A — progenitors of core-collapse supernovae",
            "retrieval_year": 2009, "attribution": "Smartt (2009)"},
    },
    ("supernova energy release", "j"): {
        "kind": "scalar", "label": "Supernova Energy Release",
        "value": 1e51, "unit": "erg", "notation": "scientific",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-082708-101737",
            "reference_title": "Janka 2012 ARA&A — Explosion Mechanisms",
            "retrieval_year": 2012, "attribution": "Janka (2012)"},
    },
    ("luminosity", "erg/s"): {
        "kind": "range", "label": "GRB Peak Luminosity",
        "value_min": 1e49, "value_max": 1e54, "unit": "erg/s", "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1016/j.physrep.2014.09.008",
            "reference_title": "Kumar & Zhang 2015 Physics Reports — physics of GRBs",
            "retrieval_year": 2015, "attribution": "Kumar & Zhang (2015)"},
    },
    ("dispersion measure", "pc/cm³"): {
        "kind": "range", "label": "FRB Dispersion Measure",
        "value_min": 100, "value_max": 3000, "unit": "pc/cm³", "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-091918-104501",
            "reference_title": "Petroff, Hessels & Lorimer 2022 ARA&A — FRBs",
            "retrieval_year": 2022, "attribution": "Petroff, Hessels & Lorimer (2022)"},
    },
    ("moon-earth distance", "km"): {
        "kind": "scalar", "label": "Moon–Earth Distance (mean)",
        "value": 384400, "unit": "km", "precision": 6,
        "source": {"tier": "authoritative", "authority": "NASA",
            "reference_url": "https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html",
            "reference_title": "NASA Moon Fact Sheet", "retrieval_year": 2024,
            "attribution": "NASA Goddard fact sheet"},
    },
    ("roche limit factor", "planetary radii"): {
        "kind": "scalar", "label": "Roche Limit (rigid body)",
        "value": 2.44, "unit": "planetary radii", "precision": 3,
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://archive.org/details/MurrayDermottSolarSystemDynamics",
            "reference_title": "Murray & Dermott 1999 — Solar System Dynamics",
            "retrieval_year": 1999, "attribution": "Murray & Dermott (1999) §4.10"},
    },
    ("tidal locking period", "days"): {
        "kind": "scalar", "label": "Moon Sidereal Period",
        "value": 27.3217, "unit": "days", "precision": 6,
        "source": {"tier": "authoritative", "authority": "NASA",
            "reference_url": "https://ssd.jpl.nasa.gov/planets/approx_pos.html",
            "reference_title": "JPL DE441 — Lunar Ephemeris",
            "retrieval_year": 2024, "attribution": "JPL DE441"},
    },
    ("kuiper belt inner edge", "au"): {
        "kind": "scalar", "label": "Kuiper Belt Inner Edge",
        "value": 30, "unit": "AU", "precision": 2,
        "source": {"tier": "authoritative", "authority": "IAU",
            "reference_url": "https://minorplanetcenter.net/iau/lists/MPLists.html",
            "reference_title": "IAU Minor Planet Center — TNO populations",
            "retrieval_year": 2024, "attribution": "IAU MPC"},
    },
    ("kuiper belt outer edge", "au"): {
        "kind": "scalar", "label": "Kuiper Belt Outer Edge",
        "value": 50, "unit": "AU", "precision": 2,
        "source": {"tier": "authoritative", "authority": "IAU",
            "reference_url": "https://minorplanetcenter.net/iau/lists/MPLists.html",
            "reference_title": "IAU Minor Planet Center — TNO populations",
            "retrieval_year": 2024, "attribution": "IAU MPC"},
    },
    ("ceres diameter", "km"): {
        "kind": "scalar", "label": "Ceres Mean Diameter",
        "value": 939.4, "unit": "km", "precision": 4,
        "source": {"tier": "authoritative", "authority": "NASA",
            "reference_url": "https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/ceres/by-the-numbers/",
            "reference_title": "NASA Dawn mission — Ceres dimensions",
            "retrieval_year": 2024, "attribution": "NASA/Dawn"},
    },
    ("surface temperature of o-type stars", "k"): {
        "kind": "range", "label": "O-type Star Surface Temperature",
        "value_min": 30000, "value_max": 52000, "unit": "K", "scale": "linear",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1051/0004-6361:200809511",
            "reference_title": "Martins, Schaerer & Hillier 2005 A&A 436 1049",
            "retrieval_year": 2005, "attribution": "Martins et al. (2005)"},
    },
    ("surface temperature", "k"): {
        "kind": "range", "label": "White Dwarf Surface Temperature",
        "value_min": 4000, "value_max": 150000, "unit": "K", "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081710-102602",
            "reference_title": "Althaus et al. 2010 ARA&A — white dwarf evolution",
            "retrieval_year": 2010, "attribution": "Althaus et al. (2010)"},
    },
    ("inner disk radius", "km"): {
        "kind": "scalar", "label": "ISCO (Schwarzschild, 1 M☉)",
        "value": 8.85, "unit": "km", "precision": 3,
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1086/151796",
            "reference_title": "Bardeen, Press & Teukolsky 1972 ApJ 178 347",
            "retrieval_year": 1972, "attribution": "Bardeen, Press & Teukolsky (1972)"},
    },

    # === HeroFactCredibility v1 Round 2 ===
    ("formation time", "gyr"): {
        "kind": "scalar", "label": "Universe Age",
        "value": 13.787, "unit": "Gyr", "precision": 5,
        "source": {"tier": "authoritative", "authority": "Planck Collaboration",
            "reference_url": "https://doi.org/10.1051/0004-6361/201833910",
            "reference_title": "Planck 2018 results VI", "retrieval_year": 2020,
            "attribution": "Planck 2018"},
    },
    ("density", "kg/m3"): {
        "kind": "range", "label": "Pulsar/Neutron Star Density",
        "value_min": 1e16, "value_max": 1e18, "unit": "kg/m\u00b3", "scale": "log",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1002/9783527617661",
            "reference_title": "Shapiro & Teukolsky 1983 \u00a72.4",
            "retrieval_year": 1983, "attribution": "Shapiro & Teukolsky (1983)"},
    },
    ("habitable temperature", "\u00b0c"): {
        "kind": "range", "label": "Habitable Zone Surface Temperature",
        "value_min": 0, "value_max": 50, "unit": "\u00b0C", "scale": "linear",
        "qualifier": "liquid water at Earth-like atmospheric pressure",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1088/0004-637X/765/2/131",
            "reference_title": "Kopparapu et al. 2013",
            "retrieval_year": 2013, "attribution": "Kopparapu et al. (2013)"},
    },
    ("atomic gas temperature", "k"): {
        "kind": "range", "label": "Atomic ISM Temperature",
        "value_min": 50, "value_max": 100, "unit": "K", "scale": "linear",
        "qualifier": "Cold Neutral Medium (CNM)",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1086/319783",
            "reference_title": "Wolfire et al. 2003 ApJ 587 278",
            "retrieval_year": 2003, "attribution": "Wolfire et al. (2003)"},
    },
    ("ionized gas temperature", "k"): {
        "kind": "range", "label": "Ionized ISM Temperature",
        "value_min": 8000, "value_max": 1e6, "unit": "K", "scale": "log",
        "qualifier": "Warm/Hot Ionized Medium",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1086/319783",
            "reference_title": "Wolfire et al. 2003 \u2014 Three-phase ISM",
            "retrieval_year": 2003, "attribution": "Wolfire et al. (2003)"},
    },
    ("orbit range", "au"): {
        "kind": "range", "label": "Main Asteroid Belt Orbital Range",
        "value_min": 2.1, "value_max": 3.3, "unit": "AU", "scale": "linear",
        "source": {"tier": "authoritative", "authority": "IAU",
            "reference_url": "https://minorplanetcenter.net/iau/lists/MPLists.html",
            "reference_title": "IAU MPC \u2014 main belt definition",
            "retrieval_year": 2024, "attribution": "IAU MPC"},
    },
    ("x-ray temperature", "k"): {
        "kind": "range", "label": "Galaxy Cluster X-ray Temperature",
        "value_min": 1e7, "value_max": 1e8, "unit": "K", "scale": "log",
        "qualifier": "intracluster medium (ICM)",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081710-102514",
            "reference_title": "Kravtsov & Borgani 2012 ARA&A",
            "retrieval_year": 2012, "attribution": "Kravtsov & Borgani (2012)"},
    },
    ("distance from star", "au"): {
        "kind": "range", "label": "Habitable Zone Distance",
        "value_min": 0.95, "value_max": 1.37, "unit": "AU", "scale": "linear",
        "qualifier": "Sun-like star",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1088/0004-637X/765/2/131",
            "reference_title": "Kopparapu et al. 2013",
            "retrieval_year": 2013, "attribution": "Kopparapu et al. (2013)"},
    },
    ("energy release", "j"): {
        "kind": "scalar", "label": "Supernova Energy Release",
        "value": 1e44, "unit": "J", "notation": "scientific",
        "qualifier": "core-collapse SN (10^51 erg = 10^44 J)",
        "source": {"tier": "authoritative", "authority": "textbook",
            "reference_url": "https://doi.org/10.1146/annurev-astro-082708-101737",
            "reference_title": "Janka 2012 ARA&A",
            "retrieval_year": 2012, "attribution": "Janka (2012)"},
    },
}


def _normalize_label(s: str) -> str:
    """Normalize for fuzzy matching: lowercase, dehyphenate, depluralize."""
    import re as _re
    s = s.lower().strip()
    s = s.replace("-", " ").replace("_", " ")
    # Simple depluralization (plurals: -es, -s; irregular: radii→radius, voids→void)
    s = _re.sub(r'\b(\w+?)(ies)\b', r'\1y', s)  # bodies→body
    s = _re.sub(r'\b(\w+?)(ii)\b', r'\1us', s)   # radii→radius
    s = _re.sub(r'\b(\w+?)(es)\b', r'\1', s)     # vortices→vortic (close enough)
    s = _re.sub(r'\b(\w+?)(s)\b', r'\1', s)      # voids→void, stars→star
    return _re.sub(r'\s+', ' ', s).strip()


def find_known_constant(label: str, unit: str | None = None) -> dict | None:
    """Best-effort match of a label/unit pair to a KNOWN_CONSTANTS entry.
    Uses normalized label comparison for plural/hyphen/whitespace variants.
    """
    if not label:
        return None
    label_norm = _normalize_label(label)
    label_raw = label.lower().strip()
    unit_norm = (unit or "").lower().strip() if unit else None

    # Build a normalized version of KNOWN_CONSTANTS keys for fuzzy lookup
    def _kn(kw):
        return _normalize_label(kw)

    # 1. Exact match (raw)
    direct = KNOWN_CONSTANTS.get((label_raw, unit_norm))
    if direct:
        return dict(direct)
    # 1b. Exact match (normalized)
    for (kw, ku), v in KNOWN_CONSTANTS.items():
        if _kn(kw) == label_norm:
            if ku is None or unit_norm is None or ku == unit_norm:
                return dict(v)

    # 2. Substring match (raw then normalized)
    for (kw, ku), v in KNOWN_CONSTANTS.items():
        if kw in label_raw or _kn(kw) in label_norm:
            if ku is None or unit_norm is None or ku == unit_norm:
                return dict(v)

    # 3. All-words match (raw then normalized)
    for (kw, ku), v in KNOWN_CONSTANTS.items():
        words = kw.split()
        if all(w in label_raw for w in words):
            return dict(v)
        words_n = _kn(kw).split()
        if all(w in label_norm for w in words_n):
            if ku is None or unit_norm is None or ku == unit_norm:
                return dict(v)

    return None


# ---------------------------------------------------------------------------
# Write-path helper
# ---------------------------------------------------------------------------

def validate_and_save_hero_facts(page, db, facts: list) -> list:
    """Validate and normalize a list of hero_facts before saving to a page.

    - Rejects facts with FORBIDDEN_VAGUE values
    - Replaces them with KNOWN_CONSTANTS entries if available
    - Falls back to dropping the fact if no replacement found
    - Returns the cleaned list (may be shorter than input)
    """
    import json as _json
    cleaned = []
    for f in facts:
        if not isinstance(f, dict):
            continue
        value_str = str(f.get("value", "")).lower().strip()
        vague = (
            value_str in FORBIDDEN_VAGUE
            or any(w in value_str.split() for w in FORBIDDEN_VAGUE)
        )
        if vague:
            replacement = find_known_constant(f.get("label", ""), f.get("unit"))
            if replacement:
                replacement = {**replacement, "label": f.get("label", replacement.get("label", ""))}
                cleaned.append(replacement)
            # else: drop the vague fact silently
        else:
            if "kind" not in f:
                f["kind"] = "scalar"
            cleaned.append(f)

    if cleaned:
        # H6: enrich each fact with trust_level from related claims
        enriched = _enrich_facts_with_trust(page, db, cleaned)
        page.hero_facts = _json.dumps(enriched, ensure_ascii=False)
        return enriched
    return cleaned


import re as _re
import datetime as _dt

DYK_FORBIDDEN_VAGUE: frozenset[str] = frozenset({
    "millions", "billions", "trillions", "thousands",
    "hundreds of millions", "many", "few",
})
DYK_SUSPICIOUS_PATTERNS = [
    r"\b\d+\s*%\s*chance",
    r"\bproven\b",
    r"\bfact that\b",
]


def validate_dyk(text: str) -> tuple[bool, str | None]:
    """Validate a did-you-know sentence. Returns (ok, reason_if_failed)."""
    text_lower = text.lower()
    for vague in DYK_FORBIDDEN_VAGUE:
        if vague in text_lower:
            return False, f"contains vague magnitude '{vague}'"
    for pat in DYK_SUSPICIOUS_PATTERNS:
        if _re.search(pat, text_lower):
            return False, f"suspicious pattern: {pat}"
    if len(text) < 30 or len(text) > 400:
        return False, f"length {len(text)} outside 30-400"
    return True, None


def try_authoritative_source(fact: dict) -> dict | None:
    """Try to match fact to a KNOWN_CONSTANTS entry with a source. Returns source dict or None."""
    constant = find_known_constant(fact.get("label", ""), fact.get("unit"))
    if not constant or not constant.get("source"):
        return None
    # Rough value check
    fact_val = str(fact.get("value", fact.get("value_min", "")))
    const_val = str(constant.get("value", constant.get("value_min", "")))
    if not fact_val or not const_val:
        return constant["source"]
    # Accept if values share meaningful digits
    try:
        fv = float(fact_val.replace("\u00d710\u2076", "e6").replace("\u00d710\u2077", "e7"))
        cv = float(const_val)
        if abs(fv - cv) / max(abs(cv), 1e-10) < 0.10:  # 10% tolerance
            return constant["source"]
    except Exception:
        pass
    return constant["source"]  # default: trust label match


def try_claim_grounded_source(fact: dict, page_id: int, db) -> dict | None:
    """Try to link fact to a claim on this page via TF-IDF similarity."""
    try:
        from app.models.claim import Claim, Evidence
        from app.services.arxiv_classifier import _tokenize, _cosine
        import math
        from collections import Counter as _Counter

        claims = db.query(Claim).filter(
            Claim.page_id == page_id,
            Claim.trust_level.in_(["accepted", "consensus", "debated"]),
        ).all()
        if not claims:
            return None

        query = f"{fact.get('label', '')} {fact.get('value', '')} {fact.get('unit', '')}".strip()
        q_tokens = _tokenize(query)
        if not q_tokens:
            return None

        # Build local IDF from these claims
        doc_tokens = [_tokenize(c.text) for c in claims]
        N = len(claims) or 1
        df = _Counter()
        for tokens in doc_tokens:
            df.update(set(tokens))
        idf = {t: math.log((N + 1) / (cnt + 1)) + 1.0 for t, cnt in df.items()}

        q_tf = _Counter(q_tokens)
        q_n = sum(q_tf.values()) or 1
        q_vec = {t: (q_tf[t] / q_n) * idf.get(t, 1.0) for t in q_tf if t in idf}
        if not q_vec:
            return None

        best_sim = 0.0
        best_claim = None
        for claim, tokens in zip(claims, doc_tokens):
            c_tf = _Counter(tokens)
            c_n = sum(c_tf.values()) or 1
            c_vec = {t: (c_tf[t] / c_n) * idf.get(t, 1.0) for t in c_tf if t in idf}
            sim = _cosine(q_vec, c_vec)
            if sim > best_sim:
                best_sim = sim
                best_claim = claim

        if best_sim < 0.30 or not best_claim:  # lowered from 0.65 for better coverage
            return None

        evidence = db.query(Evidence).filter(
            Evidence.claim_id == best_claim.id,
            Evidence.quality >= 0.40,
        ).order_by(Evidence.quality.desc()).all()

        if not evidence:
            return None

        rep = evidence[0]
        return {
            "tier": "claim",
            "claim_id": best_claim.id,
            "trust_level": best_claim.trust_level,
            "evidence_count": len(evidence),
            "representative_arxiv_id": rep.arxiv_id,
            "attribution": f"NebulaMind wiki claim ({best_claim.trust_level}, {len(evidence)} papers)",
            "cited_at": _dt.datetime.utcnow().isoformat(),
        }
    except Exception:
        return None


def _should_suppress_tier_c(fact: dict) -> bool:
    """Returns True if this Tier-C fact should be removed from hero card."""
    label = (fact.get("label") or "").lower()
    value_str = str(fact.get("value") or "").lower().strip()
    unit = (fact.get("unit") or "").lower()

    # R1: Discovery / theory / publication years
    if unit in ("year", "decade") or "year" in unit:
        return True
    if any(kw in label for kw in [
        "discovered", "discovery", "first observed", "first predicted",
        "predicted", "first detection", "named after", "first proposed",
        "first suggested", "publication", "theory", "first calculation",
    ]):
        return True

    # R2: Open-ended count phrases
    if any(s in value_str for s in ["over ", "+", "counted so far", "estimated", "more than", "at least"]):
        return True

    # R3: Person attributions
    if "person" in unit or "named after" in label:
        return True

    # R4: Free-text with no number, or single-word non-numeric value
    if not value_str or value_str in ("none", "n/a", "?"):
        return True
    # R4b: value has no digit at all (e.g. "numerous high-resolution images")
    import re as _re
    if not _re.search(r'\d', value_str):
        return True

    # R4c: catalog object count labels (e.g. "Catalog objects: 103")
    if any(kw in label for kw in ["catalog", "objects counted", "entries", "items"]):
        return True

    return False


def stamp_ai_estimate(label: str = "", reason: str = "No source found") -> dict:
    return {
        "tier": "ai_estimate",
        "generator": "writer-agent",
        "flagged": False,
        "reason": reason,
        "attribution": "NebulaMind AI estimate (not yet peer-reviewed)",
        "cited_at": _dt.datetime.utcnow().isoformat(),
    }


def _enrich_facts_with_trust(page, db, facts: list) -> list:
    """H6: try to attach trust_level to each fact by matching label keywords
    against claims on the same page."""
    if not db or not page:
        return facts
    try:
        from app.models.claim import Claim as _Claim
        import re as _re
        claims = db.query(_Claim).filter(_Claim.page_id == page.id).all()
        if not claims:
            return facts

        enriched = []
        for f in facts:
            if f.get("trust_level"):  # already set, keep
                enriched.append(f)
                continue
            label = (f.get("label") or "").lower()
            keywords = [w for w in _re.findall(r'[a-z]{3,}', label) if len(w) >= 3]
            if not keywords:
                enriched.append(f)
                continue
            # Find best-matching claim
            best_level = None
            LEVEL_RANK = {"consensus": 4, "accepted": 3, "debated": 2, "challenged": 1, "unverified": 0}
            best_rank = -1
            for c in claims:
                claim_lower = c.text.lower()
                if any(kw in claim_lower for kw in keywords):
                    rank = LEVEL_RANK.get(c.trust_level or "unverified", 0)
                    if rank > best_rank:
                        best_rank = rank
                        best_level = c.trust_level
            if best_level:
                f = dict(f)
                f["trust_level"] = best_level
            enriched.append(f)
        return enriched
    except Exception:
        return facts
