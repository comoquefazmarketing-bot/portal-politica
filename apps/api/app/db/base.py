from __future__ import annotations

from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models import article, article_raw, audit_log, check, source  # noqa: E402,F401
