"""survey_health.py — compute_survey_health() and compute_quality() for surveys.

Composite: quality = 0.55 * structural_score/100 + 0.45 * utility_score/10
Weight split 0.55/0.45 per Papa-approved decision (heavier structural weight for
metadata loop vs wiki's 0.35/0.65 — survey quality is mostly deterministic).
"""
import re
import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SurveyHealthComponents:
    field_completeness:       float = 0.0
    description_richness:     float = 0.0
    science_goals_specificity: float = 0.0
    url_validity:             float = 0.0
    dr_freshness:             float = 0.0
    instruments_count:        float = 0.0
    programs_count:           float = 0.0


@dataclass
class SurveyHealthResult:
    score: float                         # 0..100
    components: SurveyHealthComponents = field(default_factory=SurveyHealthComponents)

    def to_dict(self) -> dict:
        c = self.components
        return {
            "score":                    round(self.score, 2),
            "field_completeness":       round(c.field_completeness, 3),
            "description_richness":     round(c.description_richness, 3),
            "science_goals_specificity": round(c.science_goals_specificity, 3),
            "url_validity":             round(c.url_validity, 3),
            "dr_freshness":             round(c.dr_freshness, 3),
            "instruments_count":        round(c.instruments_count, 3),
            "programs_count":           round(c.programs_count, 3),
        }


_REQUIRED_FIELDS = [
    "slug", "name", "full_name", "description", "wavelength_range", "wavelength_band",
    "sky_coverage_deg2", "sky_coverage_note", "redshift_range", "instruments_json",
    "current_data_release", "data_volume", "primary_science_goals", "flagship_programs_json",
    "operator", "status", "archive_url", "mission_url",
]

_SCIENCE_TARGETS = re.compile(
    r"\b(galaxy|galaxies|dark matter|dark energy|BAO|baryon|exoplanet|stellar|star formation|"
    r"AGN|quasar|lensing|cosmic web|large.scale structure|ISM|CGM|IGM|reionization|"
    r"cosmolog|supernovae|black hole|cluster|filament|void|metallicity|kinematics)\b",
    re.IGNORECASE,
)
_QUANTITATIVE = re.compile(
    r"\b(\d+\.?\d*\s*(deg²|deg2|arcmin|μm|nm|GHz|MHz|keV|eV|mag|Mpc|kpc|redshift|z\s*[=<>]|"
    r"million|billion|objects|sources|spectra|galaxies|stars|sq\.?\s*deg))\b",
    re.IGNORECASE,
)

_DR_YEAR_RE = re.compile(r"(20\d{2}|19\d{2})")


def _attr(survey, name, default=None):
    """Safe attribute access for both ORM row and plain dict."""
    if isinstance(survey, dict):
        return survey.get(name, default)
    return getattr(survey, name, default)


def compute_survey_health(survey, url_archive_ok: Optional[bool] = None,
                           url_mission_ok: Optional[bool] = None) -> SurveyHealthResult:
    """
    Compute deterministic structural quality score (0..100) per §1.2.
    url_*_ok: pass cached HEAD probe results; if None, treat as unchecked (score 0).
    """
    c = SurveyHealthComponents()

    # field_completeness (0.25 weight)
    filled = 0
    for f in _REQUIRED_FIELDS:
        val = _attr(survey, f)
        if val is None:
            continue
        if isinstance(val, (list, dict)):
            if len(val) >= 1:
                filled += 1
        elif str(val).strip():
            filled += 1
    c.field_completeness = filled / len(_REQUIRED_FIELDS)

    # description_richness (0.15 weight)
    desc = _attr(survey, "description") or ""
    if len(desc) < 150:
        c.description_richness = 0.0
    else:
        length_factor = min(1.0, len(desc) / 600)
        paragraph_count = max(1, desc.count("\n\n") + 1)
        para_factor = min(1.0, paragraph_count / 2)
        c.description_richness = length_factor * para_factor

    # science_goals_specificity (0.15 weight)
    goals = _attr(survey, "primary_science_goals") or ""
    distinct_targets = len(set(_SCIENCE_TARGETS.findall(goals)))
    has_quantitative = bool(_QUANTITATIVE.search(goals))
    if distinct_targets >= 2 and has_quantitative:
        c.science_goals_specificity = 1.0
    elif distinct_targets >= 2 or has_quantitative:
        c.science_goals_specificity = 0.5
    else:
        c.science_goals_specificity = 0.0

    # url_validity (0.15 weight)
    archive_ok = url_archive_ok if url_archive_ok is not None else bool(_attr(survey, "url_archive_ok"))
    mission_ok = url_mission_ok if url_mission_ok is not None else bool(_attr(survey, "url_mission_ok"))
    c.url_validity = (float(archive_ok) + float(mission_ok)) / 2.0

    # dr_freshness (0.15 weight)
    status = (_attr(survey, "status") or "").lower()
    if status in ("retired", "decommissioned"):
        c.dr_freshness = 1.0
    else:
        dr_str = _attr(survey, "current_data_release") or ""
        years = _DR_YEAR_RE.findall(dr_str)
        if years:
            dr_year = int(max(years))
            today = datetime.date.today()
            age_years = (today.year - dr_year) + (today.month - 1) / 12.0
            c.dr_freshness = max(0.0, 1.0 - age_years / 3.0)
        else:
            c.dr_freshness = 0.0

    # instruments_count (0.10 weight)
    instruments = _attr(survey, "instruments_json") or []
    c.instruments_count = min(1.0, len(instruments) / 4.0)

    # programs_count (0.05 weight)
    if status in ("retired", "decommissioned"):
        c.programs_count = 1.0
    else:
        programs = _attr(survey, "flagship_programs_json") or []
        c.programs_count = min(1.0, len(programs) / 3.0)

    # Weighted sum → 0..100
    score = (
        c.field_completeness       * 0.25 +
        c.description_richness     * 0.15 +
        c.science_goals_specificity * 0.15 +
        c.url_validity             * 0.15 +
        c.dr_freshness             * 0.15 +
        c.instruments_count        * 0.10 +
        c.programs_count           * 0.05
    ) * 100.0

    return SurveyHealthResult(score=round(score, 2), components=c)


def compute_quality(survey, utility_score: Optional[float] = None,
                    url_archive_ok: Optional[bool] = None,
                    url_mission_ok: Optional[bool] = None) -> float:
    """
    Composite quality 0..1 — 0.55*structural + 0.45*utility (Papa-approved split).
    utility_score: 0..10 from LLM judge; if None, uses 0 (worst-case estimate).
    """
    health = compute_survey_health(survey, url_archive_ok=url_archive_ok,
                                   url_mission_ok=url_mission_ok)
    struct_component = 0.55 * (health.score / 100.0)
    utility_norm     = 0.45 * (min(10.0, max(0.0, utility_score or 0.0)) / 10.0)
    return round(struct_component + utility_norm, 4)
