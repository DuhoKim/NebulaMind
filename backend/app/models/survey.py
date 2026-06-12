import re
from sqlalchemy import (
    Boolean, Column, Date, Integer, String, Text, Numeric, Float, BigInteger,
    TIMESTAMP, ForeignKey, func, UniqueConstraint, event, JSON
)
from sqlalchemy.orm.attributes import get_history
from app.database import Base


# ---------------------------------------------------------------------------
# Numeric-field parsers
# ---------------------------------------------------------------------------

def _parse_wavelength_um(wr: str):
    """Return center wavelength in μm from free-text wavelength_range."""
    if not wr:
        return None

    def _avg(a, b):  return (a + b) / 2
    def _geo(a, b):  return (a * b) ** 0.5

    # Energy units (high → low energy)
    m = re.search(r'([\d.]+)\s*MeV\s*[–\-]\s*([\d.]+)\s*TeV', wr, re.I)
    if m: return 1.23984e-6 / _geo(float(m[1]), float(m[2]) * 1e6)
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*TeV', wr, re.I)
    if m: return 1.23984e-12 / _geo(float(m[1]), float(m[2]))
    m = re.search(r'([\d.]+)\s*TeV', wr, re.I)
    if m: return 1.23984e-12 / float(m[1])
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*GeV', wr, re.I)
    if m: return 1.23984e-9 / _geo(float(m[1]), float(m[2]))
    m = re.search(r'([\d.]+)\s*GeV', wr, re.I)
    if m: return 1.23984e-9 / float(m[1])
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*MeV', wr, re.I)
    if m: return 1.23984e-6 / _geo(float(m[1]), float(m[2]))
    m = re.search(r'([\d.]+)\s*MeV', wr, re.I)
    if m: return 1.23984e-6 / float(m[1])
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*keV', wr, re.I)
    if m: return 1.23984e-3 / _avg(float(m[1]), float(m[2]))
    m = re.search(r'([\d.]+)\s*keV', wr, re.I)
    if m: return 1.23984e-3 / float(m[1])

    # Wavelength units (short → long)
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*μm', wr)
    if m: return _avg(float(m[1]), float(m[2]))
    m = re.search(r'([\d.]+)\s*μm', wr)
    if m: return float(m[1])
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*nm', wr, re.I)
    if m: return _avg(float(m[1]), float(m[2])) / 1000
    m = re.search(r'([\d.]+)\s*nm', wr, re.I)
    if m: return float(m[1]) / 1000
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*mm', wr, re.I)
    if m: return _avg(float(m[1]), float(m[2])) * 1000
    m = re.search(r'([\d.]+)\s*mm', wr, re.I)
    if m: return float(m[1]) * 1000

    # Frequency units
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*GHz', wr, re.I)
    if m: return 3e5 / _avg(float(m[1]), float(m[2]))
    m = re.search(r'([\d.]+)\s*GHz', wr, re.I)
    if m: return 3e5 / float(m[1])
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*MHz', wr, re.I)
    if m: return 3e8 / _avg(float(m[1]), float(m[2]))
    m = re.search(r'([\d.]+)\s*MHz', wr, re.I)
    if m: return 3e8 / float(m[1])

    return None


def _parse_z_max(rr: str):
    """Return maximum redshift from free-text redshift_range."""
    if not rr:
        return None
    if re.search(r'stellar|milky way|all distances|nearby stars', rr, re.I):
        return None
    m = re.search(r'z\s*[≈=~]\s*[\d.]+\s*[–\-]\s*([\d.]+)\+?', rr)
    if m: return float(m[1])
    m = re.search(r'z\s*(?:up to|=|~|≈|<)\s*([\d.]+)', rr, re.I)
    if m: return float(m[1])
    # range like "z = 0.01 – 6.5" matched by first pattern; also try bare lo–hi
    m = re.search(r'z\s*=?\s*[\d.]+\s*[–\-]\s*([\d.]+)', rr)
    if m: return float(m[1])
    m = re.search(r'z\s*([\d.]+)', rr)
    if m: return float(m[1])
    return None


def _parse_dr_year(dr: str):
    """Return 4-digit year from free-text current_data_release."""
    if not dr:
        return None
    if re.search(r'no data|not yet|planned|tbd', dr, re.I):
        return None
    m = re.search(r'\b(19|20)\d{2}\b', dr)
    return int(m[0]) if m else None


def _parse_data_volume_tb(dv: str):
    """Return data volume in TB from free-text data_volume."""
    if not dv:
        return None
    m = re.search(r'~?([\d.]+)\s*PB', dv, re.I)
    if m: return float(m[1]) * 1000
    m = re.search(r'~?([\d.]+)\s*TB', dv, re.I)
    if m: return float(m[1])
    return None


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True)
    slug = Column(String(40), nullable=False, unique=True)
    name = Column(String(60), nullable=False)
    full_name = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    wavelength_range = Column(String(120), nullable=False)
    wavelength_band = Column(String(20), nullable=False)
    sky_coverage_deg2 = Column(Numeric(10, 2), nullable=True)
    sky_coverage_note = Column(String(200), nullable=True)
    redshift_range = Column(String(120), nullable=True)
    instruments_json = Column(JSON, nullable=False, server_default="[]")
    current_data_release = Column(String(120), nullable=True)
    data_volume = Column(String(120), nullable=True)
    primary_science_goals = Column(Text, nullable=False)
    flagship_programs_json = Column(JSON, nullable=False, server_default="[]")
    operator = Column(String(120), nullable=True)
    status = Column(String(20), nullable=False, server_default="operational")
    archive_url = Column(Text, nullable=True)
    mission_url = Column(Text, nullable=True)
    emoji = Column(String(10), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    # Added by autowiki_surveys_v1 migration
    operator_url_allowlist = Column(JSON, nullable=False, server_default="[]")
    quality_score = Column(Numeric(4, 3), nullable=True)
    quality_updated_at = Column(TIMESTAMP, nullable=True)
    url_checked_at = Column(TIMESTAMP, nullable=True)
    url_archive_ok = Column(JSON, nullable=True)   # stored as boolean in DB
    url_mission_ok = Column(JSON, nullable=True)   # stored as boolean in DB

    # Added by add_survey_numeric_fields migration
    wavelength_center_um = Column(Float, nullable=True)
    z_max                = Column(Float, nullable=True)
    dr_year              = Column(Integer, nullable=True)
    data_volume_tb       = Column(Float, nullable=True)
    limiting_magnitude   = Column(Float, nullable=True)
    num_sources_count    = Column(BigInteger, nullable=True)


class SurveyWikiPage(Base):
    __tablename__ = "survey_wiki_pages"

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False)
    page_id = Column(Integer, ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False)

    __table_args__ = (UniqueConstraint("survey_id", "page_id", name="uq_survey_wiki_pages"),)


class SurveyFacilityLink(Base):
    __tablename__ = "survey_facility_links"

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False)
    facility_profile_id = Column(Integer, ForeignKey("facility_profiles.id", ondelete="CASCADE"), nullable=False)
    relation_type = Column(String(40), nullable=False, server_default="same_facility")
    is_primary = Column(Boolean, nullable=False, server_default="true")
    confidence = Column(Numeric(3, 2), nullable=False, server_default="1.00")
    source = Column(String(80), nullable=False, server_default="manual_seed_20260613")
    notes = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    __table_args__ = (
        UniqueConstraint(
            "survey_id",
            "facility_profile_id",
            "relation_type",
            name="uq_survey_facility_links_relation",
        ),
    )


class SurveyDataRelease(Base):
    __tablename__ = "survey_data_releases"

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False)
    label = Column(String(60), nullable=False)
    release_date = Column(Date, nullable=True)
    release_year = Column(Integer, nullable=True)
    summary = Column(Text, nullable=False)
    n_objects = Column(BigInteger, nullable=True)
    sky_coverage_deg2 = Column(Numeric(10, 2), nullable=True)
    data_volume_tb = Column(Float, nullable=True)
    doi = Column(String(200), nullable=True)
    bibcode = Column(String(40), nullable=True)
    url = Column(Text, nullable=True)
    status = Column(String(20), nullable=False, server_default="released")
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    __table_args__ = (UniqueConstraint("survey_id", "label", name="uq_survey_data_releases_survey_label"),)


class SurveyCatalogField(Base):
    __tablename__ = "survey_catalog_fields"

    id = Column(Integer, primary_key=True)
    dataset_id = Column(Integer, ForeignKey("survey_datasets.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(80), nullable=False)
    dtype = Column(String(20), nullable=True)
    unit = Column(String(40), nullable=True)
    ucd = Column(String(80), nullable=True)
    description = Column(Text, nullable=False)
    example = Column(String(120), nullable=True)
    is_key = Column(Boolean, nullable=False, server_default="false")
    sort_order = Column(Integer, nullable=False, server_default="0")
    source_url = Column(Text, nullable=False)

    __table_args__ = (UniqueConstraint("dataset_id", "name", name="uq_survey_catalog_fields_dataset_name"),)


# ---------------------------------------------------------------------------
# before_update listener — recompute derived numeric fields on ORM-level saves
# ---------------------------------------------------------------------------

_DERIVED_SOURCES = ("wavelength_range", "redshift_range", "current_data_release", "data_volume")


@event.listens_for(Survey, "before_update")
def _recompute_survey_numeric_fields(mapper, connection, target):
    """
    Fires before any ORM-level UPDATE on Survey.
    Recomputes wavelength_center_um, z_max, dr_year, data_volume_tb
    whenever any of their source text fields changes.
    """
    if not any(get_history(target, col).has_changes() for col in _DERIVED_SOURCES):
        return

    target.wavelength_center_um = _parse_wavelength_um(target.wavelength_range or "")
    target.z_max                = _parse_z_max(target.redshift_range)
    target.dr_year              = _parse_dr_year(target.current_data_release)
    target.data_volume_tb       = _parse_data_volume_tb(target.data_volume)
