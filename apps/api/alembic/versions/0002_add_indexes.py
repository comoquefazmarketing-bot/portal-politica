"""add indexes

Revision ID: 0002_add_indexes
Revises: 0001_init
Create Date: 2024-01-01 00:00:00.000000
"""

from __future__ import annotations

from alembic import op

revision = "0002_add_indexes"
down_revision = "0001_init"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index("ix_articles_source_id", "articles", ["source_id"])
    op.create_index("ix_articles_raw_source_id", "articles_raw", ["source_id"])
    op.create_index("ix_checks_article_id", "checks", ["article_id"])


def downgrade() -> None:
    op.drop_index("ix_checks_article_id", table_name="checks")
    op.drop_index("ix_articles_raw_source_id", table_name="articles_raw")
    op.drop_index("ix_articles_source_id", table_name="articles")
