"""candidate_grounded_atom_coverage_v1

Revision ID: candidate_grounded_atom_coverage_v1
Revises: <add_previous_revision_here_if_applied>
Create Date: 2026-05-28 22:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'candidate_grounded_atom_coverage_v1'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'arxiv_wiki_candidate_atom_coverage',
        sa.Column('id', sa.BigInteger(), primary_key=True, autoincrement=True),
        sa.Column('coverage_key', sa.Text(), nullable=False, unique=True),
        sa.Column('retrieval_filter_run_id', sa.Integer(), nullable=False),
        sa.Column('claim_id', sa.Integer(), nullable=False),
        sa.Column('element_id', sa.Text(), nullable=False),
        sa.Column('arxiv_id', sa.Text(), nullable=False),
        sa.Column('candidate_atom_coverage_status', sa.Text(), nullable=False),
        sa.Column('candidate_atoms', postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default='[]'),
        sa.Column('deterministic_anchors', postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default='{}'),
        sa.Column('source_hashes', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column('backfill_model', sa.Text(), nullable=False),
        sa.Column('backfill_prompt_version', sa.Text(), nullable=False),
        sa.Column('rationale', sa.Text(), nullable=True),
        sa.Column('failure_mode', sa.Text(), nullable=True),
        sa.Column('raw_response', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('idx_candidate_atom_coverage_tuple', 'arxiv_wiki_candidate_atom_coverage', ['retrieval_filter_run_id', 'claim_id', 'element_id', 'arxiv_id'], unique=False)
    op.create_index('idx_candidate_atom_coverage_status', 'arxiv_wiki_candidate_atom_coverage', ['retrieval_filter_run_id', 'candidate_atom_coverage_status'], unique=False)

def downgrade() -> None:
    op.drop_index('idx_candidate_atom_coverage_status', table_name='arxiv_wiki_candidate_atom_coverage')
    op.drop_index('idx_candidate_atom_coverage_tuple', table_name='arxiv_wiki_candidate_atom_coverage')
    op.drop_table('arxiv_wiki_candidate_atom_coverage')
