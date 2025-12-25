from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.article import ArticleCreate, ArticleRead
from app.services.articles import create_article, get_article, list_articles

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("", response_model=list[ArticleRead])
def list_articles_route(
    status: str | None = None,
    q: str | None = None,
    topic: str | None = None,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
) -> list[ArticleRead]:
    return list_articles(
        db=db,
        status=status,
        q=q,
        topic=topic,
        limit=limit,
        offset=offset,
    )


@router.get("/{article_id}", response_model=ArticleRead)
def get_article_route(article_id: int, db: Session = Depends(get_db)) -> ArticleRead:
    article = get_article(db=db, article_id=article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found.")
    return article


@router.post("", response_model=ArticleRead, status_code=status.HTTP_201_CREATED)
def create_article_route(payload: ArticleCreate, db: Session = Depends(get_db)) -> ArticleRead:
    article = create_article(db=db, payload=payload)
    if not article:
        raise HTTPException(status_code=404, detail="Source not found.")
    return article
