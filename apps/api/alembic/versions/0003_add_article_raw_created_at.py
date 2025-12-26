"""add article_raw created_at

Revision ID: 0003_add_article_raw_created_at
Revises: 0002_add_indexes
Create Date: 2024-01-01 00:00:00.000000
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "0003_add_article_raw_created_at"
down_revision = "0002_add_indexes"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "articles_raw",
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.alter_column("articles_raw", "created_at", nullable=False)


def downgrade() -> None:
    op.drop_column("articles_raw", "created_at")
