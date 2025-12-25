from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Article
from app.schemas.article import ArticleRead

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("", response_model=list[ArticleRead])
def list_articles(
    status: str | None = None,
    q: str | None = None,
    topic: str | None = None,
    limit: int = 20,
    offset: int = 0,
    db: Session = Depends(get_db),
) -> list[Article]:
    query = db.query(Article)
    if status:
        query = query.filter(Article.status == status)
    if topic:
        query = query.filter(Article.topic == topic)
    if q:
        like_value = f"%{q}%"
        query = query.filter(
            or_(
                Article.title.ilike(like_value),
                Article.summary.ilike(like_value),
                Article.content.ilike(like_value),
            )
        )
    return query.order_by(Article.created_at.desc()).offset(offset).limit(limit).all()


@router.get("/{article_id}", response_model=ArticleRead)
def get_article(article_id: int, db: Session = Depends(get_db)) -> Article:
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found.")
    return article
