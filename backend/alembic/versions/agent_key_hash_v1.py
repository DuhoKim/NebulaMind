"""Agent API key hashing — add api_key_hash column

Revision ID: agent_key_hash_v1
Revises: llm_routing_telemetry_v1
"""
from alembic import op
import sqlalchemy as sa

revision = "agent_key_hash_v1"
down_revision = "llm_routing_telemetry_v1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("agents", sa.Column("api_key_hash", sa.String(64), nullable=True))
    op.create_index("idx_agents_api_key_hash", "agents", ["api_key_hash"])

    # Enable pgcrypto for SHA-256 hashing
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
    # Hash existing plaintext keys
    op.execute("""
        UPDATE agents
        SET api_key_hash = encode(digest(api_key, 'sha256'), 'hex')
        WHERE api_key IS NOT NULL AND api_key_hash IS NULL
    """)


def downgrade():
    op.drop_index("idx_agents_api_key_hash", "agents")
    op.drop_column("agents", "api_key_hash")
