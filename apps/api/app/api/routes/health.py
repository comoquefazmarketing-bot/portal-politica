from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter()


@router.get("/health")
def health_check(db: Session = Depends(get_db)) -> dict:
    db_connected = True
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        db_connected = False
    return {"status": "ok", "db_connected": db_connected}
