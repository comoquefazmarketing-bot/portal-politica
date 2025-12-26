from __future__ import annotations

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models import Article, Source
from app.schemas.article import ArticleCreate


def list_articles(
    db: Session,
    status: str | None,
    q: str | None,
    topic: str | None,
    limit: int,
    offset: int,
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


def get_article(db: Session, article_id: int) -> Article | None:
    return db.query(Article).filter(Article.id == article_id).first()


def create_article(db: Session, payload: ArticleCreate) -> Article | None:
    source = db.query(Source).filter(Source.id == payload.source_id).first()
    if not source:
        return None
    article = Article(**payload.model_dump())
    db.add(article)
    db.commit()
    db.refresh(article)
    return article
