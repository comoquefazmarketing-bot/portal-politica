from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.sources import create_source, list_sources
from app.schemas.source import SourceCreate, SourceRead

router = APIRouter(prefix="/sources", tags=["sources"])


@router.get("", response_model=list[SourceRead])
def list_sources_route(
    limit: int = 20,
    offset: int = 0,
    db: Session = Depends(get_db),
) -> list[SourceRead]:
    return list_sources(db=db, limit=limit, offset=offset)


@router.post("", response_model=SourceRead, status_code=status.HTTP_201_CREATED)
def create_source_route(payload: SourceCreate, db: Session = Depends(get_db)) -> SourceRead:
    return create_source(db=db, payload=payload)
