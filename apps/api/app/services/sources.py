from __future__ import annotations

from sqlalchemy.orm import Session

from app.models import Source
from app.schemas.source import SourceCreate


def list_sources(db: Session, limit: int, offset: int) -> list[Source]:
    return db.query(Source).order_by(Source.id).offset(offset).limit(limit).all()


def create_source(db: Session, payload: SourceCreate) -> Source:
    source = Source(**payload.model_dump())
    db.add(source)
    db.commit()
    db.refresh(source)
    return source
