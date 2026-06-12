"""autowiki_surveys_v1: survey_revisions, autowiki_surveys_runs, operator_url_allowlist

Revision ID: autowiki_surveys_v1
Revises: auto_research_improvement_v1
Create Date: 2026-05-13
"""
import json
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "autowiki_surveys_v1"
down_revision = "auto_research_improvement_v1"
branch_labels = None
depends_on = None

_ALLOWLISTS = {
    'sdss':      ['sdss.org', 'pha.jhu.edu'],
    'sdss-v':    ['sdss.org', 'apo.nmsu.edu'],
    'desi':      ['lbl.gov', 'kpno.noirlab.edu', 'desi.lbl.gov'],
    'gaia':      ['esa.int', 'cosmos.esa.int', 'gea.esac.esa.int'],
    'jwst':      ['nasa.gov', 'stsci.edu', 'esa.int', 'mast.stsci.edu'],
    'hst':       ['nasa.gov', 'stsci.edu', 'esa.int', 'mast.stsci.edu'],
    'euclid':    ['esa.int', 'cosmos.esa.int', 'euclid.esac.esa.int'],
    'roman':     ['nasa.gov', 'ipac.caltech.edu', 'irsa.ipac.caltech.edu'],
    'rubin-lsst':['lsst.org', 'rubinobservatory.org', 'data.lsst.cloud'],
    'spherex':   ['ipac.caltech.edu', 'nasa.gov', 'caltech.edu'],
    'alma':      ['eso.org', 'nrao.edu', 'almascience.eso.org'],
    'vla':       ['nrao.edu', 'data.nrao.edu', 'public.nrao.edu'],
    'meerkat':   ['sarao.ac.za', 'archive.sarao.ac.za'],
    'lofar':     ['astron.nl', 'lofar-surveys.org', 'strw.leidenuniv.nl'],
    'askap-emu': ['csiro.au', 'research.csiro.au', 'casda.csiro.au'],
    'hipass':    ['atnf.csiro.au', 'csiro.au'],
    'ska1':      ['skao.int', 'ska.ac.za'],
    'ngvla':     ['nrao.edu', 'ngvla.nrao.edu'],
    'act':       ['princeton.edu', 'gsfc.nasa.gov', 'lambda.gsfc.nasa.gov'],
    'spt':       ['uchicago.edu', 'pole.uchicago.edu'],
    'cmb-s4':    ['cmb-s4.org', 'berkeley.edu', 'lbl.gov'],
    'planck':    ['esa.int', 'cosmos.esa.int', 'pla.esac.esa.int'],
    'galex':     ['stsci.edu', 'caltech.edu', 'galex.stsci.edu'],
    '2mass':     ['ipac.caltech.edu', 'irsa.ipac.caltech.edu'],
    'wise':      ['ipac.caltech.edu', 'irsa.ipac.caltech.edu', 'unwise.me'],
    'viking':    ['eso.org', 'roe.ac.uk'],
    'ukidss':    ['roe.ac.uk', 'wsa.roe.ac.uk'],
    'h-atlas':   ['h-atlas.org', 'esa.int'],
    'chandra':   ['nasa.gov', 'cfa.harvard.edu', 'cxc.cfa.harvard.edu'],
    'cdf-s':     ['nasa.gov', 'cfa.harvard.edu', 'cxc.cfa.harvard.edu'],
    'cdf-n':     ['nasa.gov', 'cfa.harvard.edu', 'cxc.cfa.harvard.edu'],
    'xmm':       ['esa.int', 'cosmos.esa.int'],
    'rosat':     ['mpe.mpg.de', 'xmm.esac.esa.int'],
    'erosita':   ['mpe.mpg.de', 'erosita.mpe.mpg.de'],
    'fermi-lat': ['nasa.gov', 'gsfc.nasa.gov', 'fermi.gsfc.nasa.gov'],
    'hsc-ssp':   ['nao.ac.jp', 'subarutelescope.org', 'mtk.nao.ac.jp'],
    'des':       ['ncsa.illinois.edu', 'darkenergysurvey.org', 'des.ncsa.illinois.edu'],
    'kids':      ['strw.leidenuniv.nl', 'astro-wise.org'],
    'panstarrs': ['stsci.edu', 'ifa.hawaii.edu', 'catalogs.mast.stsci.edu'],
    'cosmos2020':['eso.org', 'cosmos2020.calet.org', 'irsa.ipac.caltech.edu'],
    'unions':    ['skysurvey.cc', 'cfht.hawaii.edu'],
    '4most':     ['eso.org', '4most.eu'],
    'weave':     ['ing.iac.es', 'astro.dur.ac.uk'],
    'gama':      ['gama-survey.org', 'roe.ac.uk'],
    'vipers':    ['vipers.inaf.it', 'inaf.it'],
    'zcosmos':   ['eso.org'],
    'deep2':     ['uci.edu', 'ps.uci.edu', 'deep.ps.uci.edu'],
    'hetdex':    ['hetdex.org', 'utexas.edu'],
    'pfs':       ['ipmu.jp', 'pfs.ipmu.jp'],
    'elt':       ['eso.org', 'elt.eso.org'],
}


def upgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())
    existing_cols = {c["name"] for c in insp.get_columns("surveys")}

    # 1. operator_url_allowlist column on surveys
    if "operator_url_allowlist" not in existing_cols:
        op.add_column("surveys", sa.Column(
            "operator_url_allowlist", JSONB(), nullable=False, server_default="[]"
        ))
        # Seed per-survey
        for slug, domains in _ALLOWLISTS.items():
            conn.execute(
                sa.text("UPDATE surveys SET operator_url_allowlist = :d WHERE slug = :s"),
                {"d": json.dumps(domains), "s": slug},
            )

    # 2. survey_revisions — full-row JSONB snapshots for rollback
    if "autowiki_surveys_runs" not in existing_tables:
        # Create runs table first (survey_revisions references it)
        op.create_table(
            "autowiki_surveys_runs",
            sa.Column("id",                   sa.Integer(), primary_key=True),
            sa.Column("survey_id",            sa.Integer(), sa.ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False),
            sa.Column("started_at",           sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
            sa.Column("finished_at",          sa.TIMESTAMP(), nullable=True),
            sa.Column("trigger",              sa.String(20), nullable=False),
            sa.Column("edit_type",            sa.String(20), nullable=False),
            sa.Column("field_path",           sa.String(80), nullable=True),
            sa.Column("model_proposer",       sa.String(40), nullable=False),
            sa.Column("model_judge",          sa.String(40), nullable=True),
            sa.Column("h0_struct",            sa.Numeric(5, 2), nullable=True),
            sa.Column("h1_struct",            sa.Numeric(5, 2), nullable=True),
            sa.Column("components_before",    JSONB(), nullable=True),
            sa.Column("components_after",     JSONB(), nullable=True),
            sa.Column("u0_median",            sa.Numeric(4, 2), nullable=True),
            sa.Column("u1_median",            sa.Numeric(4, 2), nullable=True),
            sa.Column("u0_runs",              JSONB(), nullable=True),
            sa.Column("u1_runs",              JSONB(), nullable=True),
            sa.Column("judge_rationale",      sa.Text(), nullable=True),
            sa.Column("judge_prompt_version", sa.String(20), nullable=True),
            sa.Column("q0",                   sa.Numeric(4, 3), nullable=True),
            sa.Column("q1",                   sa.Numeric(4, 3), nullable=True),
            sa.Column("delta_q",              sa.Numeric(4, 3), nullable=True),
            sa.Column("source_url",           sa.Text(), nullable=True),
            sa.Column("url_probe_status",     sa.SmallInteger(), nullable=True),
            sa.Column("decision",             sa.String(20), nullable=False),
            sa.Column("reject_reason",        sa.Text(), nullable=True),
            sa.Column("revision_id",          sa.Integer(), nullable=True),
            sa.Column("latency_ms_breakdown", JSONB(), nullable=True),
            sa.Column("error_text",           sa.Text(), nullable=True),
        )
        op.create_index("ix_aws_runs_survey_started", "autowiki_surveys_runs", ["survey_id", "started_at"])
        op.create_index("ix_aws_runs_decision",       "autowiki_surveys_runs", ["decision"])

    if "survey_revisions" not in existing_tables:
        op.create_table(
            "survey_revisions",
            sa.Column("id",              sa.Integer(), primary_key=True),
            sa.Column("survey_id",       sa.Integer(), sa.ForeignKey("surveys.id", ondelete="CASCADE"), nullable=False),
            sa.Column("snapshot",        JSONB(), nullable=False),
            sa.Column("edit_type",       sa.String(20), nullable=False),
            sa.Column("field_path",      sa.String(80), nullable=True),
            sa.Column("editor_agent",    sa.String(60), nullable=False),
            sa.Column("autowiki_run_id", sa.Integer(),
                       sa.ForeignKey("autowiki_surveys_runs.id", ondelete="SET NULL"), nullable=True),
            sa.Column("created_at",      sa.TIMESTAMP(), nullable=False, server_default=sa.text("NOW()")),
        )
        op.create_index("ix_survey_revisions_survey", "survey_revisions", ["survey_id", "created_at"])

        # Add FK from autowiki_surveys_runs → survey_revisions (deferred add after both tables exist)
        op.create_foreign_key(
            "fk_aws_runs_revision_id",
            "autowiki_surveys_runs", "survey_revisions",
            ["revision_id"], ["id"],
            ondelete="SET NULL",
        )

    # 3. Survey quality score cache column
    if "quality_score" not in existing_cols:
        op.add_column("surveys", sa.Column("quality_score", sa.Numeric(4, 3), nullable=True))
    if "quality_updated_at" not in existing_cols:
        op.add_column("surveys", sa.Column("quality_updated_at", sa.TIMESTAMP(), nullable=True))
    if "url_checked_at" not in existing_cols:
        op.add_column("surveys", sa.Column("url_checked_at", sa.TIMESTAMP(), nullable=True))
    if "url_archive_ok" not in existing_cols:
        op.add_column("surveys", sa.Column("url_archive_ok", sa.Boolean(), nullable=True))
    if "url_mission_ok" not in existing_cols:
        op.add_column("surveys", sa.Column("url_mission_ok", sa.Boolean(), nullable=True))


def downgrade():
    conn = op.get_bind()
    insp = sa.inspect(conn)
    existing_tables = set(insp.get_table_names())

    # Drop FK before tables
    try:
        op.drop_constraint("fk_aws_runs_revision_id", "autowiki_surveys_runs", type_="foreignkey")
    except Exception:
        pass

    for tbl in ("survey_revisions", "autowiki_surveys_runs"):
        if tbl in existing_tables:
            op.drop_table(tbl)

    for col in ("operator_url_allowlist", "quality_score", "quality_updated_at",
                "url_checked_at", "url_archive_ok", "url_mission_ok"):
        op.execute(f"ALTER TABLE surveys DROP COLUMN IF EXISTS {col}")
