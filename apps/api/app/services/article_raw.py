from __future__ import annotations

from sqlalchemy.orm import Session

from app.models import ArticleRaw, Source
from app.schemas.article_raw import ArticleRawCreate


def create_article_raw(db: Session, payload: ArticleRawCreate) -> ArticleRaw | None:
    source = db.query(Source).filter(Source.id == payload.source_id).first()
    if not source:
        return None
    article_raw = ArticleRaw(**payload.model_dump())
    db.add(article_raw)
    db.commit()
    db.refresh(article_raw)
    return article_raw
