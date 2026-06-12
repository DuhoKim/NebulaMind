from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, SmallInteger, TIMESTAMP, ForeignKey, func, UniqueConstraint, BigInteger, JSON
from app.models import ARRAY
from app.database import Base


class ResearchIdea(Base):
    __tablename__ = "research_ideas"

    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey("wiki_pages.id", ondelete="CASCADE"), nullable=False)
    survey_combo = Column(String(40), nullable=False)
    question = Column(Text, nullable=False)
    why_now = Column(Text, nullable=False)
    approach = Column(Text, nullable=False)
    systematics_json = Column(JSON, nullable=True)
    novelty = Column(Numeric(3, 2), nullable=False)
    feasibility = Column(Numeric(3, 2), nullable=False)
    status = Column(String(20), nullable=False, server_default="active")
    model_chain = Column(String(120), nullable=False)
    generated_by_run_id = Column(Integer, ForeignKey("autowiki_runs.id", ondelete="SET NULL"), nullable=True)
    saved_by_papa = Column(Boolean, nullable=False, server_default="false")
    seeded = Column(Boolean, nullable=False, server_default="false")
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    last_seen_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    # Phase 3 columns
    claim_id = Column(Integer, ForeignKey("claims.id", ondelete="SET NULL"), nullable=True)
    well_posed_score = Column(Numeric(3, 2), nullable=True)
    well_posed_updated_at = Column(TIMESTAMP, nullable=True)
    datasets_verified = Column(Boolean, nullable=False, server_default="false")
    datasets_verified_at = Column(TIMESTAMP, nullable=True)
    factual_verified = Column(Boolean, nullable=False, server_default="false")
    factual_verified_at = Column(TIMESTAMP, nullable=True)
    factual_verification_notes = Column(JSON, nullable=False, server_default="{}")
    coverage_status = Column(String(20), nullable=True)
    closest_prior_work = Column(JSON, nullable=True)
    coverage_checked_at = Column(TIMESTAMP(timezone=True), nullable=True)
    # Karpathy v2 columns
    gap_type = Column(String(20), nullable=True)
    conflicting_claim_ids = Column(ARRAY(Integer), nullable=True)
    bridge_section_pair = Column(ARRAY(Text), nullable=True)


class ResearchIdeaAnchor(Base):
    __tablename__ = "research_idea_anchors"

    id = Column(Integer, primary_key=True)
    idea_id = Column(Integer, ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False)
    kind = Column(String(20), nullable=False)
    ref_id = Column(String(40), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())


class ResearchIdeaVote(Base):
    __tablename__ = "research_idea_votes"

    id = Column(Integer, primary_key=True)
    idea_id = Column(Integer, ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, nullable=True)
    value = Column(SmallInteger, nullable=False)
    note = Column(Text, nullable=True)
    axis = Column(String(20), nullable=False, server_default="overall")
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    # Unique index is now on (idea_id, COALESCE(user_id,-1), axis) — managed via migration, not ORM constraint


class ResearchIdeaSurvey(Base):
    __tablename__ = "research_idea_surveys"

    id = Column(Integer, primary_key=True)
    idea_id = Column(Integer, ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False)
    survey_id = Column(Integer, ForeignKey("surveys.id", ondelete="RESTRICT"), nullable=False)

    __table_args__ = (UniqueConstraint("idea_id", "survey_id", name="uq_research_idea_surveys"),)


class SurveyDataset(Base):
    __tablename__ = "survey_datasets"

    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False)
    slug = Column(String(80), nullable=False, unique=True)
    name = Column(String(120), nullable=False)
    full_name = Column(String(300), nullable=False)
    description = Column(Text, nullable=False)
    data_type = Column(String(40), nullable=False)
    release_year = Column(Integer, nullable=True)
    release_label = Column(String(60), nullable=True)
    redshift_range = Column(String(60), nullable=True)
    sky_coverage_deg2 = Column(Numeric(10, 2), nullable=True)
    sample_size = Column(BigInteger, nullable=True)
    doi = Column(String(200), nullable=True)
    primary_url = Column(Text, nullable=False)
    archive_url = Column(Text, nullable=True)
    bibcode = Column(String(40), nullable=True)
    registry = Column(String(40), nullable=True)
    license = Column(String(60), nullable=True)
    status = Column(String(20), nullable=False, server_default="active")
    url_verified_at = Column(TIMESTAMP, nullable=True)
    url_verified_ok = Column(Boolean, nullable=True)
    url_verified_note = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())


class ResearchIdeaDataset(Base):
    __tablename__ = "research_idea_datasets"

    id = Column(Integer, primary_key=True)
    idea_id = Column(Integer, ForeignKey("research_ideas.id", ondelete="CASCADE"), nullable=False)
    dataset_id = Column(Integer, ForeignKey("survey_datasets.id", ondelete="RESTRICT"), nullable=False)
    role = Column(String(20), nullable=False, server_default="primary")
    note = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    __table_args__ = (UniqueConstraint("idea_id", "dataset_id", name="uq_research_idea_datasets"),)
