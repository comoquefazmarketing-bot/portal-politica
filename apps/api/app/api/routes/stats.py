from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Article

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("")
def get_stats(db: Session = Depends(get_db)) -> dict:
    results = db.query(Article.status, func.count(Article.id)).group_by(Article.status).all()
    return {"articles_by_status": {status or "unknown": count for status, count in results}}
